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
        4,0,13,153,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,1,0,1,0,1,1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,3,
        1,3,1,4,1,4,1,5,1,5,1,5,5,5,63,8,5,10,5,12,5,66,9,5,1,6,3,6,69,8,
        6,1,6,1,6,5,6,73,8,6,10,6,12,6,76,9,6,1,6,3,6,79,8,6,1,7,3,7,82,
        8,7,1,7,1,7,3,7,86,8,7,1,7,3,7,89,8,7,1,7,1,7,1,7,3,7,94,8,7,3,7,
        96,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,105,8,8,1,9,1,9,3,9,109,8,
        9,1,9,1,9,1,10,1,10,1,11,1,11,1,12,4,12,118,8,12,11,12,12,12,119,
        1,13,1,13,1,14,1,14,1,15,1,15,1,16,4,16,129,8,16,11,16,12,16,130,
        1,16,1,16,1,16,1,16,5,16,137,8,16,10,16,12,16,140,9,16,3,16,142,
        8,16,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,138,0,21,
        1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,0,19,0,21,0,23,0,25,0,27,0,
        29,0,31,0,33,9,35,10,37,11,39,12,41,13,1,0,7,2,0,69,69,101,101,2,
        0,70,70,102,102,2,0,43,43,45,45,3,0,65,90,95,95,97,122,1,0,48,57,
        1,0,49,57,3,0,9,10,13,13,32,32,160,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,
        0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,
        0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,
        0,0,1,43,1,0,0,0,3,45,1,0,0,0,5,49,1,0,0,0,7,55,1,0,0,0,9,57,1,0,
        0,0,11,59,1,0,0,0,13,68,1,0,0,0,15,81,1,0,0,0,17,104,1,0,0,0,19,
        106,1,0,0,0,21,112,1,0,0,0,23,114,1,0,0,0,25,117,1,0,0,0,27,121,
        1,0,0,0,29,123,1,0,0,0,31,125,1,0,0,0,33,141,1,0,0,0,35,145,1,0,
        0,0,37,147,1,0,0,0,39,149,1,0,0,0,41,151,1,0,0,0,43,44,5,44,0,0,
        44,2,1,0,0,0,45,46,5,105,0,0,46,47,5,110,0,0,47,48,5,116,0,0,48,
        4,1,0,0,0,49,50,5,102,0,0,50,51,5,108,0,0,51,52,5,111,0,0,52,53,
        5,97,0,0,53,54,5,116,0,0,54,6,1,0,0,0,55,56,5,59,0,0,56,8,1,0,0,
        0,57,58,5,61,0,0,58,10,1,0,0,0,59,64,3,27,13,0,60,63,3,27,13,0,61,
        63,3,29,14,0,62,60,1,0,0,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,
        0,0,64,65,1,0,0,0,65,12,1,0,0,0,66,64,1,0,0,0,67,69,3,23,11,0,68,
        67,1,0,0,0,68,69,1,0,0,0,69,78,1,0,0,0,70,74,3,31,15,0,71,73,3,29,
        14,0,72,71,1,0,0,0,73,76,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,
        79,1,0,0,0,76,74,1,0,0,0,77,79,5,48,0,0,78,70,1,0,0,0,78,77,1,0,
        0,0,79,14,1,0,0,0,80,82,3,23,11,0,81,80,1,0,0,0,81,82,1,0,0,0,82,
        95,1,0,0,0,83,85,3,17,8,0,84,86,3,19,9,0,85,84,1,0,0,0,85,86,1,0,
        0,0,86,88,1,0,0,0,87,89,3,21,10,0,88,87,1,0,0,0,88,89,1,0,0,0,89,
        96,1,0,0,0,90,91,3,25,12,0,91,93,3,19,9,0,92,94,3,21,10,0,93,92,
        1,0,0,0,93,94,1,0,0,0,94,96,1,0,0,0,95,83,1,0,0,0,95,90,1,0,0,0,
        96,16,1,0,0,0,97,98,3,25,12,0,98,99,5,46,0,0,99,100,3,25,12,0,100,
        105,1,0,0,0,101,102,3,25,12,0,102,103,5,46,0,0,103,105,1,0,0,0,104,
        97,1,0,0,0,104,101,1,0,0,0,105,18,1,0,0,0,106,108,7,0,0,0,107,109,
        3,23,11,0,108,107,1,0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,111,
        3,25,12,0,111,20,1,0,0,0,112,113,7,1,0,0,113,22,1,0,0,0,114,115,
        7,2,0,0,115,24,1,0,0,0,116,118,3,29,14,0,117,116,1,0,0,0,118,119,
        1,0,0,0,119,117,1,0,0,0,119,120,1,0,0,0,120,26,1,0,0,0,121,122,7,
        3,0,0,122,28,1,0,0,0,123,124,7,4,0,0,124,30,1,0,0,0,125,126,7,5,
        0,0,126,32,1,0,0,0,127,129,7,6,0,0,128,127,1,0,0,0,129,130,1,0,0,
        0,130,128,1,0,0,0,130,131,1,0,0,0,131,142,1,0,0,0,132,133,5,47,0,
        0,133,134,5,47,0,0,134,138,1,0,0,0,135,137,9,0,0,0,136,135,1,0,0,
        0,137,140,1,0,0,0,138,139,1,0,0,0,138,136,1,0,0,0,139,142,1,0,0,
        0,140,138,1,0,0,0,141,128,1,0,0,0,141,132,1,0,0,0,142,143,1,0,0,
        0,143,144,6,16,0,0,144,34,1,0,0,0,145,146,9,0,0,0,146,36,1,0,0,0,
        147,148,9,0,0,0,148,38,1,0,0,0,149,150,9,0,0,0,150,40,1,0,0,0,151,
        152,9,0,0,0,152,42,1,0,0,0,17,0,62,64,68,74,78,81,85,88,93,95,104,
        108,119,130,138,141,1,6,0,0
    ]

class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    Int = 2
    Flt = 3
    Semi = 4
    Assignment = 5
    Id = 6
    Integer = 7
    Float = 8
    Skip = 9
    ERROR_CHAR = 10
    UNCLOSE_STRING = 11
    ILLEGAL_ESCAPE = 12
    UNTERMINATED_COMMENT = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "','", "'int'", "'float'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>",
            "Int", "Flt", "Semi", "Assignment", "Id", "Integer", "Float", 
            "Skip", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "T__0", "Int", "Flt", "Semi", "Assignment", "Id", "Integer", 
                  "Float", "FragtionalConstant", "ExponentPart", "FloatingPart", 
                  "Sign", "DigitSequence", "NonDigit", "Digit", "NonZeroDigit", 
                  "Skip", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
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


