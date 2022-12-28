from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *


class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx: BKITParser.ProgramContext):
        return Prog(ctx.expression().accept(self))

    def visitExpression(self, ctx: BKITParser.ExpressionContext):
        if ctx.expression():
            op = ctx.Add().getText() if ctx.Add() else ctx.Sub().getText()
            left = ctx.term().accept(self)
            right = ctx.expression().accept(self)

            return BinOp(op, left, right)

        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx: BKITParser.TermContext):
        if ctx.term():
            op = ""
            if ctx.Mul():
                op = ctx.Mul().getText()
            elif ctx.Div():
                op = ctx.Div().getText()
            else:
                op = ctx.Mod().getText()

            left = ctx.factor().accept(self)
            right = ctx.term().accept(self)

            return BinOp(op, left, right)

        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx: BKITParser.FactorContext):
        if ctx.intTerm():
            return ctx.intTerm().accept(self)
        else:
            return ctx.expression().accept(self)

    def visitIntTerm(self, ctx: BKITParser.IntTermContext):
        return Int(int(ctx.Integer().getText()))