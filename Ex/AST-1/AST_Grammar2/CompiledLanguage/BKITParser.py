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
        4,1,7,12,2,0,7,0,2,1,7,1,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,0,0,2,0,
        2,0,0,9,0,4,1,0,0,0,2,9,1,0,0,0,4,5,3,2,1,0,5,6,5,1,0,0,6,7,3,2,
        1,0,7,8,5,0,0,1,8,1,1,0,0,0,9,10,5,2,0,0,10,3,1,0,0,0,0
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
    RULE_idTerm = 1

    ruleNames =  [ "program", "idTerm" ]

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

        def idTerm(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.IdTermContext)
            else:
                return self.getTypedRuleContext(BKITParser.IdTermContext,i)


        def Add(self):
            return self.getToken(BKITParser.Add, 0)

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
            self.state = 4
            self.idTerm()
            self.state = 5
            self.match(BKITParser.Add)
            self.state = 6
            self.idTerm()
            self.state = 7
            self.match(BKITParser.EOF)
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
        self.enterRule(localctx, 2, self.RULE_idTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self.match(BKITParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





