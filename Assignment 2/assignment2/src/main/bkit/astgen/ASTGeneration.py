from BKITVisitor import BKITVisitor
from BKITParser import BKITParser
from AST import *
import functools
class ASTGeneration(BKITVisitor):
    def visitProgram(self,ctx:BKITParser.ProgramContext):
        listDecl = self.visit(ctx.globalVardecl()) 
        finalList = functools.reduce(lambda x, y: x + y, listDecl, []) + self.visit(ctx.globalFuncdecl())
        return Program(finalList)
    
    def visitGlobalVardecl(self,ctx:BKITParser.ProgramContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.varDecl())] + self.visit(ctx.globalVardecl())
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.varDecl())]
        else:
            return []

    def visitVarDecl(self,ctx:BKITParser.ProgramContext):
        return self.visit(ctx.varList())
    
    def visitVarList(self,ctx:BKITParser.ProgramContext):
        if ctx.getChildCount() == 3: # var COMMA varList => child Count = 3
            return [self.visit(ctx.var())] + self.visit(ctx.varList())
        else:
            return [self.visit(ctx.var())]

    def visitVar(self,ctx:BKITParser.ProgramContext):
        if ctx.basicVar():
            if ctx.EQUAL_ASSIGN():
                return VarDecl(self.visit(ctx.basicVar()), [], self.visit(ctx.initialValue()))
            else:
                return VarDecl(self.visit(ctx.basicVar()), [], None)
        else:
            var = self.visit(ctx.arrayVar())
            if ctx.EQUAL_ASSIGN():
                return VarDecl(var[0], var[1], self.visit(ctx.initialValue()))
            else:
                return VarDecl(var[0], var[1], None)
    
    def visitInitialValue(self,ctx:BKITParser.ProgramContext):
        if ctx.INTLIT():
            if (("x" in ctx.INTLIT().getText()) or ("X" in ctx.INTLIT().getText())): 
                return IntLiteral(int(ctx.INTLIT().getText(), base = 16))
            elif (("o" in ctx.INTLIT().getText()) or ("O" in ctx.INTLIT().getText())):
                return IntLiteral(int(ctx.INTLIT().getText(), base = 8))
            else: 
                return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return BooleanLiteral(self.visit(ctx.booleanLit()))
    
    def visitBooleanLit(self,ctx:BKITParser.ProgramContext):
        if ctx.TRUE():
            return True
        else:
            return False

    def visitArrayVar(self,ctx:BKITParser.ProgramContext):
        return (Id(ctx.ID().getText()), self.visit(ctx.multiDimension()))

    def visitMultiDimension(self, ctx:BKITParser.ProgramContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.dimension())] + self.visit(ctx.multiDimension())
        else:
            return [self.visit(ctx.dimension())]
    
    def visitDimension(self, ctx:BKITParser.ProgramContext):
        if (("x" in ctx.INTLIT().getText()) or ("X" in ctx.INTLIT().getText())): 
            return int(ctx.INTLIT().getText(), base = 16)
        elif (("o" in ctx.INTLIT().getText()) or ("O" in ctx.INTLIT().getText())):
            return int(ctx.INTLIT().getText(), base = 8)
        else: 
            return int(ctx.INTLIT().getText())

    def visitBasicVar(self,ctx:BKITParser.ProgramContext):
        return Id(ctx.ID().getText())
    
    def visitGlobalFuncdecl(self,ctx:BKITParser.ProgramContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.funcDecl())] + self.visit(ctx.globalFuncdecl())
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.funcDecl())]
        else:
            return []
    
    def visitFuncDecl(self,ctx:BKITParser.ProgramContext):
        if ctx.mainFuncDecl():
            return self.visit(ctx.mainFuncDecl())
        else:
            return self.visit(ctx.nonMainFuncDecl())

    def visitMainFuncDecl(self,ctx:BKITParser.ProgramContext):
        vardecl = self.visit(ctx.globalVardecl())
        vardeclList = functools.reduce(lambda x, y: x + y, vardecl, [])
        stmtList = self.visit(ctx.statementList())
        return FuncDecl(Id("main"),self.visit(ctx.varList()) if ctx.PARAMETER() else [],(vardeclList, stmtList))

    def visitNonMainFuncDecl(self,ctx:BKITParser.ProgramContext):
        vardecl = self.visit(ctx.globalVardecl())
        vardeclList = functools.reduce(lambda x, y: x + y, vardecl, [])
        stmtList = self.visit(ctx.statementList())
        return FuncDecl(self.visit(ctx.funcName()),self.visit(ctx.varList()) if ctx.PARAMETER() else [],(vardeclList, stmtList))

    def visitFuncName(self,ctx:BKITParser.ProgramContext):
        return Id(ctx.ID().getText())

    def visitStatementList(self,ctx:BKITParser.ProgramContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.statement())] + self.visit(ctx.statementList())
        elif ctx.getChildCount() == 1:
            return [self.visit(ctx.statement())] 
        else:
            return []

    def visitStatement(self,ctx:BKITParser.ProgramContext):
        if ctx.assignStmt():
            return self.visit(ctx.assignStmt())
        elif ctx.ifStmt():
            return self.visit(ctx.ifStmt())
        elif ctx.forStmt():
            return self.visit(ctx.forStmt())
        elif ctx.whileStmt():
            return self.visit(ctx.whileStmt())
        elif ctx.dowhileStmt():
            return self.visit(ctx.dowhileStmt())
        elif ctx.breakStmt(): 
            return self.visit(ctx.breakStmt())
        elif ctx.continueStmt():
            return self.visit(ctx.continueStmt())
        elif ctx.callStmt():
            return self.visit(ctx.callStmt())
        else: # returnStmt
            return self.visit(ctx.returnStmt())
    
    def visitAssignStmt(self,ctx:BKITParser.ProgramContext):
        return Assign(self.visit(ctx.variable()), self.visit(ctx.expression()))
    
    def visitVariable(self,ctx:BKITParser.ProgramContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        else:
            return self.visit(ctx.indexExpression())

    def visitIfStmt(self,ctx:BKITParser.ProgramContext):
        # ELSEIF
        ifthenStmt = []       
        if ctx.ELSEIF():
            for x in range(0, (len(ctx.ELSEIF()) + 1)): #range(0,x) = [0,1,...,x-1], range(0,x + 1) = [0,1,...x]
                vardecl = self.visit(ctx.globalVardecl(x))
                vardeclList = functools.reduce(lambda x, y: x + y, vardecl, [])                
                stmtList = self.visit(ctx.statementList(x))
                exp = self.visit(ctx.expression(x))
                ifthenStmt = ifthenStmt + [(exp,vardeclList,stmtList)]
        else:
            vardecl = self.visit(ctx.globalVardecl(0))
            vardeclList = functools.reduce(lambda x, y: x + y, vardecl, [])     
            stmtList = self.visit(ctx.statementList(0))
            exp = self.visit(ctx.expression(0))
            ifthenStmt = [(exp, vardeclList, stmtList)]
        # ELSE
        if ctx.ELSE():
            vardecl = self.visit(ctx.globalVardecl(len(ctx.globalVardecl()) - 1))
            vardeclList = functools.reduce(lambda x, y: x + y, vardecl, [])
            stmtList = self.visit(ctx.statementList(len(ctx.globalVardecl()) - 1))
            elseStmt = (vardeclList,stmtList)
        else:
            elseStmt = ([],[])
        return If(ifthenStmt, elseStmt)
    
    def visitForStmt(self,ctx:BKITParser.ProgramContext):
        vardecl = self.visit(ctx.globalVardecl())
        vardeclList = functools.reduce(lambda x, y: x + y, vardecl, [])
        stmtList = self.visit(ctx.statementList())
        return For(Id(ctx.ID(0).getText()), 
                   self.visit(ctx.expression(0)),
                   self.visit(ctx.expression(1)),
                   Id(ctx.ID(1).getText()),
                   self.visit(ctx.expression(2)),
                   (vardeclList, stmtList))

    def visitWhileStmt(self,ctx:BKITParser.ProgramContext):
        vardecl = self.visit(ctx.globalVardecl())
        vardeclList = functools.reduce(lambda x, y: x + y, vardecl, [])
        stmtList = self.visit(ctx.statementList())
        return While(self.visit(ctx.expression()), (vardeclList, stmtList))

    def visitDowhileStmt(self,ctx:BKITParser.ProgramContext):
        vardecl = self.visit(ctx.globalVardecl())
        vardeclList = functools.reduce(lambda x, y: x + y, vardecl, [])
        stmtList = self.visit(ctx.statementList())   
        return Dowhile((vardeclList, stmtList), self.visit(ctx.expression()))

    def visitBreakStmt(self,ctx:BKITParser.ProgramContext):
        return Break()

    def visitContinueStmt(self,ctx:BKITParser.ProgramContext):
        return Continue()

    def visitCallStmt(self,ctx:BKITParser.ProgramContext):
        return CallStmt(self.visit(ctx.funcName()), self.visit(ctx.argumentList()))

    def visitArgumentList(self,ctx:BKITParser.ProgramContext):
        if ctx.getChildCount() == 2:
            return [self.visit(ctx.expression())] + self.visit(ctx.manyArgument())
        else:
            return []
    
    def visitManyArgument(self,ctx:BKITParser.ProgramContext):
        if ctx.getChildCount() == 3:
            return [self.visit(ctx.expression())] + self.visit(ctx.manyArgument())
        else:
            return []

    def visitReturnStmt(self,ctx:BKITParser.ProgramContext):
        if ctx.expression():
            return Return(self.visit(ctx.expression()))
        else:
            return Return(None)

    def visitExpression(self,ctx:BKITParser.ProgramContext):
        if ctx.INT_EQUAL():
            return BinaryOp(ctx.INT_EQUAL().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.INT_NOT_EQUAL():
            return BinaryOp(ctx.INT_NOT_EQUAL().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.INT_LESS_THAN():
            return BinaryOp(ctx.INT_LESS_THAN().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.INT_MORE_THAN():
            return BinaryOp(ctx.INT_MORE_THAN().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.INT_LESS_OR_EQUAL():
            return BinaryOp(ctx.INT_LESS_OR_EQUAL().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.INT_MORE_OR_EQUAL():
            return BinaryOp(ctx.INT_MORE_OR_EQUAL().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.FLOAT_NOT_EQUAL():
            return BinaryOp(ctx.FLOAT_NOT_EQUAL().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.FLOAT_LESS_THAN():
            return BinaryOp(ctx.FLOAT_LESS_THAN().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.FLOAT_MORE_THAN():
            return BinaryOp(ctx.FLOAT_MORE_THAN().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.FLOAT_LESS_OR_EQUAL():
            return BinaryOp(ctx.FLOAT_LESS_OR_EQUAL().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        elif ctx.FLOAT_MORE_OR_EQUAL():
            return BinaryOp(ctx.FLOAT_MORE_OR_EQUAL().getText(), self.visit(ctx.expression()), self.visit(ctx.expression1()))
        else:
            return self.visit(ctx.expression1())

    def visitExpression1(self,ctx:BKITParser.ProgramContext):
        if ctx.AND():
            return BinaryOp(ctx.AND().getText(), self.visit(ctx.expression1()), self.visit(ctx.expression2()))
        if ctx.OR():
            return BinaryOp(ctx.OR().getText(), self.visit(ctx.expression1()), self.visit(ctx.expression2()))
        else:
            return self.visit(ctx.expression2())

    def visitExpression2(self,ctx:BKITParser.ProgramContext):
        if ctx.INT_ADD():
            return BinaryOp(ctx.INT_ADD().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        if ctx.INT_SUB():
            return BinaryOp(ctx.INT_SUB().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        if ctx.FLOAT_ADD():
            return BinaryOp(ctx.FLOAT_ADD().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        if ctx.FLOAT_SUB():
            return BinaryOp(ctx.FLOAT_SUB().getText(), self.visit(ctx.expression2()), self.visit(ctx.expression3()))
        else:
            return self.visit(ctx.expression3())
    
    def visitExpression3(self,ctx:BKITParser.ProgramContext):
        if ctx.INT_MUL():
            return BinaryOp(ctx.INT_MUL().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        if ctx.FLOAT_MUL():
            return BinaryOp(ctx.FLOAT_MUL().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        if ctx.INT_DIV():
            return BinaryOp(ctx.INT_DIV().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        if ctx.FLOAT_DIV():
            return BinaryOp(ctx.FLOAT_DIV().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        if ctx.INT_MOD():
            return BinaryOp(ctx.INT_MOD().getText(), self.visit(ctx.expression3()), self.visit(ctx.expression4()))
        else:
            return self.visit(ctx.expression4())
    
    def visitExpression4(self,ctx:BKITParser.ProgramContext):
        if ctx.NOT():
            return UnaryOp(ctx.NOT().getText(), self.visit(ctx.expression5()))
        else:
            return self.visit(ctx.expression5())
        
    def visitExpression5(self,ctx:BKITParser.ProgramContext):
        if ctx.INT_SUB():
            return UnaryOp(ctx.INT_SUB().getText(), self.visit(ctx.expression6()))
        if ctx.FLOAT_SUB():
            return UnaryOp(ctx.FLOAT_SUB().getText(), self.visit(ctx.expression6()))
        else:
            return self.visit(ctx.expression6())
    
    def visitExpression6(self,ctx:BKITParser.ProgramContext):
        if ctx.indexExpression():
            return self.visit(ctx.indexExpression())
        elif ctx.funccallExpression():
            return self.visit(ctx.funccallExpression())
        elif ctx.LB():
            return self.visit(ctx.expression())
        elif ctx.ID():
            return Id(ctx.ID().getText())
        elif ctx.INTLIT():
            if (("x" in ctx.INTLIT().getText()) or ("X" in ctx.INTLIT().getText())): 
                return IntLiteral(int(ctx.INTLIT().getText(), base = 16))
            elif (("o" in ctx.INTLIT().getText()) or ("O" in ctx.INTLIT().getText())):
                return IntLiteral(int(ctx.INTLIT().getText(), base = 8))
            else: 
                return IntLiteral(int(ctx.INTLIT().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.STRINGLIT():
            return StringLiteral(ctx.STRINGLIT().getText())
        else:
            return BooleanLiteral(self.visit(ctx.booleanLit()))

    def visitFunccallExpression(self,ctx:BKITParser.ProgramContext):
        return CallExpr(self.visit(ctx.funcName()), self.visit(ctx.argumentList()))
    
    def visitIndexExpression(self,ctx:BKITParser.ProgramContext):
        return ArrayCell(Id(ctx.ID().getText()), self.visit(ctx.indexOperator()))
    
    def visitIndexOperator(self,ctx:BKITParser.ProgramContext):
        if ctx.getChildCount() == 4:
            return [self.visit(ctx.expression())] + self.visit(ctx.indexOperator())
        else:
            return [self.visit(ctx.expression())]