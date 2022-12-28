# Generated from BKIT.g4 by ANTLR 4.11.1
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
        4,1,30,11,2,0,7,0,1,0,5,0,4,8,0,10,0,12,0,7,9,0,1,0,1,0,1,0,0,0,
        1,0,0,1,1,0,1,25,10,0,5,1,0,0,0,2,4,7,0,0,0,3,2,1,0,0,0,4,7,1,0,
        0,0,5,3,1,0,0,0,5,6,1,0,0,0,6,8,1,0,0,0,7,5,1,0,0,0,8,9,5,0,0,1,
        9,1,1,0,0,0,1,5
    ]

class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'#include'", "'if'", "'while'", "'using'", 
                     "'namespace'", "'cout'", "<INVALID>", "'int'", "'main'", 
                     "'return'", "';'", "'('", "')'", "'{'", "'}'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'='" ]

    symbolicNames = [ "<INVALID>", "Include", "If", "While", "Using", "NameSpace", 
                      "Cout", "InternalLib", "Int", "Main", "Return", "Semi", 
                      "OpenPara", "ClosePara", "OpenBraket", "CloseBraket", 
                      "Shift", "InEq", "Inc", "Eq", "Assignment", "Id", 
                      "Integer", "Float", "String", "Char", "Skip", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    Include=1
    If=2
    While=3
    Using=4
    NameSpace=5
    Cout=6
    InternalLib=7
    Int=8
    Main=9
    Return=10
    Semi=11
    OpenPara=12
    ClosePara=13
    OpenBraket=14
    CloseBraket=15
    Shift=16
    InEq=17
    Inc=18
    Eq=19
    Assignment=20
    Id=21
    Integer=22
    Float=23
    String=24
    Char=25
    Skip=26
    ERROR_CHAR=27
    UNCLOSE_STRING=28
    ILLEGAL_ESCAPE=29
    UNTERMINATED_COMMENT=30

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def Include(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Include)
            else:
                return self.getToken(BKITParser.Include, i)

        def If(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.If)
            else:
                return self.getToken(BKITParser.If, i)

        def While(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.While)
            else:
                return self.getToken(BKITParser.While, i)

        def Using(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Using)
            else:
                return self.getToken(BKITParser.Using, i)

        def NameSpace(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.NameSpace)
            else:
                return self.getToken(BKITParser.NameSpace, i)

        def Cout(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Cout)
            else:
                return self.getToken(BKITParser.Cout, i)

        def InternalLib(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.InternalLib)
            else:
                return self.getToken(BKITParser.InternalLib, i)

        def Int(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Int)
            else:
                return self.getToken(BKITParser.Int, i)

        def Main(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Main)
            else:
                return self.getToken(BKITParser.Main, i)

        def Return(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Return)
            else:
                return self.getToken(BKITParser.Return, i)

        def Semi(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Semi)
            else:
                return self.getToken(BKITParser.Semi, i)

        def OpenPara(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.OpenPara)
            else:
                return self.getToken(BKITParser.OpenPara, i)

        def ClosePara(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ClosePara)
            else:
                return self.getToken(BKITParser.ClosePara, i)

        def OpenBraket(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.OpenBraket)
            else:
                return self.getToken(BKITParser.OpenBraket, i)

        def CloseBraket(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.CloseBraket)
            else:
                return self.getToken(BKITParser.CloseBraket, i)

        def Shift(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Shift)
            else:
                return self.getToken(BKITParser.Shift, i)

        def InEq(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.InEq)
            else:
                return self.getToken(BKITParser.InEq, i)

        def Eq(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Eq)
            else:
                return self.getToken(BKITParser.Eq, i)

        def Inc(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Inc)
            else:
                return self.getToken(BKITParser.Inc, i)

        def Assignment(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Assignment)
            else:
                return self.getToken(BKITParser.Assignment, i)

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Id)
            else:
                return self.getToken(BKITParser.Id, i)

        def Integer(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Integer)
            else:
                return self.getToken(BKITParser.Integer, i)

        def Float(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Float)
            else:
                return self.getToken(BKITParser.Float, i)

        def String(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.String)
            else:
                return self.getToken(BKITParser.String, i)

        def Char(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Char)
            else:
                return self.getToken(BKITParser.Char, i)

        def getRuleIndex(self):
            return BKITParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((_la) & ~0x3f) == 0 and ((1 << _la) & 67108862) != 0:
                self.state = 2
                _la = self._input.LA(1)
                if not(((_la) & ~0x3f) == 0 and ((1 << _la) & 67108862) != 0):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 7
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 8
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





