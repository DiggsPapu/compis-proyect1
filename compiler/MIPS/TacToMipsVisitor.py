import re

class TacToMipsVisitor:
    def __init__(self, tac_file, register_manager):
        self.tac_file = tac_file
        self.instructions = []
        self.mips_code = []
        self.register_manager = register_manager
        self.string_table = {}  # Diccionario para almacenar strings únicos
        self.variable_types = {}

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
        # Divide la instrucción respetando las comillas
        parts = re.findall(r'".*?"|\S+', instruction)

        if not parts:
            return ""  # Ignorar líneas vacías

        # Detectar etiquetas
        if ":" in instruction and not re.search(r'".*:.*"', instruction):
            return instruction

        # Manejar asignaciones simples: var = value
        if "=" in instruction and len(parts) == 3:
            var, _, value = parts

            if value.startswith('"') and value.endswith('"'):
                # Manejar cadenas
                label = f"str_{value[1:-1].replace(' ', '_')}"  # Crear una etiqueta para la cadena
                # print(f"str_{value[1:-1].replace(' ', '_')}")
                if label not in self.string_table:
                    self.string_table[label] = value[1:-1]  # Guardar la cadena en la tabla de strings
                reg = self.register_manager.getReg(var)
                self.variable_types[var] = "string"  # Marcar como cadena
                return f"la {reg}, {label}  # Load address of string {value} into {var}"
            
            elif value.isdigit():  # Asignación de un valor constante
                reg = self.register_manager.getReg(var)
                self.variable_types[var] = "number"  # Marcar como número
                return f"li {reg}, {value}  # Assign {value} to {var}"
            elif value in ["true", "false"]:
                # Manejar booleanos
                boolean_value = 1 if value == "true" else 0
                self.variable_types[var] = "boolean"  # Marcar como número
                return f"li {self.register_manager.getReg(var)}, {boolean_value}  # Assign boolean {value}"
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
            print(instruction)
            result, _, op1, operator, op2 = parts
            reg_result = self.register_manager.getReg(result)
            reg_op1 = self.register_manager.getReg(op1)
            reg_op2 = self.register_manager.getReg(op2)

            # Registrar literales de cadenas
            if op1.startswith('"') and op1.endswith('"') and op1 not in self.variable_types:
                self.variable_types[op1] = "string"
                self.addToStrTable(op1, reg_op1)


            if op2.startswith('"') and op2.endswith('"') and op2 not in self.variable_types:
                self.variable_types[op2] = "string"
                self.addToStrTable(op2, reg_op2)

            # Comprobar si los operandos son digitos
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
                if self.variable_types[op1] == "string" or self.variable_types[op2] == "string": #Concatenación
                    return self.handle_string_concatenation(reg_result, reg_op1, self.variable_types[op1], reg_op2, self.variable_types[op2])
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
            self.newLine()
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
        if value.startswith('"') and value.endswith('"'):  # Si es una cadena: print "hola"
            label = f"str_{value[1:-1].replace(' ', '_')}"  # Crear etiqueta para la cadena
            if label not in self.string_table:
                self.string_table[label] = value[1:-1]  # Guardar la cadena en .data
            return f"""la $a0, {label}  # Cargar dirección de cadena {value}\nli $v0, 4  # syscall para imprimir cadena\nsyscall"""

        elif value in self.string_table:  # Si es una variable que apunta a una cadena
            return f"""la $a0, {value}  # Cargar dirección de cadena {value}\nli $v0, 4  # syscall para imprimir cadena\nsyscall"""

        elif value.isdigit():  # Si es un número inmediato: print 10
            return f"""li $a0, {value}  # Cargar valor inmediato {value}\nli $v0, 1  # syscall para imprimir entero\nsyscall"""

        elif value.startswith("$t"):  # Si es un registro temporal con concatenación
            return f"""move $a0, {value}  # Mover valor de {value} a $a0\nli $v0, 4  # syscall para imprimir concatenación\nsyscall"""

        elif value in ["true", "false"]:  # Si es un booleano: print true
            bool_value = 1 if value == "true" else 0
            return f"""li $a0, {bool_value}  # Cargar valor booleano {value}\nli $v0, 1  # syscall para imprimir entero\nsyscall"""

        else:  # Si es una variable
            reg = self.register_manager.getReg(value)
            if self.variable_types.get(value) == "string":  # Si la variable es una cadena
                return f"""move $a0, {reg}  # Mover dirección de cadena {value} a $a0\nli $v0, 4  # syscall para imprimir cadena\nsyscall"""
            else:  # Variable numérica o desconocida
                return f"""move $a0, {reg}  # Mover valor de {value} a $a0\nli $v0, 1  # syscall para imprimir entero\nsyscall"""

    def handle_call(self, function_name):
        """Generar código MIPS para una instrucción call."""
        return f"jal {function_name}"

    def handle_string_concatenation(self, result, op1, op1Type, op2, op2Type):
        """Generar MIPS para concatenación de cadenas."""
        code = []

        # Manejar operandos que pueden ser literales o variables
        if op1.startswith('"') and op1.endswith('"'):  # Si op1 es un literal
            label1 = f"str_{op1[1:-1].replace(' ', '_')}"
            if label1 not in self.string_table:
                self.string_table[label1] = op1[1:-1]
            code.append(f"la $t0, {label1}  # Cargar dirección de cadena {op1}")
        else:  # Si op1 es una variable
            reg_op1 = self.register_manager.getReg(op1)
            code.append(f"move $t0, {reg_op1}  # Cargar {op1}")

        if op2.startswith('"') and op2.endswith('"'):  # Si op2 es un literal
            label2 = f"str_{op2[1:-1].replace(' ', '_')}"
            if label2 not in self.string_table:
                self.string_table[label2] = op2[1:-1]
            code.append(f"la $t1, {label2}  # Cargar dirección de cadena {op2}")
        else:  # Si op2 es una variable
            reg_op2 = self.register_manager.getReg(op2)
            code.append(f"move $t1, {reg_op2}  # Cargar {op2}")

        # Reservar espacio para la cadena resultante
        result_label = f"str_{result}"
        if result_label not in self.string_table:
            self.string_table[result_label] = ".space 256"  # Inicializar como vacío
        code.append(f"la $t2, {result_label}  # Cargar dirección para resultado")

        #tipos de impresión primer operador
        if op1Type == "string":
            op1Tam = 4
        else: #Impresion de booleanos y enteros
            op1Tam = 1

        #tipos de impresión segundo operador
        if op2Type == "string":
            op2Tam = 4
        else: #Impresion de booleanos y enteros
            op2Tam = 1

        # Concatenar cadenas
        code.append(f"""\n\n# Concatenación de cadenas\nmove $a0, $t0  # Primera cadena\nli $v0, {op1Tam}      # syscall para imprimir cadena\nsyscall""")
        code.append(f"""\nli $a0, 32     # Cargar el valor ASCII del espacio en blanco en $a0\nli $v0, 11     # syscall para imprimir un carácter\nsyscall        # Llamada al sistema""")
        code.append(f"""\nmove $a0, $t1  # Segunda cadena\nli $v0, {op2Tam}      # syscall para imprimir cadena\nsyscall""")

        # Almacenar la dirección del resultado en el registro
        reg_result = self.register_manager.getReg(result)
        code.append(f"move {reg_result}, $t2  # Guardar dirección del resultado en {result}")

        return "\n".join(code)

    def get_strings(self):
        """Extraer cadenas únicas del TAC."""
        for line in self.instructions:
            if '"' in line:
                matches = re.findall(r'"(.*?)"', line)
                for match in matches:
                    label = f'str_{match.replace(" ", "_")}'
                    if label not in self.string_table:
                        self.string_table[label] = match
        return self.string_table

    def is_string(self, value):
        """Verifica si un valor es una cadena de texto."""
        return isinstance(value, str) and value.startswith('"') and value.endswith('"')

    def addToStrTable(self, value, regName):
        value = f"{value[1:-1].replace(',', ' ')}"
        value = f"{value.replace(':', ' ')}"
        value = value.strip()
        label1 = f"str_{value.replace(' ', '_')}"

        if label1 not in self.string_table:
            self.string_table[label1] = value

        self.mips_code.append(f"la {regName}, {label1}  # Cargar direccion de cadena {value}")

    def newLine(self):
        self.mips_code.append(F"""li $a0, 10\nli $v0, 11\nsyscall""")
    def save_mips_code(self, output_file):
        """Guardar el código MIPS generado en un archivo."""
        with open(output_file, "w") as file:
            # Sección de datos para almacenar cadenas
            file.write(".data\n")
            for label, string in self.string_table.items():
                if ".space" in string:
                    file.write(f"{label}: {string}\n")
                    continue

                file.write(f'{label}: .asciiz "{string}"\n')

            # Sección de texto para el código MIPS
            file.write(".text\n")
            file.write("\n".join(self.mips_code))
