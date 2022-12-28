# Generated from BKIT.g4 by ANTLR 4.11.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *


def serializedATN():
    return [
        4,0,7,45,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,1,0,1,0,5,0,18,8,0,10,0,12,0,21,9,0,1,0,3,0,24,8,0,1,1,4,1,
        27,8,1,11,1,12,1,28,1,2,4,2,32,8,2,11,2,12,2,33,1,2,1,2,1,3,1,3,
        1,4,1,4,1,5,1,5,1,6,1,6,0,0,7,1,1,3,2,5,3,7,4,9,5,11,6,13,7,1,0,
        5,1,0,49,57,1,0,48,57,1,0,48,48,1,0,97,122,3,0,9,10,13,13,32,32,
        48,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,
        11,1,0,0,0,0,13,1,0,0,0,1,23,1,0,0,0,3,26,1,0,0,0,5,31,1,0,0,0,7,
        37,1,0,0,0,9,39,1,0,0,0,11,41,1,0,0,0,13,43,1,0,0,0,15,19,7,0,0,
        0,16,18,7,1,0,0,17,16,1,0,0,0,18,21,1,0,0,0,19,17,1,0,0,0,19,20,
        1,0,0,0,20,24,1,0,0,0,21,19,1,0,0,0,22,24,7,2,0,0,23,15,1,0,0,0,
        23,22,1,0,0,0,24,2,1,0,0,0,25,27,7,3,0,0,26,25,1,0,0,0,27,28,1,0,
        0,0,28,26,1,0,0,0,28,29,1,0,0,0,29,4,1,0,0,0,30,32,7,4,0,0,31,30,
        1,0,0,0,32,33,1,0,0,0,33,31,1,0,0,0,33,34,1,0,0,0,34,35,1,0,0,0,
        35,36,6,2,0,0,36,6,1,0,0,0,37,38,9,0,0,0,38,8,1,0,0,0,39,40,9,0,
        0,0,40,10,1,0,0,0,41,42,9,0,0,0,42,12,1,0,0,0,43,44,9,0,0,0,44,14,
        1,0,0,0,5,0,19,23,28,33,1,6,0,0
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Integer = 1
    Identifier = 2
    WS = 3
    ERROR_CHAR = 4
    UNCLOSE_STRING = 5
    ILLEGAL_ESCAPE = 6
    UNTERMINATED_COMMENT = 7

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "Integer", "Identifier", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Integer", "Identifier", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.11.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


