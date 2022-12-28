from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        expr = ctx.expression().accept(self)
        return Prog(expr)

    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.Add():
            left = ctx.idTerm().accept(self)
            right = ctx.term().accept(self)

            return BinOp(ctx.Add().getText(), left, right)
        elif ctx.Sub():
            left = ctx.idTerm().accept(self)
            right = ctx.term().accept(self)
            return BinOp(ctx.Sub().getText(), left, right)
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx: BKITParser.TermContext):
        if ctx.idTerm():
            return ctx.idTerm().accept(self)

        elif ctx.intTerm():
            return ctx.intTerm().accept(self)

        else:
            return ctx.expression().accept(self)

    def visitIntTerm(self, ctx: BKITParser.IntTermContext):
        return Int(int(ctx.Integer().getText()))

    def visitIdTerm(self, ctx: BKITParser.IdTermContext):
        return Id(ctx.Identifier().getText())
