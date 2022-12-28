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
        4,0,9,53,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,5,2,26,8,2,10,2,12,
        2,29,9,2,1,2,3,2,32,8,2,1,3,4,3,35,8,3,11,3,12,3,36,1,4,4,4,40,8,
        4,11,4,12,4,41,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,0,0,9,1,1,
        3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,1,0,5,1,0,49,57,1,0,48,57,1,
        0,48,48,1,0,97,122,3,0,9,10,13,13,32,32,56,0,1,1,0,0,0,0,3,1,0,0,
        0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,
        0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,21,1,0,0,0,5,31,1,0,0,0,
        7,34,1,0,0,0,9,39,1,0,0,0,11,45,1,0,0,0,13,47,1,0,0,0,15,49,1,0,
        0,0,17,51,1,0,0,0,19,20,5,43,0,0,20,2,1,0,0,0,21,22,5,45,0,0,22,
        4,1,0,0,0,23,27,7,0,0,0,24,26,7,1,0,0,25,24,1,0,0,0,26,29,1,0,0,
        0,27,25,1,0,0,0,27,28,1,0,0,0,28,32,1,0,0,0,29,27,1,0,0,0,30,32,
        7,2,0,0,31,23,1,0,0,0,31,30,1,0,0,0,32,6,1,0,0,0,33,35,7,3,0,0,34,
        33,1,0,0,0,35,36,1,0,0,0,36,34,1,0,0,0,36,37,1,0,0,0,37,8,1,0,0,
        0,38,40,7,4,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,43,1,0,0,0,43,44,6,4,0,0,44,10,1,0,0,0,45,46,9,0,0,0,
        46,12,1,0,0,0,47,48,9,0,0,0,48,14,1,0,0,0,49,50,9,0,0,0,50,16,1,
        0,0,0,51,52,9,0,0,0,52,18,1,0,0,0,5,0,27,31,36,41,1,6,0,0
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Add = 1
    Sub = 2
    Integer = 3
    Identifier = 4
    WS = 5
    ERROR_CHAR = 6
    UNCLOSE_STRING = 7
    ILLEGAL_ESCAPE = 8
    UNTERMINATED_COMMENT = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "Add", "Sub", "Integer", "Identifier", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Add", "Sub", "Integer", "Identifier", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

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


