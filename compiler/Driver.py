import sys
from antlr4 import *
from Syntax.CompiScriptLanguageLexer import *
from Syntax.CompiScriptLanguageParser import *
from Semantic.CompiScriptVisitorSemantic import *
from Syntax.CompiScriptLanguageVisitor import *
from TAC.CompiScriptTacVisitor import CompiScriptTacVisitor
from antlr4.tree.Trees import Trees
import graphviz
import os

class RegisterManager:
    def __init__(self):
        self.registers = {f"$t{i}": None for i in range(10)}  # $t0-$t9 disponibles
        self.stack = []  # Pila para valores desbordados
        self.usage = {}  # Seguimiento de uso de variables/temporales
    def getReg(self, var_name):
        """Asignar un registro para una variable/temporal."""
        # Si ya tiene un registro asignado, devuélvelo
        for reg, value in self.registers.items():
            if value == var_name:
                return reg
        # Si hay registros libres, asígnalos
        for reg, value in self.registers.items():
            if value is None:
                self.registers[reg] = var_name
                return reg
        # Si no hay registros libres, hacer spill al stack
        return self.spillToStack(var_name)
    def freeReg(self, var_name):
        """Liberar el registro asociado a una variable/temporal."""
        for reg, value in self.registers.items():
            if value == var_name:
                self.registers[reg] = None
                return
    def spillToStack(self, var_name):
        """Guardar en el stack el valor de un registro."""
        # Seleccionar el registro menos reciente
        spilled_reg = list(self.registers.keys())[0]
        spilled_value = self.registers[spilled_reg]
        # Guardar el valor en el stack
        self.stack.append((spilled_value, spilled_reg))
        self.registers[spilled_reg] = var_name
        return spilled_reg
    def loadFromStack(self, var_name):
        """Cargar una variable del stack a un registro."""
        for i, (value, reg) in enumerate(self.stack):
            if value == var_name:
                self.stack.pop(i)
                self.registers[reg] = var_name
                return reg
        raise ValueError(f"Variable {var_name} no encontrada en el stack.")

def main(argv):
    register_manager = RegisterManager()

    # Leer el código desde stdin (el código que se envía desde Django)
    input_stream = FileStream(f"{os.getcwd()}/compiler/Textos/Brolo1.txt")
    # input_stream = InputStream(sys.stdin.read())
    lexer = CompiScriptLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiScriptLanguageParser(stream)
    tree = parser.program()  # Usar 'program' como regla inicial según la gramática CompiScript
    
    semantic_visitor = CompiScriptVisitorSemantic()
    
    # Generar el árbol como texto
    tree_str = Trees.toStringTree(tree, None, parser)
    print(tree_str)
    print(tree)
    
    semantic_visitor.visit(tree)
    semantic_visitor.imprimirTablaDeSimbolos()

    tac_visitor = CompiScriptTacVisitor(semantic_visitor.TablaDeAmbitos, semantic_visitor.node_ids, register_manager)  # Crear instancia del visitor TAC
    tac_visitor.visit(tree)  # Recorrer el árbol de sintaxis con el visitor TAC
    
    # Obtener las instrucciones TAC generadas
    tac_visitor.generateTAC()
    tac_instructions = tac_visitor.instructions  # Lista de instrucciones TAC

if __name__ == '__main__':
    main(sys.argv)
