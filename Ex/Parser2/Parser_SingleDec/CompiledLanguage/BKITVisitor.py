# Generated from BKIT.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDeclStmt.
    def visitVarDeclStmt(self, ctx:BKITParser.VarDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multVarDeclStmt.
    def visitMultVarDeclStmt(self, ctx:BKITParser.MultVarDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#optInitVarDeclStmt.
    def visitOptInitVarDeclStmt(self, ctx:BKITParser.OptInitVarDeclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#typeInd.
    def visitTypeInd(self, ctx:BKITParser.TypeIndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#primaryLiteral.
    def visitPrimaryLiteral(self, ctx:BKITParser.PrimaryLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:BKITParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#floatLiteral.
    def visitFloatLiteral(self, ctx:BKITParser.FloatLiteralContext):
        return self.visitChildren(ctx)



del BKITParser