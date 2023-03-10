from ASTUtils import *
from functools import reduce


class CodeRunner:
    def visitProgram(self, ctx: Prog):
        return str(ctx.expr.accept(self))

    def visitBinaryOp(self, ctx: BinOp):
        left = ctx.left.accept(self)
        right = ctx.right.accept(self)

        if ctx.op == "+":
            return left + right
        elif ctx.op == "-":
            return left - right
        elif ctx.op == "*":
            return left * right
        elif ctx.op == "/":
            return left / right
        elif ctx.op == "%":
            return left % right

    def visitUnaryOp(self, ctx: UnaryOp):
        return - ctx.body.accept(self)

    def visitInteger(self, node: Int):
        return node.value