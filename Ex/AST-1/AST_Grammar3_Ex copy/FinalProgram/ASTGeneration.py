from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils
        '''
        if ctx.Add() or ctx.Sub():
            op = ctx.Add().getText() if ctx.Add() else ctx.Sub().getText()
            left = ctx.idTerm().accept(self)
            right = ctx.term().accept(self)
            return Prog(BinOp(op, left, right))
        else:
            _term = ctx.term().accept(self)
            return Prog(_term)

    def visitTerm(self, ctx:BKITParser.TermContext):
        if ctx.idTerm():
            return ctx.idTerm().accept(self)
        else:
            return ctx.intTerm().accept(self)

    def visitIntTerm(self, ctx:BKITParser.IntTermContext):
        '''
            Int: dataclass in ASTUtils
        '''
        return Int(int(ctx.Integer().getText()))

    def visitIdTerm(self, ctx:BKITParser.IdTermContext):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id(ctx.Identifier().getText())