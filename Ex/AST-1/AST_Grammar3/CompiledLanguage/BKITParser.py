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
        4,1,7,20,2,0,7,0,2,1,7,1,2,2,7,2,1,0,1,0,1,0,1,0,1,0,3,0,12,8,0,
        1,0,1,0,1,1,1,1,1,2,1,2,1,2,0,0,3,0,2,4,0,0,17,0,11,1,0,0,0,2,15,
        1,0,0,0,4,17,1,0,0,0,6,7,3,4,2,0,7,8,5,1,0,0,8,9,3,2,1,0,9,12,1,
        0,0,0,10,12,3,2,1,0,11,6,1,0,0,0,11,10,1,0,0,0,12,13,1,0,0,0,13,
        14,5,0,0,1,14,1,1,0,0,0,15,16,3,4,2,0,16,3,1,0,0,0,17,18,5,2,0,0,
        18,5,1,0,0,0,1,11
    ]

class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'" ]

    symbolicNames = [ "<INVALID>", "Add", "Identifier", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_term = 1
    RULE_idTerm = 2

    ruleNames =  [ "program", "term", "idTerm" ]

    EOF = Token.EOF
    Add=1
    Identifier=2
    WS=3
    ERROR_CHAR=4
    UNCLOSE_STRING=5
    ILLEGAL_ESCAPE=6
    UNTERMINATED_COMMENT=7

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
            self.state = 11
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.state = 6
                self.idTerm()
                self.state = 7
                self.match(BKITParser.Add)
                self.state = 8
                self.term()
                pass

            elif la_ == 2:
                self.state = 10
                self.term()
                pass


            self.state = 13
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
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self.idTerm()
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





