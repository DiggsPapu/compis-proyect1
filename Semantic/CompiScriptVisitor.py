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

class ParsingError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} at line {line}, column {column}")
        self.line = line
        self.column = column
        
# Implementacion
class CompiScriptVisitor(CompiScriptLanguageVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.TablaDeTipos = HashMap()
        # Tabla de simbolos por ambito entonces por cada ambito (contexto) habra una tabla de simbolos
        self.TablaDeAmbitos = HashMap()
        self.ambitoActual = 0
        self.cantidadDeParametrosDefinidos = 0
    
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
        # Crear el contexto main que seria el contexto 0
        self.TablaDeAmbitos.put(0, Ambito(0, HashMap()))
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
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


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
            return self.visit(ctx.call())
                
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        # en caso de que la cantidad de hijos sea 1 entonces solo es un primary
        if ctx.getChildCount() == 1:
            if type(ctx.primary())==list:
                for child in ctx.primary():
                    return self.visit(child)
            else:
                return self.visit(ctx.primary())
            
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        # Primary es el tipo basico, puede ser casi cualquier cosa, una expresion, una definicion de variable, etc
        # Es una variable o es un super.IDENTIFIER hay que buscarlo en la tabla de simbolos
        if ctx.IDENTIFIER():
            id = ctx.IDENTIFIER().symbol.text
            ambitoActual:Ambito = self.TablaDeAmbitos.get(self.ambitoActual)
            tablaDeSimbolosActual:HashMap = ambitoActual.tablaDeSimbolos
            # Chequear que la variable exista en el ambito actual
            if tablaDeSimbolosActual.contains_key(id):
                
                tablaDeSimbolosActual.get(id)
                
            
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
        funcion = Funcion(nombreFuncion, TipoFuncion(), self.ambitoActual)
        # Si la funcion tiene parametros
        if ctx.parameters():
            # Obtener los parametros y meterlos en la tabla de simbolos actual no la de la funcion para desglosar la funcion
            parametros = self.visit(ctx.parameters())
            for parametro in parametros:
                ambitoActual.tablaDeSimbolos.put(f"parametro{self.cantidadDeParametrosDefinidos}", Parametro(parametro, ambito=self.ambitoActual, funcionPertenece=nombreFuncion))
                funcion.aniadirParametro(f"parametro{self.cantidadDeParametrosDefinidos}")
                self.cantidadDeParametrosDefinidos+=1
            ambitoActual.tablaDeSimbolos.put(nombreFuncion, funcion)
        # previo a que se visiten los nodos hijos que definen el ambito de la funcion se creara un nuevo ambito para la funcion con todos los simbolos de la tabla de simbolos pasada
        self.ambitoActual=self.TablaDeAmbitos.size()
        ambitoDeLaFuncion:Ambito = Ambito(self.TablaDeAmbitos.size(), tablaDeSimbolos=HashMap())
        ambitoDeLaFuncion.tablaDeSimbolos.replaceMap(ambitoActual.tablaDeSimbolos)
        self.TablaDeAmbitos.put(self.ambitoActual, ambitoDeLaFuncion)
        # Ahora hay que visitar al bloque que define la funcion
        self.visit(ctx.block())
        # Se retorna al ambito superior antes del ambito de la funcion
        self.ambitoActual = ambitoActual.identificadorAmbito


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