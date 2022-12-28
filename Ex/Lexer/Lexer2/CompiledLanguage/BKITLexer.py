# Generated from BKIT.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\16")
        buf.write("G\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2")
        buf.write("\3\2\3\2\3\2\3\2\3\2\5\2\"\n\2\3\3\6\3%\n\3\r\3\16\3&")
        buf.write("\3\4\6\4*\n\4\r\4\16\4+\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\b\5\b\67\n\b\3\t\6\t:\n\t\r\t\16\t;\3\t\3\t\3\n\3")
        buf.write("\n\3\13\3\13\3\f\3\f\3\r\3\r\2\2\16\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\3\2\5\3\2\62;\3")
        buf.write("\2c|\5\2\13\f\17\17\"\"\2K\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write("\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2")
        buf.write("\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2")
        buf.write("\2\2\31\3\2\2\2\3!\3\2\2\2\5$\3\2\2\2\7)\3\2\2\2\t-\3")
        buf.write("\2\2\2\13/\3\2\2\2\r\61\3\2\2\2\17\66\3\2\2\2\219\3\2")
        buf.write("\2\2\23?\3\2\2\2\25A\3\2\2\2\27C\3\2\2\2\31E\3\2\2\2\33")
        buf.write("\34\7k\2\2\34\"\7h\2\2\35\36\7g\2\2\36\37\7n\2\2\37 \7")
        buf.write("u\2\2 \"\7g\2\2!\33\3\2\2\2!\35\3\2\2\2\"\4\3\2\2\2#%")
        buf.write("\t\2\2\2$#\3\2\2\2%&\3\2\2\2&$\3\2\2\2&\'\3\2\2\2\'\6")
        buf.write("\3\2\2\2(*\t\3\2\2)(\3\2\2\2*+\3\2\2\2+)\3\2\2\2+,\3\2")
        buf.write("\2\2,\b\3\2\2\2-.\7=\2\2.\n\3\2\2\2/\60\7*\2\2\60\f\3")
        buf.write("\2\2\2\61\62\7+\2\2\62\16\3\2\2\2\63\64\7?\2\2\64\67\7")
        buf.write("?\2\2\65\67\7?\2\2\66\63\3\2\2\2\66\65\3\2\2\2\67\20\3")
        buf.write("\2\2\28:\t\4\2\298\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2")
        buf.write("\2<=\3\2\2\2=>\b\t\2\2>\22\3\2\2\2?@\13\2\2\2@\24\3\2")
        buf.write("\2\2AB\13\2\2\2B\26\3\2\2\2CD\13\2\2\2D\30\3\2\2\2EF\13")
        buf.write("\2\2\2F\32\3\2\2\2\b\2!&+\66;\3\b\2\2")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    Key = 1
    Interger = 2
    Id = 3
    Semic = 4
    Openparen = 5
    Closeparen = 6
    Op = 7
    WS = 8
    ERROR_CHAR = 9
    UNCLOSE_STRING = 10
    ILLEGAL_ESCAPE = 11
    UNTERMINATED_COMMENT = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "Key", "Interger", "Id", "Semic", "Openparen", "Closeparen", 
            "Op", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
            "UNTERMINATED_COMMENT" ]

    ruleNames = [ "Key", "Interger", "Id", "Semic", "Openparen", "Closeparen", 
                  "Op", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                  "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
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


