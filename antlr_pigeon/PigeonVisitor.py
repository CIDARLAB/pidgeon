# Generated from /Users/benlaskaris/Documents/GitHub/pidgeon/Pigeon.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PigeonParser import PigeonParser
else:
    from PigeonParser import PigeonParser

# This class defines a complete generic visitor for a parse tree produced by PigeonParser.

class PigeonVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PigeonParser#script.
    def visitScript(self, ctx:PigeonParser.ScriptContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#pigeoncommands.
    def visitPigeoncommands(self, ctx:PigeonParser.PigeoncommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#promoter.
    def visitPromoter(self, ctx:PigeonParser.PromoterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#repressor.
    def visitRepressor(self, ctx:PigeonParser.RepressorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#codingseq.
    def visitCodingseq(self, ctx:PigeonParser.CodingseqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#transcription.
    def visitTranscription(self, ctx:PigeonParser.TranscriptionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#stop.
    def visitStop(self, ctx:PigeonParser.StopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#operator.
    def visitOperator(self, ctx:PigeonParser.OperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#degredationtag.
    def visitDegredationtag(self, ctx:PigeonParser.DegredationtagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#righttriangle.
    def visitRighttriangle(self, ctx:PigeonParser.RighttriangleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#lefttriangle.
    def visitLefttriangle(self, ctx:PigeonParser.LefttriangleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#invert.
    def visitInvert(self, ctx:PigeonParser.InvertContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#label.
    def visitLabel(self, ctx:PigeonParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#color.
    def visitColor(self, ctx:PigeonParser.ColorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#ignorecolor.
    def visitIgnorecolor(self, ctx:PigeonParser.IgnorecolorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#arccommands.
    def visitArccommands(self, ctx:PigeonParser.ArccommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by PigeonParser#arc.
    def visitArc(self, ctx:PigeonParser.ArcContext):
        return self.visitChildren(ctx)



del PigeonParser