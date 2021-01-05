# Generated from main/bkit/parser/BKIT.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .BKITParser import BKITParser
else:
    from BKITParser import BKITParser

# This class defines a complete generic visitor for a parse tree produced by BKITParser.

class BKITVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by BKITParser#program.
    def visitProgram(self, ctx:BKITParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#globalVardecl.
    def visitGlobalVardecl(self, ctx:BKITParser.GlobalVardeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varDecl.
    def visitVarDecl(self, ctx:BKITParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#varList.
    def visitVarList(self, ctx:BKITParser.VarListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#var.
    def visitVar(self, ctx:BKITParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#initialValue.
    def visitInitialValue(self, ctx:BKITParser.InitialValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#arrayVar.
    def visitArrayVar(self, ctx:BKITParser.ArrayVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#multiDimension.
    def visitMultiDimension(self, ctx:BKITParser.MultiDimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dimension.
    def visitDimension(self, ctx:BKITParser.DimensionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#basicVar.
    def visitBasicVar(self, ctx:BKITParser.BasicVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#globalFuncdecl.
    def visitGlobalFuncdecl(self, ctx:BKITParser.GlobalFuncdeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcDecl.
    def visitFuncDecl(self, ctx:BKITParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#mainFuncDecl.
    def visitMainFuncDecl(self, ctx:BKITParser.MainFuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#nonMainFuncDecl.
    def visitNonMainFuncDecl(self, ctx:BKITParser.NonMainFuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funcName.
    def visitFuncName(self, ctx:BKITParser.FuncNameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statementList.
    def visitStatementList(self, ctx:BKITParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#statement.
    def visitStatement(self, ctx:BKITParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#assignStmt.
    def visitAssignStmt(self, ctx:BKITParser.AssignStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#variable.
    def visitVariable(self, ctx:BKITParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#ifStmt.
    def visitIfStmt(self, ctx:BKITParser.IfStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#forStmt.
    def visitForStmt(self, ctx:BKITParser.ForStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#whileStmt.
    def visitWhileStmt(self, ctx:BKITParser.WhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#dowhileStmt.
    def visitDowhileStmt(self, ctx:BKITParser.DowhileStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#breakStmt.
    def visitBreakStmt(self, ctx:BKITParser.BreakStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#continueStmt.
    def visitContinueStmt(self, ctx:BKITParser.ContinueStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#callStmt.
    def visitCallStmt(self, ctx:BKITParser.CallStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#returnStmt.
    def visitReturnStmt(self, ctx:BKITParser.ReturnStmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression.
    def visitExpression(self, ctx:BKITParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression1.
    def visitExpression1(self, ctx:BKITParser.Expression1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression2.
    def visitExpression2(self, ctx:BKITParser.Expression2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression3.
    def visitExpression3(self, ctx:BKITParser.Expression3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression4.
    def visitExpression4(self, ctx:BKITParser.Expression4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression5.
    def visitExpression5(self, ctx:BKITParser.Expression5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#expression6.
    def visitExpression6(self, ctx:BKITParser.Expression6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#booleanLit.
    def visitBooleanLit(self, ctx:BKITParser.BooleanLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#funccallExpression.
    def visitFunccallExpression(self, ctx:BKITParser.FunccallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#argumentList.
    def visitArgumentList(self, ctx:BKITParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#manyArgument.
    def visitManyArgument(self, ctx:BKITParser.ManyArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexExpression.
    def visitIndexExpression(self, ctx:BKITParser.IndexExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by BKITParser#indexOperator.
    def visitIndexOperator(self, ctx:BKITParser.IndexOperatorContext):
        return self.visitChildren(ctx)



del BKITParser