import re

class TacToMipsVisitor:
    def __init__(self, tac_file, register_manager):
        self.tac_file = tac_file
        self.instructions = []
        self.mips_code = []
        self.register_manager = register_manager
        self.string_table = {}  # Diccionario para almacenar strings únicos

    def read_tac_instructions(self):
        """Leer las instrucciones TAC desde el archivo de texto."""
        with open(self.tac_file, "r") as file:
            self.instructions = file.readlines()

    def translate(self):
        """Traducir las instrucciones TAC a MIPS."""
        for line in self.instructions:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # Ignorar líneas vacías o comentarios
            translated = self.translate_instruction(line)
            if translated:
                self.mips_code.append(translated)

    def translate_instruction(self, instruction):
        """Traducir una sola instrucción TAC a MIPS."""
        parts = instruction.split()
        if not parts:
            return ""  # Ignorar líneas vacías

        # Detectar etiquetas
        if ":" in instruction:
            return instruction

        # Manejar asignaciones simples: var = value
        if "=" in instruction and len(parts) == 3:
            var, _, value = parts
            if value.isdigit():  # Asignación de un valor constante
                reg = self.register_manager.getReg(var)
                return f"li {reg}, {value}  # Assign {value} to {var}"
            else:  # Asignación de una variable
                reg_var = self.register_manager.getReg(var)
                reg_value = self.register_manager.getReg(value)
                return f"move {reg_var}, {reg_value}  # Assign {value} to {var}"

        if "=" in instruction and len(parts) == 4:
            # Manejar operaciones unarias: $t2 = -variable2
            result, _, operator, operand = parts
            reg_result = self.register_manager.getReg(result)
            reg_operand = self.register_manager.getReg(operand)
            
            if operator == "-":
                return f"neg {reg_result}, {reg_operand}  # {result} = -{operand}"
            else:
                return f"# Unhandled unary operator: {operator}"

        # Manejar operaciones aritméticas: result = op1 operator op2
        if "=" in instruction and len(parts) == 5:
            result, _, op1, operator, op2 = parts
            reg_result = self.register_manager.getReg(result)
            reg_op1 = self.register_manager.getReg(op1)
            reg_op2 = self.register_manager.getReg(op2)

            # Comprobar si los operandos son literales
            if op1.isdigit():
                reg_op1 = self.register_manager.getReg("temp_op1")
                self.mips_code.append(f"li {reg_op1}, {op1}  # Cargar literal {op1}")
            else:
                reg_op1 = self.register_manager.getReg(op1)

            if op2.isdigit():
                reg_op2 = self.register_manager.getReg("temp_op2")
                self.mips_code.append(f"li {reg_op2}, {op2}  # Cargar literal {op2}")
            else:
                reg_op2 = self.register_manager.getReg(op2)

            if operator == "+":
                if self.is_string(reg_op1) or self.is_string(reg_op2):
                    return self.handle_string_concatenation(reg_result, reg_op1, reg_op2)
                else:
                    return f"add {reg_result}, {reg_op1}, {reg_op2}  # {result} = {op1} + {op2}"
            elif operator == "-":
                return f"sub {reg_result}, {reg_op1}, {reg_op2}  # {result} = {op1} - {op2}"
            elif operator == "*":
                return f"mul {reg_result}, {reg_op1}, {reg_op2}  # {result} = {op1} * {op2}"
            elif operator == "/":
                return f"div {reg_op1}, {reg_op2}  # Divide {op1} / {op2}\nmflo {reg_result}  # Store result in {result}"
            elif operator == "%":
                return f"""div {reg_op1}, {reg_op2}  # Divide {op1} by {op2}\nmfhi {reg_result}         # {result} = {op1} % {op2} (remainder)"""
            elif operator == "<":
                return f"slt {reg_result}, {reg_op1}, {reg_op2}  # {result} = ({op1} < {op2})"
            elif operator == ">":
                return f"slt {reg_result}, {reg_op2}, {reg_op1}  # {result} = ({op1} > {op2})"
            elif operator == "<=":
                return f"""slt {reg_result}, {reg_op2}, {reg_op1}  # {result} = (b > a)\nxori {reg_result}, {reg_result}, 1      # {result} = not({result})"""
            elif operator == ">=":
                return f"""slt {reg_result}, {reg_op1}, {reg_op2}  # {result} = (b < a)\nxori {reg_result}, {reg_result}, 1      # {result} = not({result})"""
            elif operator == "==":
                return f"seq {reg_result}, {reg_op1}, {reg_op2}  # {result} = ({op1} == {op2})"
            elif operator == "!=":
                return f"sne {reg_result}, {reg_op1}, {reg_op2}  # {result} = ({op1} != {op2})"
            elif operator == "and":
                return f"and {reg_result}, {reg_op1}, {reg_op2}  # {result} = {op1} and {op2}"
            elif operator == "or":
                return f"or {reg_result}, {reg_op1}, {reg_op2}  # {result} = {op1} or {op2}"
            else:
                return f"# Unhandled operator: {operator}"

        # Manejar saltos: goto label
        if parts[0] == "goto":
            return f"j {parts[1]}"

        # Manejar condicionales: if condition goto label
        if parts[0] == "if":
            condition = parts[1]
            label = parts[-1]
            reg_condition = self.register_manager.getReg(condition)
            return f"bne {reg_condition}, $zero, {label}  # Conditional jump"

        # Manejar impresión
        if parts[0] == "print":
            value = parts[1]
            return self.handle_print(value)

        # Manejar funciones
        if parts[0] == "call":
            function_name = parts[1]
            return self.handle_call(function_name)

        if parts[0] == "param":
            param = parts[1]
            reg = self.register_manager.getReg(param)
            return f"""# Save parameter {param} to the stack\naddi $sp, $sp, -4  # Move stack pointer\nsw {reg}, 0($sp)  # Store the parameter"""

        # Manejar returns
        if parts[0] == "return":
            return_value = parts[1]
            reg = self.register_manager.getReg(return_value)
            return f"""move $v0, {reg}  # Move return value to $v0\njr $ra  # Return {return_value}"""
            
        # Manejar EndFunc
        if parts[0] == "EndFunc":
            return """# End of function\nlw $ra, 4($sp)  # Restore return address\nlw $fp, 0($sp)  # Restore frame pointer\naddiu $sp, $sp, 8  # Adjust stack pointer\njr $ra  # Return to caller"""
        
        # Instrucción no manejada
        return f"# Unhandled TAC operation: {instruction}"

    def handle_print(self, value):
        """Generar código MIPS para una instrucción print."""
        return f"""li $v0, 1\nmove $a0, {self.register_manager.getReg(value)}\nsyscall"""

    def handle_call(self, function_name):
        """Generar código MIPS para una instrucción call."""
        return f"jal {function_name}"

    def handle_string_concatenation(self, result, op1, op2):
        """Generar MIPS para concatenación de cadenas."""
        code = []

        # Manejar operandos que son cadenas o variables
        if self.is_string(op1):
            code.append(f'la $t0, str_{op1[1:-1]}  # Cargar cadena "{op1}"')
        else:
            reg_op1 = self.register_manager.getReg(op1)
            code.append(f'move $t0, {reg_op1}  # Cargar variable {op1}')

        if self.is_string(op2):
            code.append(f'la $t1, str_{op2[1:-1]}  # Cargar cadena "{op2}"')
        else:
            reg_op2 = self.register_manager.getReg(op2)
            code.append(f'move $t1, {reg_op2}  # Cargar variable {op2}')

        # Concatenar las cadenas
        code.append('move $a0, $t0  # Copiar primera cadena al buffer')
        code.append('li $v0, 4  # syscall para imprimir cadena')
        code.append('syscall')
        code.append('move $a0, $t1  # Copiar segunda cadena al buffer')
        code.append('li $v0, 4  # syscall para imprimir cadena')
        code.append('syscall')

        # Devolver la referencia concatenada (puede ser un registro o memoria)
        reg_result = self.register_manager.getReg(result)
        code.append(f'move {reg_result}, $a0  # Guardar resultado en {result}')

        return "\n".join(code)

    def get_strings(self):
        """Extraer cadenas únicas del TAC."""
        strings = set()
        for line in self.instructions:
            if '"' in line:
                match = re.findall(r'"(.*?)"', line)
                strings.update(match)
        return strings

    def is_string(self, value):
        """
        Verifica si un valor es una cadena de texto.
        Una cadena se define como un valor entre comillas dobles.
        """
        if isinstance(value, str) and (value.startswith('"') and value.endswith('"')):
            return True
        # Si el valor está en la tabla de cadenas (en caso de tener una tabla de strings)
        if value in self.string_table:
            return True
        return False

    def save_mips_code(self, output_file):
        """Guardar el código MIPS generado en un archivo."""
        with open(output_file, "w") as file:
            # Sección de datos para almacenar cadenas
            file.write(".data\n")
            for string in self.get_strings():
                file.write(f'str_{string}: .asciiz "{string}"\n')

            # Sección de texto para el código MIPS
            file.write(".text\n")
            file.write("\n".join(self.mips_code))