# Generated from BKIT.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\16")
        buf.write("\r\4\2\t\2\3\2\7\2\6\n\2\f\2\16\2\t\13\2\3\2\3\2\3\2\2")
        buf.write("\2\3\2\2\3\3\2\3\t\2\f\2\7\3\2\2\2\4\6\t\2\2\2\5\4\3\2")
        buf.write("\2\2\6\t\3\2\2\2\7\5\3\2\2\2\7\b\3\2\2\2\b\n\3\2\2\2\t")
        buf.write("\7\3\2\2\2\n\13\7\2\2\3\13\3\3\2\2\2\3\7")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "Key", "Interger", "Id", "Semic", "Openparen", 
                      "Closeparen", "Op", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    Key=1
    Interger=2
    Id=3
    Semic=4
    Openparen=5
    Closeparen=6
    Op=7
    WS=8
    ERROR_CHAR=9
    UNCLOSE_STRING=10
    ILLEGAL_ESCAPE=11
    UNTERMINATED_COMMENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def Key(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Key)
            else:
                return self.getToken(BKITParser.Key, i)

        def Interger(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Interger)
            else:
                return self.getToken(BKITParser.Interger, i)

        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Id)
            else:
                return self.getToken(BKITParser.Id, i)

        def Semic(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Semic)
            else:
                return self.getToken(BKITParser.Semic, i)

        def Openparen(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Openparen)
            else:
                return self.getToken(BKITParser.Openparen, i)

        def Closeparen(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Closeparen)
            else:
                return self.getToken(BKITParser.Closeparen, i)

        def Op(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Op)
            else:
                return self.getToken(BKITParser.Op, i)

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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Key) | (1 << BKITParser.Interger) | (1 << BKITParser.Id) | (1 << BKITParser.Semic) | (1 << BKITParser.Openparen) | (1 << BKITParser.Closeparen) | (1 << BKITParser.Op))) != 0):
                self.state = 2
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.Key) | (1 << BKITParser.Interger) | (1 << BKITParser.Id) | (1 << BKITParser.Semic) | (1 << BKITParser.Openparen) | (1 << BKITParser.Closeparen) | (1 << BKITParser.Op))) != 0)):
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





