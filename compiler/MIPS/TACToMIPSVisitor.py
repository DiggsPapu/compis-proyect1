class TacToMipsVisitor:
    def __init__(self, tac_instructions, register_manager):
        self.tac_instructions = tac_instructions  # Lista de instrucciones TAC
        self.mips_code = []  # Lista para almacenar las instrucciones MIPS
        self.registers = register_manager

    def emit(self, line):
        """Agrega una línea al código MIPS."""
        self.mips_code.append(line)

    def translate(self):
        """Traduce las instrucciones TAC a MIPS."""
        # print("\n\n-----------------------------------------")
        for instr in self.tac_instructions:
            self.visit(instr)
        return "\n".join(self.mips_code)

    def visit(self, instr):
        """Traduce una instrucción TAC a MIPS."""
        # print(f"Procesando instrucción TAC: {instr}")  # Mostrar qué operación se está traduciendo

        if instr.operacion in ['+', '-', '*', '/']:
            self.translate_arithmetic(instr)
        elif instr.operacion in ['and', 'or']:
            self.translate_logical(instr)
        elif instr.operacion in ['>', '>=', '<', '<=', '==', '!=']:
            self.translate_comparison(instr)
        elif instr.operacion == '=':
            self.translate_assignment(instr)
        elif instr.operacion == 'if':
            self.translate_conditional(instr)
        elif instr.operacion == 'goto':
            self.emit(f"j {instr.resultado}")
        elif instr.operacion == 'label':
            self.emit(f"{instr.resultado}:")
        elif instr.operacion == 'print':
            self.translate_print(instr)
        elif instr.operacion == 'return':
            self.translate_return(instr)

        # Mostrar el resultado de la traducción
        # print(f"Resultado de la traducción a MIPS:\n{self.mips_code[-1] if self.mips_code else 'No se generó código'} \n")

    def translate_arithmetic(self, instr):
        """Traduce instrucciones aritméticas del TAC a MIPS."""
        # Asignar registros a los operandos y al resultado
        reg_arg1 = self.get_register(instr.arg1)  # Validar formato del operando 1
        reg_arg2 = self.get_register(instr.arg2)  # Validar formato del operando 2
        reg_result = self.get_register(instr.resultado)  # Validar formato del resultado

        # Seleccionar la instrucción MIPS correspondiente
        operation = {'+': 'add', '-': 'sub', '*': 'mul', '/': 'div'}[instr.operacion]

        # Generar la instrucción MIPS
        self.emit(f"{operation} {reg_result}, {reg_arg1}, {reg_arg2}")

        # Liberar registros para operandos si no se necesitan más adelante
        self.free_register(instr.arg1)
        self.free_register(instr.arg2)

    def translate_logical(self, instr):
        """Traduce operaciones lógicas (and, or) a MIPS."""
        reg_arg1 = self.get_register(instr.arg1)
        reg_arg2 = self.get_register(instr.arg2)
        reg_result = self.get_register(instr.resultado)

        if instr.operacion == 'and':
            self.emit(f"and {reg_result}, {reg_arg1}, {reg_arg2}")
        elif instr.operacion == 'or':
            self.emit(f"or {reg_result}, {reg_arg1}, {reg_arg2}")

        self.free_register(instr.arg1)
        self.free_register(instr.arg2)

    def translate_comparison(self, instr):
        """Traduce comparaciones (>, >=, <, <=, ==, !=) a MIPS."""
        reg_arg1 = self.get_register(instr.arg1)
        reg_arg2 = self.get_register(instr.arg2)
        reg_result = self.get_register(instr.resultado)

        if instr.operacion == '>':
            self.emit(f"slt {reg_result}, {reg_arg2}, {reg_arg1}")
        elif instr.operacion == '<':
            self.emit(f"slt {reg_result}, {reg_arg1}, {reg_arg2}")
        elif instr.operacion == '>=':
            temp = f"$t9"  # Uso temporal
            self.emit(f"slt {temp}, {reg_arg1}, {reg_arg2}")  # temp = reg_arg1 < reg_arg2
            self.emit(f"seq {reg_result}, {temp}, $zero")     # reg_result = !(temp)
        elif instr.operacion == '<=':
            temp = f"$t9"  # Uso temporal
            self.emit(f"slt {temp}, {reg_arg2}, {reg_arg1}")  # temp = reg_arg2 < reg_arg1
            self.emit(f"seq {reg_result}, {temp}, $zero")     # reg_result = !(temp)
        elif instr.operacion == '==':
            self.emit(f"seq {reg_result}, {reg_arg1}, {reg_arg2}")
        elif instr.operacion == '!=':
            self.emit(f"sne {reg_result}, {reg_arg1}, {reg_arg2}")

        self.free_register(instr.arg1)
        self.free_register(instr.arg2)

    def translate_assignment(self, instr):
        """Traduce asignaciones (=) a MIPS."""
        reg_result = self.get_register(instr.resultado)
        if isinstance(instr.arg1, int):  # Si es un literal
            self.emit(f"li {reg_result}, {instr.arg1}")
        else:  # Si es una variable o temporal
            reg_arg1 = self.get_register(instr.arg1)
            self.emit(f"move {reg_result}, {reg_arg1}")
            self.free_register(instr.arg1)

    def translate_conditional(self, instr):
        """Traduce condicionales (if) a MIPS."""
        reg_arg1 = self.get_register(instr.arg1)
        reg_arg2 = self.get_register(instr.arg2)
        self.emit(f"beq {reg_arg1}, {reg_arg2}, {instr.resultado}")

        self.free_register(instr.arg1)
        self.free_register(instr.arg2)

    def translate_print(self, instr):
        """Traduce impresión (print) a MIPS."""
        reg = self.get_register(instr.arg1)
        self.emit(f"move $a0, {reg}")
        self.emit("li $v0, 1")  # Syscall para imprimir enteros
        self.emit("syscall")
        self.free_register(instr.arg1)

    def translate_return(self, instr):
        """Traduce return a MIPS."""
        reg_result = self.get_register(instr.resultado)
        self.emit(f"move $v0, {reg_result}")
        self.emit("jr $ra")

    def get_register(self, operand):
        """
        Devuelve un registro en el formato adecuado.
        Si el operando ya tiene formato MIPS ($tX), lo retorna tal cual.
        Si no, asigna un nuevo registro.
        """
        if isinstance(operand, str) and operand.startswith('$'):
            return operand  # Ya está en formato de registro
        return self.registers.getReg(operand)

    def free_register(self, operand):
        """
        Libera un registro si el operando no tiene formato MIPS.
        """
        if not (isinstance(operand, str) and operand.startswith('$')):
            self.registers.freeReg(operand)
