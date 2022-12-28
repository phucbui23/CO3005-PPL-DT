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
        4,1,9,36,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,0,1,1,
        1,1,1,1,1,1,1,1,3,1,19,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,
        2,30,8,2,1,3,1,3,1,4,1,4,1,4,0,0,5,0,2,4,6,8,0,0,33,0,10,1,0,0,0,
        2,18,1,0,0,0,4,29,1,0,0,0,6,31,1,0,0,0,8,33,1,0,0,0,10,11,3,2,1,
        0,11,12,5,0,0,1,12,1,1,0,0,0,13,14,3,4,2,0,14,15,5,1,0,0,15,16,3,
        2,1,0,16,19,1,0,0,0,17,19,3,4,2,0,18,13,1,0,0,0,18,17,1,0,0,0,19,
        3,1,0,0,0,20,21,3,6,3,0,21,22,5,2,0,0,22,23,3,4,2,0,23,30,1,0,0,
        0,24,25,3,6,3,0,25,26,5,3,0,0,26,27,3,4,2,0,27,30,1,0,0,0,28,30,
        3,6,3,0,29,20,1,0,0,0,29,24,1,0,0,0,29,28,1,0,0,0,30,5,1,0,0,0,31,
        32,3,8,4,0,32,7,1,0,0,0,33,34,5,4,0,0,34,9,1,0,0,0,2,18,29
    ]

class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'" ]

    symbolicNames = [ "<INVALID>", "Add", "Sub", "Mul", "Identifier", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_expression = 1
    RULE_term = 2
    RULE_factor = 3
    RULE_idTerm = 4

    ruleNames =  [ "program", "expression", "term", "factor", "idTerm" ]

    EOF = Token.EOF
    Add=1
    Sub=2
    Mul=3
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

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

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
            self.state = 10
            self.expression()
            self.state = 11
            self.match(BKITParser.EOF)
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

        def term(self):
            return self.getTypedRuleContext(BKITParser.TermContext,0)


        def Add(self):
            return self.getToken(BKITParser.Add, 0)

        def expression(self):
            return self.getTypedRuleContext(BKITParser.ExpressionContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = BKITParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 18
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 13
                self.term()
                self.state = 14
                self.match(BKITParser.Add)
                self.state = 15
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 17
                self.term()
                pass


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

        def factor(self):
            return self.getTypedRuleContext(BKITParser.FactorContext,0)


        def Sub(self):
            return self.getToken(BKITParser.Sub, 0)

        def term(self):
            return self.getTypedRuleContext(BKITParser.TermContext,0)


        def Mul(self):
            return self.getToken(BKITParser.Mul, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_term

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = BKITParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_term)
        try:
            self.state = 29
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 20
                self.factor()
                self.state = 21
                self.match(BKITParser.Sub)
                self.state = 22
                self.term()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.factor()
                self.state = 25
                self.match(BKITParser.Mul)
                self.state = 26
                self.term()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 28
                self.factor()
                pass


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

        def idTerm(self):
            return self.getTypedRuleContext(BKITParser.IdTermContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_factor

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = BKITParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
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
        self.enterRule(localctx, 8, self.RULE_idTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.match(BKITParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





