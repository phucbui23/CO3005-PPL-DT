from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils

            We need to visit all children of program. They are list of expressions.
            ctx.expression() returns the list we desire.

            Then we call expression.accept(self) or self.visitExpression(expression), 
            function visitExpression() will be triggered.
        '''
        expressions = ctx.expressions().accept(self)
        return Prog(expressions)

    def visitExpressions(self, ctx:BKITParser.ExpressionsContext):
        list_expressions = []
        if ctx.expressions():
            list_expressions.extend(ctx.expressions().accept(self))
            list_expressions.append(ctx.expression().accept(self))

        return list_expressions

    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        '''
            BinOp: dataclass in ASTUtils
        '''
        if ctx.expression():
            sign  = ""
            if ctx.Add():
                sign = ctx.Add().getText()
            elif ctx.Sub():
                sign = ctx.Sub().getText()

            return BinOp(sign, ctx.expression().accept(self), ctx.factor().accept(self))
        else:
            return ctx.factor().accept(self)

    def visitFactor(self, ctx:BKITParser.FactorContext):
        '''
            BinOp: dataclass in ASTUtils
        '''
        if ctx.factor():
            sign  = ""
            if ctx.Mul():
                sign = ctx.Mul().getText()
            elif ctx.Div():
                sign = ctx.Div().getText()

            return BinOp(sign, ctx.factor().accept(self), ctx.term().accept(self))
        else:
            return ctx.term().accept(self)

    def visitTerm(self, ctx:BKITParser.TermContext):
        '''
            As defined in BKIT.g4, term can be either an Integer or an Id,
            so that we need to check if this term contains Integer or Id.

            Because Integer and Id are leaf nodes in AST, 
            we must directly call function self.visitInteger(ctx.Integer()) or self.visitId(ctx.Id())
        '''
        if ctx.Integer():
            return self.visitInteger(ctx.Integer())
        elif ctx.Identifier():
            return self.visitIdentifier(ctx.Identifier())

    def visitInteger(self, node:BKITParser.Integer):
        '''
            Int: dataclass in ASTUtils
        '''
        return Int()

    def visitIdentifier(self, node:BKITParser.Identifier):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id()