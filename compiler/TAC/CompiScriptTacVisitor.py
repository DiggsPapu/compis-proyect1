# Generated from CompiScriptLanguage.g4 by ANTLR 4.13.1
from antlr4 import *

from Semantic.Structures import Stack

from .Structures import Cuadrupleta
if "." in __name__:
    from Syntax.CompiScriptLanguageParser import CompiScriptLanguageParser
else:
    from Syntax.CompiScriptLanguageParser import CompiScriptLanguageParser
from antlr4.tree.Tree import TerminalNodeImpl

# This class defines a complete generic visitor for a parse tree produced by CompiScriptLanguageParser.

class CodeGenerator:
    def _init_(self):
        self.label_counter = 0
        self.code = []

    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def emit(self, code_line):
        self.code.append(code_line)

    def get_code(self):
        return "\n".join(self.code)

class CompiScriptTacVisitor(ParseTreeVisitor):
    def __init__(self, tablaDeAmbitos, correspondenciaNodosAmbitos):
        self.instructions = []  # Lista para almacenar las instrucciones TAC
        self.temp_counter = 0  # Contador para los temporales
        self.tablaDeAmbitos = tablaDeAmbitos    # Tabla de ámbitos con tabla de símbolos y de tipos
        self.correspondenciaNodosAmbitos = correspondenciaNodosAmbitos  # Diccionario que relaciona nodos con ámbitos
        self.ambitoActual = None    # Ámbito actual
        self.label_counter = self.tablaDeAmbitos.size()
        self.stackAmbitos = Stack()
        self.intoAmbito = False
        self.code = []

    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def emit(self, code_line):
        self.code.append(code_line)

    def get_code(self):
        return "\n".join(self.code)
    
    def generateTAC(self):
        for ambitoIndex in range(self.tablaDeAmbitos.size()-1,-1,-1):
            ambito = self.tablaDeAmbitos.get(ambitoIndex)
            print(ambito.labelAmbito+":")
            for instruccion in ambito.codigo:
                if instruccion.operacion == 'if':
                    print(f'    {instruccion.operacion} {instruccion.arg1} {instruccion.resultado}')
                elif instruccion.operacion == 'else':
                    print(f'    {instruccion.operacion} {instruccion.resultado}')
                elif instruccion.operacion == 'new_label':
                    print(f'    {instruccion.resultado}:')
                else: print(f'  {instruccion.resultado} = {instruccion.arg1} {instruccion.operacion if instruccion.operacion else ""} {instruccion.arg2 if instruccion.arg2 else ""}')
        
    def visit(self, ctx):
        """
        This method is called each time a node is visited explicitly.
        """
        # Asignar el ambito actual
        self.ambitoActual = self.correspondenciaNodosAmbitos.get(ctx)
        if self.intoAmbito:
            self.stackAmbitos.push(self.ambitoActual)
            self.intoAmbito = False
        # Visit the children of the node (traverse the tree)
        return super().visit(ctx)

    def visitChildren(self, ctx):
        """
        This method is called each time a node's children are visited.
        """
        self.ultimoAmbito = self.ambitoActual
        # Asignar el ambito actual
        self.ambitoActual = self.correspondenciaNodosAmbitos.get(ctx)
        # Continue visiting the children as usual
        return super().visitChildren(ctx)
    
    # Método para obtener un nuevo temporal  
    def new_temp(self):
        temp = f'_t{self.temp_counter}'  # Crear un nuevo temporal
        self.temp_counter += 1
        return temp
    
    # Método para manejar una operacion basica
    def handleBasicOperation(self, ctx):
        def procesar_operadores(operadores, operandos):
            # Procesar operadores con mayor precedencia (* y /)
            while len(operadores) > 0:
                operador = operadores.pop(0)
                operando1 = operandos.pop(0)
                operando2 = operandos.pop(0)
                
                instruction = Cuadrupleta()
                instruction.arg1 = operando1
                instruction.operacion = operador
                instruction.arg2 = operando2
                instruction.resultado = self.new_temp()  # Crear temporal para el resultado
                
                self.tablaDeAmbitos.get(self.ambitoActual).aniadirCodigo(instruction)
                operandos.insert(0, instruction.resultado)  # Insertar el resultado de vuelta a los operandos
        
        # Si solo hay un término (número o variable)
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))
        
        # Separar operadores y operandos
        operandos = []
        operadores = []
        
        for i in range(ctx.getChildCount()):
            if i % 2 == 0:  # Es un operando
                operandos.append(self.visit(ctx.getChild(i)))
            else:  # Es un operador
                operadores.append(ctx.getChild(i).getText())
        
        # Primero, procesar operadores de mayor precedencia (*, /)
        operadores_pendientes = []
        operandos_pendientes = [operandos.pop(0)]  # El primer operando

        i = 0
        while i < len(operadores):
            operador = operadores[i]
            if operador in ['*', '/', '%', 'and', '>', '>=', '<', '<=', '!=', '==']:
                instruction = Cuadrupleta()
                instruction.arg1 = operandos_pendientes.pop()  # Último operando procesado
                instruction.operacion = operador
                instruction.arg2 = operandos.pop(0)  # Siguiente operando
                
                instruction.resultado = self.new_temp()  # Crear temporal para el resultado
                self.tablaDeAmbitos.get(self.ambitoActual).aniadirCodigo(instruction)
                
                operandos_pendientes.append(instruction.resultado)  # Guardar el resultado
            else:
                operadores_pendientes.append(operador)
                operandos_pendientes.append(operandos.pop(0))  # Guardar el siguiente operando pendiente
            i += 1
        
        # Luego, procesar operadores de menor precedencia (+, -)
        procesar_operadores(operadores_pendientes, operandos_pendientes)
        
        # El último resultado es el valor final
        return operandos_pendientes[0]
                
    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#declaration.
    def visitDeclaration(self, ctx:CompiScriptLanguageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        instruccion = Cuadrupleta()
        instruccion.resultado = ctx.IDENTIFIER().getText()
        instruccion.arg1 = self.visit(ctx.expression()) if ctx.expression() else "null"
        self.tablaDeAmbitos.get(self.ambitoActual).aniadirCodigo(instruccion)
        return instruccion.resultado


    # Visit a parse tree produced by CompiScriptLanguageParser#statement.
    def visitStatement(self, ctx:CompiScriptLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        ambitoIf = self.ambitoActual
        rangoBlock = len(ctx.block())
        rangoExpr = len(ctx.expression())
        ifInstr = []
        for index in range(rangoBlock-1,-1,-1):
            instruccion = Cuadrupleta()
            # Generar el codigo del bloque de primero
            self.visit(ctx.block(index))
            # Significa que hay un else
            if rangoBlock>rangoExpr and index==rangoBlock-1:
                instruccion.operacion = 'else'
                instruccion.resultado = f'goto {self.tablaDeAmbitos.get(self.ultimoAmbito).labelAmbito}'
            else:
                instruccion.operacion = 'if'
                instruccion.arg1 = self.visit(ctx.expression(index))
                instruccion.resultado = f'goto {self.tablaDeAmbitos.get(self.ultimoAmbito).labelAmbito}'
            ifInstr.append(instruccion)
        ifInstr.reverse()
        for instruccion in ifInstr: 
            self.tablaDeAmbitos.get(ambitoIf).aniadirCodigo(instruccion)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        self.instructions.append(f'print {ctx.expression().getText()}')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#array.
    def visitArray(self, ctx:CompiScriptLanguageParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arrayCreation.
    def visitArrayCreation(self, ctx:CompiScriptLanguageParser.ArrayCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arrayAccess.
    def visitArrayAccess(self, ctx:CompiScriptLanguageParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arrayPush.
    def visitArrayPush(self, ctx:CompiScriptLanguageParser.ArrayPushContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arrayPop.
    def visitArrayPop(self, ctx:CompiScriptLanguageParser.ArrayPopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logic.
    def visitLogic(self, ctx:CompiScriptLanguageParser.LogicContext):
        return self.handleBasicOperation(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        return self.handleBasicOperation(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx: CompiScriptLanguageParser.TermContext):
        return self.handleBasicOperation(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#unary.
    def visitUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        # En caso de que sea una call que retorne solo el call
        if ctx.call():
            return self.visit(ctx.call())
        # Esto implica que puede negarse el valor o puede volverse negativo
        if ctx.unary():
            instruction = Cuadrupleta()
            # Para el unary vamos a crear un temporal que almacene los valores de la operación booleana en cuestion
            instruction.resultado = self.new_temp()
            instruction.operacion = self.visit(ctx.getChild(0))
            instruction.arg1 = self.visit(ctx.unary())
            self.tablaDeAmbitos.get(self.ambitoActual).aniadirCodigo(instruction)
            return instruction.resultado


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        if ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.STRING():
            return ctx.STRING().getText()
        elif ctx.expression():
            return self.visit(ctx.expression())
        elif ctx.getText() == "false" or ctx.getText() == "true" or "nil": return ctx.getText()
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        return self.visitChildren(ctx)