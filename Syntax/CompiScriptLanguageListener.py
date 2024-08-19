# Generated from CompiScriptLanguage.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .CompiScriptLanguageParser import CompiScriptLanguageParser
else:
    from CompiScriptLanguageParser import CompiScriptLanguageParser

# This class defines a complete listener for a parse tree produced by CompiScriptLanguageParser.
class CompiScriptLanguageListener(ParseTreeListener):

    # Enter a parse tree produced by CompiScriptLanguageParser#program.
    def enterProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#program.
    def exitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#declaration.
    def enterDeclaration(self, ctx:CompiScriptLanguageParser.DeclarationContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#declaration.
    def exitDeclaration(self, ctx:CompiScriptLanguageParser.DeclarationContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#classDecl.
    def enterClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def exitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#funDecl.
    def enterFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def exitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#varDecl.
    def enterVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def exitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#statement.
    def enterStatement(self, ctx:CompiScriptLanguageParser.StatementContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#statement.
    def exitStatement(self, ctx:CompiScriptLanguageParser.StatementContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def enterExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def exitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#forStmt.
    def enterForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def exitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def enterIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def exitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#printStmt.
    def enterPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def exitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def enterReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def exitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def enterWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def exitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#block.
    def enterBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#block.
    def exitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#expression.
    def enterExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#expression.
    def exitExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#logic_or.
    def enterLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#logic_or.
    def exitLogic_or(self, ctx:CompiScriptLanguageParser.Logic_orContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#logic_and.
    def enterLogic_and(self, ctx:CompiScriptLanguageParser.Logic_andContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#logic_and.
    def exitLogic_and(self, ctx:CompiScriptLanguageParser.Logic_andContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#equality.
    def enterEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#equality.
    def exitEquality(self, ctx:CompiScriptLanguageParser.EqualityContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#comparison.
    def enterComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#comparison.
    def exitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#term.
    def enterTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#term.
    def exitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#factor.
    def enterFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#factor.
    def exitFactor(self, ctx:CompiScriptLanguageParser.FactorContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#unary.
    def enterUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#unary.
    def exitUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#call.
    def enterCall(self, ctx:CompiScriptLanguageParser.CallContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#call.
    def exitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#primary.
    def enterPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#primary.
    def exitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#function.
    def enterFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#function.
    def exitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#parameters.
    def enterParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#parameters.
    def exitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        pass


    # Enter a parse tree produced by CompiScriptLanguageParser#arguments.
    def enterArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by CompiScriptLanguageParser#arguments.
    def exitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        pass



del CompiScriptLanguageParser