from Syntax.CompiScriptLanguageVisitor import *
from Syntax.CompiScriptLanguageParser import *
from Structures.HashMap import *
from Structures.Ambito import *
from Structures.Tipos.Tipo import *
from Structures.Simbolos.Variable import *
from Structures.Tipos.Numero import *
from Structures.Tipos.Nil import *
from Structures.Tipos.Cadena import *
from Structures.Tipos.Booleano import *

# Implementacion
class CompiScriptVisitor(CompiScriptLanguageVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.TablaDeSimbolos = HashMap()
        self.TablaDeTipos = HashMap()
        self.TablaDeAmbitos = HashMap()
        self.ambitoActual = 0
        
    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        # Crear el contexto main que seria el contexto 0
        self.TablaDeAmbitos.put(0, Ambito(identificador=0))
        for child in ctx.declaration():
            self.visit(child)

    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        id = ctx.IDENTIFIER().symbol.text
        # Averiguaremos el tipo despues y la inicializacion despues
        self.TablaDeSimbolos.put(id, Variable(nombreSimbolo=id, ambito=self.ambitoActual))
        # En caso de que tenga una expresion, porque puede que sea una variable solo definida sin inicializar
        if ctx.expression():
            # Obtener tipo
            variableTipo = self.visit(ctx.expression())
            # Inicializar la variable y definir el tipo porque al principio es nil
            simbolo:Variable = self.TablaDeSimbolos.get(id) 
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
            symbol = self.TablaDeSimbolos.get(id)
            
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        return self.visitChildren(ctx)