from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils
        '''
        op = ctx.Add().getText()
        left = ctx.idTerm()[0].accept(self)
        right = ctx.idTerm()[1].accept(self)
        return Prog(BinOp(op, left, right))

    def visitIdTerm(self, ctx:BKITParser.IdTermContext):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id(ctx.Identifier().getText())