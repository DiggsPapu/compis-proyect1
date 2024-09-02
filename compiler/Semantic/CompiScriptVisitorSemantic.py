from Syntax.CompiScriptLanguageVisitor import *
from Syntax.CompiScriptLanguageParser import *
from .Structures import HashMap, Ambito, Variable, Numero, Nil, Simbolo, Tipo, TipoFuncion, Funcion, Booleano, DefinidoPorUsuario, Stack, Campo, Parametro, Cadena, Metodo
from antlr4.tree.Tree import TerminalNodeImpl
import re
# Manejo de errores lexicos
class LexicalError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} at line {line}, column {column}")
        self.line = line
        self.column = column
# Manejo de errores Sintacticos
class ParsingError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} at line {line}, column {column}")
        self.line = line
        self.column = column
class SemanticError(Exception):
    def __init__(self, message):
        super().__init__(message)    
# Implementacion
class CompiScriptVisitorSemantic(CompiScriptLanguageVisitor):
    def __init__(self) -> None:
        super().__init__()
        # Tabla de simbolos por ambito entonces por cada ambito (contexto) habra una tabla de simbolos
        self.TablaDeAmbitos = HashMap()
        self.TablaDeAmbitos.put(0, Ambito(0, HashMap()))
        self.stackAmbitos = Stack([0])
        self.currentFuncion = Stack()
        self.classDeclarationName = Stack()
        self.insideVariable = Stack()
        self.variableEnDefinicion = Stack()  
        
    def imprimirTablaDeSimbolos(self):
        llaves = self.TablaDeAmbitos.keys()
        for llave in llaves:
            ambito:Ambito = self.TablaDeAmbitos.get(llave)
            print(f'''ambito: {ambito.identificadorAmbito}''')
            keys = ambito.tablaDeSimbolos.keys()
            for key in keys:
                symbol:Simbolo
                symbol = ambito.tablaDeSimbolos.get(key)
                print(f'''
                  nombre simbolo: {symbol.nombreSimbolo}    ambito del simbolo: {symbol.ambito}     tipo del simbolo: {symbol.tipo}
                  ''')
    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        # Recorrer el programa
        for child in ctx.declaration():
            self.visit(child)


    # Visit a parse tree produced by CompiScriptLanguageParser#declaration.
    def visitDeclaration(self, ctx:CompiScriptLanguageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        self.visit(ctx.function())


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        # Esta mal escrito y no se puede obtener la variable en la definicion de la variable
        if ctx.IDENTIFIER() == None:
            raise SemanticError(f'Error semantico, declaracion de variable invalida')
        # Obtener el nombre del simbolo
        id = ctx.IDENTIFIER().symbol.text
        # Setear el tipo de la variable a Nil inicialmente
        variableTipo = Nil()
        # La variable en definicion actual es esa, se setea asi porque puede que hayan mas variables en definicion dentro de esta como en clases
        self.variableEnDefinicion.insert(id)
        # Si ya hay una variable definida entonces se lanza un error de redeclaracion de variable
        if self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.contains_key(id):
            raise SemanticError(f"Error semantico, no se puede re declarar una variable ya creada en el ambito, \"{id}\"")
        if ctx.expression():
            # Obtener tipo
            variableTipo = self.visit(ctx.expression())
            if isinstance(variableTipo, Simbolo):
                variableTipo = variableTipo.tipo
        self.variableEnDefinicion.remove_first()
        # Inicializar la variable y definir el tipo, no hay return
        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(id,Variable(nombreSimbolo=id,tipo=variableTipo,inicializador=variableTipo))

    # Visit a parse tree produced by CompiScriptLanguageParser#statement.
    def visitStatement(self, ctx:CompiScriptLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        # Visitarlo para ver que todo este correcto
        self.visit(ctx.expression())


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        # Evaluar la expresión condicional del while
        condicion = self.visit(ctx.expression())
        # Verificar que la condición sea un booleano
        if not isinstance(condicion, Booleano):
            raise SemanticError(f"Error semántico: la condición del while no es un valor booleano.")
        # Retornar lo que sea que diga el bloque, solo hay que chequear que lo que haya dentro del statement sea un bloque
        return self.visit(ctx.statement())


    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logic.
    def visitLogic(self, ctx:CompiScriptLanguageParser.LogicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#unary.
    def visitUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        # En caso de que sea una call que retorne solo el call
        if ctx.call():return self.visit(ctx.call())
        # Esto implica que puede negarse el valor o puede volverse negativo
        if ctx.unary():
            operation, variable = None
            for child in ctx.getChildren():
                variableTemp = self.visit(child)
                # Obtener el tipo del simbolo
                if isinstance(variableTemp, Variable) or isinstance(variableTemp, Parametro) or isinstance(variableTemp, Campo):variableTemp = variableTemp.tipo
                # Manejo de las operaciones
                if not operation == '!' and (isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='-'):operation = '-'
                elif not operation == '-' and (isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='!'):operation = '!'
                elif isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='-' or isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='!': raise SemanticError(f'Error semantico, no se puede negar un booleano con \'-\' o negar un número con \'!\'')
                # Manejo de los tipos
                elif variable == None and isinstance(variableTemp, Numero) and operation == '-':variable = Numero() 
                elif variable == None and isinstance(variableTemp, Booleano) and operation == '!':variable = Booleano()
                elif isinstance(variable, Numero) and isinstance(variableTemp, Numero) and operation == '-':variable = Numero() 
                elif isinstance(variable, Booleano) and isinstance(variableTemp, Booleano) and operation == '!':variable = Booleano()
                else: raise  SemanticError(f'Error semantico, no se puede negar un no booleano o no se puede poner en negativo un no numero')
            # Retornar el tipo de la operacion
            return variable


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        # Primary es el tipo basico, puede ser casi cualquier cosa, una expresion, una definicion de variable, etc
        # En este caso puede ser una expresion, o super.IDENTIFIER entonces este se tiene que encargar del identifier
        if not ctx.expression() and ctx.getChildCount()>1:
            # Es un super, hay que chequear que se esta inicializando o se esta trabajando dentro de una clase
            if (self.classDeclarationName.first()!= None or (self.insideVariable.first()!=None and isinstance(self.insideVariable.first(), DefinidoPorUsuario))) and self.visit(ctx.getChild(0)) == "super":
                # Ejecutar la funcion del super
                # Buscar la clase que se esta inicializando
                claseInicializando:DefinidoPorUsuario = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(self.classDeclarationName.first())
                retorno = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{claseInicializando.inheritance}.{ctx.getChild(2)}')
                if retorno == None:
                    raise SemanticError(f"La super clase \"{ctx.getChild(2)}\" invocada no existe")
                # Retornar la funcion a ejecutar -> heredada
                return retorno
        # Es una variable o es un super.IDENTIFIER hay que buscarlo en la tabla de simbolos
        if ctx.IDENTIFIER():
            id = ctx.IDENTIFIER().symbol.text
            ambitoActual:Ambito = self.TablaDeAmbitos.get(self.stackAmbitos.first())
            tablaDeTiposActual:HashMap = ambitoActual.tablaDeTipos
            tablaDeSimbolosActual:HashMap = ambitoActual.tablaDeSimbolos
            # Puede retornar una variable o el nombre de una funcion
            if (tablaDeSimbolosActual.get(id)== None and tablaDeTiposActual.get(id)==None):
                raise SemanticError(f"Error semantico la variable, la clase o la funcion \"{id}\" no existe")
            return tablaDeSimbolosActual.get(id)
        # Tipo numero
        elif ctx.NUMBER(): return Numero()
        # Tipo string
        elif ctx.STRING():
            return Cadena()
        # Tipo booleano
        elif ctx.getText() == "false" or ctx.getText() == "true":
            return Booleano()
        # Tipo booleano
        elif ctx.getText() == "nil":
            return Nil()
        # Expresion a resolver
        elif ctx.expression():
            return self.visit(ctx.expression())
        # Acceder a un valor para asignarlo o desde un metodo para hacer algo con el
        elif ctx.getText() == "this":
            return "this"
        return self.visitChildren(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        nombreFuncion = ctx.IDENTIFIER().symbol.text
        funcion = None
        # En caso de que no se este declarando una clase
        if (self.classDeclarationName.first()==None):
            self.currentFuncion = nombreFuncion
            funcion = Funcion(nombreFuncion, TipoFuncion(), self.stackAmbitos.first())
        # Metodos de una clase
        else:
            nombreFuncion = self.classDeclarationName.first()+"."+nombreFuncion
            # en este caso basicamente solo hay que obtener los fields de la clase
            funcion = Metodo(nombreSimbolo=nombreFuncion, tipo=TipoFuncion(), ambito=self.stackAmbitos.first())
        # Si la funcion/metodo tiene parametros
        if ctx.parameters():
            # Obtener los parametros y meterlos en la tabla de simbolos actual no la de la funcion para desglosar la funcion
            parametros = self.visit(ctx.parameters())
            for parametro in parametros:
                # Solamente almacenar el parametro en la funcion
                funcion.aniadirParametro(parametro)
        # Solamente se va a almacenar el contexto de la ejecucion de la funcion
        funcion.aniadirContexto(ctx.block())
        # Agregar la funcion al ambito actual de la tabla de simbolos
        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(nombreFuncion, funcion)
            
        
    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        # Esta visita de parametros solo se puede hacer cuando se instancia la funcion
        if ctx.IDENTIFIER():
            if ctx.getChildCount()>1:
                if type(ctx.IDENTIFIER()) == list:
                    parametros = []
                    for parametro in ctx.IDENTIFIER():
                        # Aniadir el parametro a la lista para instanciarlo en el contexto superior de funcion
                        parametros.append(parametro.symbol.text)
                    # retornar el array con los parametros
                    return parametros
            else:
                # retornar un array con el unico parametro
                return [ctx.getChild(0).symbol.text]
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        arguments = []
        for child in ctx.getChildren():
            if isinstance(child, CompiScriptLanguageParser.ExpressionContext):
                arguments.append(child)
            else:
                self.visit(child)
        return arguments
    
    # Encontrar nodos de error
    def visitErrorNode(self, node: ErrorNode):
        # Lanzar errores
        raise ParsingError(f"Syntax error, encountered: {node.getText()}", node.symbol.line, node.symbol.column)
    
    # Chequeo para verificar si es o no un nodo malformado
    def visitTerminal(self, node):
        # Verifica si el token es malformado
        if node.symbol.type == CompiScriptLanguageParser.MALFORMED:
            line = node.symbol.line
            column = node.symbol.column
            raise LexicalError(f"Unrecognized token '{node.getText()}'", line, column)
        # Continua con la visita normal
        self.visitChildren(node)
        return node.symbol.text