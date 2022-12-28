from ASTUtils import *
from utils import lookup

"""
In utils.py, we have a function lookup(string) that returns the value of a variable in the environment.
Usage: lookup("x") ==> value of variable x
"""


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

    def visitInteger(self, node: Int):
        return node.value

    def visitId(self, node: Id):
        return lookup(node.name)
