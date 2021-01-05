import unittest
from TestUtils import TestChecker
from StaticError import *
from AST import *

class CheckSuite(unittest.TestCase):
    
    def test_vardecl_1(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main  
        Body:
            Var: y;
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_vardecl_2(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main 
        Parameter:  y[1][2]
        Body:
            Var: x;
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_vardecl_3(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main 
        Parameter:  y[1][2] , y
        Body:
            Var: t;
        EndBody.           
                   """
        expect = str(Redeclared(Parameter(),"y"))
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_vardecl_4(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Var: y;
        Function: main 
        Body:
            Var: t;
        EndBody.           
                   """
        expect = str(Redeclared(Variable(),"y"))
        self.assertTrue(TestChecker.test(input,expect,403))
    
    def test_vardecl_5(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Var: y;
        Function: main 
        Body:
            Var: t;
        EndBody.           
                   """
        expect = str(Redeclared(Variable(),"y"))
        self.assertTrue(TestChecker.test(input,expect,404))
    
    def test_vardecl_6(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main 
        Parameter : x
        Body:
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_vardecl_7(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main 
        Parameter: x,y,z
        Body: 
            Var: t;
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_vardecl_8(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main 
        Parameter: x,x         
        Body:
            Var: t;
        EndBody.           
                   """
        expect = "Redeclared Parameter: x"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_vardecl_9(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main 
        Body:
            Var: t;
            Var: x, y, z;
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_vardecl_10(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main 
        Body:
            Var: t;
            Var: x , x;
        EndBody.           
                   """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_FuncDecl_1(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: x
        Body:
        EndBody.           
                   """
        expect = "Redeclared Method: x"
        self.assertTrue(TestChecker.test(input,expect,410)) 

    def test_FuncDecl_2(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Var: foo;
        Function: foo
        Body:
        EndBody.           
                   """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,411)) 

    def test_FuncDecl_3(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: foo
        Body:
        EndBody.  
        
        Function: foo
        Body:
        EndBody.         
                   """
        expect = "Redeclared Method: foo"
        self.assertTrue(TestChecker.test(input,expect,412)) 

    def test_FuncDecl_4(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: foo
        Body:
        EndBody.  
        
        Function: e
        Body:
        EndBody.   

        Function: f
        Body:
            Var: hehe;
        EndBody.  

        Function: g
        Parameter: zozo
        Body:
        EndBody.      

        Function: hehe  
        Body:
        EndBody. 

        Function: zozo
        Body:
        EndBody. 
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,413)) 

    def test_FuncDecl_5(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: foo
        Body:
            Var: foo1 = 5;
        EndBody.  
        
        Function: foo1
        Body:
            Var: foo;
        EndBody.         
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,414)) 
    
    def test_assignStmt_1(self):
         """Simple program: main"""
         input = """
         Var: x[2][3] = 5, y[3][4]=2 , z[3];
         Function: main  
         Body:
             Var: t;
             t = x[2][y[z[2]][4]];
             z[1] = 5.0 +. 2.0;
         EndBody.           
                    """
         expect = "Type Mismatch In Statement: Assign(ArrayCell(Id(z),[IntLiteral(1)]),BinaryOp(+.,FloatLiteral(5.0),FloatLiteral(2.0)))"
         self.assertTrue(TestChecker.test(input,expect,415))

    def test_assignStmt_2(self):
         """Simple program: main"""
         input = """
         Var: x[2][3] = 5, y, z;
         Function: main  
         Body:
             Var: t;
             t = x[2][y];
             y = z;
         EndBody.           
                    """
         expect = ""
         self.assertTrue(TestChecker.test(input,expect,416))  

    def test_assignStmt_3(self):
         """Simple program: main"""
         input = """
         Var: x[2][3] = 5, y, z;
         Function: main  
         Body:
             Var: t;
             t = z + x[2][y];
             y = False;
         EndBody.           
                    """
         expect = "Type Mismatch In Statement: Assign(Id(y),BooleanLiteral(false))"
         self.assertTrue(TestChecker.test(input,expect,417))   

    def test_assignStmt_4(self):
         """Simple program: main"""
         input = """
         Var: x[2][3] = 5, y, z[3] ;
         Function: main  
         Body:
             Var: t;
             t = y + x[2][z[3]];
             z[3] = 2.5;
         EndBody.           
                    """
         expect = "Type Mismatch In Statement: Assign(ArrayCell(Id(z),[IntLiteral(3)]),FloatLiteral(2.5))"
         self.assertTrue(TestChecker.test(input,expect,418))   

    def test_assignStmt_5(self):
         """Simple program: main"""
         input = """
         Var: x[2][3] = 5, y, z[3];
         Function: foo
         Parameter: x, y, z
         Body:
             Var: t;
         EndBody.   

         Function: main  
         Body:
             Var: t = 2;
             t = foo(2,x[2][3],z[3]);
         EndBody.           
                    """
         expect = "Type Cannot Be Inferred: Assign(Id(t),CallExpr(Id(foo),[IntLiteral(2),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(3)]),ArrayCell(Id(z),[IntLiteral(3)])]))"
         self.assertTrue(TestChecker.test(input,expect,419))  

    def test_assignStmt_6(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   

         Function: main  
         Body:
             Var: t = 2;
             t = foo(y);
         EndBody.           
                    """
         expect = "Type Cannot Be Inferred: Assign(Id(t),CallExpr(Id(foo),[Id(y)]))"
         self.assertTrue(TestChecker.test(input,expect,420))  

    def test_assignStmt_7(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   

         Function: main  
         Body:
             Var: t = 2;
             t = foo(z[2][3]);
         EndBody.           
                    """
         expect = "Type Cannot Be Inferred: Assign(Id(t),CallExpr(Id(foo),[ArrayCell(Id(z),[IntLiteral(2),IntLiteral(3)])]))"
         self.assertTrue(TestChecker.test(input,expect,421))  

    def test_assignStmt_8(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   

         Function: main  
         Body:
             Var: t = 2;
             t = foo(x[2][3] + z[3]);
         EndBody.           
                    """
         expect = ""
         self.assertTrue(TestChecker.test(input,expect,422))  

    def test_assignStmt_9(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   

         Function: main  
         Body:
             Var: t = 2;
             t = foo(x[2][3] + z[3]);
         EndBody.           
                    """
         expect = ""
         self.assertTrue(TestChecker.test(input,expect,423))  

    def test_assignStmt_10(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   

         Function: main  
         Body:
             Var: t = 2;
             t = foo(!x[1][2]);
         EndBody.           
                    """
         expect = ""
         self.assertTrue(TestChecker.test(input,expect,424))

    def test_assignStmt_11(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   
        
         Function: foo1
         Parameter: x
         Body:
             Var: t;
         EndBody.   
        
         Function: main  
         Body:
             Var: t = 2;
             t = foo(foo1(y));
         EndBody.           
                    """
         expect = "Type Cannot Be Inferred: Assign(Id(t),CallExpr(Id(foo),[CallExpr(Id(foo1),[Id(y)])]))"
         self.assertTrue(TestChecker.test(input,expect,425))
    
    def test_assignStmt_12(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y = 5, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   
        
         Function: foo1
         Parameter: x[2][3]
         Body:
             Var: t;
         EndBody.   
        
         Function: main  
         Body:
             Var: t = 2;
             t = foo(foo1(z[3]));
         EndBody.           
                    """
         expect = "Type Cannot Be Inferred: Assign(Id(t),CallExpr(Id(foo),[CallExpr(Id(foo1),[ArrayCell(Id(z),[IntLiteral(3)])])]))"
         self.assertTrue(TestChecker.test(input,expect,426))

    def test_assignStmt_13(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y = 5, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   
    
         Function: main  
         Body:
             Var: t = 2;
             t = foo(8);
         EndBody.           
                    """
         expect = ""
         self.assertTrue(TestChecker.test(input,expect,427))

    def test_assignStmt_14(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y = 5, z[3];
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   
        
        Function: foo1
         Parameter: x[2][3]
         Body:
             Var: t;
         EndBody. 

         Function: main  
         Body:
             Var: t = 2;
             t = z[foo(2) + x[2][foo1(z[3])]];
         EndBody.           
                    """
         expect = "Type Cannot Be Inferred: Assign(Id(t),ArrayCell(Id(z),[BinaryOp(+,CallExpr(Id(foo),[IntLiteral(2)]),ArrayCell(Id(x),[IntLiteral(2),CallExpr(Id(foo1),[ArrayCell(Id(z),[IntLiteral(3)])])]))]))"
         self.assertTrue(TestChecker.test(input,expect,428))

    def test_assignStmt_15(self):
         """Simple program: main"""
         input = """
         Var: x[2][3], y = 5, z[3] = True;
         Function: foo
         Parameter: x
         Body:
             Var: t;
         EndBody.   
        
        Function: foo1
         Parameter: x[2][3], y
         Body:
             Var: t;
         EndBody. 

         Function: main  
         Body:
             Var: t, v = 3.5, f[9];
             t = x[2][foo(y)] + f[foo1(z[3], 12.1 -. v*.v)];
         EndBody.           
                    """
         expect = ""
         self.assertTrue(TestChecker.test(input,expect,429))

    def test_IfStmt_1(self):
        """Simple program: main"""
        input = """
        Var: x, y = False, z = True;
        Function: main
        Parameter: t 
        Body:
            If x Then
            EndIf.
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,430))

    def test_IfStmt_2(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: t 
        Body:
            If y Then
            EndIf.
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: If(Id(y),[],[])Else([],[])"
        self.assertTrue(TestChecker.test(input,expect,431))

    def test_IfStmt_3(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z[2][3] = True;
        Function: main
        Parameter: t 
        Body:
            If (!z[x][2] && False) Then
            EndIf.
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,432))

    def test_IfStmt_4(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z[2][3] = True;
        Function: main
        Parameter: t 
        Body:
            If (x +. y) Then
            EndIf.
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: If(BinaryOp(+.,Id(x),Id(y)),[],[])Else([],[])"
        self.assertTrue(TestChecker.test(input,expect,433))

    def test_IfStmt_5(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z[2][3] = True;
        Function: main
        Parameter: t 
        Body:
            If (False) Then
            EndIf.
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,434))

    def test_IfStmt_6(self):
        """Simple program: main"""
        input = """
        Var: x = 2 , y = 2.0, z[2][3] = True;
        Function: foo
        Parameter: x , y, z 
        Body:
        EndBody.           
        
        Function: main
        Parameter: t 
        Body:
            If (foo(x,y,z[2][3])) Then
            EndIf.
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,435))

    def test_IfStmt_7(self):
        """Simple program: main"""
        input = """
        Var: x = 2 , y, z[2][3] = True;
        Function: foo
        Parameter: x , y, z 
        Body:
        EndBody.           
        
        Function: main
        Parameter: t 
        Body:
            If (foo(x,y,z[2][3])) Then
            EndIf.
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: If(CallExpr(Id(foo),[Id(x),Id(y),ArrayCell(Id(z),[IntLiteral(2),IntLiteral(3)])]),[],[])Else([],[])"
        self.assertTrue(TestChecker.test(input,expect,436))

    def test_IfStmt_8(self):
        """Simple program: main"""
        input = """
        Var: x = 2 , y, z[2][3] = True;
        Function: foo
        Parameter: x , y, z 
        Body:
        EndBody.           
        
        Function: main
        Parameter: t 
        Body:
            x = foo(x,x,x);
            If (!foo(x,x,x)) Then
            EndIf.
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: UnaryOp(!,CallExpr(Id(foo),[Id(x),Id(x),Id(x)]))"
        self.assertTrue(TestChecker.test(input,expect,437))

    def test_IfStmt_9(self):
        """Simple program: main"""
        input = """
        Var: x = 2 , y, z[2][3] = True;
        
        Function: foo
        Parameter: x , y, z 
        Body:
        EndBody.           
        
        Function: main
        Parameter: t 
        Body:
            If (!(False)&&(2.5 >=. 1.0)) Then
                Var : x;
                x = 1;
            ElseIf (z[2][3]) Then
                x = 3;
            ElseIf (y) Then
                x = 4;
            Else
                x = 5; 
            EndIf.
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,438))

    def test_IfStmt_10(self):
        """Simple program: main"""
        input = """
        Var: x = 2 , y, z[2][3] = True;
        Function: foo
        Parameter: x , y, z 
        Body:
        EndBody.           
        
        Function: main
        Parameter: t 
        Body:
            If (!(False)&&(2.5 >=. 1.0)) Then
                y = foo(x,"String",z[1][2]);
            EndIf.
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: Assign(Id(y),CallExpr(Id(foo),[Id(x),StringLiteral(String),ArrayCell(Id(z),[IntLiteral(1),IntLiteral(2)])]))"
        self.assertTrue(TestChecker.test(input,expect,439))


    def test_ForStmt_1(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: t
        Body:
            For (i = 0, i < 10, i = i + 2) Do
            EndFor.
        EndBody.           
                   """
        expect = "Undeclared Identifier: i"
        self.assertTrue(TestChecker.test(input,expect,440))

    def test_ForStmt_2(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            For (i = 1.0, i < 10, i = i + 2) Do
            EndFor.
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: For(Id(i),FloatLiteral(1.0),BinaryOp(<,Id(i),IntLiteral(10)),Id(i),BinaryOp(+,Id(i),IntLiteral(2)),[],[])"
        self.assertTrue(TestChecker.test(input,expect,441))

    def test_ForStmt_3(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            For (i = 1, i \\ 10, i = i + 2) Do
                Var: t, a[2][3];
                t = y*.y;
            EndFor.
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: For(Id(i),IntLiteral(1),BinaryOp(\,Id(i),IntLiteral(10)),Id(i),BinaryOp(+,Id(i),IntLiteral(2)),[VarDecl(Id(t)),VarDecl(Id(a),[2,3])],[Assign(Id(t),BinaryOp(*.,Id(y),Id(y)))])"
        self.assertTrue(TestChecker.test(input,expect,442))

    def test_ForStmt_4(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            For (i = 1, i < 10, i = y *. y) Do
                y = y +. 1;
            EndFor.
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: For(Id(i),IntLiteral(1),BinaryOp(<,Id(i),IntLiteral(10)),Id(i),BinaryOp(*.,Id(y),Id(y)),[],[Assign(Id(y),BinaryOp(+.,Id(y),IntLiteral(1)))])"
        self.assertTrue(TestChecker.test(input,expect,443))

    def test_ForStmt_5(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;

        Function: foo
        Parameter: i
        Body:
        EndBody.  

        Function: main
        Parameter: i
        Body:
            For (i = foo(x), i < 10, i = i + 1) Do
                x = 2;
            EndFor.
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: For(Id(i),CallExpr(Id(foo),[Id(x)]),BinaryOp(<,Id(i),IntLiteral(10)),Id(i),BinaryOp(+,Id(i),IntLiteral(1)),[],[Assign(Id(x),IntLiteral(2))])"
        self.assertTrue(TestChecker.test(input,expect,444))

    def test_DowhileStmt_1(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            Do
                x = !x;
            While (x);
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,445))

    def test_DowhileStmt_2(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i
        Body:
        EndBody.     
        
        Function: main
        Parameter: i
        Body:
            Var: a[2][2], b;
            Do
                x = x + y;
            While (!a[2][foo(b)]);
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: Dowhile([],[Assign(Id(x),BinaryOp(+,Id(x),Id(y)))],UnaryOp(!,ArrayCell(Id(a),[IntLiteral(2),CallExpr(Id(foo),[Id(b)])])))"
        self.assertTrue(TestChecker.test(input,expect,446))    

    def test_DowhileStmt_3(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            Do
                x = x + y;
            While ("True");
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: Dowhile([],[Assign(Id(x),BinaryOp(+,Id(x),Id(y)))],StringLiteral(True))"
        self.assertTrue(TestChecker.test(input,expect,447))    

    def test_DowhileStmt_4(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            Do
                Var: t[2] = 5.0;
                t[2] = -. y;
            While(!(!(!(!(z&&False||True)))));
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,448))    

    def test_DowhileStmt_5(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i = True
        Body:
        EndBody.

        Function: main
        Parameter: i
        Body:
            Do
                Var: t[2] = 5.0;
                t[2] = -. y;
            While(z && foo(x));
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,449))

    def test_WhileStmt_1(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            While (x) Do
                Var: t = 5;
                x = x - t;
            EndWhile.
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: BinaryOp(-,Id(x),Id(t))"
        self.assertTrue(TestChecker.test(input,expect,450))    

    def test_WhileStmt_2(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            While (y) Do
                Var: t = 5;
                x = x - t;
            EndWhile.
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: While(Id(y),[VarDecl(Id(t),IntLiteral(5))],[Assign(Id(x),BinaryOp(-,Id(x),Id(t)))])"
        self.assertTrue(TestChecker.test(input,expect,451))    

    def test_WhileStmt_3(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            While ("!False") Do
                Var: t = 5;
                x = x - t;
            EndWhile.
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: While(StringLiteral(!False),[VarDecl(Id(t),IntLiteral(5))],[Assign(Id(x),BinaryOp(-,Id(x),Id(t)))])"
        self.assertTrue(TestChecker.test(input,expect,452))  

    def test_WhileStmt_4(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i
        Body:
        EndBody. 
        

        Function: main
        Parameter: i
        Body:
            While (foo(x)) Do
                Var: t = 5;
                x = x - t;
            EndWhile.
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: While(CallExpr(Id(foo),[Id(x)]),[VarDecl(Id(t),IntLiteral(5))],[Assign(Id(x),BinaryOp(-,Id(x),Id(t)))])"
        self.assertTrue(TestChecker.test(input,expect,453))  

    def test_WhileStmt_5(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        Function: main
        Parameter: i
        Body:
            While (!((True)&&(z)&&(x > i)) || False) Do
                Var: t = 5;
                x = x - t;
            EndWhile.
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,454)) 

    def test_CallStmt_1(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i
        Body:
            
        EndBody.
        
        Function: main
        Parameter: i
        Body:
            fo(i);
        EndBody.           
                   """
        expect = "Undeclared Method: fo"
        self.assertTrue(TestChecker.test(input,expect,455))

    def test_CallStmt_2(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i
        Body:
            
        EndBody.
        
        Function: main
        Parameter: i
        Body:
            foo(i,i);
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(i),Id(i)])"
        self.assertTrue(TestChecker.test(input,expect,456))

    def test_CallStmt_3(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i
        Body:
            
        EndBody.
        
        Function: main
        Parameter: i
        Body:
            foo(x);
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: CallStmt(Id(foo),[Id(x)])"
        self.assertTrue(TestChecker.test(input,expect,457))

    def test_CallStmt_4(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i 
        Body:
            
        EndBody.
        
        Function: main
        Parameter: i
        Body:
            foo(i);
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: CallStmt(Id(foo),[Id(i)])"
        self.assertTrue(TestChecker.test(input,expect,458))

    def test_CallStmt_5(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i = 2 
        Body:
            
        EndBody.
        
        Function: main
        Parameter: i
        Body:
            y = foo(x);
            foo(i);
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(i)])"
        self.assertTrue(TestChecker.test(input,expect,459))

    def test_CallStmt_6(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i = 2 
        Body:
            
        EndBody.
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            foo(foo(a[3][3]));
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,460))

    def test_CallStmt_7(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: main
        Parameter: i, a[4][3]   
        Body:
            foo(1,3,4);
        EndBody.           

        Function: foo
        Parameter: x, y, z
        Body:
        EndBody.
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,461))

    def test_CallStmt_8(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i 
        Body:   
            i = 3;
        EndBody.
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            foo(1,2);
        EndBody.           
                   """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[IntLiteral(1),IntLiteral(2)])"
        self.assertTrue(TestChecker.test(input,expect,462))

    def test_CallStmt_9(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i
        Body:
            i = z;
        EndBody.
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            foo(False);
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,463))

    def test_CallStmt_10(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            foo(i);
        EndBody.           

        Function: foo
        Parameter: i 
        Body:
            i = 5;
        EndBody.
                   """
        expect = "Type Cannot Be Inferred: CallStmt(Id(foo),[Id(i)])"
        self.assertTrue(TestChecker.test(input,expect,464))
    
    def test_ReturnStmt_1(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i 
        Body:
            i = 5;
            Return 5;
        EndBody.
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            x = foo(i);
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,465))

    def test_ReturnStmt_2(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i 
        Body:
            i = 5;
            Return 2.5;
        EndBody.
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            foo(i);
        EndBody. 
                   """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(i)])"
        self.assertTrue(TestChecker.test(input,expect,466))

    def test_ReturnStmt_3(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: foo
        Parameter: i 
        Body:
            i = 5;
            Return False;
        EndBody.
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            foo(i);
        EndBody. 
                   """
        expect = "Type Mismatch In Statement: CallStmt(Id(foo),[Id(i)])"
        self.assertTrue(TestChecker.test(input,expect,467))

    def test_ReturnStmt_4(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            foo(i);
        EndBody.           

        Function: foo
        Parameter: i = False
        Body:
            Return z;
        EndBody.
                   """
        expect = "Type Mismatch In Statement: Return(Id(z))"
        self.assertTrue(TestChecker.test(input,expect,468))

    def test_ReturnStmt_5(self):
        """Simple program: main"""
        input = """
        Var: x, y = 2.0, z = True;
        
        Function: main
        Parameter: i, a[4][3]
        Body:
            foo(i);
        EndBody.           

        Function: foo
        Parameter: i  = 2
        Body:
            Return;
        EndBody.
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,469))
    
    def test_unaryOp_expression_1(self):
        """Simple program: main"""
        input = """
        Var: x, y, z;
        Function: main  
        Body:
            Var: t;
            t = 3;
            t = -2.0;
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: UnaryOp(-,FloatLiteral(2.0))"
        self.assertTrue(TestChecker.test(input,expect,470))

    def test_unaryOp_expression_2(self):
        """Simple program: main"""
        input = """
        Var: x, y = 5.0, z;
        Function: main  
        Body:
            Var: t;
            t = 0.3;
            t = -.(y);
            z = -(t);
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: UnaryOp(-,Id(t))"
        self.assertTrue(TestChecker.test(input,expect,471))
    
    def test_unaryOp_expression_3(self):
        """Simple program: main"""
        input = """
        Var: x, y, z;
        Function: main  
        Body:
            Var: t;
            t = -.z;
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,472))

    def test_unaryOp_expression_4(self):
        """Simple program: main"""
        input = """
        Var: x, y, z;
        Function: foo  
        Body:
            Return 5;
        EndBody.
        
        Function: main  
        Body:
            Var: x;
            x = -foo();
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,473))

    def test_unaryOp_expression_5(self):
        """Simple program: main"""
        input = """
        Var: x, y[3][4], z;
        Function: main  
        Body:
            Var: t;
            t = !(y[3][4]);
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,474))


    def test_binaryOp_1(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z;
        Function: main 
        Body:
            x = y[1][2] +. z;
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: BinaryOp(+.,ArrayCell(Id(y),[IntLiteral(1),IntLiteral(2)]),Id(z))"
        self.assertTrue(TestChecker.test(input,expect,475))

    def test_binaryOp_2(self):
        """Simple program: main"""
        input = """
        Var: x, y[1][2] = 5, z = 2.5;
        Function: main 
        Body:
            x = y[1][2] - z;
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: BinaryOp(-,ArrayCell(Id(y),[IntLiteral(1),IntLiteral(2)]),Id(z))"
        self.assertTrue(TestChecker.test(input,expect,476))
    
    def test_binaryOp_3(self):
        """Simple program: main"""
        input = """
        Var: x, y, z = 2;
        Function: main
        Parameter: t 
        Body:
            t = 5;
            x = t * z;
            y = (x >=. t); 
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: BinaryOp(>=.,Id(x),Id(t))"
        self.assertTrue(TestChecker.test(input,expect,477))

    def test_binaryOp_4(self):
        """Simple program: main"""
        input = """
        Var: x, y = False, z = True;
        Function: main
        Parameter: t 
        Body:
            t = 5;
            x = y && z;
            x = x + t;
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(x),Id(t))"
        self.assertTrue(TestChecker.test(input,expect,478))

    def test_binaryOp_5(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        Function: main
        Parameter: t 
        Body:
            t = 5;
            t = x[2][3] + x[2][3];
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,479))

    def test_binaryOp_6(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        Function: main
        Parameter: t 
        Body:
            t = 5;
            t = x[2][3] + x[2][3] -. x[2][3];
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: BinaryOp(-.,BinaryOp(+,ArrayCell(Id(x),[IntLiteral(2),IntLiteral(3)]),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(3)])),ArrayCell(Id(x),[IntLiteral(2),IntLiteral(3)]))"
        self.assertTrue(TestChecker.test(input,expect,480))

    def test_binaryOp_7(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        Function: main
        Parameter: t 
        Body:
            t = 5;
            t = (x[2][3] - 5) >= (t) || (z);
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: BinaryOp(||,Id(t),Id(z))"
        self.assertTrue(TestChecker.test(input,expect,481))

    def test_binaryOp_8(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: sum
        Parameter: x,y,z
        Body:
            Var: sum;
            sum = x + y + z;
            Return sum;
        EndBody. 
        
        Function: main
        Parameter: t 
        Body:
            t = 5;
            t = sum(t,t,t) \\ t;
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,482))

    def test_binaryOp_9(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: floatsub
        Parameter: x,y,z
        Body:
            Var: result;
            result = x -. y -. z ;
            Return result;
        EndBody.    

        Function: main
        Parameter: t 
        Body:
            Var: result;
            result = floatsub(x[2][3],x[2][3],x[2][3]);
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,483))

    def test_binaryOp_10(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: foo
        Parameter: t 
        Body:
        EndBody.    

        Function: main
        Parameter: t 
        Body:
            Var: x;
            While (y) Do
                Var: x;
                x = x + x; 
            EndWhile.
            x = x +. x;
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,484))

    def test_ArrayCell_1(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True; 

        Function: main
        Parameter: t 
        Body:
            x[2][3] = y;
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,485))

    def test_ArrayCell_2(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
    
        Function: main
        Parameter: t 
        Body:
            x[y][z] = t - 4;
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),[Id(y),Id(z)])"
        self.assertTrue(TestChecker.test(input,expect,486))

    def test_ArrayCell_3(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: main
        Parameter: t 
        Body:
            t = x[t -. 10.1][t +. 9.9];
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),[BinaryOp(-.,Id(t),FloatLiteral(10.1)),BinaryOp(+.,Id(t),FloatLiteral(9.9))])"
        self.assertTrue(TestChecker.test(input,expect,487))

    def test_ArrayCell_4(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: foo
        Parameter: t 
        Body:
        EndBody.    

        Function: main
        Parameter: t 
        Body:
            t = x[foo(t)][foo(t)];
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: Assign(Id(t),ArrayCell(Id(x),[CallExpr(Id(foo),[Id(t)]),CallExpr(Id(foo),[Id(t)])]))"
        self.assertTrue(TestChecker.test(input,expect,488))

    def test_ArrayCell_5(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: foo
        Parameter: t = 5
        Body:
            Return t;
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            t = x[foo(t)][foo(t)];
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,489))

    def test_CallExpr_1(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: foo
        Parameter: t = 5
        Body:
            Return t;
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            x = foo(x);
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(x)])"
        self.assertTrue(TestChecker.test(input,expect,490))

    def test_CallExpr_2(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: foo
        Parameter: t = 5
        Body:
            Return t;
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            x = foo(x);
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo),[Id(x)])"
        self.assertTrue(TestChecker.test(input,expect,491))

    def test_CallExpr_3(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: foo
        Parameter: t
        Body:
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            x = foo(y && z);
        EndBody.           
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,492))

    def test_CallExpr_4(self):
        """Simple program: main"""
        input = """
        Var: x[2][3], y = False, z = True;
        
        Function: foo
        Parameter: t
        Body:
            Return 2;
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            Var: x = 2.0;
            x = foo(x) +. foo(x);
        EndBody.           
                   """
        expect = "Type Mismatch In Expression: BinaryOp(+.,CallExpr(Id(foo),[Id(x)]),CallExpr(Id(foo),[Id(x)]))"
        self.assertTrue(TestChecker.test(input,expect,493))

    def test_CallExpr_5(self):
        """Simple program: main"""
        input = """
        Var: x[2][3] = 2, y = False, z = True;
        
        Function: foo
        Parameter: t
        Body:
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            Var: x;
            x = foo(foo(foo(x)));
        EndBody.           
                   """
        expect = "Type Cannot Be Inferred: Assign(Id(x),CallExpr(Id(foo),[CallExpr(Id(foo),[CallExpr(Id(foo),[Id(x)])])]))"
        self.assertTrue(TestChecker.test(input,expect,494))

    def test_CallExpr_6(self):
        """Simple program: main"""
        input = """
        Var: x[2][3] = 2, y = False, z = True;
        
        Function: foo1
        Parameter: t = 1
        Body:
            Return 1;
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            Var: x;
            x = foo1(foo2(foo3(x)));
        EndBody.  

        Function: foo2
        Parameter: t = 2
        Body:
            Return 2;
        EndBody. 

        Function: foo3
        Parameter: t = 3
        Body:
            Return 3;
        EndBody.          
                   """
        expect = ""
        self.assertTrue(TestChecker.test(input,expect,495))

    def test_CallExpr_7(self):
        """Simple program: main"""
        input = """
        Var: x[2][3] = 2, y = False, z = True;
        
        Function: foo1
        Parameter: t = 1
        Body:
            Return 1;
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            Var: x;
            If (foo1(t,t)) Then
            EndIf.
        EndBody.      
                   """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo1),[Id(t),Id(t)])"
        self.assertTrue(TestChecker.test(input,expect,496))

    def test_CallExpr_8(self):
        """Simple program: main"""
        input = """
        Var: x[2][3] = 2, y = False, z = True;
        
        Function: foo1
        Parameter: t = 1
        Body:
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            Var: x[3][3];
            x[3][3] = foo1();
        EndBody.      
                   """
        expect = "Type Mismatch In Expression: CallExpr(Id(foo1),[])"
        self.assertTrue(TestChecker.test(input,expect,497))

    def test_CallExpr_9(self):
        """Simple program: main"""
        input = """
        Var: x[2][3] = 2, y = False, z = True;
        
        Function: foo1
        Parameter: t = 1
        Body:
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            For (t = 1, t  < 10, t = t + 1) Do
                Var: y = 1;
                For (t = 1, t < 5, t = t + 1) Do
                    Var: x = 2.0;
                        x = foo1(5);
                EndFor.
                y = foo1(3);
            EndFor.
        EndBody.      
                   """
        expect = "Type Mismatch In Statement: Assign(Id(y),CallExpr(Id(foo1),[IntLiteral(3)]))"
        self.assertTrue(TestChecker.test(input,expect,498))
    
    def test_CallExpr_10(self):
        """Simple program: main"""
        input = """
        Var: x[2][3] = 2, y = False, z = True;
        
        Function: foo1
        Parameter: t = 1
        Body:
        EndBody.    

        Function: main
        Parameter: t = 2
        Body:
            For (t = 1, t  < 10, t = t + 1) Do
                Var: y = 1.0;
                For (t = 1, t < 5, t = t + 1) Do
                    Var: x = 2.0;
                        x = foo1(5);
                EndFor.
                y = foo1(3);
            EndFor.

            While(True) Do
                Do
                    x[2][3] = foo1(10);
                While (z);
            EndWhile.
        EndBody.      
                   """
        expect = "Type Mismatch In Statement: Assign(ArrayCell(Id(x),[IntLiteral(2),IntLiteral(3)]),CallExpr(Id(foo1),[IntLiteral(10)]))"
        self.assertTrue(TestChecker.test(input,expect,499))

    