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


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#term.
    def visitTerm(self, ctx:BKITParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#factor.
    def visitFactor(self, ctx:BKITParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#intTerm.
    def visitIntTerm(self, ctx:BKITParser.IntTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#idTerm.
    def visitIdTerm(self, ctx:BKITParser.IdTermContext):
        return self.visitChildren(ctx)



del BKITParser