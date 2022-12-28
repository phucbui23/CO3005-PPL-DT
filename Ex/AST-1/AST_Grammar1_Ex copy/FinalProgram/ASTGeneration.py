from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from ASTUtils import *

class ASTGeneration(BKITVisitor):
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        '''
            Prog: dataclass in ASTUtils
        '''
        if ctx.idTerm():
            id = ctx.idTerm().accept(self)
            return Prog(id)
        elif ctx.intTerm():
            int_term = ctx.intTerm().accept(self)
            return Prog(int_term)

    def visitIntTerm(self, ctx:BKITParser.IntTermContext):
        '''
            Int: dataclass in ASTUtils
        '''
        value = ctx.Integer().getText()
        return Int(int(value))

    def visitIdTerm(self, ctx:BKITParser.IdTermContext):
        '''
            Id: dataclass in ASTUtils
        '''
        return Id(ctx.Identifier().getText())