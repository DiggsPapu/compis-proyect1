from Syntax.CompiScriptLanguageVisitor import *
from Syntax.CompiScriptLanguageParser import *
from Structures.HashMap import *
from Structures.Ambito import *
from Structures.Tipos.Tipo import *
from Structures.Simbolos.Variable import *

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

    # Visit a parse tree produced by CompiScriptLanguageParser#classDeclaration.
    def visitClassDeclaration(self, ctx:CompiScriptLanguageParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:CompiScriptLanguageParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#variableDeclaration.
    def visitVariableDeclaration(self, ctx:CompiScriptLanguageParser.VariableDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#statementDeclaration.
    def visitStatementDeclaration(self, ctx:CompiScriptLanguageParser.StatementDeclarationContext):
        return self.visitChildren(ctx)


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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CompiScriptLanguageParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStatement.
    def visitForStatement(self, ctx:CompiScriptLanguageParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStatement.
    def visitIfStatement(self, ctx:CompiScriptLanguageParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#printStatement.
    def visitPrintStatement(self, ctx:CompiScriptLanguageParser.PrintStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStatement.
    def visitReturnStatement(self, ctx:CompiScriptLanguageParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStatement.
    def visitWhileStatement(self, ctx:CompiScriptLanguageParser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#blockStatement.
    def visitBlockStatement(self, ctx:CompiScriptLanguageParser.BlockStatementContext):
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
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#assignment.
    def visitAssignment(self, ctx:CompiScriptLanguageParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_or.
    def visitLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#logic_and.
    def visitLogic_and(self, ctx:CompiScriptLanguageParser.Logic_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#equality.
    def visitEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#factor.
    def visitFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#unary.
    def visitUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
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