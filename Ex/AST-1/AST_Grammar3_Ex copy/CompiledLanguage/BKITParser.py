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
        4,1,9,30,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,0,1,0,1,0,
        1,0,1,0,1,0,3,0,18,8,0,1,0,1,0,1,1,1,1,3,1,24,8,1,1,2,1,2,1,3,1,
        3,1,3,0,0,4,0,2,4,6,0,0,28,0,17,1,0,0,0,2,23,1,0,0,0,4,25,1,0,0,
        0,6,27,1,0,0,0,8,9,3,6,3,0,9,10,5,1,0,0,10,11,3,2,1,0,11,18,1,0,
        0,0,12,13,3,6,3,0,13,14,5,2,0,0,14,15,3,2,1,0,15,18,1,0,0,0,16,18,
        3,2,1,0,17,8,1,0,0,0,17,12,1,0,0,0,17,16,1,0,0,0,18,19,1,0,0,0,19,
        20,5,0,0,1,20,1,1,0,0,0,21,24,3,6,3,0,22,24,3,4,2,0,23,21,1,0,0,
        0,23,22,1,0,0,0,24,3,1,0,0,0,25,26,5,3,0,0,26,5,1,0,0,0,27,28,5,
        4,0,0,28,7,1,0,0,0,2,17,23
    ]

class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "Add", "Sub", "Integer", "Identifier", 
                      "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_term = 1
    RULE_intTerm = 2
    RULE_idTerm = 3

    ruleNames =  [ "program", "term", "intTerm", "idTerm" ]

    EOF = Token.EOF
    Add=1
    Sub=2
    Integer=3
    Identifier=4
    WS=5
    ERROR_CHAR=6
    UNCLOSE_STRING=7
    ILLEGAL_ESCAPE=8
    UNTERMINATED_COMMENT=9

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


        def Add(self):
            return self.getToken(BKITParser.Add, 0)

        def term(self):
            return self.getTypedRuleContext(BKITParser.TermContext,0)


        def Sub(self):
            return self.getToken(BKITParser.Sub, 0)

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
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 8
                self.idTerm()
                self.state = 9
                self.match(BKITParser.Add)
                self.state = 10
                self.term()
                pass

            elif la_ == 2:
                self.state = 12
                self.idTerm()
                self.state = 13
                self.match(BKITParser.Sub)
                self.state = 14
                self.term()
                pass

            elif la_ == 3:
                self.state = 16
                self.term()
                pass


            self.state = 19
            self.match(BKITParser.EOF)
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

        def idTerm(self):
            return self.getTypedRuleContext(BKITParser.IdTermContext,0)


        def intTerm(self):
            return self.getTypedRuleContext(BKITParser.IntTermContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BKITParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 23
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 21
                self.idTerm()
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 22
                self.intTerm()
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


    class IntTermContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(BKITParser.Integer, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_intTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntTerm" ):
                return visitor.visitIntTerm(self)
            else:
                return visitor.visitChildren(self)




    def intTerm(self):

        localctx = BKITParser.IntTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_intTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(BKITParser.Integer)
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
        self.enterRule(localctx, 6, self.RULE_idTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(BKITParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





