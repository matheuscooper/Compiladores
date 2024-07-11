# Generated from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniC.g by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser
else:
    from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser

# This class defines a complete generic visitor for a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.

class BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#program.
    def visitProgram(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#definition.
    def visitDefinition(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.DefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#data_definition.
    def visitData_definition(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Data_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#declarator.
    def visitDeclarator(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.DeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#function_definition.
    def visitFunction_definition(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Function_definitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#function_header.
    def visitFunction_header(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Function_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#parameter_list.
    def visitParameter_list(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Parameter_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#parameter_declaration.
    def visitParameter_declaration(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Parameter_declarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#function_body.
    def visitFunction_body(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Function_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#statement.
    def visitStatement(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#expression.
    def visitExpression(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#binary.
    def visitBinary(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.BinaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#unary.
    def visitUnary(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.UnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#primary.
    def visitPrimary(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#tipo.
    def visitTipo(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#argument_list.
    def visitArgument_list(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Argument_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#value.
    def visitValue(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#stat.
    def visitStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#ifStat.
    def visitIfStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.IfStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#whileStat.
    def visitWhileStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.WhileStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#assignStat.
    def visitAssignStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.AssignStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#exprStat.
    def visitExprStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExprStatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser#expr.
    def visitExpr(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExprContext):
        return self.visitChildren(ctx)



del BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser