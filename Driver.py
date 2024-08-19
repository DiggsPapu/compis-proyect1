import sys
from antlr4 import *
from Syntax.CompiScriptLanguageLexer import *
from Syntax.CompiScriptLanguageParser import *
from Semantic.CompiScriptVisitor import *
from Syntax.CompiScriptLanguageVisitor import *
from antlr4.tree.Trees import Trees
import graphviz
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
    input_stream = FileStream('./Textos/Statement.txt')
    lexer = CompiScriptLanguageLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CompiScriptLanguageParser(stream)
    tree = parser.program()  # We are using 'program' since this is the starting rule based on our CompiScriptLanguage grammar, yay!
    
    visitor = CompiScriptVisitor()
    
    # Genera el árbol como texto
    tree_str = Trees.toStringTree(tree, None, parser)
    print(tree_str)
    print(tree)
    # create_visual_tree(tree, parser)

    visitor.visit(tree)
    
if __name__ == '__main__':
    main(sys.argv)
