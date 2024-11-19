class TacToMipsVisitor:
    def __init__(self, tac_file, register_manager):
        self.tac_file = tac_file
        self.instructions = []
        self.mips_code = []
        self.register_manager = register_manager

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

            if operator == "+":
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

        # Instrucción no manejada
        return f"# Unhandled TAC operation: {instruction}"

    def handle_print(self, value):
        """Generar código MIPS para una instrucción print."""
        return f"""
        li $v0, 1
        move $a0, {self.register_manager.getReg(value)}
        syscall
        """

    def handle_call(self, function_name):
        """Generar código MIPS para una instrucción call."""
        return f"jal {function_name}"

    def save_mips_code(self, output_file):
        """Guardar el código MIPS generado en un archivo."""
        with open(output_file, "w") as file:
            file.write("\n".join(self.mips_code))
