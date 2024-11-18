import sys
from antlr4 import *
from Syntax.CompiScriptLanguageLexer import *
from Syntax.CompiScriptLanguageParser import *
from Semantic.CompiScriptVisitorSemantic import *
from Syntax.CompiScriptLanguageVisitor import *
from TAC.CompiScriptTacVisitor import CompiScriptTacVisitor
from MIPS.TACToMIPSVisitor import TacToMipsVisitor
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

def create_visual_tree(tree, parser):
    # Generate the DOT format string
    tree_dot = Trees.toStringTree(tree, None, parser)
    
    # Print DOT format for inspection
    print(tree_dot)
    
    # Save the DOT format to a file
    with open("parse_tree.dot", "w") as dot_file:
        dot_file.write(tree_dot)
    
    # Use graphviz to create a visualization of the tree
    dot = graphviz.Source.from_file("parse_tree.dot")
    dot.render("parse_tree", format="png", cleanup=True)

def main(argv):
    register_manager = RegisterManager()

    # Leer el código desde stdin (el código que se envía desde Django)
    input_stream = FileStream(f"{os.getcwd()}/compiler/Textos/pruebasRegistros.txt")
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
    
    # Descomenta si deseas generar la visualización del árbol
    # create_visual_tree(tree, parser)

    semantic_visitor.visit(tree)
    semantic_visitor.imprimirTablaDeSimbolos()

    tac_visitor = CompiScriptTacVisitor(semantic_visitor.TablaDeAmbitos, semantic_visitor.node_ids, register_manager)  # Crear instancia del visitor TAC
    tac_visitor.visit(tree)  # Recorrer el árbol de sintaxis con el visitor TAC
    
    # Obtener las instrucciones TAC generadas
    tac_visitor.generateTAC()
    tac_instructions = tac_visitor.instructions  # Lista de instrucciones TAC
    
    mips_visitor = TacToMipsVisitor(tac_instructions, register_manager)
    mips_code = mips_visitor.translate()

    # Imprimir el código MIPS en la consola
    print("\n=== Código MIPS generado ===")
    print(mips_code)

if __name__ == '__main__':
    main(sys.argv)
