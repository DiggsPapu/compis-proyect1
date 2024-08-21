from Syntax.CompiScriptLanguageVisitor import *
from Syntax.CompiScriptLanguageParser import *
from Structures.HashMap import *
from Structures.Ambito import *
from Structures.Simbolos.Simbolo import *
from Structures.Simbolos.Variable import *
from Structures.Simbolos.Funcion import *
from Structures.Simbolos.Parametro import *
from Structures.Tipos.Tipo import *
from Structures.Tipos.TipoFuncion import *
from Structures.Tipos.Numero import *
from Structures.Tipos.Nil import *
from Structures.Tipos.Cadena import *
from Structures.Tipos.Booleano import *
from Structures.Ambito import *
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
class CompiScriptVisitor(CompiScriptLanguageVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.TablaDeTipos = HashMap()
        # Tabla de simbolos por ambito entonces por cada ambito (contexto) habra una tabla de simbolos
        self.TablaDeAmbitos = HashMap()
        self.ambitoActual = 0
        self.ambitoPasado = 0
        self.cantidadDeParametrosDefinidos = 0
        self.cantidadDeVariablesDeRetorno = 0
        self.currentFuncion = None
    
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
        if (self.TablaDeAmbitos.size()==0):
            # Crear el contexto main que seria el contexto 0
            self.TablaDeAmbitos.put(0, Ambito(0, HashMap()))
            for child in ctx.declaration():
                self.visit(child)
        # En cualquier otro caso es que se esta dentro de un block que  puede ser declarado como un bloque o como una funcion
        else:
            # De manera que recorrer la declaracion sirve para declarar parametros o demas cosas dentro del ambito del bloque o funcion
            for child in ctx.declaration():
                self.visit(child)

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
        id = ctx.IDENTIFIER().symbol.text
        # Averiguaremos el tipo despues y la inicializacion despues
        ambito:Ambito = self.TablaDeAmbitos.get(self.ambitoActual)
        ambito.tablaDeSimbolos.put(id, Variable(nombreSimbolo=id, ambito=self.ambitoActual))
        # En caso de que tenga una expresion, porque puede que sea una variable solo definida sin inicializar
        if ctx.expression():
            # Obtener tipo
            variableTipo = self.visit(ctx.expression())
            # Inicializar la variable y definir el tipo porque al principio es nil
            ambito:Ambito= self.TablaDeAmbitos.get(self.ambitoActual)
            simbolo:Variable = ambito.tablaDeSimbolos.get(id) 
            simbolo.definirInicializador(variableTipo)
            simbolo.redefinirTipo(variableTipo)
            

    # Visit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        # Se hace la visita de los hijos completos porque se realiza un chequeo sintactico para verificar que el ; existe
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        # Lo unico que puede haber en un bloque es una declaracion
        for declarations in ctx.declaration():
            self.visit(declarations)


    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        # Solo es un logic_or
        if ctx.logic_or():
            return self.visit(ctx.logic_or())
        return self.visitChildren(ctx)
    

    # Visit a parse tree produced by CompiScriptLanguageParser#logic_or.
    def visitLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        # En caso de que sea solo un hijo entonces solo sera un logic_and
        if ctx.getChildCount() == 1:
            if type(ctx.logic_and())==list:
                for child in ctx.logic_and():
                    return self.visit(child)
            else:
                return self.visit(ctx.logic_and())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_and.
    def visitLogic_and(self, ctx:CompiScriptLanguageParser.Logic_andContext):
        # En caso de que sea solo un hijo entonces solo sera un equality
        if ctx.getChildCount() == 1:
            if type(ctx.equality())==list:
                for child in ctx.equality():
                    return self.visit(child)
            else:
                return self.visit(ctx.equality())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#equality.
    def visitEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        # En caso de que sea solo un hijo entonces solo sera un comparison
        if ctx.getChildCount() == 1:
            if type(ctx.comparison())==list:
                for child in ctx.comparison():
                    return self.visit(child)
            else:
                return self.visit(ctx.comparison())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        # En caso de que sea solo un hijo entonces solo sera un term
        if ctx.getChildCount() == 1:
            if type(ctx.term())==list:
                for child in ctx.term():
                    return self.visit(child)
            else:
                return self.visit(ctx.term())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        # En caso de que sea solo un hijo entonces solo sera un factor
        if ctx.getChildCount() == 1:
            if type(ctx.factor())==list:
                for child in ctx.factor():
                    return self.visit(child)
            else:
                return self.visit(ctx.factor())
        # En caso de que sea mas de un hijo probablemente sea una operacion aritmetica o un string
        # Averiguar el tipo de operacion es imperativo por lo que son los pares
        currentOperation = ''
        variable = None
        for index in range(0, ctx.getChildCount()):
            # Si es el primer hijo
            if index == 0:
                variable = self.visit(ctx.getChild(index))
            # Es operacion
            elif (index%2==1):
                child = ctx.getChild(index)
                currentOperation = self.visit(child)
            else:
                # variable o valor
                variableTemp = self.visit(ctx.getChild(index))
                # Si es suma y es cadena o numero, casteo implicito en caso de que sea string + numero
                if (isinstance(variable, Numero) or isinstance(variable, Cadena)) and (isinstance(variableTemp, Numero) or isinstance(variableTemp, Cadena)) and currentOperation=='+':
                    # Se asigna el valor de numero o cadena
                    if isinstance(variable, Cadena) or isinstance(variableTemp, Cadena): 
                        variable = Cadena()
                    else:
                        variable = Numero()
                # Si es resta es numero
                elif  isinstance(variable, Numero) and isinstance(variableTemp, Numero) and (currentOperation=='-'):
                    variable = Numero()
                else:
                    raise SemanticError(f'Error semantico, operacion invalida en suma o resta, tipo invalido')
        # Retorna el ultimo valor que obtiene la variable luego de operar
        return variable

    # Visit a parse tree produced by CompiScriptLanguageParser#factor.
    def visitFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        # En caso de que sea solo un hijo entonces solo sera un unary
        if ctx.getChildCount() == 1:
            if type(ctx.unary())==list:
                for child in ctx.unary():
                    return self.visit(child)
            else:
                return self.visit(ctx.unary())
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#unary.
    def visitUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        # En caso de que sea una call que retorne solo el call
        if ctx.call():
            call = ctx.call()
            return self.visit(ctx.call())
                
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        # en caso de que la cantidad de hijos sea 1 entonces solo es un primary lo que significa que no es una llamada a una funcion
        if ctx.getChildCount() == 1:
            if type(ctx.primary())==list:
                for child in ctx.primary():
                    return self.visit(child)
            else:
                return self.visit(ctx.primary())
        # En caso de que sean argumentos puede que haya algo como funcion().otrafuncion().otrafuncion2() o algo como funcion().identificador o identificadores
        else:
            idSimbolo = ""
            # Es necesario visitar los nodos en orden ya que puede que sean secuenciales como los ejemplos de arriba
            for index in range(0, ctx.getChildCount()):
                child = ctx.getChild(index)
                # El primero siempre sera un identifier entonces ese es el unico que se ignora
                if index == 0:
                    idSimbolo = self.visit(child)
                # Son argumentos, parametros a pasarle a la funcion
                elif isinstance(child, CompiScriptLanguageParser.ArgumentsContext):
                    self.visit(child)
                # Es un identifier, una propiedad
                elif isinstance(child, CompiScriptLanguageParser.PrimaryContext):
                    pass
                # Este es para verificar sintacticamente que todo bien
                else:
                    self.visit(child)
                    
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        # Primary es el tipo basico, puede ser casi cualquier cosa, una expresion, una definicion de variable, etc
        # Es una variable o es un super.IDENTIFIER hay que buscarlo en la tabla de simbolos
        if ctx.IDENTIFIER():
            id = ctx.IDENTIFIER().symbol.text
            ambitoActual:Ambito = self.TablaDeAmbitos.get(self.ambitoActual)
            tablaDeSimbolosActual:HashMap = ambitoActual.tablaDeSimbolos
            # Puede retornar una variable o el nombre de una funcion
            return tablaDeSimbolosActual.get(id)
            # # Esto implica que esta llevandose a cabo dentro del bloque de la funcion
            # if self.currentFuncion != None:
            #     # Para averiguar si es un parametro esta definido en la funcion
            #     for parametro in self.TablaDeAmbitos.get(self.ambitoPasado).get(self.currentFuncion):
            #         if parametro.nombreSimbolo == id:
            #             return True
            #     # Si no lo encontre entonces tal vez es una variable global y estaria definida en el contexto actual
            #     if tablaDeSimbolosActual.contains_key(id):
            #         return True
            #     # Si no es variable global entonces error semantico
            #     else:
            #         raise SemanticError(f"Error Semantico, variable o parametro {id} no existe en la funcion")
                
                
            
        # Tipo numero
        elif ctx.NUMBER():
            return Numero()
        # Tipo string
        elif ctx.STRING():
            return Cadena()
        # Tipo booleano
        elif ctx.getText() == "false" or ctx.getText() == "true":
            return Booleano()
        # Tipo booleano
        elif ctx.getText() == "nil":
            return Nil()
        
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        ambitoActual:Ambito = self.TablaDeAmbitos.get(self.ambitoActual)
        nombreFuncion = ctx.IDENTIFIER().symbol.text
        self.currentFuncion = nombreFuncion
        funcion = Funcion(nombreFuncion, TipoFuncion(), self.ambitoActual)
        # Si la funcion tiene parametros
        if ctx.parameters():
            # Obtener los parametros y meterlos en la tabla de simbolos actual no la de la funcion para desglosar la funcion
            parametros = self.visit(ctx.parameters())
            for parametro in parametros:
                # Solamente almacenar el parametro en la funcion
                funcion.aniadirParametro(parametro)
            
        # Solamente se va a almacenar el contexto de la ejecucion de la funcion
        funcion.aniadirContexto(ctx.block())
        # Agregar la funcion al ambito actual de la tabla de simbolos
        ambitoActual.tablaDeSimbolos.put(nombreFuncion, funcion)
        
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
                    return [parametro.symbol.text]
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        return self.visitChildren(ctx)
    
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
        # Averiguar la operacion que es
        elif node.symbol.text == '-':
            return '-'
        elif node.symbol.text == '+':
            return '+'
        elif node.symbol.text == '*':
            return '*'
        elif node.symbol.text == '/':
            return '/'
        elif node.symbol.text == '%':
            return '%'
        # Continua con la visita normal
        return self.visitChildren(node)