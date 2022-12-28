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
        4,0,12,62,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,1,1,
        1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,4,5,37,8,5,11,5,12,5,38,1,6,1,6,5,
        6,43,8,6,10,6,12,6,46,9,6,1,7,4,7,49,8,7,11,7,12,7,50,1,7,1,7,1,
        8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,19,10,21,11,23,12,1,0,4,1,0,48,57,3,0,65,90,95,
        95,97,122,4,0,48,57,65,90,95,95,97,122,3,0,9,10,13,13,32,32,64,0,
        1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,27,1,0,0,0,5,29,1,0,0,0,7,31,1,
        0,0,0,9,33,1,0,0,0,11,36,1,0,0,0,13,40,1,0,0,0,15,48,1,0,0,0,17,
        54,1,0,0,0,19,56,1,0,0,0,21,58,1,0,0,0,23,60,1,0,0,0,25,26,5,43,
        0,0,26,2,1,0,0,0,27,28,5,45,0,0,28,4,1,0,0,0,29,30,5,42,0,0,30,6,
        1,0,0,0,31,32,5,47,0,0,32,8,1,0,0,0,33,34,5,37,0,0,34,10,1,0,0,0,
        35,37,7,0,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,1,
        0,0,0,39,12,1,0,0,0,40,44,7,1,0,0,41,43,7,2,0,0,42,41,1,0,0,0,43,
        46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,14,1,0,0,0,46,44,1,0,0,
        0,47,49,7,3,0,0,48,47,1,0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,
        1,0,0,0,51,52,1,0,0,0,52,53,6,7,0,0,53,16,1,0,0,0,54,55,9,0,0,0,
        55,18,1,0,0,0,56,57,9,0,0,0,57,20,1,0,0,0,58,59,9,0,0,0,59,22,1,
        0,0,0,60,61,9,0,0,0,61,24,1,0,0,0,4,0,38,44,50,1,6,0,0
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Add = 1
    Sub = 2
    Mul = 3
    Div = 4
    Mod = 5
    Integer = 6
    Identifier = 7
    WS = 8
    ERROR_CHAR = 9
    UNCLOSE_STRING = 10
    ILLEGAL_ESCAPE = 11
    UNTERMINATED_COMMENT = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>",
            "Add", "Sub", "Mul", "Div", "Mod", "Integer", "Identifier", 
            "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Add", "Sub", "Mul", "Div", "Mod", "Integer", "Identifier", 
                  "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

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

