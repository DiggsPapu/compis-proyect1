# Generated from CompiScriptLanguage.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,40,273,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,5,0,54,
        8,0,10,0,12,0,57,9,0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,65,8,1,1,2,1,2,
        1,2,1,2,3,2,71,8,2,1,2,1,2,5,2,75,8,2,10,2,12,2,78,9,2,1,2,1,2,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,89,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,
        1,5,1,5,3,5,100,8,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,3,7,110,8,7,
        1,7,3,7,113,8,7,1,7,1,7,3,7,117,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,
        1,8,1,8,1,8,3,8,129,8,8,1,9,1,9,1,9,1,9,1,10,1,10,3,10,137,8,10,
        1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,5,12,149,8,12,
        10,12,12,12,152,9,12,1,12,1,12,1,13,1,13,1,13,3,13,159,8,13,1,13,
        1,13,1,13,1,13,3,13,165,8,13,1,14,1,14,1,14,5,14,170,8,14,10,14,
        12,14,173,9,14,1,15,1,15,1,15,5,15,178,8,15,10,15,12,15,181,9,15,
        1,16,1,16,1,16,5,16,186,8,16,10,16,12,16,189,9,16,1,17,1,17,1,17,
        5,17,194,8,17,10,17,12,17,197,9,17,1,18,1,18,1,18,5,18,202,8,18,
        10,18,12,18,205,9,18,1,19,1,19,1,19,5,19,210,8,19,10,19,12,19,213,
        9,19,1,20,1,20,1,20,3,20,218,8,20,1,21,1,21,1,21,3,21,223,8,21,1,
        21,1,21,1,21,5,21,228,8,21,10,21,12,21,231,9,21,1,22,1,22,1,22,1,
        22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,247,8,
        22,1,23,1,23,1,23,3,23,252,8,23,1,23,1,23,1,23,1,24,1,24,1,24,5,
        24,260,8,24,10,24,12,24,263,9,24,1,25,1,25,1,25,5,25,268,8,25,10,
        25,12,25,271,9,25,1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,0,5,1,0,20,21,2,0,2,2,22,
        24,1,0,25,26,1,0,27,29,2,0,25,25,30,30,289,0,55,1,0,0,0,2,64,1,0,
        0,0,4,66,1,0,0,0,6,81,1,0,0,0,8,84,1,0,0,0,10,99,1,0,0,0,12,101,
        1,0,0,0,14,104,1,0,0,0,16,121,1,0,0,0,18,130,1,0,0,0,20,134,1,0,
        0,0,22,140,1,0,0,0,24,146,1,0,0,0,26,164,1,0,0,0,28,166,1,0,0,0,
        30,174,1,0,0,0,32,182,1,0,0,0,34,190,1,0,0,0,36,198,1,0,0,0,38,206,
        1,0,0,0,40,217,1,0,0,0,42,219,1,0,0,0,44,246,1,0,0,0,46,248,1,0,
        0,0,48,256,1,0,0,0,50,264,1,0,0,0,52,54,3,2,1,0,53,52,1,0,0,0,54,
        57,1,0,0,0,55,53,1,0,0,0,55,56,1,0,0,0,56,58,1,0,0,0,57,55,1,0,0,
        0,58,59,5,0,0,1,59,1,1,0,0,0,60,65,3,4,2,0,61,65,3,6,3,0,62,65,3,
        8,4,0,63,65,3,10,5,0,64,60,1,0,0,0,64,61,1,0,0,0,64,62,1,0,0,0,64,
        63,1,0,0,0,65,3,1,0,0,0,66,67,5,1,0,0,67,70,5,39,0,0,68,69,5,2,0,
        0,69,71,5,39,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,76,
        5,3,0,0,73,75,3,46,23,0,74,73,1,0,0,0,75,78,1,0,0,0,76,74,1,0,0,
        0,76,77,1,0,0,0,77,79,1,0,0,0,78,76,1,0,0,0,79,80,5,4,0,0,80,5,1,
        0,0,0,81,82,5,5,0,0,82,83,3,46,23,0,83,7,1,0,0,0,84,85,5,6,0,0,85,
        88,5,39,0,0,86,87,5,7,0,0,87,89,3,26,13,0,88,86,1,0,0,0,88,89,1,
        0,0,0,89,90,1,0,0,0,90,91,5,8,0,0,91,9,1,0,0,0,92,100,3,12,6,0,93,
        100,3,14,7,0,94,100,3,16,8,0,95,100,3,18,9,0,96,100,3,20,10,0,97,
        100,3,22,11,0,98,100,3,24,12,0,99,92,1,0,0,0,99,93,1,0,0,0,99,94,
        1,0,0,0,99,95,1,0,0,0,99,96,1,0,0,0,99,97,1,0,0,0,99,98,1,0,0,0,
        100,11,1,0,0,0,101,102,3,26,13,0,102,103,5,8,0,0,103,13,1,0,0,0,
        104,105,5,9,0,0,105,109,5,10,0,0,106,110,3,8,4,0,107,110,3,12,6,
        0,108,110,5,8,0,0,109,106,1,0,0,0,109,107,1,0,0,0,109,108,1,0,0,
        0,110,112,1,0,0,0,111,113,3,26,13,0,112,111,1,0,0,0,112,113,1,0,
        0,0,113,114,1,0,0,0,114,116,5,8,0,0,115,117,3,26,13,0,116,115,1,
        0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,119,5,11,0,0,119,120,3,
        10,5,0,120,15,1,0,0,0,121,122,5,12,0,0,122,123,5,10,0,0,123,124,
        3,26,13,0,124,125,5,11,0,0,125,128,3,10,5,0,126,127,5,13,0,0,127,
        129,3,10,5,0,128,126,1,0,0,0,128,129,1,0,0,0,129,17,1,0,0,0,130,
        131,5,14,0,0,131,132,3,26,13,0,132,133,5,8,0,0,133,19,1,0,0,0,134,
        136,5,15,0,0,135,137,3,26,13,0,136,135,1,0,0,0,136,137,1,0,0,0,137,
        138,1,0,0,0,138,139,5,8,0,0,139,21,1,0,0,0,140,141,5,16,0,0,141,
        142,5,10,0,0,142,143,3,26,13,0,143,144,5,11,0,0,144,145,3,10,5,0,
        145,23,1,0,0,0,146,150,5,3,0,0,147,149,3,2,1,0,148,147,1,0,0,0,149,
        152,1,0,0,0,150,148,1,0,0,0,150,151,1,0,0,0,151,153,1,0,0,0,152,
        150,1,0,0,0,153,154,5,4,0,0,154,25,1,0,0,0,155,156,3,42,21,0,156,
        157,5,17,0,0,157,159,1,0,0,0,158,155,1,0,0,0,158,159,1,0,0,0,159,
        160,1,0,0,0,160,161,5,39,0,0,161,162,5,7,0,0,162,165,3,26,13,0,163,
        165,3,28,14,0,164,158,1,0,0,0,164,163,1,0,0,0,165,27,1,0,0,0,166,
        171,3,30,15,0,167,168,5,18,0,0,168,170,3,30,15,0,169,167,1,0,0,0,
        170,173,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,29,1,0,0,0,173,
        171,1,0,0,0,174,179,3,32,16,0,175,176,5,19,0,0,176,178,3,32,16,0,
        177,175,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,1,0,0,0,
        180,31,1,0,0,0,181,179,1,0,0,0,182,187,3,34,17,0,183,184,7,0,0,0,
        184,186,3,34,17,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,
        0,187,188,1,0,0,0,188,33,1,0,0,0,189,187,1,0,0,0,190,195,3,36,18,
        0,191,192,7,1,0,0,192,194,3,36,18,0,193,191,1,0,0,0,194,197,1,0,
        0,0,195,193,1,0,0,0,195,196,1,0,0,0,196,35,1,0,0,0,197,195,1,0,0,
        0,198,203,3,38,19,0,199,200,7,2,0,0,200,202,3,38,19,0,201,199,1,
        0,0,0,202,205,1,0,0,0,203,201,1,0,0,0,203,204,1,0,0,0,204,37,1,0,
        0,0,205,203,1,0,0,0,206,211,3,40,20,0,207,208,7,3,0,0,208,210,3,
        40,20,0,209,207,1,0,0,0,210,213,1,0,0,0,211,209,1,0,0,0,211,212,
        1,0,0,0,212,39,1,0,0,0,213,211,1,0,0,0,214,215,7,4,0,0,215,218,3,
        40,20,0,216,218,3,42,21,0,217,214,1,0,0,0,217,216,1,0,0,0,218,41,
        1,0,0,0,219,229,3,44,22,0,220,222,5,10,0,0,221,223,3,50,25,0,222,
        221,1,0,0,0,222,223,1,0,0,0,223,224,1,0,0,0,224,228,5,11,0,0,225,
        226,5,17,0,0,226,228,5,39,0,0,227,220,1,0,0,0,227,225,1,0,0,0,228,
        231,1,0,0,0,229,227,1,0,0,0,229,230,1,0,0,0,230,43,1,0,0,0,231,229,
        1,0,0,0,232,247,5,31,0,0,233,247,5,32,0,0,234,247,5,33,0,0,235,247,
        5,34,0,0,236,247,5,37,0,0,237,247,5,38,0,0,238,247,5,39,0,0,239,
        240,5,10,0,0,240,241,3,26,13,0,241,242,5,11,0,0,242,247,1,0,0,0,
        243,244,5,35,0,0,244,245,5,17,0,0,245,247,5,39,0,0,246,232,1,0,0,
        0,246,233,1,0,0,0,246,234,1,0,0,0,246,235,1,0,0,0,246,236,1,0,0,
        0,246,237,1,0,0,0,246,238,1,0,0,0,246,239,1,0,0,0,246,243,1,0,0,
        0,247,45,1,0,0,0,248,249,5,39,0,0,249,251,5,10,0,0,250,252,3,48,
        24,0,251,250,1,0,0,0,251,252,1,0,0,0,252,253,1,0,0,0,253,254,5,11,
        0,0,254,255,3,24,12,0,255,47,1,0,0,0,256,261,5,39,0,0,257,258,5,
        36,0,0,258,260,5,39,0,0,259,257,1,0,0,0,260,263,1,0,0,0,261,259,
        1,0,0,0,261,262,1,0,0,0,262,49,1,0,0,0,263,261,1,0,0,0,264,269,3,
        26,13,0,265,266,5,36,0,0,266,268,3,26,13,0,267,265,1,0,0,0,268,271,
        1,0,0,0,269,267,1,0,0,0,269,270,1,0,0,0,270,51,1,0,0,0,271,269,1,
        0,0,0,28,55,64,70,76,88,99,109,112,116,128,136,150,158,164,171,179,
        187,195,203,211,217,222,227,229,246,251,261,269
    ]

class CompiScriptLanguageParser ( Parser ):

    grammarFileName = "CompiScriptLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'<'", "'{'", "'}'", "'fun'", 
                     "'var'", "'='", "';'", "'for'", "'('", "')'", "'if'", 
                     "'else'", "'print'", "'return'", "'while'", "'.'", 
                     "'or'", "'and'", "'!='", "'=='", "'>'", "'>='", "'<='", 
                     "'-'", "'+'", "'/'", "'*'", "'%'", "'!'", "'true'", 
                     "'false'", "'nil'", "'this'", "'super'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMBER", "STRING", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_classDecl = 2
    RULE_funDecl = 3
    RULE_varDecl = 4
    RULE_statement = 5
    RULE_exprStmt = 6
    RULE_forStmt = 7
    RULE_ifStmt = 8
    RULE_printStmt = 9
    RULE_returnStmt = 10
    RULE_whileStmt = 11
    RULE_block = 12
    RULE_expression = 13
    RULE_logic_or = 14
    RULE_logic_and = 15
    RULE_equality = 16
    RULE_comparison = 17
    RULE_term = 18
    RULE_factor = 19
    RULE_unary = 20
    RULE_call = 21
    RULE_primary = 22
    RULE_function = 23
    RULE_parameters = 24
    RULE_arguments = 25

    ruleNames =  [ "program", "declaration", "classDecl", "funDecl", "varDecl", 
                   "statement", "exprStmt", "forStmt", "ifStmt", "printStmt", 
                   "returnStmt", "whileStmt", "block", "expression", "logic_or", 
                   "logic_and", "equality", "comparison", "term", "factor", 
                   "unary", "call", "primary", "function", "parameters", 
                   "arguments" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    NUMBER=37
    STRING=38
    IDENTIFIER=39
    WS=40

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CompiScriptLanguageParser.EOF, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.DeclarationContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CompiScriptLanguageParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1029752084074) != 0):
                self.state = 52
                self.declaration()
                self.state = 57
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 58
            self.match(CompiScriptLanguageParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def classDecl(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ClassDeclContext,0)


        def funDecl(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.FunDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.VarDeclContext,0)


        def statement(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.StatementContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaration" ):
                return visitor.visitDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def declaration(self):

        localctx = CompiScriptLanguageParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaration)
        try:
            self.state = 64
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.classDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.funDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 62
                self.varDecl()
                pass
            elif token in [3, 9, 10, 12, 14, 15, 16, 25, 30, 31, 32, 33, 34, 35, 37, 38, 39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 63
                self.statement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ClassDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CompiScriptLanguageParser.IDENTIFIER)
            else:
                return self.getToken(CompiScriptLanguageParser.IDENTIFIER, i)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.FunctionContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.FunctionContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_classDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterClassDecl" ):
                listener.enterClassDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitClassDecl" ):
                listener.exitClassDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassDecl" ):
                return visitor.visitClassDecl(self)
            else:
                return visitor.visitChildren(self)




    def classDecl(self):

        localctx = CompiScriptLanguageParser.ClassDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_classDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(CompiScriptLanguageParser.T__0)
            self.state = 67
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 68
                self.match(CompiScriptLanguageParser.T__1)
                self.state = 69
                self.match(CompiScriptLanguageParser.IDENTIFIER)


            self.state = 72
            self.match(CompiScriptLanguageParser.T__2)
            self.state = 76
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 73
                self.function()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 79
            self.match(CompiScriptLanguageParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.FunctionContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_funDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunDecl" ):
                listener.enterFunDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunDecl" ):
                listener.exitFunDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunDecl" ):
                return visitor.visitFunDecl(self)
            else:
                return visitor.visitChildren(self)




    def funDecl(self):

        localctx = CompiScriptLanguageParser.FunDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(CompiScriptLanguageParser.T__4)
            self.state = 82
            self.function()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CompiScriptLanguageParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = CompiScriptLanguageParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(CompiScriptLanguageParser.T__5)
            self.state = 85
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 88
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 86
                self.match(CompiScriptLanguageParser.T__6)
                self.state = 87
                self.expression()


            self.state = 90
            self.match(CompiScriptLanguageParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExprStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ForStmtContext,0)


        def ifStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.IfStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.PrintStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ReturnStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.WhileStmtContext,0)


        def block(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.BlockContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CompiScriptLanguageParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_statement)
        try:
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 25, 30, 31, 32, 33, 34, 35, 37, 38, 39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.exprStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
                self.forStmt()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 3)
                self.state = 94
                self.ifStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 4)
                self.state = 95
                self.printStmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 5)
                self.state = 96
                self.returnStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 6)
                self.state = 97
                self.whileStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 7)
                self.state = 98
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_exprStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStmt" ):
                listener.enterExprStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStmt" ):
                listener.exitExprStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprStmt" ):
                return visitor.visitExprStmt(self)
            else:
                return visitor.visitChildren(self)




    def exprStmt(self):

        localctx = CompiScriptLanguageParser.ExprStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exprStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.expression()
            self.state = 102
            self.match(CompiScriptLanguageParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.StatementContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.VarDeclContext,0)


        def exprStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExprStmtContext,0)


        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = CompiScriptLanguageParser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(CompiScriptLanguageParser.T__8)
            self.state = 105
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 109
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 106
                self.varDecl()
                pass
            elif token in [10, 25, 30, 31, 32, 33, 34, 35, 37, 38, 39]:
                self.state = 107
                self.exprStmt()
                pass
            elif token in [8]:
                self.state = 108
                self.match(CompiScriptLanguageParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1029751964672) != 0):
                self.state = 111
                self.expression()


            self.state = 114
            self.match(CompiScriptLanguageParser.T__7)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1029751964672) != 0):
                self.state = 115
                self.expression()


            self.state = 118
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 119
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.StatementContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.StatementContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = CompiScriptLanguageParser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ifStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(CompiScriptLanguageParser.T__11)
            self.state = 122
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 123
            self.expression()
            self.state = 124
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 125
            self.statement()
            self.state = 128
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 126
                self.match(CompiScriptLanguageParser.T__12)
                self.state = 127
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrintStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_printStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintStmt" ):
                listener.enterPrintStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintStmt" ):
                listener.exitPrintStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrintStmt" ):
                return visitor.visitPrintStmt(self)
            else:
                return visitor.visitChildren(self)




    def printStmt(self):

        localctx = CompiScriptLanguageParser.PrintStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(CompiScriptLanguageParser.T__13)
            self.state = 131
            self.expression()
            self.state = 132
            self.match(CompiScriptLanguageParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_returnStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStmt" ):
                listener.enterReturnStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStmt" ):
                listener.exitReturnStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStmt" ):
                return visitor.visitReturnStmt(self)
            else:
                return visitor.visitChildren(self)




    def returnStmt(self):

        localctx = CompiScriptLanguageParser.ReturnStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 134
            self.match(CompiScriptLanguageParser.T__14)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1029751964672) != 0):
                self.state = 135
                self.expression()


            self.state = 138
            self.match(CompiScriptLanguageParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,0)


        def statement(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.StatementContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = CompiScriptLanguageParser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self.match(CompiScriptLanguageParser.T__15)
            self.state = 141
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 142
            self.expression()
            self.state = 143
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 144
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.DeclarationContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = CompiScriptLanguageParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(CompiScriptLanguageParser.T__2)
            self.state = 150
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1029752084074) != 0):
                self.state = 147
                self.declaration()
                self.state = 152
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 153
            self.match(CompiScriptLanguageParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CompiScriptLanguageParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,0)


        def call(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.CallContext,0)


        def logic_or(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.Logic_orContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CompiScriptLanguageParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 155
                    self.call()
                    self.state = 156
                    self.match(CompiScriptLanguageParser.T__16)


                self.state = 160
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                self.state = 161
                self.match(CompiScriptLanguageParser.T__6)
                self.state = 162
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.logic_or()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_orContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic_and(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.Logic_andContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.Logic_andContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_logic_or

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_or" ):
                listener.enterLogic_or(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_or" ):
                listener.exitLogic_or(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_or" ):
                return visitor.visitLogic_or(self)
            else:
                return visitor.visitChildren(self)




    def logic_or(self):

        localctx = CompiScriptLanguageParser.Logic_orContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_logic_or)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
            self.logic_and()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==18:
                self.state = 167
                self.match(CompiScriptLanguageParser.T__17)
                self.state = 168
                self.logic_and()
                self.state = 173
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logic_andContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equality(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.EqualityContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.EqualityContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_logic_and

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic_and" ):
                listener.enterLogic_and(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic_and" ):
                listener.exitLogic_and(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic_and" ):
                return visitor.visitLogic_and(self)
            else:
                return visitor.visitChildren(self)




    def logic_and(self):

        localctx = CompiScriptLanguageParser.Logic_andContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_logic_and)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
            self.equality()
            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19:
                self.state = 175
                self.match(CompiScriptLanguageParser.T__18)
                self.state = 176
                self.equality()
                self.state = 181
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.ComparisonContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.ComparisonContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_equality

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquality" ):
                listener.enterEquality(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquality" ):
                listener.exitEquality(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEquality" ):
                return visitor.visitEquality(self)
            else:
                return visitor.visitChildren(self)




    def equality(self):

        localctx = CompiScriptLanguageParser.EqualityContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_equality)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.comparison()
            self.state = 187
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20 or _la==21:
                self.state = 183
                _la = self._input.LA(1)
                if not(_la==20 or _la==21):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 184
                self.comparison()
                self.state = 189
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ComparisonContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.TermContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.TermContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_comparison

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison" ):
                listener.enterComparison(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison" ):
                listener.exitComparison(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparison" ):
                return visitor.visitComparison(self)
            else:
                return visitor.visitChildren(self)




    def comparison(self):

        localctx = CompiScriptLanguageParser.ComparisonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.term()
            self.state = 195
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 29360132) != 0):
                self.state = 191
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 29360132) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 192
                self.term()
                self.state = 197
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.FactorContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.FactorContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = CompiScriptLanguageParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.factor()
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==25 or _la==26:
                self.state = 199
                _la = self._input.LA(1)
                if not(_la==25 or _la==26):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 200
                self.factor()
                self.state = 205
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.UnaryContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.UnaryContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = CompiScriptLanguageParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_factor)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.unary()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0):
                self.state = 207
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 939524096) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.unary()
                self.state = 213
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.UnaryContext,0)


        def call(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.CallContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_unary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnary" ):
                listener.enterUnary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnary" ):
                listener.exitUnary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnary" ):
                return visitor.visitUnary(self)
            else:
                return visitor.visitChildren(self)




    def unary(self):

        localctx = CompiScriptLanguageParser.UnaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                _la = self._input.LA(1)
                if not(_la==25 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 215
                self.unary()
                pass
            elif token in [10, 31, 32, 33, 34, 35, 37, 38, 39]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.call()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primary(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.PrimaryContext,0)


        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CompiScriptLanguageParser.IDENTIFIER)
            else:
                return self.getToken(CompiScriptLanguageParser.IDENTIFIER, i)

        def arguments(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.ArgumentsContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.ArgumentsContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCall" ):
                listener.enterCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCall" ):
                listener.exitCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCall" ):
                return visitor.visitCall(self)
            else:
                return visitor.visitChildren(self)




    def call(self):

        localctx = CompiScriptLanguageParser.CallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.primary()
            self.state = 229
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 227
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [10]:
                        self.state = 220
                        self.match(CompiScriptLanguageParser.T__9)
                        self.state = 222
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 1029751964672) != 0):
                            self.state = 221
                            self.arguments()


                        self.state = 224
                        self.match(CompiScriptLanguageParser.T__10)
                        pass
                    elif token in [17]:
                        self.state = 225
                        self.match(CompiScriptLanguageParser.T__16)
                        self.state = 226
                        self.match(CompiScriptLanguageParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(CompiScriptLanguageParser.NUMBER, 0)

        def STRING(self):
            return self.getToken(CompiScriptLanguageParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(CompiScriptLanguageParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_primary

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary" ):
                listener.enterPrimary(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary" ):
                listener.exitPrimary(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimary" ):
                return visitor.visitPrimary(self)
            else:
                return visitor.visitChildren(self)




    def primary(self):

        localctx = CompiScriptLanguageParser.PrimaryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_primary)
        try:
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(CompiScriptLanguageParser.T__30)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.match(CompiScriptLanguageParser.T__31)
                pass
            elif token in [33]:
                self.enterOuterAlt(localctx, 3)
                self.state = 234
                self.match(CompiScriptLanguageParser.T__32)
                pass
            elif token in [34]:
                self.enterOuterAlt(localctx, 4)
                self.state = 235
                self.match(CompiScriptLanguageParser.T__33)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 5)
                self.state = 236
                self.match(CompiScriptLanguageParser.NUMBER)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 6)
                self.state = 237
                self.match(CompiScriptLanguageParser.STRING)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 7)
                self.state = 238
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 8)
                self.state = 239
                self.match(CompiScriptLanguageParser.T__9)
                self.state = 240
                self.expression()
                self.state = 241
                self.match(CompiScriptLanguageParser.T__10)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 9)
                self.state = 243
                self.match(CompiScriptLanguageParser.T__34)
                self.state = 244
                self.match(CompiScriptLanguageParser.T__16)
                self.state = 245
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CompiScriptLanguageParser.IDENTIFIER, 0)

        def block(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ParametersContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = CompiScriptLanguageParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 249
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==39:
                self.state = 250
                self.parameters()


            self.state = 253
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 254
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(CompiScriptLanguageParser.IDENTIFIER)
            else:
                return self.getToken(CompiScriptLanguageParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = CompiScriptLanguageParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 257
                self.match(CompiScriptLanguageParser.T__35)
                self.state = 258
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = CompiScriptLanguageParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.expression()
            self.state = 269
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==36:
                self.state = 265
                self.match(CompiScriptLanguageParser.T__35)
                self.state = 266
                self.expression()
                self.state = 271
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





