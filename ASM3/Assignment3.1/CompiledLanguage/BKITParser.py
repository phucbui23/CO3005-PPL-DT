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
        4,1,8,20,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,3,0,9,8,0,1,0,1,0,1,1,1,
        1,1,1,3,1,16,8,1,1,2,1,2,1,2,0,0,3,0,2,4,0,0,18,0,8,1,0,0,0,2,15,
        1,0,0,0,4,17,1,0,0,0,6,9,3,4,2,0,7,9,3,2,1,0,8,6,1,0,0,0,8,7,1,0,
        0,0,9,10,1,0,0,0,10,11,5,0,0,1,11,1,1,0,0,0,12,16,5,2,0,0,13,14,
        5,1,0,0,14,16,5,2,0,0,15,12,1,0,0,0,15,13,1,0,0,0,16,3,1,0,0,0,17,
        18,5,3,0,0,18,5,1,0,0,0,2,8,15
    ]

class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'-'" ]

    symbolicNames = [ "<INVALID>", "Sub", "Integer", "Identifier", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_intTerm = 1
    RULE_idTerm = 2

    ruleNames =  [ "program", "intTerm", "idTerm" ]

    EOF = Token.EOF
    Sub=1
    Integer=2
    Identifier=3
    WS=4
    ERROR_CHAR=5
    UNCLOSE_STRING=6
    ILLEGAL_ESCAPE=7
    UNTERMINATED_COMMENT=8

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

        def idTerm(self):
            return self.getTypedRuleContext(BKITParser.IdTermContext,0)


        def intTerm(self):
            return self.getTypedRuleContext(BKITParser.IntTermContext,0)


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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3]:
                self.state = 6
                self.idTerm()
                pass
            elif token in [1, 2]:
                self.state = 7
                self.intTerm()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 10
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IntTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(BKITParser.Integer, 0)

        def Sub(self):
            return self.getToken(BKITParser.Sub, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_intTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntTerm" ):
                return visitor.visitIntTerm(self)
            else:
                return visitor.visitChildren(self)




    def intTerm(self):

        localctx = BKITParser.IntTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_intTerm)
        try:
            self.state = 15
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 12
                self.match(BKITParser.Integer)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 13
                self.match(BKITParser.Sub)
                self.state = 14
                self.match(BKITParser.Integer)
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


    class IdTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(BKITParser.Identifier, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_idTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdTerm" ):
                return visitor.visitIdTerm(self)
            else:
                return visitor.visitChildren(self)




    def idTerm(self):

        localctx = BKITParser.IdTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_idTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(BKITParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





