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


    # Visit a parse tree produced by BKITParser#libIncl.
    def visitLibIncl(self, ctx:BKITParser.LibInclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#libInclStmt.
    def visitLibInclStmt(self, ctx:BKITParser.LibInclStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#nsDef.
    def visitNsDef(self, ctx:BKITParser.NsDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#nsDefStmt.
    def visitNsDefStmt(self, ctx:BKITParser.NsDefStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mainFunc.
    def visitMainFunc(self, ctx:BKITParser.MainFuncContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#main_body.
    def visitMain_body(self, ctx:BKITParser.Main_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#decl.
    def visitDecl(self, ctx:BKITParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_struct.
    def visitWhile_struct(self, ctx:BKITParser.While_structContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#while_body.
    def visitWhile_body(self, ctx:BKITParser.While_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#return_stmt.
    def visitReturn_stmt(self, ctx:BKITParser.Return_stmtContext):
        return self.visitChildren(ctx)



del BKITParser