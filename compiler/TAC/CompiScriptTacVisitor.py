# Generated from CompiScriptLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from Syntax.CompiScriptLanguageParser import CompiScriptLanguageParser
else:
    from Syntax.CompiScriptLanguageParser import CompiScriptLanguageParser

# This class defines a complete generic visitor for a parse tree produced by CompiScriptLanguageParser.

class CompiScriptTacVisitor(ParseTreeVisitor):
    def __init__(self):
        self.instructions = []  # Lista para almacenar las instrucciones TAC
        self.temp_counter = 0  # Contador para los temporales
    
    def new_temp(self):
        temp = f't{self.temp_counter}'  # Crear un nuevo temporal
        self.temp_counter += 1
        return temp

    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx: CompiScriptLanguageParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#declaration.
    def visitDeclaration(self, ctx: CompiScriptLanguageParser.DeclarationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        # Evaluar la expresión en el lado derecho de la asignación
        expr_value = self.visit(ctx.expression())  # Esto debería devolver el resultado de la operación binaria
        # print(expr_value)
        # Añadir la instrucción de asignación a TAC
        self.instructions.append({
            'operacion': 'assign',
            'arg1': expr_value,  # Aquí debería ir el resultado de la expresión evaluada
            'arg2': None,
            'resultado': ctx.IDENTIFIER().getText()  # El identificador de la variable
        })
        return None

    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitExpression(self, ctx: CompiScriptLanguageParser.ExpressionContext):
        return self.visit(ctx.logic())  # Descender en el árbol al nodo 'logic'

    # Visit a parse tree produced by CompiScriptLanguageParser#logic.
    def visitLogic(self, ctx: CompiScriptLanguageParser.LogicContext):
        return self.visit(ctx.comparison())  # Descender al nodo 'comparison'

    def visitComparison(self, ctx: CompiScriptLanguageParser.ComparisonContext):       
        terms = ctx.term()

        if isinstance(terms, list) and len(terms) > 1:  # Si hay múltiples términos
            left = self.visit(terms[0])  # Procesar el primer término
            print(f"Primer término: {left}")
            for i in range(1, len(terms)):
                operator = ctx.getChild(2 * i - 1).getText()  # Obtener el operador
                right = self.visit(terms[i])  # Procesar el siguiente término
                print(f"Operador: {operator}, Derecho: {right}")
                result = self.new_temp()  # Crear un temporal para el resultado

                # Generar la instrucción TAC para esta operación
                self.instructions.append({
                    'operacion': operator,
                    'arg1': left,
                    'arg2': right,
                    'resultado': result
                })
                left = result  # El resultado se convierte en el nuevo 'left'
            return left  # Devolver el último resultado
        else:
            return self.visit(terms[0])

    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx: CompiScriptLanguageParser.TermContext):        
        if ctx.getChildCount() == 3:  # Caso de una operación binaria simple
            left = self.visit(ctx.getChild(0))  # Lado izquierdo de la operación
            operator = ctx.getChild(1).getText()  # Operador
            right = self.visit(ctx.getChild(2))  # Lado derecho de la operación
            result = self.new_temp()  # Crear un temporal para el resultado

            # Generar la instrucción TAC
            self.instructions.append({
                'operacion': operator,
                'arg1': left,
                'arg2': right,
                'resultado': result
            })
            return result
        
        elif ctx.getChildCount() > 3:  # Caso de una expresión con más de un operador
            # Proceso de operadores múltiples: resolver según la precedencia
            left = self.visit(ctx.getChild(0))  # Procesar el primer término
            for i in range(1, ctx.getChildCount(), 2):  # Iterar sobre los operadores y términos
                operator = ctx.getChild(i).getText()  # Obtener el operador
                right = self.visit(ctx.getChild(i + 1))  # Procesar el siguiente término
                result = self.new_temp()  # Crear un temporal para el resultado

                # Generar la instrucción TAC
                self.instructions.append({
                    'operacion': operator,
                    'arg1': left,
                    'arg2': right,
                    'resultado': result
                })
                left = result  # El resultado se convierte en el nuevo 'left' para la siguiente iteración
            return left
        
        elif ctx.getChildCount() == 1:  # Un solo término, como un número o variable
            return self.visit(ctx.getChild(0))  # Visitar el valor del término
        
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        if ctx.NUMBER():  # Si es un número
            return ctx.NUMBER().getText()  # Devolver el valor del número como string
        elif ctx.IDENTIFIER():  # Si es una variable
            return ctx.IDENTIFIER().getText()  # Devolver el nombre de la variable
        else:
            return self.visitChildren(ctx)  # Para otros casos

    # Método para obtener las instrucciones TAC generadas
    def get_tac(self):
        return self.instructions

    # Visit a parse tree produced by CompiScriptLanguageParser#logic.
    def visitLogic(self, ctx:CompiScriptLanguageParser.LogicContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#unary.
    def visitUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        return self.visit(ctx.call())  # Descender a 'call'

    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        return self.visit(ctx.primary())  # Descender a 'primary'

    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        return self.visitChildren(ctx)
