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
        4,1,46,259,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,1,0,5,0,48,8,0,10,0,12,0,51,9,0,1,0,1,0,
        1,1,1,1,1,1,1,1,3,1,59,8,1,1,2,1,2,1,2,1,2,3,2,65,8,2,1,2,1,2,5,
        2,69,8,2,10,2,12,2,72,9,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,
        4,83,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,94,8,5,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,110,8,7,10,7,
        12,7,113,9,7,1,7,1,7,3,7,117,8,7,1,8,1,8,1,8,1,8,1,8,3,8,124,8,8,
        1,8,3,8,127,8,8,1,8,1,8,3,8,131,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,
        1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,3,11,148,8,11,1,11,1,11,1,
        12,1,12,5,12,154,8,12,10,12,12,12,157,9,12,1,12,1,12,1,13,1,13,1,
        13,3,13,164,8,13,1,13,1,13,1,13,1,13,3,13,170,8,13,1,14,1,14,1,14,
        5,14,175,8,14,10,14,12,14,178,9,14,1,15,1,15,1,15,5,15,183,8,15,
        10,15,12,15,186,9,15,1,16,1,16,1,16,5,16,191,8,16,10,16,12,16,194,
        9,16,1,17,1,17,1,17,3,17,199,8,17,1,18,3,18,202,8,18,1,18,1,18,1,
        18,3,18,207,8,18,1,18,1,18,1,18,5,18,212,8,18,10,18,12,18,215,9,
        18,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,19,1,19,3,19,233,8,19,1,20,1,20,1,20,3,20,238,8,20,1,20,
        1,20,1,20,1,21,1,21,1,21,5,21,246,8,21,10,21,12,21,249,9,21,1,22,
        1,22,1,22,5,22,254,8,22,10,22,12,22,257,9,22,1,22,0,0,23,0,2,4,6,
        8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,0,4,1,0,
        19,20,1,0,21,26,1,0,27,31,2,0,27,27,32,32,279,0,49,1,0,0,0,2,58,
        1,0,0,0,4,60,1,0,0,0,6,75,1,0,0,0,8,78,1,0,0,0,10,93,1,0,0,0,12,
        95,1,0,0,0,14,98,1,0,0,0,16,118,1,0,0,0,18,135,1,0,0,0,20,141,1,
        0,0,0,22,145,1,0,0,0,24,151,1,0,0,0,26,169,1,0,0,0,28,171,1,0,0,
        0,30,179,1,0,0,0,32,187,1,0,0,0,34,198,1,0,0,0,36,201,1,0,0,0,38,
        232,1,0,0,0,40,234,1,0,0,0,42,242,1,0,0,0,44,250,1,0,0,0,46,48,3,
        2,1,0,47,46,1,0,0,0,48,51,1,0,0,0,49,47,1,0,0,0,49,50,1,0,0,0,50,
        52,1,0,0,0,51,49,1,0,0,0,52,53,5,0,0,1,53,1,1,0,0,0,54,59,3,4,2,
        0,55,59,3,6,3,0,56,59,3,8,4,0,57,59,3,10,5,0,58,54,1,0,0,0,58,55,
        1,0,0,0,58,56,1,0,0,0,58,57,1,0,0,0,59,3,1,0,0,0,60,61,5,1,0,0,61,
        64,5,44,0,0,62,63,5,2,0,0,63,65,5,44,0,0,64,62,1,0,0,0,64,65,1,0,
        0,0,65,66,1,0,0,0,66,70,5,3,0,0,67,69,3,40,20,0,68,67,1,0,0,0,69,
        72,1,0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,
        0,73,74,5,4,0,0,74,5,1,0,0,0,75,76,5,5,0,0,76,77,3,40,20,0,77,7,
        1,0,0,0,78,79,5,6,0,0,79,82,5,44,0,0,80,81,5,7,0,0,81,83,3,26,13,
        0,82,80,1,0,0,0,82,83,1,0,0,0,83,84,1,0,0,0,84,85,5,8,0,0,85,9,1,
        0,0,0,86,94,3,12,6,0,87,94,3,14,7,0,88,94,3,16,8,0,89,94,3,18,9,
        0,90,94,3,20,10,0,91,94,3,22,11,0,92,94,3,24,12,0,93,86,1,0,0,0,
        93,87,1,0,0,0,93,88,1,0,0,0,93,89,1,0,0,0,93,90,1,0,0,0,93,91,1,
        0,0,0,93,92,1,0,0,0,94,11,1,0,0,0,95,96,3,26,13,0,96,97,5,8,0,0,
        97,13,1,0,0,0,98,99,5,9,0,0,99,100,5,10,0,0,100,101,3,26,13,0,101,
        102,5,11,0,0,102,111,3,24,12,0,103,104,5,12,0,0,104,105,5,10,0,0,
        105,106,3,26,13,0,106,107,5,11,0,0,107,108,3,24,12,0,108,110,1,0,
        0,0,109,103,1,0,0,0,110,113,1,0,0,0,111,109,1,0,0,0,111,112,1,0,
        0,0,112,116,1,0,0,0,113,111,1,0,0,0,114,115,5,13,0,0,115,117,3,24,
        12,0,116,114,1,0,0,0,116,117,1,0,0,0,117,15,1,0,0,0,118,119,5,14,
        0,0,119,123,5,10,0,0,120,124,3,8,4,0,121,124,3,12,6,0,122,124,5,
        8,0,0,123,120,1,0,0,0,123,121,1,0,0,0,123,122,1,0,0,0,124,126,1,
        0,0,0,125,127,3,26,13,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,
        1,0,0,0,128,130,5,8,0,0,129,131,3,26,13,0,130,129,1,0,0,0,130,131,
        1,0,0,0,131,132,1,0,0,0,132,133,5,11,0,0,133,134,3,24,12,0,134,17,
        1,0,0,0,135,136,5,15,0,0,136,137,5,10,0,0,137,138,3,26,13,0,138,
        139,5,11,0,0,139,140,3,24,12,0,140,19,1,0,0,0,141,142,5,16,0,0,142,
        143,3,26,13,0,143,144,5,8,0,0,144,21,1,0,0,0,145,147,5,17,0,0,146,
        148,3,26,13,0,147,146,1,0,0,0,147,148,1,0,0,0,148,149,1,0,0,0,149,
        150,5,8,0,0,150,23,1,0,0,0,151,155,5,3,0,0,152,154,3,2,1,0,153,152,
        1,0,0,0,154,157,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,158,
        1,0,0,0,157,155,1,0,0,0,158,159,5,4,0,0,159,25,1,0,0,0,160,161,3,
        36,18,0,161,162,5,18,0,0,162,164,1,0,0,0,163,160,1,0,0,0,163,164,
        1,0,0,0,164,165,1,0,0,0,165,166,5,44,0,0,166,167,5,7,0,0,167,170,
        3,26,13,0,168,170,3,28,14,0,169,163,1,0,0,0,169,168,1,0,0,0,170,
        27,1,0,0,0,171,176,3,30,15,0,172,173,7,0,0,0,173,175,3,30,15,0,174,
        172,1,0,0,0,175,178,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,
        29,1,0,0,0,178,176,1,0,0,0,179,184,3,32,16,0,180,181,7,1,0,0,181,
        183,3,32,16,0,182,180,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,184,
        185,1,0,0,0,185,31,1,0,0,0,186,184,1,0,0,0,187,192,3,34,17,0,188,
        189,7,2,0,0,189,191,3,34,17,0,190,188,1,0,0,0,191,194,1,0,0,0,192,
        190,1,0,0,0,192,193,1,0,0,0,193,33,1,0,0,0,194,192,1,0,0,0,195,196,
        7,3,0,0,196,199,3,34,17,0,197,199,3,36,18,0,198,195,1,0,0,0,198,
        197,1,0,0,0,199,35,1,0,0,0,200,202,5,33,0,0,201,200,1,0,0,0,201,
        202,1,0,0,0,202,203,1,0,0,0,203,213,3,38,19,0,204,206,5,10,0,0,205,
        207,3,44,22,0,206,205,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,
        212,5,11,0,0,209,210,5,18,0,0,210,212,5,44,0,0,211,204,1,0,0,0,211,
        209,1,0,0,0,212,215,1,0,0,0,213,211,1,0,0,0,213,214,1,0,0,0,214,
        37,1,0,0,0,215,213,1,0,0,0,216,233,5,34,0,0,217,233,5,35,0,0,218,
        233,5,36,0,0,219,233,5,37,0,0,220,233,5,38,0,0,221,233,5,39,0,0,
        222,233,5,42,0,0,223,233,5,43,0,0,224,233,5,44,0,0,225,226,5,10,
        0,0,226,227,3,26,13,0,227,228,5,11,0,0,228,233,1,0,0,0,229,230,5,
        40,0,0,230,231,5,18,0,0,231,233,5,44,0,0,232,216,1,0,0,0,232,217,
        1,0,0,0,232,218,1,0,0,0,232,219,1,0,0,0,232,220,1,0,0,0,232,221,
        1,0,0,0,232,222,1,0,0,0,232,223,1,0,0,0,232,224,1,0,0,0,232,225,
        1,0,0,0,232,229,1,0,0,0,233,39,1,0,0,0,234,235,5,44,0,0,235,237,
        5,10,0,0,236,238,3,42,21,0,237,236,1,0,0,0,237,238,1,0,0,0,238,239,
        1,0,0,0,239,240,5,11,0,0,240,241,3,24,12,0,241,41,1,0,0,0,242,247,
        5,44,0,0,243,244,5,41,0,0,244,246,5,44,0,0,245,243,1,0,0,0,246,249,
        1,0,0,0,247,245,1,0,0,0,247,248,1,0,0,0,248,43,1,0,0,0,249,247,1,
        0,0,0,250,255,3,26,13,0,251,252,5,41,0,0,252,254,3,26,13,0,253,251,
        1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,45,1,
        0,0,0,257,255,1,0,0,0,27,49,58,64,70,82,93,111,116,123,126,130,147,
        155,163,169,176,184,192,198,201,206,211,213,232,237,247,255
    ]

class CompiScriptLanguageParser ( Parser ):

    grammarFileName = "CompiScriptLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'extends'", "'{'", "'}'", 
                     "'fun'", "'var'", "'='", "';'", "'if'", "'('", "')'", 
                     "'else if'", "'else'", "'for'", "'while'", "'print'", 
                     "'return'", "'.'", "'and'", "'or'", "'>'", "'>='", 
                     "'<'", "'<='", "'!='", "'=='", "'-'", "'+'", "'/'", 
                     "'*'", "'%'", "'!'", "'new'", "'true'", "'false'", 
                     "'nil'", "'this'", "'break'", "'continue'", "'super'", 
                     "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUMBER", "STRING", "IDENTIFIER", 
                      "WS", "MALFORMED" ]

    RULE_program = 0
    RULE_declaration = 1
    RULE_classDecl = 2
    RULE_funDecl = 3
    RULE_varDecl = 4
    RULE_statement = 5
    RULE_exprStmt = 6
    RULE_ifStmt = 7
    RULE_forStmt = 8
    RULE_whileStmt = 9
    RULE_printStmt = 10
    RULE_returnStmt = 11
    RULE_block = 12
    RULE_expression = 13
    RULE_logic = 14
    RULE_comparison = 15
    RULE_term = 16
    RULE_unary = 17
    RULE_call = 18
    RULE_primary = 19
    RULE_function = 20
    RULE_parameters = 21
    RULE_arguments = 22

    ruleNames =  [ "program", "declaration", "classDecl", "funDecl", "varDecl", 
                   "statement", "exprStmt", "ifStmt", "forStmt", "whileStmt", 
                   "printStmt", "returnStmt", "block", "expression", "logic", 
                   "comparison", "term", "unary", "call", "primary", "function", 
                   "parameters", "arguments" ]

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
    T__36=37
    T__37=38
    T__38=39
    T__39=40
    T__40=41
    NUMBER=42
    STRING=43
    IDENTIFIER=44
    WS=45
    MALFORMED=46

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
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32981188331114) != 0):
                self.state = 46
                self.declaration()
                self.state = 51
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 52
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
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.classDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.funDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.varDecl()
                pass
            elif token in [3, 9, 10, 14, 15, 16, 17, 27, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44]:
                self.enterOuterAlt(localctx, 4)
                self.state = 57
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
            self.state = 60
            self.match(CompiScriptLanguageParser.T__0)
            self.state = 61
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 62
                self.match(CompiScriptLanguageParser.T__1)
                self.state = 63
                self.match(CompiScriptLanguageParser.IDENTIFIER)


            self.state = 66
            self.match(CompiScriptLanguageParser.T__2)
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==44:
                self.state = 67
                self.function()
                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
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
            self.state = 75
            self.match(CompiScriptLanguageParser.T__4)
            self.state = 76
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
            self.state = 78
            self.match(CompiScriptLanguageParser.T__5)
            self.state = 79
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 82
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 80
                self.match(CompiScriptLanguageParser.T__6)
                self.state = 81
                self.expression()


            self.state = 84
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


        def ifStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.IfStmtContext,0)


        def forStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ForStmtContext,0)


        def whileStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.WhileStmtContext,0)


        def printStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.PrintStmtContext,0)


        def returnStmt(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ReturnStmtContext,0)


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
            self.state = 93
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 27, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44]:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.exprStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 87
                self.ifStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 88
                self.forStmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 89
                self.whileStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 90
                self.printStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 91
                self.returnStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 7)
                self.state = 92
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
            self.state = 95
            self.expression()
            self.state = 96
            self.match(CompiScriptLanguageParser.T__7)
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

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.ExpressionContext,i)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.BlockContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.BlockContext,i)


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
        self.enterRule(localctx, 14, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.match(CompiScriptLanguageParser.T__8)
            self.state = 99
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 100
            self.expression()
            self.state = 101
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 102
            self.block()
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 103
                self.match(CompiScriptLanguageParser.T__11)
                self.state = 104
                self.match(CompiScriptLanguageParser.T__9)
                self.state = 105
                self.expression()
                self.state = 106
                self.match(CompiScriptLanguageParser.T__10)
                self.state = 107
                self.block()
                self.state = 113
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 114
                self.match(CompiScriptLanguageParser.T__12)
                self.state = 115
                self.block()


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

        def block(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.BlockContext,0)


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
        self.enterRule(localctx, 16, self.RULE_forStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(CompiScriptLanguageParser.T__13)
            self.state = 119
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 123
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 120
                self.varDecl()
                pass
            elif token in [10, 27, 32, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44]:
                self.state = 121
                self.exprStmt()
                pass
            elif token in [8]:
                self.state = 122
                self.match(CompiScriptLanguageParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32981188084736) != 0):
                self.state = 125
                self.expression()


            self.state = 128
            self.match(CompiScriptLanguageParser.T__7)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32981188084736) != 0):
                self.state = 129
                self.expression()


            self.state = 132
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 133
            self.block()
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


        def block(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.BlockContext,0)


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
        self.enterRule(localctx, 18, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(CompiScriptLanguageParser.T__14)
            self.state = 136
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 137
            self.expression()
            self.state = 138
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 139
            self.block()
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
        self.enterRule(localctx, 20, self.RULE_printStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(CompiScriptLanguageParser.T__15)
            self.state = 142
            self.expression()
            self.state = 143
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
        self.enterRule(localctx, 22, self.RULE_returnStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 145
            self.match(CompiScriptLanguageParser.T__16)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32981188084736) != 0):
                self.state = 146
                self.expression()


            self.state = 149
            self.match(CompiScriptLanguageParser.T__7)
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
            self.state = 151
            self.match(CompiScriptLanguageParser.T__2)
            self.state = 155
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 32981188331114) != 0):
                self.state = 152
                self.declaration()
                self.state = 157
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 158
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


        def logic(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.LogicContext,0)


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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 163
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 160
                    self.call()
                    self.state = 161
                    self.match(CompiScriptLanguageParser.T__17)


                self.state = 165
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                self.state = 166
                self.match(CompiScriptLanguageParser.T__6)
                self.state = 167
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.logic()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicContext(ParserRuleContext):
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
            return CompiScriptLanguageParser.RULE_logic

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogic" ):
                listener.enterLogic(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogic" ):
                listener.exitLogic(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogic" ):
                return visitor.visitLogic(self)
            else:
                return visitor.visitChildren(self)




    def logic(self):

        localctx = CompiScriptLanguageParser.LogicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_logic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.comparison()
            self.state = 176
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 172
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 173
                self.comparison()
                self.state = 178
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
        self.enterRule(localctx, 30, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 179
            self.term()
            self.state = 184
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0):
                self.state = 180
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 132120576) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 181
                self.term()
                self.state = 186
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

        def unary(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.UnaryContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.UnaryContext,i)


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
        self.enterRule(localctx, 32, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            self.unary()
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4160749568) != 0):
                self.state = 188
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4160749568) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 189
                self.unary()
                self.state = 194
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
        self.enterRule(localctx, 34, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 198
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 195
                _la = self._input.LA(1)
                if not(_la==27 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 196
                self.unary()
                pass
            elif token in [10, 33, 34, 35, 36, 37, 38, 39, 40, 42, 43, 44]:
                self.enterOuterAlt(localctx, 2)
                self.state = 197
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
        self.enterRule(localctx, 36, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 200
                self.match(CompiScriptLanguageParser.T__32)


            self.state = 203
            self.primary()
            self.state = 213
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 211
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [10]:
                        self.state = 204
                        self.match(CompiScriptLanguageParser.T__9)
                        self.state = 206
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 32981188084736) != 0):
                            self.state = 205
                            self.arguments()


                        self.state = 208
                        self.match(CompiScriptLanguageParser.T__10)
                        pass
                    elif token in [18]:
                        self.state = 209
                        self.match(CompiScriptLanguageParser.T__17)
                        self.state = 210
                        self.match(CompiScriptLanguageParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 215
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
        self.enterRule(localctx, 38, self.RULE_primary)
        try:
            self.state = 232
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [34]:
                self.enterOuterAlt(localctx, 1)
                self.state = 216
                self.match(CompiScriptLanguageParser.T__33)
                pass
            elif token in [35]:
                self.enterOuterAlt(localctx, 2)
                self.state = 217
                self.match(CompiScriptLanguageParser.T__34)
                pass
            elif token in [36]:
                self.enterOuterAlt(localctx, 3)
                self.state = 218
                self.match(CompiScriptLanguageParser.T__35)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 4)
                self.state = 219
                self.match(CompiScriptLanguageParser.T__36)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 5)
                self.state = 220
                self.match(CompiScriptLanguageParser.T__37)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 6)
                self.state = 221
                self.match(CompiScriptLanguageParser.T__38)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 7)
                self.state = 222
                self.match(CompiScriptLanguageParser.NUMBER)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 8)
                self.state = 223
                self.match(CompiScriptLanguageParser.STRING)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 9)
                self.state = 224
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 10)
                self.state = 225
                self.match(CompiScriptLanguageParser.T__9)
                self.state = 226
                self.expression()
                self.state = 227
                self.match(CompiScriptLanguageParser.T__10)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 11)
                self.state = 229
                self.match(CompiScriptLanguageParser.T__39)
                self.state = 230
                self.match(CompiScriptLanguageParser.T__17)
                self.state = 231
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
        self.enterRule(localctx, 40, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 235
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 237
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==44:
                self.state = 236
                self.parameters()


            self.state = 239
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 240
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
        self.enterRule(localctx, 42, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 247
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 243
                self.match(CompiScriptLanguageParser.T__40)
                self.state = 244
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                self.state = 249
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
        self.enterRule(localctx, 44, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 250
            self.expression()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==41:
                self.state = 251
                self.match(CompiScriptLanguageParser.T__40)
                self.state = 252
                self.expression()
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





