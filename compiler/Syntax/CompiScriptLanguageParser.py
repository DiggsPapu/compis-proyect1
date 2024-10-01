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
        4,1,48,277,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,1,0,5,0,50,8,0,10,0,12,0,53,9,
        0,1,0,1,0,1,1,1,1,1,1,1,1,3,1,61,8,1,1,2,1,2,1,2,1,2,3,2,67,8,2,
        1,2,1,2,5,2,71,8,2,10,2,12,2,74,9,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,
        1,4,1,4,3,4,85,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,96,8,
        5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,112,
        8,7,10,7,12,7,115,9,7,1,7,1,7,3,7,119,8,7,1,8,1,8,1,8,1,8,1,8,3,
        8,126,8,8,1,8,3,8,129,8,8,1,8,1,8,3,8,133,8,8,1,8,1,8,1,8,1,9,1,
        9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,11,1,11,3,11,150,8,11,1,
        11,1,11,1,12,1,12,5,12,156,8,12,10,12,12,12,159,9,12,1,12,1,12,1,
        13,1,13,1,13,3,13,166,8,13,1,13,1,13,1,13,1,13,1,13,3,13,173,8,13,
        3,13,175,8,13,1,14,1,14,1,14,1,14,5,14,181,8,14,10,14,12,14,184,
        9,14,3,14,186,8,14,1,14,1,14,1,15,1,15,1,15,5,15,193,8,15,10,15,
        12,15,196,9,15,1,16,1,16,1,16,5,16,201,8,16,10,16,12,16,204,9,16,
        1,17,1,17,1,17,5,17,209,8,17,10,17,12,17,212,9,17,1,18,1,18,1,18,
        3,18,217,8,18,1,19,3,19,220,8,19,1,19,1,19,1,19,3,19,225,8,19,1,
        19,1,19,1,19,5,19,230,8,19,10,19,12,19,233,9,19,1,20,1,20,1,20,1,
        20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,1,20,3,
        20,251,8,20,1,21,1,21,1,21,3,21,256,8,21,1,21,1,21,1,21,1,22,1,22,
        1,22,5,22,264,8,22,10,22,12,22,267,9,22,1,23,1,23,1,23,5,23,272,
        8,23,10,23,12,23,275,9,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,
        22,24,26,28,30,32,34,36,38,40,42,44,46,0,4,1,0,22,23,1,0,24,29,1,
        0,30,34,2,0,30,30,35,35,299,0,51,1,0,0,0,2,60,1,0,0,0,4,62,1,0,0,
        0,6,77,1,0,0,0,8,80,1,0,0,0,10,95,1,0,0,0,12,97,1,0,0,0,14,100,1,
        0,0,0,16,120,1,0,0,0,18,137,1,0,0,0,20,143,1,0,0,0,22,147,1,0,0,
        0,24,153,1,0,0,0,26,174,1,0,0,0,28,176,1,0,0,0,30,189,1,0,0,0,32,
        197,1,0,0,0,34,205,1,0,0,0,36,216,1,0,0,0,38,219,1,0,0,0,40,250,
        1,0,0,0,42,252,1,0,0,0,44,260,1,0,0,0,46,268,1,0,0,0,48,50,3,2,1,
        0,49,48,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,54,
        1,0,0,0,53,51,1,0,0,0,54,55,5,0,0,1,55,1,1,0,0,0,56,61,3,4,2,0,57,
        61,3,6,3,0,58,61,3,8,4,0,59,61,3,10,5,0,60,56,1,0,0,0,60,57,1,0,
        0,0,60,58,1,0,0,0,60,59,1,0,0,0,61,3,1,0,0,0,62,63,5,1,0,0,63,66,
        5,46,0,0,64,65,5,2,0,0,65,67,5,46,0,0,66,64,1,0,0,0,66,67,1,0,0,
        0,67,68,1,0,0,0,68,72,5,3,0,0,69,71,3,42,21,0,70,69,1,0,0,0,71,74,
        1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,72,1,0,0,0,
        75,76,5,4,0,0,76,5,1,0,0,0,77,78,5,5,0,0,78,79,3,42,21,0,79,7,1,
        0,0,0,80,81,5,6,0,0,81,84,5,46,0,0,82,83,5,7,0,0,83,85,3,26,13,0,
        84,82,1,0,0,0,84,85,1,0,0,0,85,86,1,0,0,0,86,87,5,8,0,0,87,9,1,0,
        0,0,88,96,3,12,6,0,89,96,3,14,7,0,90,96,3,16,8,0,91,96,3,18,9,0,
        92,96,3,20,10,0,93,96,3,22,11,0,94,96,3,24,12,0,95,88,1,0,0,0,95,
        89,1,0,0,0,95,90,1,0,0,0,95,91,1,0,0,0,95,92,1,0,0,0,95,93,1,0,0,
        0,95,94,1,0,0,0,96,11,1,0,0,0,97,98,3,26,13,0,98,99,5,8,0,0,99,13,
        1,0,0,0,100,101,5,9,0,0,101,102,5,10,0,0,102,103,3,26,13,0,103,104,
        5,11,0,0,104,113,3,24,12,0,105,106,5,12,0,0,106,107,5,10,0,0,107,
        108,3,26,13,0,108,109,5,11,0,0,109,110,3,24,12,0,110,112,1,0,0,0,
        111,105,1,0,0,0,112,115,1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,
        114,118,1,0,0,0,115,113,1,0,0,0,116,117,5,13,0,0,117,119,3,24,12,
        0,118,116,1,0,0,0,118,119,1,0,0,0,119,15,1,0,0,0,120,121,5,14,0,
        0,121,125,5,10,0,0,122,126,3,8,4,0,123,126,3,12,6,0,124,126,5,8,
        0,0,125,122,1,0,0,0,125,123,1,0,0,0,125,124,1,0,0,0,126,128,1,0,
        0,0,127,129,3,26,13,0,128,127,1,0,0,0,128,129,1,0,0,0,129,130,1,
        0,0,0,130,132,5,8,0,0,131,133,3,26,13,0,132,131,1,0,0,0,132,133,
        1,0,0,0,133,134,1,0,0,0,134,135,5,11,0,0,135,136,3,24,12,0,136,17,
        1,0,0,0,137,138,5,15,0,0,138,139,5,10,0,0,139,140,3,26,13,0,140,
        141,5,11,0,0,141,142,3,24,12,0,142,19,1,0,0,0,143,144,5,16,0,0,144,
        145,3,26,13,0,145,146,5,8,0,0,146,21,1,0,0,0,147,149,5,17,0,0,148,
        150,3,26,13,0,149,148,1,0,0,0,149,150,1,0,0,0,150,151,1,0,0,0,151,
        152,5,8,0,0,152,23,1,0,0,0,153,157,5,3,0,0,154,156,3,2,1,0,155,154,
        1,0,0,0,156,159,1,0,0,0,157,155,1,0,0,0,157,158,1,0,0,0,158,160,
        1,0,0,0,159,157,1,0,0,0,160,161,5,4,0,0,161,25,1,0,0,0,162,163,3,
        38,19,0,163,164,5,18,0,0,164,166,1,0,0,0,165,162,1,0,0,0,165,166,
        1,0,0,0,166,167,1,0,0,0,167,168,5,46,0,0,168,169,5,7,0,0,169,175,
        3,26,13,0,170,173,3,30,15,0,171,173,3,28,14,0,172,170,1,0,0,0,172,
        171,1,0,0,0,173,175,1,0,0,0,174,165,1,0,0,0,174,172,1,0,0,0,175,
        27,1,0,0,0,176,185,5,19,0,0,177,182,3,30,15,0,178,179,5,20,0,0,179,
        181,3,30,15,0,180,178,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,0,182,
        183,1,0,0,0,183,186,1,0,0,0,184,182,1,0,0,0,185,177,1,0,0,0,185,
        186,1,0,0,0,186,187,1,0,0,0,187,188,5,21,0,0,188,29,1,0,0,0,189,
        194,3,32,16,0,190,191,7,0,0,0,191,193,3,32,16,0,192,190,1,0,0,0,
        193,196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,0,195,31,1,0,0,0,196,
        194,1,0,0,0,197,202,3,34,17,0,198,199,7,1,0,0,199,201,3,34,17,0,
        200,198,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,0,0,0,
        203,33,1,0,0,0,204,202,1,0,0,0,205,210,3,36,18,0,206,207,7,2,0,0,
        207,209,3,36,18,0,208,206,1,0,0,0,209,212,1,0,0,0,210,208,1,0,0,
        0,210,211,1,0,0,0,211,35,1,0,0,0,212,210,1,0,0,0,213,214,7,3,0,0,
        214,217,3,36,18,0,215,217,3,38,19,0,216,213,1,0,0,0,216,215,1,0,
        0,0,217,37,1,0,0,0,218,220,5,36,0,0,219,218,1,0,0,0,219,220,1,0,
        0,0,220,221,1,0,0,0,221,231,3,40,20,0,222,224,5,10,0,0,223,225,3,
        46,23,0,224,223,1,0,0,0,224,225,1,0,0,0,225,226,1,0,0,0,226,230,
        5,11,0,0,227,228,5,18,0,0,228,230,5,46,0,0,229,222,1,0,0,0,229,227,
        1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,39,1,
        0,0,0,233,231,1,0,0,0,234,251,5,37,0,0,235,251,5,38,0,0,236,251,
        5,39,0,0,237,251,5,40,0,0,238,251,5,41,0,0,239,251,5,42,0,0,240,
        251,5,44,0,0,241,251,5,45,0,0,242,251,5,46,0,0,243,244,5,10,0,0,
        244,245,3,26,13,0,245,246,5,11,0,0,246,251,1,0,0,0,247,248,5,43,
        0,0,248,249,5,18,0,0,249,251,5,46,0,0,250,234,1,0,0,0,250,235,1,
        0,0,0,250,236,1,0,0,0,250,237,1,0,0,0,250,238,1,0,0,0,250,239,1,
        0,0,0,250,240,1,0,0,0,250,241,1,0,0,0,250,242,1,0,0,0,250,243,1,
        0,0,0,250,247,1,0,0,0,251,41,1,0,0,0,252,253,5,46,0,0,253,255,5,
        10,0,0,254,256,3,44,22,0,255,254,1,0,0,0,255,256,1,0,0,0,256,257,
        1,0,0,0,257,258,5,11,0,0,258,259,3,24,12,0,259,43,1,0,0,0,260,265,
        5,46,0,0,261,262,5,20,0,0,262,264,5,46,0,0,263,261,1,0,0,0,264,267,
        1,0,0,0,265,263,1,0,0,0,265,266,1,0,0,0,266,45,1,0,0,0,267,265,1,
        0,0,0,268,273,3,26,13,0,269,270,5,20,0,0,270,272,3,26,13,0,271,269,
        1,0,0,0,272,275,1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,47,1,
        0,0,0,275,273,1,0,0,0,30,51,60,66,72,84,95,113,118,125,128,132,149,
        157,165,172,174,182,185,194,202,210,216,219,224,229,231,250,255,
        265,273
    ]

class CompiScriptLanguageParser ( Parser ):

    grammarFileName = "CompiScriptLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'extends'", "'{'", "'}'", 
                     "'fun'", "'var'", "'='", "';'", "'if'", "'('", "')'", 
                     "'else if'", "'else'", "'for'", "'while'", "'print'", 
                     "'return'", "'.'", "'['", "','", "']'", "'and'", "'or'", 
                     "'>'", "'>='", "'<'", "'<='", "'!='", "'=='", "'-'", 
                     "'+'", "'/'", "'*'", "'%'", "'!'", "'new'", "'true'", 
                     "'false'", "'nil'", "'this'", "'break'", "'continue'", 
                     "'super'" ]

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
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "STRING", "IDENTIFIER", "WS", "MALFORMED" ]

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
    RULE_array = 14
    RULE_logic = 15
    RULE_comparison = 16
    RULE_term = 17
    RULE_unary = 18
    RULE_call = 19
    RULE_primary = 20
    RULE_function = 21
    RULE_parameters = 22
    RULE_arguments = 23

    ruleNames =  [ "program", "declaration", "classDecl", "funDecl", "varDecl", 
                   "statement", "exprStmt", "ifStmt", "forStmt", "whileStmt", 
                   "printStmt", "returnStmt", "block", "expression", "array", 
                   "logic", "comparison", "term", "unary", "call", "primary", 
                   "function", "parameters", "arguments" ]

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
    T__41=42
    T__42=43
    NUMBER=44
    STRING=45
    IDENTIFIER=46
    WS=47
    MALFORMED=48

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
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140704203130474) != 0):
                self.state = 48
                self.declaration()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
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
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.classDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.funDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 58
                self.varDecl()
                pass
            elif token in [3, 9, 10, 14, 15, 16, 17, 19, 30, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 4)
                self.state = 59
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
            self.state = 62
            self.match(CompiScriptLanguageParser.T__0)
            self.state = 63
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 64
                self.match(CompiScriptLanguageParser.T__1)
                self.state = 65
                self.match(CompiScriptLanguageParser.IDENTIFIER)


            self.state = 68
            self.match(CompiScriptLanguageParser.T__2)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==46:
                self.state = 69
                self.function()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 75
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
            self.state = 77
            self.match(CompiScriptLanguageParser.T__4)
            self.state = 78
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
            self.state = 80
            self.match(CompiScriptLanguageParser.T__5)
            self.state = 81
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 82
                self.match(CompiScriptLanguageParser.T__6)
                self.state = 83
                self.expression()


            self.state = 86
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
            self.state = 95
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 19, 30, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.exprStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 89
                self.ifStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 90
                self.forStmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 91
                self.whileStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 92
                self.printStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 93
                self.returnStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 7)
                self.state = 94
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
            self.state = 97
            self.expression()
            self.state = 98
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
            self.state = 100
            self.match(CompiScriptLanguageParser.T__8)
            self.state = 101
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 102
            self.expression()
            self.state = 103
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 104
            self.block()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 105
                self.match(CompiScriptLanguageParser.T__11)
                self.state = 106
                self.match(CompiScriptLanguageParser.T__9)
                self.state = 107
                self.expression()
                self.state = 108
                self.match(CompiScriptLanguageParser.T__10)
                self.state = 109
                self.block()
                self.state = 115
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 116
                self.match(CompiScriptLanguageParser.T__12)
                self.state = 117
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
            self.state = 120
            self.match(CompiScriptLanguageParser.T__13)
            self.state = 121
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 125
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 122
                self.varDecl()
                pass
            elif token in [10, 19, 30, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]:
                self.state = 123
                self.exprStmt()
                pass
            elif token in [8]:
                self.state = 124
                self.match(CompiScriptLanguageParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140704202884096) != 0):
                self.state = 127
                self.expression()


            self.state = 130
            self.match(CompiScriptLanguageParser.T__7)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140704202884096) != 0):
                self.state = 131
                self.expression()


            self.state = 134
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 135
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
            self.state = 137
            self.match(CompiScriptLanguageParser.T__14)
            self.state = 138
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 139
            self.expression()
            self.state = 140
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 141
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
            self.state = 143
            self.match(CompiScriptLanguageParser.T__15)
            self.state = 144
            self.expression()
            self.state = 145
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
            self.state = 147
            self.match(CompiScriptLanguageParser.T__16)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140704202884096) != 0):
                self.state = 148
                self.expression()


            self.state = 151
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
            self.state = 153
            self.match(CompiScriptLanguageParser.T__2)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 140704203130474) != 0):
                self.state = 154
                self.declaration()
                self.state = 159
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 160
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


        def array(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ArrayContext,0)


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
            self.state = 174
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 165
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 162
                    self.call()
                    self.state = 163
                    self.match(CompiScriptLanguageParser.T__17)


                self.state = 167
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                self.state = 168
                self.match(CompiScriptLanguageParser.T__6)
                self.state = 169
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 172
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [10, 30, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]:
                    self.state = 170
                    self.logic()
                    pass
                elif token in [19]:
                    self.state = 171
                    self.array()
                    pass
                else:
                    raise NoViableAltException(self)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logic(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CompiScriptLanguageParser.LogicContext)
            else:
                return self.getTypedRuleContext(CompiScriptLanguageParser.LogicContext,i)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = CompiScriptLanguageParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
            self.match(CompiScriptLanguageParser.T__18)
            self.state = 185
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140704202359808) != 0):
                self.state = 177
                self.logic()
                self.state = 182
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 178
                    self.match(CompiScriptLanguageParser.T__19)
                    self.state = 179
                    self.logic()
                    self.state = 184
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 187
            self.match(CompiScriptLanguageParser.T__20)
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
        self.enterRule(localctx, 30, self.RULE_logic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.comparison()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22 or _la==23:
                self.state = 190
                _la = self._input.LA(1)
                if not(_la==22 or _la==23):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 191
                self.comparison()
                self.state = 196
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
        self.enterRule(localctx, 32, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.term()
            self.state = 202
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0):
                self.state = 198
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1056964608) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 199
                self.term()
                self.state = 204
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
        self.enterRule(localctx, 34, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 205
            self.unary()
            self.state = 210
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 33285996544) != 0):
                self.state = 206
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 33285996544) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 207
                self.unary()
                self.state = 212
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
        self.enterRule(localctx, 36, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [30, 35]:
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                _la = self._input.LA(1)
                if not(_la==30 or _la==35):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 214
                self.unary()
                pass
            elif token in [10, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46]:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
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
        self.enterRule(localctx, 38, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 218
                self.match(CompiScriptLanguageParser.T__35)


            self.state = 221
            self.primary()
            self.state = 231
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 229
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [10]:
                        self.state = 222
                        self.match(CompiScriptLanguageParser.T__9)
                        self.state = 224
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 140704202884096) != 0):
                            self.state = 223
                            self.arguments()


                        self.state = 226
                        self.match(CompiScriptLanguageParser.T__10)
                        pass
                    elif token in [18]:
                        self.state = 227
                        self.match(CompiScriptLanguageParser.T__17)
                        self.state = 228
                        self.match(CompiScriptLanguageParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 233
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        self.enterRule(localctx, 40, self.RULE_primary)
        try:
            self.state = 250
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(CompiScriptLanguageParser.T__36)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(CompiScriptLanguageParser.T__37)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
                self.match(CompiScriptLanguageParser.T__38)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 4)
                self.state = 237
                self.match(CompiScriptLanguageParser.T__39)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 5)
                self.state = 238
                self.match(CompiScriptLanguageParser.T__40)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 6)
                self.state = 239
                self.match(CompiScriptLanguageParser.T__41)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 7)
                self.state = 240
                self.match(CompiScriptLanguageParser.NUMBER)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 8)
                self.state = 241
                self.match(CompiScriptLanguageParser.STRING)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 9)
                self.state = 242
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 10)
                self.state = 243
                self.match(CompiScriptLanguageParser.T__9)
                self.state = 244
                self.expression()
                self.state = 245
                self.match(CompiScriptLanguageParser.T__10)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 11)
                self.state = 247
                self.match(CompiScriptLanguageParser.T__42)
                self.state = 248
                self.match(CompiScriptLanguageParser.T__17)
                self.state = 249
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
        self.enterRule(localctx, 42, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 252
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 253
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==46:
                self.state = 254
                self.parameters()


            self.state = 257
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 258
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
        self.enterRule(localctx, 44, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 265
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 261
                self.match(CompiScriptLanguageParser.T__19)
                self.state = 262
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                self.state = 267
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
        self.enterRule(localctx, 46, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.expression()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 269
                self.match(CompiScriptLanguageParser.T__19)
                self.state = 270
                self.expression()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





