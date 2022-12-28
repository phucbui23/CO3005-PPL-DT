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
        4,1,13,67,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,4,0,20,8,0,11,0,12,0,21,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,5,2,42,8,2,
        10,2,12,2,45,9,2,1,2,1,2,1,3,1,3,1,3,1,3,3,3,53,8,3,1,3,1,3,1,4,
        1,4,1,5,1,5,3,5,61,8,5,1,6,1,6,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,
        14,0,1,1,0,2,3,64,0,19,1,0,0,0,2,25,1,0,0,0,4,31,1,0,0,0,6,48,1,
        0,0,0,8,56,1,0,0,0,10,60,1,0,0,0,12,62,1,0,0,0,14,64,1,0,0,0,16,
        20,3,2,1,0,17,20,3,4,2,0,18,20,3,6,3,0,19,16,1,0,0,0,19,17,1,0,0,
        0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,23,
        1,0,0,0,23,24,5,0,0,1,24,1,1,0,0,0,25,26,3,8,4,0,26,27,5,6,0,0,27,
        28,5,5,0,0,28,29,3,10,5,0,29,30,5,4,0,0,30,3,1,0,0,0,31,32,3,8,4,
        0,32,33,5,6,0,0,33,34,5,5,0,0,34,43,3,10,5,0,35,36,5,1,0,0,36,37,
        3,8,4,0,37,38,5,6,0,0,38,39,5,5,0,0,39,40,3,10,5,0,40,42,1,0,0,0,
        41,35,1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,
        0,0,0,45,43,1,0,0,0,46,47,5,4,0,0,47,5,1,0,0,0,48,49,3,8,4,0,49,
        52,5,6,0,0,50,51,5,5,0,0,51,53,3,10,5,0,52,50,1,0,0,0,52,53,1,0,
        0,0,53,54,1,0,0,0,54,55,5,4,0,0,55,7,1,0,0,0,56,57,7,0,0,0,57,9,
        1,0,0,0,58,61,3,12,6,0,59,61,3,14,7,0,60,58,1,0,0,0,60,59,1,0,0,
        0,61,11,1,0,0,0,62,63,5,7,0,0,63,13,1,0,0,0,64,65,5,8,0,0,65,15,
        1,0,0,0,5,19,21,43,52,60
    ]

class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "','", "'int'", "'float'", "';'", "'='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "Int", "Flt", "Semi", "Assignment", 
                      "Id", "Integer", "Float", "Skip", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_varDeclStmt = 1
    RULE_multVarDeclStmt = 2
    RULE_optInitVarDeclStmt = 3
    RULE_typeInd = 4
    RULE_primaryLiteral = 5
    RULE_integerLiteral = 6
    RULE_floatLiteral = 7

    ruleNames =  [ "program", "varDeclStmt", "multVarDeclStmt", "optInitVarDeclStmt", 
                   "typeInd", "primaryLiteral", "integerLiteral", "floatLiteral" ]

    EOF = Token.EOF
    T__0=1
    Int=2
    Flt=3
    Semi=4
    Assignment=5
    Id=6
    Integer=7
    Float=8
    Skip=9
    ERROR_CHAR=10
    UNCLOSE_STRING=11
    ILLEGAL_ESCAPE=12
    UNTERMINATED_COMMENT=13

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

        def varDeclStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.VarDeclStmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.VarDeclStmtContext,i)


        def multVarDeclStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.MultVarDeclStmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.MultVarDeclStmtContext,i)


        def optInitVarDeclStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.OptInitVarDeclStmtContext)
            else:
                return self.getTypedRuleContext(BKITParser.OptInitVarDeclStmtContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                if la_ == 1:
                    self.state = 16
                    self.varDeclStmt()
                    pass

                elif la_ == 2:
                    self.state = 17
                    self.multVarDeclStmt()
                    pass

                elif la_ == 3:
                    self.state = 18
                    self.optInitVarDeclStmt()
                    pass


                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2 or _la==3):
                    break

            self.state = 23
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeInd(self):
            return self.getTypedRuleContext(BKITParser.TypeIndContext,0)


        def Id(self):
            return self.getToken(BKITParser.Id, 0)

        def Assignment(self):
            return self.getToken(BKITParser.Assignment, 0)

        def primaryLiteral(self):
            return self.getTypedRuleContext(BKITParser.PrimaryLiteralContext,0)


        def Semi(self):
            return self.getToken(BKITParser.Semi, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_varDeclStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclStmt" ):
                return visitor.visitVarDeclStmt(self)
            else:
                return visitor.visitChildren(self)




    def varDeclStmt(self):

        localctx = BKITParser.VarDeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_varDeclStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.typeInd()
            self.state = 26
            self.match(BKITParser.Id)
            self.state = 27
            self.match(BKITParser.Assignment)
            self.state = 28
            self.primaryLiteral()
            self.state = 29
            self.match(BKITParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultVarDeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeInd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.TypeIndContext)
            else:
                return self.getTypedRuleContext(BKITParser.TypeIndContext,i)


        def Id(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Id)
            else:
                return self.getToken(BKITParser.Id, i)

        def Assignment(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.Assignment)
            else:
                return self.getToken(BKITParser.Assignment, i)

        def primaryLiteral(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.PrimaryLiteralContext)
            else:
                return self.getTypedRuleContext(BKITParser.PrimaryLiteralContext,i)


        def Semi(self):
            return self.getToken(BKITParser.Semi, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_multVarDeclStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultVarDeclStmt" ):
                return visitor.visitMultVarDeclStmt(self)
            else:
                return visitor.visitChildren(self)




    def multVarDeclStmt(self):

        localctx = BKITParser.MultVarDeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_multVarDeclStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.typeInd()
            self.state = 32
            self.match(BKITParser.Id)
            self.state = 33
            self.match(BKITParser.Assignment)
            self.state = 34
            self.primaryLiteral()
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1:
                self.state = 35
                self.match(BKITParser.T__0)
                self.state = 36
                self.typeInd()
                self.state = 37
                self.match(BKITParser.Id)
                self.state = 38
                self.match(BKITParser.Assignment)
                self.state = 39
                self.primaryLiteral()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(BKITParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OptInitVarDeclStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeInd(self):
            return self.getTypedRuleContext(BKITParser.TypeIndContext,0)


        def Id(self):
            return self.getToken(BKITParser.Id, 0)

        def Semi(self):
            return self.getToken(BKITParser.Semi, 0)

        def Assignment(self):
            return self.getToken(BKITParser.Assignment, 0)

        def primaryLiteral(self):
            return self.getTypedRuleContext(BKITParser.PrimaryLiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_optInitVarDeclStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOptInitVarDeclStmt" ):
                return visitor.visitOptInitVarDeclStmt(self)
            else:
                return visitor.visitChildren(self)




    def optInitVarDeclStmt(self):

        localctx = BKITParser.OptInitVarDeclStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_optInitVarDeclStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 48
            self.typeInd()
            self.state = 49
            self.match(BKITParser.Id)
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 50
                self.match(BKITParser.Assignment)
                self.state = 51
                self.primaryLiteral()


            self.state = 54
            self.match(BKITParser.Semi)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeIndContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Int(self):
            return self.getToken(BKITParser.Int, 0)

        def Flt(self):
            return self.getToken(BKITParser.Flt, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_typeInd

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeInd" ):
                return visitor.visitTypeInd(self)
            else:
                return visitor.visitChildren(self)




    def typeInd(self):

        localctx = BKITParser.TypeIndContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_typeInd)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            _la = self._input.LA(1)
            if not(_la==2 or _la==3):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integerLiteral(self):
            return self.getTypedRuleContext(BKITParser.IntegerLiteralContext,0)


        def floatLiteral(self):
            return self.getTypedRuleContext(BKITParser.FloatLiteralContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_primaryLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryLiteral" ):
                return visitor.visitPrimaryLiteral(self)
            else:
                return visitor.visitChildren(self)




    def primaryLiteral(self):

        localctx = BKITParser.PrimaryLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_primaryLiteral)
        try:
            self.state = 60
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 58
                self.integerLiteral()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 59
                self.floatLiteral()
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


    class IntegerLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Integer(self):
            return self.getToken(BKITParser.Integer, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_integerLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIntegerLiteral" ):
                return visitor.visitIntegerLiteral(self)
            else:
                return visitor.visitChildren(self)




    def integerLiteral(self):

        localctx = BKITParser.IntegerLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_integerLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(BKITParser.Integer)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FloatLiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Float(self):
            return self.getToken(BKITParser.Float, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_floatLiteral

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFloatLiteral" ):
                return visitor.visitFloatLiteral(self)
            else:
                return visitor.visitChildren(self)




    def floatLiteral(self):

        localctx = BKITParser.FloatLiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_floatLiteral)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            self.match(BKITParser.Float)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





