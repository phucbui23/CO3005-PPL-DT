from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils
        '''
        op = ctx.Add().getText()
        left = ctx.idTerm().accept(self)
        right = ctx.term().accept(self)
        return Prog(BinOp(op, left, right))

    def visitTerm(self, ctx:BKITParser.TermContext):
        return ctx.idTerm().accept(self)

    def visitIdTerm(self, ctx:BKITParser.IdTermContext):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id(ctx.Identifier().getText())