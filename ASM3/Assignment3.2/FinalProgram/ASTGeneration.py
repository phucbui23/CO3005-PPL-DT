from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        expr = ctx.expression().accept(self)
        return Prog(expr)

    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.Add():
            left = ctx.term().accept(self)
            right = ctx.expression().accept(self)

            return BinOp(ctx.Add().getText(), left, right)
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx: BKITParser.TermContext):
        if ctx.Sub():
            left = ctx.factor().accept(self)
            right = ctx.term().accept(self)

            return BinOp(ctx.Sub().getText(), left, right)
        elif ctx.Mul():
            left = ctx.factor().accept(self)
            right = ctx.term().accept(self)

            return BinOp(ctx.Mul().getText(), left, right)
        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx: BKITParser.FactorContext):
        return ctx.idTerm().accept(self)

    def visitIdTerm(self, ctx: BKITParser.IdTermContext):
        return Id(ctx.Identifier().getText())