# Generated from CompiScriptLanguage.g4 by ANTLR 4.13.1
import re
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
        self.label_counter = 0
        self.stackAmbitos = Stack()
        self.intoAmbito = False
        self.code = []
        self.declarandoVariable = None
    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def emit(self, code_line):
        self.code.append(code_line)

    def get_code(self):
        return "\n".join(self.code)
    
    def generateTAC(self):
        for instruccion in self.tablaDeAmbitos.get(0).codigo:
            if instruccion.operacion == 'if':
                print(f'    {instruccion.operacion} {instruccion.arg1} {instruccion.resultado}')
            elif instruccion.operacion==None and re.search(r'goto', instruccion.resultado):
                print(f'    {instruccion.resultado}')
            elif instruccion.operacion == 'new_label':
                print(f'{instruccion.resultado}:')
            elif instruccion.operacion == '=':
                print(f'    {instruccion.resultado} = {instruccion.arg1}')
            else: 
                print(f'    {instruccion.resultado} = {instruccion.arg1} {instruccion.operacion if instruccion.operacion else ""} {instruccion.arg2 if instruccion.arg2 else ""}')
        
    def visit(self, ctx):
        """
        This method is called each time a node is visited explicitly.
        """
        self.ultimoAmbito = self.ambitoActual
        # Asignar el ambito actual
        self.ambitoActual = self.correspondenciaNodosAmbitos.get(ctx)
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
                
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruction)
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
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruction)
                
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
        self.declarandoVariable = instruccion.resultado
        instruccion.arg1 = self.visit(ctx.expression()) if ctx.expression() else "null"
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruccion)
        self.declarandoVariable = None
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
        blockInstr = []
        for index in range(rangoBlock-1,-1,-1):
            instruccion = Cuadrupleta()
            instruccionLabel = Cuadrupleta()
            instruccionLabel.operacion = 'new_label'
            instruccionLabel.resultado = self.new_label()
            blockInstr.append(instruccionLabel)
            # Generar el codigo del bloque de primero
            self.visit(ctx.block(index))
            # Aniadir el bloque de codigo al ambito actual
            blockInstr.extend(self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).codigo)
            self.ultimoAmbito = self.ambitoActual
            self.ambitoActual = ambitoIf
            # Significa que hay un else
            if rangoBlock>rangoExpr and index==rangoBlock-1:
                instruccion.resultado = f'goto {instruccionLabel.resultado}'
            else:
                instruccion.operacion = 'if'
                instruccion.resultado = f'goto {instruccionLabel.resultado}'
                instruccion.arg1 = self.visit(ctx.expression(index))
            ifInstr.append(instruccion)
        ifInstr.reverse()
        for instruccion in ifInstr: 
            self.tablaDeAmbitos.get(ambitoIf).aniadirCodigo(instruccion)
        for instruccion in blockInstr:
            self.tablaDeAmbitos.get(ambitoIf).aniadirCodigo(instruccion)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        ambitoFor = self.ambitoActual
        # la declaracion de variable debe de estar en el flujo normal por ende no estara dentro del label
        if ctx.varDecl():
            self.visit(ctx.varDecl())
        # Crear un nuevo label para evaluar la condicion del for
        checkLabel = Cuadrupleta()
        checkLabel.operacion = 'new_label'
        checkLabel.resultado = self.new_label()
        self.tablaDeAmbitos.get(ambitoFor).aniadirCodigo(checkLabel)
        # Crear un nuevo label para evaluar el bloque del for
        blockLabel = Cuadrupleta()
        blockLabel.operacion = 'new_label'
        blockLabel.resultado = self.new_label()
        # Esta puede declarar condiciones por lo que asumiremos que sera el goto y que hace el chequeo en el for semantico
        if ctx.exprStmt():
            self.visit(ctx.exprStmt())
        # La primera expresion suele ser la de la condicion en vez del exprStmt
        elif ctx.expression():
            instruccion = Cuadrupleta()
            instruccion.operacion = 'if'
            instruccion.arg1 = self.visit(ctx.expression(0))
            instruccion.resultado = f'goto {blockLabel.resultado}'
        # Aniadir el label del bloque para que lo demas sea parte del bloque
        self.tablaDeAmbitos.get(ambitoFor).aniadirCodigo(blockLabel)
        # Condicion de sumar o lo que sea de la segunda expresion, eso va adentro del bloque
        if len(ctx.expression())>1:
            self.visit(ctx.expression(1))
        # Generar el bloque de codigo del for
        self.visit(ctx.block())
        # Agregar el goto para el bloque del for para que evalue la condicion
        instruccion = Cuadrupleta()
        instruccion.resultado = f'goto {checkLabel.resultado}'
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruccion)
        # Aniadir el bloque de codigo al ambito actual
        self.tablaDeAmbitos.get(ambitoFor).codigo.extend(self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).codigo)


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        ambitoWhile = self.ambitoActual
        # Crear un nuevo label para evaluar la condicion del while
        checkLabel = self.new_label()
        # Crear una instruccion en el flujo para que lleve al nuevo label en cuestión
        instruccion = Cuadrupleta()
        instruccion.resultado = f'goto {checkLabel}'
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)
        # Crear una instruccion que sea un nuevo label
        instruccion = Cuadrupleta()
        instruccion.operacion = 'new_label'
        instruccion.resultado = checkLabel
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)
        # Crear una instruccion que sea un if
        instruccion = Cuadrupleta()
        instruccion.operacion = 'if'
        instruccion.arg1 = self.visit(ctx.expression())
        # Crear un nuevo label para el bloque del while
        blockLabel = Cuadrupleta()
        blockLabel.resultado = self.new_label()
        blockLabel.operacion = 'new_label'
        self.visit(ctx.block())
        self.ultimoAmbito = self.ambitoActual
        self.ambitoActual = ambitoWhile
        # Irse al bloque del while
        instruccion.resultado = f'goto {blockLabel.resultado}'
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)
        # Aniadir el goto al bloque del while
        instruccion = Cuadrupleta()
        instruccion.resultado = f'goto {checkLabel}'
        self.tablaDeAmbitos.get(self.ultimoAmbito).aniadirCodigo(instruccion)
        # Aniadir el bloque del while al ambito actual
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(blockLabel)
        for instruccion in self.tablaDeAmbitos.get(self.ultimoAmbito).codigo:
            self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)

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
        instruccion = Cuadrupleta()
        # O es un array de arrays o es algo con elementos primitivos
        if ctx.logic() or ctx.array():
            direccionesDeMemoria = []
            inicial = None
            for index in range(len(ctx.logic() if ctx.logic() else ctx.array())):
                # Instruccion de temporal del valor
                valor = Cuadrupleta(arg1=self.visit(ctx.logic(index) if ctx.logic() else ctx.array(index)),operacion='=',resultado=self.new_temp())
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(valor)
                # Instruccion de para la direccion de memoria
                direccion = Cuadrupleta(arg1=f'&{valor.resultado}',operacion='=',resultado=self.new_temp())
                if inicial == None: inicial = direccion.resultado
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(direccion)
                direccionesDeMemoria.append(direccion.resultado)
            for index in range(0,len(direccionesDeMemoria),2):
                direccion1 = direccionesDeMemoria[index]
                direccion2 = direccionesDeMemoria[index+1] if index+1<len(direccionesDeMemoria) else 'null'
                # Temporal para calcular la direccion de memoria que tendra el puntero
                punteroDireccion = Cuadrupleta(arg1=direccion1,operacion='+',arg2=16,resultado=self.new_temp()) # 16 bytes por direccion
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(punteroDireccion)
                # Temporal para asignar la direccion de memoria al puntero
                asignarMemoria = Cuadrupleta(arg1=direccion2,operacion='=',resultado=f'*{punteroDireccion.resultado}')
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(asignarMemoria)
                if index == len(direccionesDeMemoria)-2:
                    ultimoPuntero = Cuadrupleta(arg1=direccion2,operacion='+',arg2=16,resultado=self.new_temp()) # 16 bytes por direccion
                    self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(ultimoPuntero)
                    self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(arg1='null',operacion='=',resultado=f'*{ultimoPuntero.resultado}'))
            return inicial
        # Es un array vacío
        else:
            instruccion = Cuadrupleta(arg1='null', operacion='=', resultado=self.new_temp())
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruccion)
            # Temporal para calcular la direccion de memoria que tendra el puntero
            punteroDireccion = Cuadrupleta(arg1=instruccion.resultado,operacion='+',arg2=16,resultado=self.new_temp()) # 16 bytes por direccion
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(punteroDireccion)
            # Temporal para asignar la direccion de memoria al puntero
            asignarMemoria = Cuadrupleta(arg1='null',operacion='=',resultado=f'*{punteroDireccion.resultado}')
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(asignarMemoria)
            return f'&{instruccion.resultado}'
            
        


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
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruction)
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
        # Crear una instruccion para el label de la funcion
        instruccion = Cuadrupleta()
        instruccion.operacion = 'new_label'
        instruccion.resultado = ctx.IDENTIFIER().getText()
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruccion)
        # Generar el código de la función
        self.visit(ctx.block())


    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        return self.visitChildren(ctx)