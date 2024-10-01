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
        4,1,50,306,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,1,0,5,0,58,8,0,10,0,12,0,61,9,0,1,0,1,0,1,1,1,1,1,1,1,
        1,3,1,69,8,1,1,2,1,2,1,2,1,2,3,2,75,8,2,1,2,1,2,5,2,79,8,2,10,2,
        12,2,82,9,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,1,4,1,4,3,4,93,8,4,1,4,1,
        4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,104,8,5,1,6,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,7,5,7,120,8,7,10,7,12,7,123,9,7,
        1,7,1,7,3,7,127,8,7,1,8,1,8,1,8,1,8,1,8,3,8,134,8,8,1,8,3,8,137,
        8,8,1,8,1,8,3,8,141,8,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,11,1,11,3,11,158,8,11,1,11,1,11,1,12,1,12,5,12,
        164,8,12,10,12,12,12,167,9,12,1,12,1,12,1,13,1,13,1,13,3,13,174,
        8,13,1,13,1,13,1,13,1,13,1,13,3,13,181,8,13,3,13,183,8,13,1,14,1,
        14,1,14,1,14,3,14,189,8,14,1,15,1,15,1,15,1,15,5,15,195,8,15,10,
        15,12,15,198,9,15,3,15,200,8,15,1,15,1,15,1,16,1,16,1,16,1,16,1,
        16,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,
        19,5,19,222,8,19,10,19,12,19,225,9,19,1,20,1,20,1,20,5,20,230,8,
        20,10,20,12,20,233,9,20,1,21,1,21,1,21,5,21,238,8,21,10,21,12,21,
        241,9,21,1,22,1,22,1,22,3,22,246,8,22,1,23,3,23,249,8,23,1,23,1,
        23,1,23,3,23,254,8,23,1,23,1,23,1,23,5,23,259,8,23,10,23,12,23,262,
        9,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,24,1,24,1,24,3,24,280,8,24,1,25,1,25,1,25,3,25,285,8,25,1,
        25,1,25,1,25,1,26,1,26,1,26,5,26,293,8,26,10,26,12,26,296,9,26,1,
        27,1,27,1,27,5,27,301,8,27,10,27,12,27,304,9,27,1,27,0,0,28,0,2,
        4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,
        50,52,54,0,4,1,0,24,25,1,0,26,31,1,0,32,36,2,0,32,32,37,37,327,0,
        59,1,0,0,0,2,68,1,0,0,0,4,70,1,0,0,0,6,85,1,0,0,0,8,88,1,0,0,0,10,
        103,1,0,0,0,12,105,1,0,0,0,14,108,1,0,0,0,16,128,1,0,0,0,18,145,
        1,0,0,0,20,151,1,0,0,0,22,155,1,0,0,0,24,161,1,0,0,0,26,182,1,0,
        0,0,28,188,1,0,0,0,30,190,1,0,0,0,32,203,1,0,0,0,34,208,1,0,0,0,
        36,213,1,0,0,0,38,218,1,0,0,0,40,226,1,0,0,0,42,234,1,0,0,0,44,245,
        1,0,0,0,46,248,1,0,0,0,48,279,1,0,0,0,50,281,1,0,0,0,52,289,1,0,
        0,0,54,297,1,0,0,0,56,58,3,2,1,0,57,56,1,0,0,0,58,61,1,0,0,0,59,
        57,1,0,0,0,59,60,1,0,0,0,60,62,1,0,0,0,61,59,1,0,0,0,62,63,5,0,0,
        1,63,1,1,0,0,0,64,69,3,4,2,0,65,69,3,6,3,0,66,69,3,8,4,0,67,69,3,
        10,5,0,68,64,1,0,0,0,68,65,1,0,0,0,68,66,1,0,0,0,68,67,1,0,0,0,69,
        3,1,0,0,0,70,71,5,1,0,0,71,74,5,48,0,0,72,73,5,2,0,0,73,75,5,48,
        0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,76,1,0,0,0,76,80,5,3,0,0,77,79,
        3,50,25,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,1,0,0,
        0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,5,4,0,0,84,5,1,0,0,0,85,86,5,
        5,0,0,86,87,3,50,25,0,87,7,1,0,0,0,88,89,5,6,0,0,89,92,5,48,0,0,
        90,91,5,7,0,0,91,93,3,26,13,0,92,90,1,0,0,0,92,93,1,0,0,0,93,94,
        1,0,0,0,94,95,5,8,0,0,95,9,1,0,0,0,96,104,3,12,6,0,97,104,3,14,7,
        0,98,104,3,16,8,0,99,104,3,18,9,0,100,104,3,20,10,0,101,104,3,22,
        11,0,102,104,3,24,12,0,103,96,1,0,0,0,103,97,1,0,0,0,103,98,1,0,
        0,0,103,99,1,0,0,0,103,100,1,0,0,0,103,101,1,0,0,0,103,102,1,0,0,
        0,104,11,1,0,0,0,105,106,3,26,13,0,106,107,5,8,0,0,107,13,1,0,0,
        0,108,109,5,9,0,0,109,110,5,10,0,0,110,111,3,26,13,0,111,112,5,11,
        0,0,112,121,3,24,12,0,113,114,5,12,0,0,114,115,5,10,0,0,115,116,
        3,26,13,0,116,117,5,11,0,0,117,118,3,24,12,0,118,120,1,0,0,0,119,
        113,1,0,0,0,120,123,1,0,0,0,121,119,1,0,0,0,121,122,1,0,0,0,122,
        126,1,0,0,0,123,121,1,0,0,0,124,125,5,13,0,0,125,127,3,24,12,0,126,
        124,1,0,0,0,126,127,1,0,0,0,127,15,1,0,0,0,128,129,5,14,0,0,129,
        133,5,10,0,0,130,134,3,8,4,0,131,134,3,12,6,0,132,134,5,8,0,0,133,
        130,1,0,0,0,133,131,1,0,0,0,133,132,1,0,0,0,134,136,1,0,0,0,135,
        137,3,26,13,0,136,135,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,
        140,5,8,0,0,139,141,3,26,13,0,140,139,1,0,0,0,140,141,1,0,0,0,141,
        142,1,0,0,0,142,143,5,11,0,0,143,144,3,24,12,0,144,17,1,0,0,0,145,
        146,5,15,0,0,146,147,5,10,0,0,147,148,3,26,13,0,148,149,5,11,0,0,
        149,150,3,24,12,0,150,19,1,0,0,0,151,152,5,16,0,0,152,153,3,26,13,
        0,153,154,5,8,0,0,154,21,1,0,0,0,155,157,5,17,0,0,156,158,3,26,13,
        0,157,156,1,0,0,0,157,158,1,0,0,0,158,159,1,0,0,0,159,160,5,8,0,
        0,160,23,1,0,0,0,161,165,5,3,0,0,162,164,3,2,1,0,163,162,1,0,0,0,
        164,167,1,0,0,0,165,163,1,0,0,0,165,166,1,0,0,0,166,168,1,0,0,0,
        167,165,1,0,0,0,168,169,5,4,0,0,169,25,1,0,0,0,170,171,3,46,23,0,
        171,172,5,18,0,0,172,174,1,0,0,0,173,170,1,0,0,0,173,174,1,0,0,0,
        174,175,1,0,0,0,175,176,5,48,0,0,176,177,5,7,0,0,177,183,3,26,13,
        0,178,181,3,28,14,0,179,181,3,38,19,0,180,178,1,0,0,0,180,179,1,
        0,0,0,181,183,1,0,0,0,182,173,1,0,0,0,182,180,1,0,0,0,183,27,1,0,
        0,0,184,189,3,30,15,0,185,189,3,32,16,0,186,189,3,34,17,0,187,189,
        3,36,18,0,188,184,1,0,0,0,188,185,1,0,0,0,188,186,1,0,0,0,188,187,
        1,0,0,0,189,29,1,0,0,0,190,199,5,19,0,0,191,196,3,38,19,0,192,193,
        5,20,0,0,193,195,3,38,19,0,194,192,1,0,0,0,195,198,1,0,0,0,196,194,
        1,0,0,0,196,197,1,0,0,0,197,200,1,0,0,0,198,196,1,0,0,0,199,191,
        1,0,0,0,199,200,1,0,0,0,200,201,1,0,0,0,201,202,5,21,0,0,202,31,
        1,0,0,0,203,204,5,48,0,0,204,205,5,19,0,0,205,206,5,46,0,0,206,207,
        5,21,0,0,207,33,1,0,0,0,208,209,5,48,0,0,209,210,5,22,0,0,210,211,
        3,38,19,0,211,212,5,11,0,0,212,35,1,0,0,0,213,214,5,48,0,0,214,215,
        5,23,0,0,215,216,5,46,0,0,216,217,5,11,0,0,217,37,1,0,0,0,218,223,
        3,40,20,0,219,220,7,0,0,0,220,222,3,40,20,0,221,219,1,0,0,0,222,
        225,1,0,0,0,223,221,1,0,0,0,223,224,1,0,0,0,224,39,1,0,0,0,225,223,
        1,0,0,0,226,231,3,42,21,0,227,228,7,1,0,0,228,230,3,42,21,0,229,
        227,1,0,0,0,230,233,1,0,0,0,231,229,1,0,0,0,231,232,1,0,0,0,232,
        41,1,0,0,0,233,231,1,0,0,0,234,239,3,44,22,0,235,236,7,2,0,0,236,
        238,3,44,22,0,237,235,1,0,0,0,238,241,1,0,0,0,239,237,1,0,0,0,239,
        240,1,0,0,0,240,43,1,0,0,0,241,239,1,0,0,0,242,243,7,3,0,0,243,246,
        3,44,22,0,244,246,3,46,23,0,245,242,1,0,0,0,245,244,1,0,0,0,246,
        45,1,0,0,0,247,249,5,38,0,0,248,247,1,0,0,0,248,249,1,0,0,0,249,
        250,1,0,0,0,250,260,3,48,24,0,251,253,5,10,0,0,252,254,3,54,27,0,
        253,252,1,0,0,0,253,254,1,0,0,0,254,255,1,0,0,0,255,259,5,11,0,0,
        256,257,5,18,0,0,257,259,5,48,0,0,258,251,1,0,0,0,258,256,1,0,0,
        0,259,262,1,0,0,0,260,258,1,0,0,0,260,261,1,0,0,0,261,47,1,0,0,0,
        262,260,1,0,0,0,263,280,5,39,0,0,264,280,5,40,0,0,265,280,5,41,0,
        0,266,280,5,42,0,0,267,280,5,43,0,0,268,280,5,44,0,0,269,280,5,46,
        0,0,270,280,5,47,0,0,271,280,5,48,0,0,272,273,5,10,0,0,273,274,3,
        26,13,0,274,275,5,11,0,0,275,280,1,0,0,0,276,277,5,45,0,0,277,278,
        5,18,0,0,278,280,5,48,0,0,279,263,1,0,0,0,279,264,1,0,0,0,279,265,
        1,0,0,0,279,266,1,0,0,0,279,267,1,0,0,0,279,268,1,0,0,0,279,269,
        1,0,0,0,279,270,1,0,0,0,279,271,1,0,0,0,279,272,1,0,0,0,279,276,
        1,0,0,0,280,49,1,0,0,0,281,282,5,48,0,0,282,284,5,10,0,0,283,285,
        3,52,26,0,284,283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,287,
        5,11,0,0,287,288,3,24,12,0,288,51,1,0,0,0,289,294,5,48,0,0,290,291,
        5,20,0,0,291,293,5,48,0,0,292,290,1,0,0,0,293,296,1,0,0,0,294,292,
        1,0,0,0,294,295,1,0,0,0,295,53,1,0,0,0,296,294,1,0,0,0,297,302,3,
        26,13,0,298,299,5,20,0,0,299,301,3,26,13,0,300,298,1,0,0,0,301,304,
        1,0,0,0,302,300,1,0,0,0,302,303,1,0,0,0,303,55,1,0,0,0,304,302,1,
        0,0,0,31,59,68,74,80,92,103,121,126,133,136,140,157,165,173,180,
        182,188,196,199,223,231,239,245,248,253,258,260,279,284,294,302
    ]

class CompiScriptLanguageParser ( Parser ):

    grammarFileName = "CompiScriptLanguage.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'class'", "'extends'", "'{'", "'}'", 
                     "'fun'", "'var'", "'='", "';'", "'if'", "'('", "')'", 
                     "'else if'", "'else'", "'for'", "'while'", "'print'", 
                     "'return'", "'.'", "'['", "','", "']'", "'.push('", 
                     "'.pop('", "'and'", "'or'", "'>'", "'>='", "'<'", "'<='", 
                     "'!='", "'=='", "'-'", "'+'", "'/'", "'*'", "'%'", 
                     "'!'", "'new'", "'true'", "'false'", "'nil'", "'this'", 
                     "'break'", "'continue'", "'super'" ]

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
    RULE_array = 14
    RULE_arrayCreation = 15
    RULE_arrayAccess = 16
    RULE_arrayPush = 17
    RULE_arrayPop = 18
    RULE_logic = 19
    RULE_comparison = 20
    RULE_term = 21
    RULE_unary = 22
    RULE_call = 23
    RULE_primary = 24
    RULE_function = 25
    RULE_parameters = 26
    RULE_arguments = 27

    ruleNames =  [ "program", "declaration", "classDecl", "funDecl", "varDecl", 
                   "statement", "exprStmt", "ifStmt", "forStmt", "whileStmt", 
                   "printStmt", "returnStmt", "block", "expression", "array", 
                   "arrayCreation", "arrayAccess", "arrayPush", "arrayPop", 
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
    T__43=44
    T__44=45
    NUMBER=46
    STRING=47
    IDENTIFIER=48
    WS=49
    MALFORMED=50

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
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562816810206826) != 0):
                self.state = 56
                self.declaration()
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 62
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
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 64
                self.classDecl()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 65
                self.funDecl()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 3)
                self.state = 66
                self.varDecl()
                pass
            elif token in [3, 9, 10, 14, 15, 16, 17, 19, 32, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
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
            self.state = 70
            self.match(CompiScriptLanguageParser.T__0)
            self.state = 71
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 74
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==2:
                self.state = 72
                self.match(CompiScriptLanguageParser.T__1)
                self.state = 73
                self.match(CompiScriptLanguageParser.IDENTIFIER)


            self.state = 76
            self.match(CompiScriptLanguageParser.T__2)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==48:
                self.state = 77
                self.function()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
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
            self.state = 85
            self.match(CompiScriptLanguageParser.T__4)
            self.state = 86
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
            self.state = 88
            self.match(CompiScriptLanguageParser.T__5)
            self.state = 89
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 90
                self.match(CompiScriptLanguageParser.T__6)
                self.state = 91
                self.expression()


            self.state = 94
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
            self.state = 103
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 19, 32, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 1)
                self.state = 96
                self.exprStmt()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 97
                self.ifStmt()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 3)
                self.state = 98
                self.forStmt()
                pass
            elif token in [15]:
                self.enterOuterAlt(localctx, 4)
                self.state = 99
                self.whileStmt()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 5)
                self.state = 100
                self.printStmt()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 6)
                self.state = 101
                self.returnStmt()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 7)
                self.state = 102
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
            self.state = 105
            self.expression()
            self.state = 106
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
            self.state = 108
            self.match(CompiScriptLanguageParser.T__8)
            self.state = 109
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 110
            self.expression()
            self.state = 111
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 112
            self.block()
            self.state = 121
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 113
                self.match(CompiScriptLanguageParser.T__11)
                self.state = 114
                self.match(CompiScriptLanguageParser.T__9)
                self.state = 115
                self.expression()
                self.state = 116
                self.match(CompiScriptLanguageParser.T__10)
                self.state = 117
                self.block()
                self.state = 123
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 124
                self.match(CompiScriptLanguageParser.T__12)
                self.state = 125
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
            self.state = 128
            self.match(CompiScriptLanguageParser.T__13)
            self.state = 129
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 133
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 130
                self.varDecl()
                pass
            elif token in [10, 19, 32, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]:
                self.state = 131
                self.exprStmt()
                pass
            elif token in [8]:
                self.state = 132
                self.match(CompiScriptLanguageParser.T__7)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 562816809960448) != 0):
                self.state = 135
                self.expression()


            self.state = 138
            self.match(CompiScriptLanguageParser.T__7)
            self.state = 140
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 562816809960448) != 0):
                self.state = 139
                self.expression()


            self.state = 142
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 143
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
            self.state = 145
            self.match(CompiScriptLanguageParser.T__14)
            self.state = 146
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 147
            self.expression()
            self.state = 148
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 149
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
            self.state = 151
            self.match(CompiScriptLanguageParser.T__15)
            self.state = 152
            self.expression()
            self.state = 153
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
            self.state = 155
            self.match(CompiScriptLanguageParser.T__16)
            self.state = 157
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 562816809960448) != 0):
                self.state = 156
                self.expression()


            self.state = 159
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
            self.state = 161
            self.match(CompiScriptLanguageParser.T__2)
            self.state = 165
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 562816810206826) != 0):
                self.state = 162
                self.declaration()
                self.state = 167
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 168
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


        def array(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ArrayContext,0)


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
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 173
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 170
                    self.call()
                    self.state = 171
                    self.match(CompiScriptLanguageParser.T__17)


                self.state = 175
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                self.state = 176
                self.match(CompiScriptLanguageParser.T__6)
                self.state = 177
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 180
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                if la_ == 1:
                    self.state = 178
                    self.array()
                    pass

                elif la_ == 2:
                    self.state = 179
                    self.logic()
                    pass


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

        def arrayCreation(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ArrayCreationContext,0)


        def arrayAccess(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ArrayAccessContext,0)


        def arrayPush(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ArrayPushContext,0)


        def arrayPop(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.ArrayPopContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 184
                self.arrayCreation()
                pass

            elif la_ == 2:
                self.state = 185
                self.arrayAccess()
                pass

            elif la_ == 3:
                self.state = 186
                self.arrayPush()
                pass

            elif la_ == 4:
                self.state = 187
                self.arrayPop()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayCreationContext(ParserRuleContext):
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
            return CompiScriptLanguageParser.RULE_arrayCreation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayCreation" ):
                listener.enterArrayCreation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayCreation" ):
                listener.exitArrayCreation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayCreation" ):
                return visitor.visitArrayCreation(self)
            else:
                return visitor.visitChildren(self)




    def arrayCreation(self):

        localctx = CompiScriptLanguageParser.ArrayCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_arrayCreation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.match(CompiScriptLanguageParser.T__18)
            self.state = 199
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 562816809436160) != 0):
                self.state = 191
                self.logic()
                self.state = 196
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 192
                    self.match(CompiScriptLanguageParser.T__19)
                    self.state = 193
                    self.logic()
                    self.state = 198
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 201
            self.match(CompiScriptLanguageParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CompiScriptLanguageParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(CompiScriptLanguageParser.NUMBER, 0)

        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_arrayAccess

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayAccess" ):
                listener.enterArrayAccess(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayAccess" ):
                listener.exitArrayAccess(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayAccess" ):
                return visitor.visitArrayAccess(self)
            else:
                return visitor.visitChildren(self)




    def arrayAccess(self):

        localctx = CompiScriptLanguageParser.ArrayAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_arrayAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 204
            self.match(CompiScriptLanguageParser.T__18)
            self.state = 205
            self.match(CompiScriptLanguageParser.NUMBER)
            self.state = 206
            self.match(CompiScriptLanguageParser.T__20)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayPushContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CompiScriptLanguageParser.IDENTIFIER, 0)

        def logic(self):
            return self.getTypedRuleContext(CompiScriptLanguageParser.LogicContext,0)


        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_arrayPush

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayPush" ):
                listener.enterArrayPush(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayPush" ):
                listener.exitArrayPush(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayPush" ):
                return visitor.visitArrayPush(self)
            else:
                return visitor.visitChildren(self)




    def arrayPush(self):

        localctx = CompiScriptLanguageParser.ArrayPushContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_arrayPush)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 209
            self.match(CompiScriptLanguageParser.T__21)
            self.state = 210
            self.logic()
            self.state = 211
            self.match(CompiScriptLanguageParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayPopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(CompiScriptLanguageParser.IDENTIFIER, 0)

        def NUMBER(self):
            return self.getToken(CompiScriptLanguageParser.NUMBER, 0)

        def getRuleIndex(self):
            return CompiScriptLanguageParser.RULE_arrayPop

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayPop" ):
                listener.enterArrayPop(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayPop" ):
                listener.exitArrayPop(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrayPop" ):
                return visitor.visitArrayPop(self)
            else:
                return visitor.visitChildren(self)




    def arrayPop(self):

        localctx = CompiScriptLanguageParser.ArrayPopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_arrayPop)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 214
            self.match(CompiScriptLanguageParser.T__22)
            self.state = 215
            self.match(CompiScriptLanguageParser.NUMBER)
            self.state = 216
            self.match(CompiScriptLanguageParser.T__10)
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
        self.enterRule(localctx, 38, self.RULE_logic)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.comparison()
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 219
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 220
                self.comparison()
                self.state = 225
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
        self.enterRule(localctx, 40, self.RULE_comparison)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 226
            self.term()
            self.state = 231
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0):
                self.state = 227
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4227858432) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228
                self.term()
                self.state = 233
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
        self.enterRule(localctx, 42, self.RULE_term)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.unary()
            self.state = 239
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 133143986176) != 0):
                self.state = 235
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 133143986176) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 236
                self.unary()
                self.state = 241
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
        self.enterRule(localctx, 44, self.RULE_unary)
        self._la = 0 # Token type
        try:
            self.state = 245
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [32, 37]:
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                _la = self._input.LA(1)
                if not(_la==32 or _la==37):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 243
                self.unary()
                pass
            elif token in [10, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
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
        self.enterRule(localctx, 46, self.RULE_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==38:
                self.state = 247
                self.match(CompiScriptLanguageParser.T__37)


            self.state = 250
            self.primary()
            self.state = 260
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 258
                    self._errHandler.sync(self)
                    token = self._input.LA(1)
                    if token in [10]:
                        self.state = 251
                        self.match(CompiScriptLanguageParser.T__9)
                        self.state = 253
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & 562816809960448) != 0):
                            self.state = 252
                            self.arguments()


                        self.state = 255
                        self.match(CompiScriptLanguageParser.T__10)
                        pass
                    elif token in [18]:
                        self.state = 256
                        self.match(CompiScriptLanguageParser.T__17)
                        self.state = 257
                        self.match(CompiScriptLanguageParser.IDENTIFIER)
                        pass
                    else:
                        raise NoViableAltException(self)
             
                self.state = 262
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        self.enterRule(localctx, 48, self.RULE_primary)
        try:
            self.state = 279
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [39]:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self.match(CompiScriptLanguageParser.T__38)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
                self.match(CompiScriptLanguageParser.T__39)
                pass
            elif token in [41]:
                self.enterOuterAlt(localctx, 3)
                self.state = 265
                self.match(CompiScriptLanguageParser.T__40)
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 4)
                self.state = 266
                self.match(CompiScriptLanguageParser.T__41)
                pass
            elif token in [43]:
                self.enterOuterAlt(localctx, 5)
                self.state = 267
                self.match(CompiScriptLanguageParser.T__42)
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 6)
                self.state = 268
                self.match(CompiScriptLanguageParser.T__43)
                pass
            elif token in [46]:
                self.enterOuterAlt(localctx, 7)
                self.state = 269
                self.match(CompiScriptLanguageParser.NUMBER)
                pass
            elif token in [47]:
                self.enterOuterAlt(localctx, 8)
                self.state = 270
                self.match(CompiScriptLanguageParser.STRING)
                pass
            elif token in [48]:
                self.enterOuterAlt(localctx, 9)
                self.state = 271
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 10)
                self.state = 272
                self.match(CompiScriptLanguageParser.T__9)
                self.state = 273
                self.expression()
                self.state = 274
                self.match(CompiScriptLanguageParser.T__10)
                pass
            elif token in [45]:
                self.enterOuterAlt(localctx, 11)
                self.state = 276
                self.match(CompiScriptLanguageParser.T__44)
                self.state = 277
                self.match(CompiScriptLanguageParser.T__17)
                self.state = 278
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
        self.enterRule(localctx, 50, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 282
            self.match(CompiScriptLanguageParser.T__9)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 283
                self.parameters()


            self.state = 286
            self.match(CompiScriptLanguageParser.T__10)
            self.state = 287
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
        self.enterRule(localctx, 52, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 289
            self.match(CompiScriptLanguageParser.IDENTIFIER)
            self.state = 294
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 290
                self.match(CompiScriptLanguageParser.T__19)
                self.state = 291
                self.match(CompiScriptLanguageParser.IDENTIFIER)
                self.state = 296
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
        self.enterRule(localctx, 54, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expression()
            self.state = 302
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 298
                self.match(CompiScriptLanguageParser.T__19)
                self.state = 299
                self.expression()
                self.state = 304
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





