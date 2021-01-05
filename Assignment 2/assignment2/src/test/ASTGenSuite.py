import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_vardecl_1(self):
        input = """Var:x;"""
        expect = str(Program([VarDecl(Id("x"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,301))

    def test_vardecl_2(self):
        input = """Var: b = 1;"""
        expect = str(Program([VarDecl(Id("b"),[],IntLiteral(1))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,302))

    def test_vardecl_3(self):
        input = """Var: b[1][2][3];"""
        expect = str(Program([VarDecl(Id("b"),[1,2,3],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,303))

    def test_vardecl_4(self):
        input = """Var: b[1], c[2][3] = 10;
                   Var: a = 5, d;"""
        expect = str(Program([VarDecl(Id("b"),[1], None),VarDecl(Id("c"),[2,3],IntLiteral(10)),VarDecl(Id("a"), [] , IntLiteral(5)),VarDecl(Id("d"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,304))

    def test_vardecl_5(self):
        input = """Var: b[1], a = 2, d = 10;"""
        expect = str(Program([VarDecl(Id("b"),[1], None),VarDecl(Id("a"), [], IntLiteral(2)),VarDecl(Id("d"),[],IntLiteral(10))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,305))
    
    def test_vardecl_6(self):
        input = """Var: b[1][2][3] = "hello";
                   Var: c[2] = "hi!" ; """
        expect = str(Program([VarDecl(Id('b'),[1,2,3],StringLiteral('hello')),VarDecl(Id('c'),[2],StringLiteral('hi!'))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,306))

    def test_vardecl_7(self):
        input = """Var: a = True, b = False;"""
        expect = str(Program([VarDecl(Id('a'),[],BooleanLiteral(True)),VarDecl(Id('b'),[],BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,307))

    def test_vardecl_8(self):
        input = """Var: a = 10;
                   Var: b = 5.8;
                   Var: c = "123";
                   Var: d = True;
                   Var: e = False; """
        expect = str(Program([VarDecl(Id('a'),[],IntLiteral(10)),VarDecl(Id('b'),[],FloatLiteral(5.8)),VarDecl(Id('c'),[],StringLiteral('123')),VarDecl(Id('d'),[],BooleanLiteral(True)),VarDecl(Id('e'),[],BooleanLiteral(False))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,308))

    def test_vardecl_9(self):
        input = """Var: a = 12.0e3, b = 12000., c = 5.0, d = 33.e-1547;
                   Var: e = 1.5e-97, f = 0.33E-3; """
        expect = str(Program([VarDecl(Id('a'),[],FloatLiteral(12000.0)),VarDecl(Id('b'),[],FloatLiteral(12000.0)),VarDecl(Id('c'),[],FloatLiteral(5.0)),VarDecl(Id('d'),[],FloatLiteral(0.0)),VarDecl(Id('e'),[],FloatLiteral(1.5e-97)),VarDecl(Id('f'),[],FloatLiteral(0.00033))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,309))

    def test_vardecl_10(self):
        input = """Var: a = 0xFF; 
                   Var: b[2] = 0x123ABC;
                   Var: c[3][100] = 0o567;
                   Var: d = 0O77;"""
        expect = str(Program([VarDecl(Id('a'),[],IntLiteral(255)),VarDecl(Id('b'),[2],IntLiteral(1194684)),VarDecl(Id('c'),[3,100],IntLiteral(375)),VarDecl(Id('d'),[],IntLiteral(63))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,310))
    
    def test_funcdecl_1(self):
        input = """
        Var: x = 5;
        Function: main
        Body:
            Var : a = 5;
            x = 10;
            printLn(x);
        EndBody.
        """
        expect = str(Program([
            VarDecl(Id("x"),[],IntLiteral(5)),
            FuncDecl(Id("main"),[],([VarDecl(Id("a"),[],IntLiteral(5))],[
                Assign(Id("x"),IntLiteral(10)),
                CallStmt(Id("printLn"),[Id("x")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,311))

    def test_funcdecl_2(self):
        input = """Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While (i < 5) Do
                    a[i] = b +. 1.0;
                    i = i + 1;
                EndWhile.
            EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],
        ([VarDecl(Id("i"),[],IntLiteral(0))],
        [While(BinaryOp("<",Id("i"),IntLiteral(5)),
        ([],
        [Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),
        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,312))
    
    def test_funcdecl_3(self):
        input = """Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                If (i > 0) Then
                    i = i - 1;
                    a[2] = b *. 2.5;
                EndIf.
            EndBody.
        """
        expect = str(
        Program([FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],
        ([VarDecl(Id("i"),[],IntLiteral(0))],
        [If([(BinaryOp(">",Id("i"),IntLiteral(0)),
        [],
        [Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),
        Assign(ArrayCell(Id("a"),[IntLiteral(2)]),BinaryOp("*.",Id("b"),FloatLiteral(2.5)))])],([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,313))
    
    def test_funcdecl_4(self):
        input = """Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
                While (i < 5) Do
                    a[i] = b +. 1.0;
                    i = i + 1;
                EndWhile.
            EndBody.
        """
        expect = str(Program([
        FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],
        ([VarDecl(Id("i"),[],IntLiteral(0))],
        [While(BinaryOp("<",Id("i"),IntLiteral(5)),
        ([],
        [Assign(ArrayCell(Id("a"),[Id("i")]),BinaryOp("+.",Id("b"),FloatLiteral(1.0))),
        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,314))

    def test_funcdecl_5(self):
        input = """
            Function: foo1
            Parameter: a[5], b
            Body:
                Var: i = 0;
                Var: b = 2;
            EndBody.

            Function: foo2
            Parameter: a, b
            Body:
                Var: i = 0;
                Var: c = 3;
            EndBody.
        """
        expect = str(Program([
        FuncDecl(Id("foo1"),
        [VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],
        ([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("b"),[],IntLiteral(2))],[])),
        FuncDecl(Id("foo2"),
        [VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None)],
        ([VarDecl(Id("i"),[],IntLiteral(0)),VarDecl(Id("c"),[],IntLiteral(3))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,315))

    def test_funcdecl_6(self):
        input = """
            Function: foo1
            Parameter: a[5], b
            Body:
                Var: i = 0;
            EndBody.

            Function: foo2
            Parameter: a, b, c
            Body:
                i = a + b;
                a = (b + c)*i;
            EndBody.

            Function: foo3
            Parameter: a = 10, b = "hello"
            Body:
                Var: i = 0;
                a = a * a;
            EndBody.
        """
        expect = str(Program([
        FuncDecl(Id("foo1"),
        [VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[],None)],
        ([VarDecl(Id("i"),[],IntLiteral(0))],[])),
        
        FuncDecl(Id("foo2"),
        [VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],
        ([],
        [Assign(Id("i"),BinaryOp("+",Id("a"),Id("b"))),
        Assign(Id("a"),BinaryOp("*",BinaryOp("+",Id("b"),Id("c")),Id("i")))])),
        
        FuncDecl(Id("foo3"),
        [VarDecl(Id("a"),[],IntLiteral(10)),VarDecl(Id("b"),[],StringLiteral("hello"))],
        ([VarDecl(Id("i"),[],IntLiteral(0))],
        [Assign(Id("a"),BinaryOp("*",Id("a"),Id("a")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,316))

    def test_funcdecl_7(self):
        input = """
            Function: foo
            Parameter: a[5], b
            Body:
                Var: i = 0;
            EndBody.

            Function: main
            Body:
                Var: i = 0;
            EndBody.
        """
        expect = str(Program([
        FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[5],None),VarDecl(Id("b"),[], None)],
        ([VarDecl(Id("i"),[],IntLiteral(0))],[])),
        
        FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("i"),[],IntLiteral(0))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,317))

    def test_funcdecl_8(self):
        input = """
            Function: main
            Body:
                Var: i = 0;
            EndBody.

            Function: foo
            Parameter: a
            Body:
                Var: i = 0;
            EndBody.
        """
        expect = str(Program([
        FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("i"),[],IntLiteral(0))],[])),
        FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[],None)],
        ([VarDecl(Id("i"),[],IntLiteral(0))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,318))

    def test_funcdecl_9(self):
        input = """
            Function: foo
            Parameter: a[5] = 10, b[2][3] = 10, str = "string", check = True
            Body:
            EndBody.
        """
        expect = str(Program([
        FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[5],IntLiteral(10)),
        VarDecl(Id("b"),[2,3],IntLiteral(10)),
        VarDecl(Id("str"),[],StringLiteral("string")),
        VarDecl(Id("check"),[],BooleanLiteral(True))],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,319))

    def test_funcdecl_10(self):
        input = """
            Function: main
            Parameter: a[5] = 0x124, b = "this is a string", x = True, y[30][40][50] = 1.454
            Body:
            EndBody.
        """
        expect = str(Program([
        FuncDecl(Id("main"),
        [VarDecl(Id("a"),[5],IntLiteral(292)),
        VarDecl(Id("b"),[],StringLiteral("this is a string")),
        VarDecl(Id("x"),[],BooleanLiteral(True)),
        VarDecl(Id("y"),[30,40,50],FloatLiteral(1.454))],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,320))

    def test_all_decl_1(self):
        input = """
            Var : a = 1;
            Function: foo
            Body:
            EndBody.
        """
        expect = str(Program([VarDecl(Id("a"),[],IntLiteral(1)),FuncDecl(Id("foo"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,321))

    def test_all_decl_2(self):
        input = """
            Var : a = 1;
            Var : b = 2;
            Var : c = 3;
            Function: foo
            Body:
            EndBody.
        """
        expect = str(Program([
        VarDecl(Id("a"),[],IntLiteral(1)),
        VarDecl(Id("b"),[],IntLiteral(2)),
        VarDecl(Id("c"),[],IntLiteral(3)),
        FuncDecl(Id("foo"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,322))

    def test_all_decl_3(self):
        input = """
            Var : a = 1;
            Var : array[2][3];
            Function: main
            Parameter: array[2][3]
            Body:
                Var : b = 2;
            EndBody.
        """
        expect = str(Program(
        [VarDecl(Id("a"),[],IntLiteral(1)),
        VarDecl(Id("array"),[2,3], None),
        FuncDecl(Id("main"),
        [VarDecl(Id("array"),[2,3], None)],
        ([VarDecl(Id("b"),[],IntLiteral(2))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,323))

    def test_all_decl_4(self):
        input = """
            Var : a = 1;
            Var : b = 2;
            Function: foo1
            Parameter : c[2][3] = "string"
            Body:
                c[1][2] = "miss";
            EndBody.

            Function: foo2
            Parameter : z = True
            Body:
                z = False;
            EndBody.
        """
        expect = str(Program(
        [VarDecl(Id("a"),[],IntLiteral(1)),
        VarDecl(Id("b"),[],IntLiteral(2)),
        FuncDecl(Id("foo1"),
        [VarDecl(Id("c"),[2,3],StringLiteral("string"))],
        ([],
        [Assign(ArrayCell(Id("c"),[IntLiteral(1),IntLiteral(2)]),StringLiteral("miss"))])),
        FuncDecl(Id("foo2"),
        [VarDecl(Id("z"),[],BooleanLiteral(True))],
        ([],
        [Assign(Id("z"),BooleanLiteral(False))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,324))

    def test_all_decl_5(self):
        input = """
        """
        expect = str(Program([]))
        self.assertTrue(TestAST.checkASTGen(input,expect,325))

    def test_vardecl_stmt_1(self):
        input = """
        Function: main
        Body:
            Var : b = 2;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("b"),[],IntLiteral(2))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,326))

    def test_vardecl_stmt_2(self):
        input = """
        Function: main
        Body:
            Var : a = 2, b = 3, c = 5;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("a"),[],IntLiteral(2)),
        VarDecl(Id("b"),[],IntLiteral(3)),
        VarDecl(Id("c"),[],IntLiteral(5))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,327))

    def test_vardecl_stmt_3(self):
        input = """
        Function: main
        Body:
            Var : a[2][3] = 0o456, b = 0xA2B, c[4] = False;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("a"),[2,3],IntLiteral(302)),
        VarDecl(Id("b"),[],IntLiteral(2603)),
        VarDecl(Id("c"),[4],BooleanLiteral(False))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,328))

    def test_vardecl_stmt_4(self):
        input = """
        Function: main
        Body:
            Var : b = 2;
            Var : c = 5;
            Var : array[100][100];
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("b"),[],IntLiteral(2)),
        VarDecl(Id("c"),[],IntLiteral(5)),
        VarDecl(Id("array"),[100,100],None)],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,329))

    def test_vardecl_stmt_5(self):
        input = """
        Function: main
        Body:
            Var : b = 2999, c[10000] = False;
            Var : x = "this is a String", e = 0e123;
            Var : y[2][99] = 0o223, z = 12.E-1, thing = True;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("b"),[],IntLiteral(2999)),
        VarDecl(Id("c"),[10000],BooleanLiteral(False)),
        VarDecl(Id("x"),[],StringLiteral("this is a String")),
        VarDecl(Id("e"),[],FloatLiteral(0.0)),
        VarDecl(Id("y"),[2,99],IntLiteral(147)),
        VarDecl(Id("z"),[],FloatLiteral(1.2)),
        VarDecl(Id("thing"),[],BooleanLiteral(True))],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,330))

    def test_assign_stmt_1(self):
        input = """
        Function: foo
            Parameter : a, b, c
            Body:
                a = 123;
                b = 1.5;
                c = "abc";
            EndBody. 
        """
        expect = str(Program(
        [FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],
        ([],
        [Assign(Id("a"),IntLiteral(123)),
        Assign(Id("b"),FloatLiteral(1.5)),
        Assign(Id("c"),StringLiteral("abc"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,331))    

    def test_assign_stmt_2(self):
        input = """
        Function: foo
            Parameter : a, b, c
            Body:
                a = b + c;
                a = b * c;
                a = b / c;
            EndBody. 
        """
        expect = str(Program(
        [FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[],None),VarDecl(Id("b"),[],None),VarDecl(Id("c"),[],None)],
        ([],
        [Assign(Id("a"),BinaryOp("+",Id("b"),Id("c"))),
        Assign(Id("a"),BinaryOp("*",Id("b"),Id("c"))),
        Assign(Id("a"),BinaryOp("/",Id("b"),Id("c")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,332))  

    def test_assign_stmt_3(self):
        input = """
        Function: foo
            Parameter : a, b, c
            Body:
                a = False;
                b = True;
                c = a || b;
                a = (!(b && c)||!(a && c)||!(a && b)); 
            EndBody. 
        """
        expect = str(Program(
        [FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None),
        VarDecl(Id("c"),[],None)],
        ([],
        [Assign(Id("a"),BooleanLiteral(False)),
        Assign(Id("b"),BooleanLiteral(True)),
        Assign(Id("c"),BinaryOp("||",Id("a"),Id("b"))),
        Assign(Id("a"),BinaryOp("||",BinaryOp("||",UnaryOp("!",BinaryOp("&&",Id("b"),Id("c"))),UnaryOp("!",BinaryOp("&&",Id("a"),Id("c")))),UnaryOp("!",BinaryOp("&&",Id("a"),Id("b")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,333))  

    def test_assign_stmt_4(self):
        input = """
        Function: main
        Body:
            Var: a[5][5], b = 1.55, c = 10;
            a[1][2] = b * c;
            a[2][3] = b / c;
            a[3][4] = ((b + c) - (b*c))/(b*5 - c *. -8.e15 / (a[1][1] + b + c));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("a"),[5,5],None),
        VarDecl(Id("b"),[],FloatLiteral(1.55)),
        VarDecl(Id("c"),[],IntLiteral(10))],
        [Assign(ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(2)]),BinaryOp("*",Id("b"),Id("c"))),
        Assign(ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),BinaryOp("/",Id("b"),Id("c"))),
        Assign(ArrayCell(Id("a"),[IntLiteral(3),IntLiteral(4)]),BinaryOp("/",BinaryOp("-",BinaryOp("+",Id("b"),Id("c")),BinaryOp("*",Id("b"),Id("c"))),BinaryOp("-",BinaryOp("*",Id("b"),IntLiteral(5)),BinaryOp("/",BinaryOp("*.",Id("c"),UnaryOp("-",FloatLiteral(8000000000000000.0))),BinaryOp("+",BinaryOp("+",ArrayCell(Id("a"),[IntLiteral(1),IntLiteral(1)]),Id("b")),Id("c"))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,334))  
   
    def test_assign_stmt_5(self):
        input = """
        Function: main
        Parameter : a,b,c
        Body:
            a = "hello my name is kiet";
            b = "this is my testcase";
            c = a + b;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None),
        VarDecl(Id("c"),[],None)],
        ([],
        [Assign(Id("a"),StringLiteral("hello my name is kiet")),
        Assign(Id("b"),StringLiteral("this is my testcase")),
        Assign(Id("c"),BinaryOp("+",Id("a"),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,335)) 

    def test_if_stmt_1(self):
        input = """
        Function: main
        Parameter : a,b,i
        Body:
            If (i > 0) Then
                i = i - 1;
                a[2] = b *. 2.5;
            EndIf.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None),
        VarDecl(Id("i"),[],None)],
        ([],
        [If([(BinaryOp(">",Id("i"),IntLiteral(0)),
        [],
        [Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1))),
        Assign(ArrayCell(Id("a"),[IntLiteral(2)]),BinaryOp("*.",Id("b"),FloatLiteral(2.5)))])],
        ([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,336))

    def test_if_stmt_2(self):
        input = """
        Function: main
        Parameter : i
        Body:
            If (i > 0) Then
                i = i - 1;
            ElseIf (i < 5) Then
                i = i + 1;
            EndIf.
        EndBody. 
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("i"),[],None)],
        ([],
        [If([(BinaryOp(">",Id("i"),IntLiteral(0)),
        [],
        [Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))]),
        (BinaryOp("<",Id("i"),IntLiteral(5)),
        [],
        [Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],
        ([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,337))

    def test_if_stmt_3(self):
        input = """
        Function: main
        Parameter : i
        Body:
            If (i > 0) Then
                i = i - 1;
            ElseIf (i < 5) Then
                i = i + 1;
            ElseIf (i < -5) Then
                i = i * i;
            ElseIf (i % 2 == 0) Then
                i = i + 1;
            Else
                Var: a = "end";
                print(a);
            EndIf.
        EndBody. 
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("i"),[],None)],
        ([],
        [If([(BinaryOp(">",Id("i"),IntLiteral(0)),
        [],
        [Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))]),
        (BinaryOp("<",Id("i"),IntLiteral(5)),
        [],
        [Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]),
        (BinaryOp("<",Id("i"),UnaryOp("-",IntLiteral(5))),
        [],
        [Assign(Id("i"),BinaryOp("*",Id("i"),Id("i")))]),
        (BinaryOp("==",BinaryOp("%",Id("i"),IntLiteral(2)),IntLiteral(0)),
        [],
        [Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],
        ([VarDecl(Id("a"),[],StringLiteral("end"))],
        [CallStmt(Id("print"),[Id("a")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,338))

    def test_if_stmt_4(self):
        input = """
        Function: main
        Parameter : i,a,b
        Body:
            If (i > 0) Then
                i = i - 1;
            ElseIf (i < 5) Then
                i = i + 1;
            EndIf.

            If (a > 10) Then
                a = a - 1;
            ElseIf (a < 100) Then
                a = a + 1;
            EndIf.

            If (b > -20) Then
                b = b + 1;
            ElseIf (i > -100) Then
                b = b + 100;
            EndIf.
        EndBody. 
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("i"),[],None),
        VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None)],
        ([],
        [If([(BinaryOp(">",Id("i"),IntLiteral(0)),
        [],
        [Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))]),
        (BinaryOp("<",Id("i"),IntLiteral(5)),
        [],
        [Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))])],
        ([],[])),
        If([(BinaryOp(">",Id("a"),IntLiteral(10)),
        [],
        [Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))]),
        (BinaryOp("<",Id("a"),IntLiteral(100)),
        [],
        [Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))])],
        ([],[])),
        If([(BinaryOp(">",Id("b"),UnaryOp("-",IntLiteral(20))),
        [],
        [Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(1)))]),
        (BinaryOp(">",Id("i"),UnaryOp("-",IntLiteral(100))),
        [],
        [Assign(Id("b"),BinaryOp("+",Id("b"),IntLiteral(100)))])],
        ([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,339))

    def test_if_stmt_5(self):
        input = """
        Function: main
        Parameter : i,a
        Body:
            If (i > 0) Then
                i = i - 1;
            ElseIf (i < 5) Then
                If (a == 2) Then
                    print(a + 5);
                EndIf.
            Else
                If(a % 2 == 3) Then
                    If (a % 3 == 2) Then
                        print(a + 3);
                    EndIf.
                EndIf.
            EndIf.
        EndBody. 
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("i"),[],None),
        VarDecl(Id("a"),[],None)],
        ([],
        [If([(BinaryOp(">",Id("i"),IntLiteral(0)),
        [],
        [Assign(Id("i"),BinaryOp("-",Id("i"),IntLiteral(1)))]),
        (BinaryOp("<",Id("i"),IntLiteral(5)),
        [],
        [If([(BinaryOp("==",Id("a"),IntLiteral(2)),
        [],
        [CallStmt(Id("print"),[BinaryOp("+",Id("a"),IntLiteral(5))])])],
        ([],[]))])],
        #else: If(i > 0) Then
        ([],
        [If([(BinaryOp("==",BinaryOp("%",Id("a"),IntLiteral(2)),IntLiteral(3)),
        [],
        [If([(BinaryOp("==",BinaryOp("%",Id("a"),IntLiteral(3)),IntLiteral(2)),
        [],
        [CallStmt(Id("print"),
        [BinaryOp("+",Id("a"),IntLiteral(3))])])],
        ([],[]))])],
        ([],[]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,340))

    def test_for_stmt_1(self):
        input = """
        Function: main
        Body:
            For (i = 0, i < 10, i = i + 2) Do
                writeln(i);
            EndFor.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([],
        [For(Id("i"),IntLiteral(0),BinaryOp("<",Id("i"),IntLiteral(10)),Id("i"),BinaryOp("+",Id("i"),IntLiteral(2)),
        ([],
        [CallStmt(Id("writeln"),[Id("i")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,341))

    def test_for_stmt_2(self):
        input = """
        Function: main
        Parameter : n = 100
        Body:
            For (i = n, i < n*n , i = i*i) Do
                Var: a = "hello";
                writeln(a);
            EndFor.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("n"),[],IntLiteral(100))],
        ([],
        [For(Id("i"),Id("n"),
        BinaryOp("<",Id("i"),
        BinaryOp("*",Id("n"),Id("n"))),
        Id("i"),BinaryOp("*",Id("i"),Id("i")),
        ([VarDecl(Id("a"),[],StringLiteral("hello"))],
        [CallStmt(Id("writeln"),[Id("a")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,342))

    def test_for_stmt_3(self):
        input = """
        Function: main
        Parameter : n[5] = 10
        Body:
            For (i = n[1], i < n[5] , i = i*n[3]) Do
                Var: a = 100;
                Var: b = 50;
                i = (((a / b) + b ) / b);
            EndFor.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("n"),[5],IntLiteral(10))],
        ([],
        [For(Id("i"),ArrayCell(Id("n"),[IntLiteral(1)]),
        BinaryOp("<",Id("i"),ArrayCell(Id("n"),[IntLiteral(5)])),
        Id("i"),BinaryOp("*",Id("i"),ArrayCell(Id("n"),[IntLiteral(3)])),
        ([VarDecl(Id("a"),[],IntLiteral(100)),
        VarDecl(Id("b"),[],IntLiteral(50))],
        [Assign(Id("i"),BinaryOp("/",BinaryOp("+",BinaryOp("/",Id("a"),Id("b")),Id("b")),Id("b")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,343))

    def test_for_stmt_4(self):
        input = """
        Function: main
        Parameter : n[5] = 10
        Body:
            For (i = n[1], i < n[5] , i = i*n[3]) Do
                Var: b = 10;
                For (i = 2, i < b , i = i + 1) Do
                    Var: c = 30;
                    For(i = 3, i < c, i = i + 1) Do
                        print(i);
                    EndFor.
                EndFor.
            EndFor.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("n"),[5],IntLiteral(10))],
        ([],
        [For(Id("i"),ArrayCell(Id("n"),[IntLiteral(1)]),
        BinaryOp("<",Id("i"),ArrayCell(Id("n"),[IntLiteral(5)])),
        Id("i"),BinaryOp("*",Id("i"),ArrayCell(Id("n"),[IntLiteral(3)])),
        ([VarDecl(Id("b"),[],IntLiteral(10))],
        [For(Id("i"),IntLiteral(2),
        BinaryOp("<",Id("i"),Id("b")),
        Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)),
        ([VarDecl(Id("c"),[],IntLiteral(30))],
        [For(Id("i"),IntLiteral(3),
        BinaryOp("<",Id("i"),Id("c")),
        Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)),
        ([],
        [CallStmt(Id("print"),[Id("i")])]))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,344))

    def test_for_stmt_5(self):
        input = """
        Function: main
        Parameter : n[5] = 10
        Body:
            For (i = n[1], i < n[5] , i = i*n[3]) Do
                Var: a = 100;
                print(a);
            EndFor.

            For (i = 100, i < 9999 , i = i*n[4]) Do
                Var: b = 100;
                print(c);
            EndFor.

            For (i = 100, i >= 0 , i = i / n[1]) Do
                Var: b = "hello";
                print(b);
            EndFor.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("n"),[5],IntLiteral(10))],
        ([],
        [For(Id("i"),ArrayCell(Id("n"),[IntLiteral(1)]),
        BinaryOp("<",Id("i"),ArrayCell(Id("n"),[IntLiteral(5)])),
        Id("i"),BinaryOp("*",Id("i"),ArrayCell(Id("n"),[IntLiteral(3)])),
        ([VarDecl(Id("a"),[],IntLiteral(100))],
        [CallStmt(Id("print"),[Id("a")])])),
        For(Id("i"),IntLiteral(100),
        BinaryOp("<",Id("i"),IntLiteral(9999)),
        Id("i"),BinaryOp("*",Id("i"),ArrayCell(Id("n"),[IntLiteral(4)])),
        ([VarDecl(Id("b"),[],IntLiteral(100))],
        [CallStmt(Id("print"),[Id("c")])])),
        For(Id("i"),IntLiteral(100),
        BinaryOp(">=",Id("i"),IntLiteral(0)),
        Id("i"),BinaryOp("/",Id("i"),ArrayCell(Id("n"),[IntLiteral(1)])),
        ([VarDecl(Id("b"),[],StringLiteral("hello"))],
        [CallStmt(Id("print"),[Id("b")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,345))

    def test_while_stmt_1(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            While (a > 0) Do
                Var: b = 5;
                a = a - b;
            EndWhile.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [While(BinaryOp(">",Id("a"),IntLiteral(0)),
        ([VarDecl(Id("b"),[],IntLiteral(5))],
        [Assign(Id("a"),BinaryOp("-",Id("a"),Id("b")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,346))

    def test_while_stmt_2(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            While ((a > 0)&&(a<=100)) Do
                Var: b = 5;
                a = a - b;
                print(a);
            EndWhile.
        EndBody.
        """
        expect = str(Program([
        FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [While(BinaryOp("&&",BinaryOp(">",Id("a"),IntLiteral(0)),
        BinaryOp("<=",Id("a"),IntLiteral(100))),
        ([VarDecl(Id("b"),[],IntLiteral(5))],
        [Assign(Id("a"),BinaryOp("-",Id("a"),Id("b"))),
        CallStmt(Id("print"),[Id("a")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,347))

    def test_while_stmt_3(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            While ((a > 0)&&(a<=100)) Do
                print(a);
            EndWhile.

            While (!((!True)||(False))) Do
                print(a+1);
            EndWhile.

            While (a > 0xABC) Do
                print(a+2);
                a = a - 1;
            EndWhile.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [While(BinaryOp("&&",BinaryOp(">",Id("a"),IntLiteral(0)),
        BinaryOp("<=",Id("a"),IntLiteral(100))),
        ([],
        [CallStmt(Id("print"),[Id("a")])])),
        While(UnaryOp("!",BinaryOp("||",UnaryOp("!",BooleanLiteral(True)),BooleanLiteral(False))),
        ([],
        [CallStmt(Id("print"),[BinaryOp("+",Id("a"),IntLiteral(1))])])),
        While(BinaryOp(">",Id("a"),IntLiteral(2748)),
        ([],
        [CallStmt(Id("print"),[BinaryOp("+",Id("a"),IntLiteral(2))]),
        Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,348))

    def test_while_stmt_4(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            While ((a > 0)&&(a<=100)) Do
                print(a);
                While (a > 1.22) Do
                    Var : b;
                    While (b > 0o123) Do
                        Var : c;
                    EndWhile.
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [While(BinaryOp("&&",BinaryOp(">",Id("a"),IntLiteral(0)),
        BinaryOp("<=",Id("a"),IntLiteral(100))),
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        While(BinaryOp(">",Id("a"),FloatLiteral(1.22)),
        ([VarDecl(Id("b"),[],None)],
        [While(BinaryOp(">",Id("b"),IntLiteral(83)),
        ([VarDecl(Id("c"),[],None)],
        []))]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,349))

    def test_while_stmt_5(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            While ((a > 0)&&(a<=100)) Do
                print(a);
                While (a > 1.22) Do
                    print("hello");
                EndWhile.

                While(True) Do
                    While (False) Do
                    Var: c;
                    EndWhile.
                EndWhile.

                While((!(False))&&(a>5)) Do
                    print(a);
                EndWhile.
            EndWhile.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [While(BinaryOp("&&",BinaryOp(">",Id("a"),IntLiteral(0)),
        BinaryOp("<=",Id("a"),IntLiteral(100))),
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        While(BinaryOp(">",Id("a"),FloatLiteral(1.22)),
        ([],
        [CallStmt(Id("print"),
        [StringLiteral("hello")])])),
        While(BooleanLiteral(True),
        ([],
        [While(BooleanLiteral(False),
        ([VarDecl(Id("c"),[],None)],
        []))])),
        While(BinaryOp("&&",UnaryOp("!",BooleanLiteral(False)),BinaryOp(">",Id("a"),IntLiteral(5))),
        ([],
        [CallStmt(Id("print"),[Id("a")])]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,350))

    def test_do_while_stmt_1(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            Do
                print(a);
                a = a - 1;
            While (a >= 0);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [Dowhile(
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))]),
        BinaryOp(">=",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,351))

    def test_do_while_stmt_2(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            Do
                Var: a[1] = "hello";
                print(a[1]);
            While (!((a <= 0)||(a >= 99)));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [Dowhile(([VarDecl(Id("a"),[1],StringLiteral("hello"))],
        [CallStmt(Id("print"),[ArrayCell(Id("a"),[IntLiteral(1)])])]),
        UnaryOp("!",BinaryOp("||",BinaryOp("<=",Id("a"),IntLiteral(0)),
        BinaryOp(">=",Id("a"),IntLiteral(99)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,352))

    def test_do_while_stmt_3(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            Do
                Var: b[2] = False;
                Do
                    Var: c = 10;
                    Do
                        c = c - 1;
                    While (c > 0);
                While (!b[2]);
            While (a >= 0);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [Dowhile(
        ([VarDecl(Id("b"),[2],BooleanLiteral(False))],
        [Dowhile(
        ([VarDecl(Id("c"),[],IntLiteral(10))],
        [Dowhile(
        ([],
        [Assign(Id("c"),BinaryOp("-",Id("c"),IntLiteral(1)))]),
        BinaryOp(">",Id("c"),IntLiteral(0)))]),
        UnaryOp("!",ArrayCell(Id("b"),[IntLiteral(2)])))]),
        BinaryOp(">=",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,353))

    def test_do_while_stmt_4(self):
        input = """
        Function: main
        Body:
            Var: a = 100, b = 50, c = 20;
            Do
                print(a);
                a = a - 1;
            While (a >= 0);

            Do
                print(b);
                b = b - 1;
            While (b >= 0);

            Do
                print(c);
                c = c - 1;
            While (a >= 0);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("a"),[],IntLiteral(100)),
        VarDecl(Id("b"),[],IntLiteral(50)),
        VarDecl(Id("c"),[],IntLiteral(20))],
        [Dowhile(
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))]),
        BinaryOp(">=",Id("a"),IntLiteral(0))),
        Dowhile(
        ([],
        [CallStmt(Id("print"),[Id("b")]),
        Assign(Id("b"),BinaryOp("-",Id("b"),IntLiteral(1)))]),
        BinaryOp(">=",Id("b"),IntLiteral(0))),
        Dowhile(
        ([],
        [CallStmt(Id("print"),[Id("c")]),
        Assign(Id("c"),BinaryOp("-",Id("c"),IntLiteral(1)))]),
        BinaryOp(">=",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,354))

    def test_do_while_stmt_5(self):
        input = """
        Function: main
        Parameter : a = 100
        Body:
            Do
                print(a);
                a = a - 1;
                Do
                    print(a);
                    a = a - 1;
                While (a >= 5);
                Do
                    print(a*a);
                    a = a + 5;
                While (a <= 0xAFF);
            While (a >= 0);

            Do
                Do
                    print(a);
                    a = a - 1;
                While ((a >= 100)&&(!(2000 > a)));
            While (a >= 0);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(100))],
        ([],
        [Dowhile(
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1))),
        Dowhile(
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))]),
        BinaryOp(">=",Id("a"),IntLiteral(5))),
        Dowhile(
        ([],
        [CallStmt(Id("print"),
        [BinaryOp("*",Id("a"),Id("a"))]),
        Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(5)))]),
        BinaryOp("<=",Id("a"),IntLiteral(2815)))]),
        BinaryOp(">=",Id("a"),IntLiteral(0))),
        Dowhile(
        ([],
        [Dowhile(
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        Assign(Id("a"),BinaryOp("-",Id("a"),IntLiteral(1)))]),
        BinaryOp("&&",BinaryOp(">=",Id("a"),IntLiteral(100)),
        UnaryOp("!",BinaryOp(">",IntLiteral(2000),Id("a")))))]),
        BinaryOp(">=",Id("a"),IntLiteral(0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,355))

    def test_call_stmt_1(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var : b = 100;
            print(a*b);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("b"),[],IntLiteral(100))],
        [CallStmt(Id("print"),[BinaryOp("*",Id("a"),Id("b"))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,356))

    def test_call_stmt_2(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var : b = 100;
            mul(a*b);
            div(a/b);
            add(a+b);
            sub(a-b);
            mod(a % b);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("b"),[],IntLiteral(100))],
        [CallStmt(Id("mul"),[BinaryOp("*",Id("a"),Id("b"))]),
        CallStmt(Id("div"),[BinaryOp("/",Id("a"),Id("b"))]),
        CallStmt(Id("add"),[BinaryOp("+",Id("a"),Id("b"))]),
        CallStmt(Id("sub"),[BinaryOp("-",Id("a"),Id("b"))]),
        CallStmt(Id("mod"),[BinaryOp("%",Id("a"),Id("b"))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,357))

    def test_call_stmt_3(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var : b = 1;
            print(((a*b/(a+b))%a)*(b%(c +. 10.22)));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("b"),[],IntLiteral(1))],
        [CallStmt(Id("print"),
        [BinaryOp("*",
        BinaryOp("%",
        BinaryOp("/",
        BinaryOp("*",Id("a"),Id("b")),
        BinaryOp("+",Id("a"),Id("b"))),Id("a")),
        BinaryOp("%",Id("b"),BinaryOp("+.",Id("c"),FloatLiteral(10.22))))])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,358))

    def test_call_stmt_4(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var : b = 10, c = 20;
            print(add(a,sub(b,mul(a,c))));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("b"),[],IntLiteral(10)),
        VarDecl(Id("c"),[],IntLiteral(20))],
        [CallStmt(Id("print"),
        [CallExpr(Id("add"),[Id("a"),
        CallExpr(Id("sub"),[Id("b"),
        CallExpr(Id("mul"),[Id("a"),Id("c")])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,359))

    def test_break_stmt_1(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            While (a > 0) Do
                print(a);
                Break;
                a = a + 1;
            EndWhile.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([],
        [While(BinaryOp(">",Id("a"),IntLiteral(0)),
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        Break(),
        Assign(Id("a"),BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,360))

    def test_break_stmt_2(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            For (i = 1, i < 5, i = i + 1) Do
                i = i * i;
                Break;
            EndFor.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([],
        [For(Id("i"),
        IntLiteral(1),
        BinaryOp("<",Id("i"),IntLiteral(5)),
        Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)),
        ([],
        [Assign(Id("i"),
        BinaryOp("*",Id("i"),Id("i"))),
        Break()]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,361))

    def test_continue_stmt_1(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            While (a > 0) Do
                print(a);
                Continue;
                a = a + 1;
            EndWhile.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([],
        [While(BinaryOp(">",Id("a"),IntLiteral(0)),
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        Continue(),
        Assign(Id("a"),
        BinaryOp("+",Id("a"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,362))

    def test_continue_stmt_2(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            For (i = 1, i < 5, i = i + 1) Do
                i = i * i;
                Continue;
            EndFor.
            print("hello world!");
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([],
        [For(Id("i"),IntLiteral(1),
        BinaryOp("<",Id("i"),IntLiteral(5)),
        Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)),
        ([],
        [Assign(Id("i"),BinaryOp("*",Id("i"),Id("i"))),
        Continue()])),
        CallStmt(Id("print"),[StringLiteral("hello world!")])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,363))

    def test_return_stmt_1(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var : array[1][2] = 3;
            Return;
            print(array[1][1]);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("array"),[1,2],IntLiteral(3))],
        [Return(None),
        CallStmt(Id("print"),[ArrayCell(Id("array"),[IntLiteral(1),IntLiteral(1)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,364))

    def test_return_stmt_2(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var : array[1][2] = 3;
            Return print(array[1][2]*a + mul(array[0][0],a));
            print(array[1][1]);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("array"),[1,2],IntLiteral(3))],
        [Return(CallExpr(Id("print"),
        [BinaryOp("+",BinaryOp("*",ArrayCell(Id("array"),[IntLiteral(1),IntLiteral(2)]),Id("a")),
        CallExpr(Id("mul"),[ArrayCell(Id("array"),[IntLiteral(0),IntLiteral(0)]),Id("a")]))])),
        CallStmt(Id("print"),[ArrayCell(Id("array"),[IntLiteral(1),IntLiteral(1)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,365))

    def test_expression_1(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var: b;
            b = ((a == 5)&&(a > 2));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("b"),[],None)],
        [Assign(Id("b"),
        BinaryOp("&&",
        BinaryOp("==",Id("a"),IntLiteral(5)),
        BinaryOp(">",Id("a"),IntLiteral(2))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,366))

    def test_expression_2(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var: b;
            b = ((a != 10)&&(a < 10));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("b"),[],None)],
        [Assign(Id("b"),
        BinaryOp("&&",
        BinaryOp("!=",Id("a"),IntLiteral(10)),
        BinaryOp("<",Id("a"),IntLiteral(10))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,367))

    def test_expression_3(self):
        input = """
        Function: main
        Parameter : a = 10
        Body:
            Var: b;
            b = (a <= 0x5) && ((a >= 2) || a <=. 0.5) && (a >. -7.5);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10))],
        ([VarDecl(Id("b"),[],None)],
        [Assign(Id("b"),
        BinaryOp("&&",BinaryOp("&&",
        BinaryOp("<=",Id("a"),IntLiteral(5)),
        BinaryOp("<=.",BinaryOp("||",
        BinaryOp(">=",Id("a"),IntLiteral(2)),Id("a")),FloatLiteral(0.5))),
        BinaryOp(">.",Id("a"),
        UnaryOp("-",FloatLiteral(7.5)))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,368))

    def test_expression_4(self):
        input = """
        Function: main
        Parameter : a = 10, b
        Body:
            b = ((a >=. 7.e9) || (a =/= 5.9)) && (2 <. a);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10)),
        VarDecl(Id("b"),[],None)],
        ([],
        [Assign(Id("b"),
        BinaryOp("&&",
        BinaryOp("||",
        BinaryOp(">=.",Id("a"),FloatLiteral(7000000000.0)),
        BinaryOp("=/=",Id("a"),FloatLiteral(5.9))),
        BinaryOp("<.",IntLiteral(2),Id("a"))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,369))

    def test_expression_5(self):
        input = """
        Function: main
        Parameter : a = 10, b = 5,c
        Body:
            c = (((a > 5)&&(b < 10))&&(a <= 100)||((b > a)&&(a <= b)));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],IntLiteral(10)),
        VarDecl(Id("b"),[],IntLiteral(5)),
        VarDecl(Id("c"),[],None)],
        ([],
        [Assign(Id("c"),
        BinaryOp("||",
        BinaryOp("&&",
        BinaryOp("&&",
        BinaryOp(">",Id("a"),IntLiteral(5)),
        BinaryOp("<",Id("b"),IntLiteral(10))),
        BinaryOp("<=",Id("a"),IntLiteral(100))),
        BinaryOp("&&",BinaryOp(">",Id("b"),Id("a")),
        BinaryOp("<=",Id("a"),Id("b")))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,370))

    def test_expression_6(self):
        input = """
        Function: main
        Parameter: x,y,z
        Body:
            x = 0x12A;
            y = -3.5e-10;
            z = 0o72;
            x = y *. y / ( y -. z );
            z = z * x;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("x"),[],None),
        VarDecl(Id("y"),[],None),
        VarDecl(Id("z"),[],None)],
        ([],
        [Assign(Id("x"),IntLiteral(298)),
        Assign(Id("y"),
        UnaryOp("-",FloatLiteral(3.5e-10))),
        Assign(Id("z"),IntLiteral(58)),
        Assign(Id("x"),
        BinaryOp("/",
        BinaryOp("*.",Id("y"),Id("y")),
        BinaryOp("-.",Id("y"),Id("z")))),
        Assign(Id("z"),
        BinaryOp("*",Id("z"),Id("x")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,371))

    def test_expression_7(self):
        input = """
        Function: main
        Parameter: x,y
        Body:
            x = x - x + y / y;
            y = ( y \\ y * x - x ) % (x);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("x"),[],None),
        VarDecl(Id("y"),[],None)],
        ([],
        [Assign(Id("x"),
        BinaryOp("+",
        BinaryOp("-",Id("x"),Id("x")),
        BinaryOp("/",Id("y"),Id("y")))),
        Assign(Id("y"),
        BinaryOp("%",
        BinaryOp("-",
        BinaryOp("*",
        BinaryOp("\\",Id("y"),Id("y")),Id("x")),Id("x")),Id("x")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,372))

    def test_expression_8(self):
        input = """
        Function: main
        Parameter: x,y,z,array[2][3]
        Body:
            x = 0x12A;
            y = -3.5e-10;
            z = 0o72;
            array[1][1] = y *. y * array[2][2] / ( y -. z );
            z = array[1][3] * x;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("x"),[],None),
        VarDecl(Id("y"),[],None),
        VarDecl(Id("z"),[],None),
        VarDecl(Id("array"),[2,3],None)],
        ([],
        [Assign(Id("x"),IntLiteral(298)),
        Assign(Id("y"),
        UnaryOp("-",FloatLiteral(3.5e-10))),
        Assign(Id("z"),IntLiteral(58)),
        Assign(ArrayCell(Id("array"),[IntLiteral(1),IntLiteral(1)]),
        BinaryOp("/",
        BinaryOp("*",
        BinaryOp("*.",Id("y"),Id("y")),ArrayCell(Id("array"),[IntLiteral(2),IntLiteral(2)])),
        BinaryOp("-.",Id("y"),Id("z")))),
        Assign(Id("z"),
        BinaryOp("*",ArrayCell(Id("array"),[IntLiteral(1),IntLiteral(3)]),Id("x")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,373))

    def test_expression_9(self):
        input = """
        Function: main
        Parameter: x,y,z
        Body:
            x = !(!(!y && z) || (x > 3) && !(y < 2));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("x"),[],None),
        VarDecl(Id("y"),[],None),
        VarDecl(Id("z"),[],None)],
        ([],
        [Assign(Id("x"),
        UnaryOp("!",
        BinaryOp("&&",
        BinaryOp("||",
        UnaryOp("!",
        BinaryOp("&&",
        UnaryOp("!",Id("y")),Id("z"))),
        BinaryOp(">",Id("x"),IntLiteral(3))),
        UnaryOp("!",
        BinaryOp("<",Id("y"),IntLiteral(2))))))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,374))

    def test_expression_10(self):
        input = """
        Function: main
        Parameter: x,y,z
        Body:
            If (x == y) Then
                x = ((a > 2) || (x >. 2e-3));
                a = (x != z);
            Else
                z = (x < 3) && (y > 4);
            EndIf.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("x"),[],None),
        VarDecl(Id("y"),[],None),
        VarDecl(Id("z"),[],None)],
        ([],
        [If([(BinaryOp("==",Id("x"),Id("y")),
        [],
        [Assign(Id("x"),
        BinaryOp("||",
        BinaryOp(">",Id("a"),IntLiteral(2)),
        BinaryOp(">.",Id("x"),FloatLiteral(0.002)))),
        Assign(Id("a"),
        BinaryOp("!=",Id("x"),Id("z")))])],
        ([],
        [Assign(Id("z"),
        BinaryOp("&&",
        BinaryOp("<",Id("x"),IntLiteral(3)),
        BinaryOp(">",Id("y"),IntLiteral(4))))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,375))

    def test_expression_11(self):
        input = """
        Function: main
        Parameter: a,b
        Body:
            a[3][b] = 10000 * b;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None)],
        ([],
        [Assign(ArrayCell(Id("a"),[IntLiteral(3),Id("b")]),
        BinaryOp("*",IntLiteral(10000),Id("b")))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,376))

    def test_expression_12(self):
        input = """
        Function: main
        Parameter: a,b
        Body:
            a[foo(2)] = a[2][3] + 10;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None)],
        ([],
        [Assign(ArrayCell(Id("a"),
        [CallExpr(Id("foo"),[IntLiteral(2)])]),
        BinaryOp("+",ArrayCell(Id("a"),[IntLiteral(2),IntLiteral(3)]),IntLiteral(10)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,377))

    def test_expression_13(self):
        input = """
        Function: main
        Parameter: a,b
        Body:
            a[3 + foo(2)] = a[b[2][3]] + 4;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None)],
        ([],
        [Assign(ArrayCell(Id("a"),
        [BinaryOp("+",IntLiteral(3),
        CallExpr(Id("foo"),[IntLiteral(2)]))]),
        BinaryOp("+",ArrayCell(Id("a"),
        [ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,378))

    def test_expression_14(self):
        input = """
        Function: main
        Parameter: a[10],b[10]
        Body:
            a[b[3 + foo(2)]] = a[b[2][3]] + 4;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[10],None),
        VarDecl(Id("b"),[10],None)],
        ([],
        [Assign(ArrayCell(Id("a"),
        [ArrayCell(Id("b"),
        [BinaryOp("+",IntLiteral(3),
        CallExpr(Id("foo"),[IntLiteral(2)]))])]),
        BinaryOp("+",ArrayCell(Id("a"),
        [ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,379))

    def test_expression_15(self):
        input = """
        Function: main
        Parameter: a,b,c
        Body:
            a[a[3 + foo(2)][b]][b[b]] = a[b[2][3]] + 4;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None),
        VarDecl(Id("c"),[],None)],
        ([],
        [Assign(ArrayCell(Id("a"),
        [ArrayCell(Id("a"),
        [BinaryOp("+",IntLiteral(3),
        CallExpr(Id("foo"),[IntLiteral(2)])),Id("b")]),
        ArrayCell(Id("b"),[Id("b")])]),
        BinaryOp("+",
        ArrayCell(Id("a"),
        [ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,380))

    def test_expression_16(self):
        input = """
        Function: main
        Parameter: a,b
        Body:
            a = foo(a,b);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None)],
        ([],
        [Assign(Id("a"),
        CallExpr(Id("foo"),
        [Id("a"),Id("b")]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,381))

    def test_expression_17(self):
        input = """
        Function: main
        Parameter: a,b
        Body:
            a = foo1(a) * foo2(b);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None)],
        ([],
        [Assign(Id("a"),
        BinaryOp("*",
        CallExpr(Id("foo1"),[Id("a")]),
        CallExpr(Id("foo2"),[Id("b")])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,382))

    def test_expression_18(self):
        input = """
        Function: main
        Parameter: a,b
        Body:
            foo1(foo2(foo3(foo4())));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None)],
        ([],
        [CallStmt(Id("foo1"),
        [CallExpr(Id("foo2"),
        [CallExpr(Id("foo3"),
        [CallExpr(Id("foo4"),[])])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,383))

    def test_expression_19(self):
        input = """
        Function: main
        Parameter: a,b,c
        Body:
            a = foo(foo(a),foo(a),foo(b));
            b = foo1(foo1(b),"foo1");
            c = foo2(foo2(c) + foo2(b));
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None),
        VarDecl(Id("c"),[],None)],
        ([],
        [Assign(Id("a"),
        CallExpr(Id("foo"),
        [CallExpr(Id("foo"),[Id("a")]),
        CallExpr(Id("foo"),[Id("a")]),
        CallExpr(Id("foo"),[Id("b")])])),
        Assign(Id("b"),CallExpr(Id("foo1"),
        [CallExpr(Id("foo1"),[Id("b")]),StringLiteral("foo1")])),
        Assign(Id("c"),CallExpr(Id("foo2"),
        [BinaryOp("+",CallExpr(Id("foo2"),[Id("c")]),
        CallExpr(Id("foo2"),[Id("b")]))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,384))

    def test_expression_20(self):
        input = """
        Function: main
        Parameter: a,b,c
        Body:
            If (foo(a[b][a])) Then
                change(foo(a[b][a]));
            EndIf.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None),
        VarDecl(Id("c"),[],None)],
        ([],
        [If([(CallExpr(Id("foo"),
        [ArrayCell(Id("a"),
        [Id("b"),Id("a")])]),
        [],
        [CallStmt(Id("change"),
        [CallExpr(Id("foo"),
        [ArrayCell(Id("a"),
        [Id("b"),Id("a")])])])])],([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,385))

    def test_random_case_1(self):
        input = """
        Var : a;
        Var : b[10][20];
        Var : x,y;
                    
        Function: program1
        Parameter: e,f
        Body:
            While ( e < f ) Do
                e = e + 1;
            EndWhile.
            Return e;
        EndBody.

        Function: main
        Body:
            While (f < e) Do
                f = f + 1;
            EndWhile.
            Return f;
        EndBody.
        """
        expect = str(Program(
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[10,20],None),
        VarDecl(Id("x"),[],None),
        VarDecl(Id("y"),[],None),
        FuncDecl(Id("program1"),
        [VarDecl(Id("e"),[],None),
        VarDecl(Id("f"),[],None)],
        ([],
        [While(BinaryOp("<",Id("e"),Id("f")),
        ([],
        [Assign(Id("e"),BinaryOp("+",Id("e"),IntLiteral(1)))])),
        Return(Id("e"))])),
        FuncDecl(Id("main"),
        [],
        ([],
        [While(BinaryOp("<",Id("f"),Id("e")),
        ([],
        [Assign(Id("f"),BinaryOp("+",Id("f"),IntLiteral(1)))])),
        Return(Id("f"))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,386))

    def test_random_case_2(self):
        input = """
        Var : a;
        Var : b[10][20];
        Var : x,y;
                    
        Function: program1
        Parameter: a, b
        Body:
            Return (a + b);
        EndBody.

        Function: main
        Body:
            print(program1(a,b[2][3]));
        EndBody.
        """
        expect = str(Program(
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[10,20],None),
        VarDecl(Id("x"),[],None),
        VarDecl(Id("y"),[],None),
        FuncDecl(Id("program1"),
        [VarDecl(Id("a"),[],None),
        VarDecl(Id("b"),[],None)],
        ([],
        [Return(BinaryOp("+",Id("a"),Id("b")))])),
        FuncDecl(Id("main"),
        [],
        ([],
        [CallStmt(Id("print"),
        [CallExpr(Id("program1"),
        [Id("a"),ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,387))

    def test_random_case_3(self):
        input = """ 
        Function: program1
        Parameter: e,f
        Body:
            Do
                e = e + f;
            While (True && (e < f*f));
        EndBody.

        Function: main
        Body:
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("program1"),
        [VarDecl(Id("e"),[],None),
        VarDecl(Id("f"),[],None)],
        ([],
        [Dowhile(
        ([],
        [Assign(Id("e"),
        BinaryOp("+",Id("e"),Id("f")))]),
        BinaryOp("&&",BooleanLiteral(True),
        BinaryOp("<",Id("e"),
        BinaryOp("*",Id("f"),Id("f")))))])),
        FuncDecl(Id("main"),[],([],[]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,388))

    def test_random_case_4(self):
        input = """          
        Function: main
        Body:
            Var : a1,b1,c1;
            If (a1 > b1) Then
                program1(a1,b1,c1);
            ElseIf (a1 > c1) Then
                program1(a1,c1,b1);
            ElseIf(b1 > c1) Then
                program1(b1,a1,c1);
            Else
                program1(c1,a1,b1);
            EndIf.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([VarDecl(Id("a1"),[],None),
        VarDecl(Id("b1"),[],None),
        VarDecl(Id("c1"),[],None)],
        [If([(BinaryOp(">",Id("a1"),Id("b1")),
        [],
        [CallStmt(Id("program1"),
        [Id("a1"),Id("b1"),Id("c1")])]),
        (BinaryOp(">",Id("a1"),Id("c1")),
        [],
        [CallStmt(Id("program1"),[Id("a1"),Id("c1"),Id("b1")])]),
        (BinaryOp(">",Id("b1"),Id("c1")),
        [],
        [CallStmt(Id("program1"),[Id("b1"),Id("a1"),Id("c1")])])],
        ([],[CallStmt(Id("program1"),[Id("c1"),Id("a1"),Id("b1")])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,389))

    def test_random_case_5(self):
        input = """
        Function: program1
        Parameter: e
        Body:
        EndBody.

        Function: main
        Body:
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("program1"),
        [VarDecl(Id("e"),[],None)],
        ([],
        [])),
        FuncDecl(Id("main"),
        [],
        ([],
        []))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,390))

    def test_random_case_6(self):
        input = """
        Function: program1
        Body:
        EndBody.

        Function: main
        Body:
            program1();
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("program1"),
        [],
        ([],
        [])),
        FuncDecl(Id("main"),
        [],
        ([],
        [CallStmt(Id("program1"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,391))

    def test_random_case_7(self):
        input = """
        Var : a;

        Function: program1
        Body:
        EndBody.

        Function: program2
        Body:
        EndBody.

        Function: main
        Body:
            a = program1(program2());
        EndBody.
        """
        expect = str(Program(
        [VarDecl(Id("a"),[],None),
        FuncDecl(Id("program1"),
        [],
        ([],
        [])),
        FuncDecl(Id("program2"),
        [],
        ([],
        [])),
        FuncDecl(Id("main"),
        [],
        ([],
        [Assign(Id("a"),
        CallExpr(Id("program1"),
        [CallExpr(Id("program2"),[])]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,392))

    def test_random_case_8(self):
        input = """
        Function: main
        Body:
            Do
                print(a);
                print(b);
                print(c);
                Continue;
            While(True);
            foo(a,b,c[10][20]);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("main"),
        [],
        ([],
        [Dowhile(
        ([],
        [CallStmt(Id("print"),[Id("a")]),
        CallStmt(Id("print"),[Id("b")]),
        CallStmt(Id("print"),[Id("c")]),
        Continue()]),
        BooleanLiteral(True)),
        CallStmt(Id("foo"),
        [Id("a"),Id("b"),
        ArrayCell(Id("c"),[IntLiteral(10),IntLiteral(20)])])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,393))

    def test_random_case_9(self):
        input = """
        Function: program1
        Parameter: a
        Body:
            Var: r = 10., v;
            v = (4. / 3.) *. 3.14 *. r *. r *. r;
            a = int_of_string (read ());
            b = float_of_int (a) +. 2.0;
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("program1"),
        [VarDecl(Id("a"),[],None)],
        ([VarDecl(Id("r"),[],FloatLiteral(10.0)),
        VarDecl(Id("v"),[],None)],
        [Assign(Id("v"),
        BinaryOp("*.",
        BinaryOp("*.",
        BinaryOp("*.",
        BinaryOp("*.",
        BinaryOp("/",FloatLiteral(4.0),FloatLiteral(3.0)),FloatLiteral(3.14)),Id("r")),Id("r")),Id("r"))),
        Assign(Id("a"),CallExpr(Id("int_of_string"),[CallExpr(Id("read"),[])])),
        Assign(Id("b"),BinaryOp("+.",CallExpr(Id("float_of_int"),[Id("a")]),FloatLiteral(2.0)))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,394))

    def test_random_case_10(self):
        input = """
        Function: foo1
        Parameter: a
        Body:
            If (foo2() == False) Then
                Return True;
            EndIf.
        EndBody.
                                                 
        Function: foo2
        Parameter: b
        Body:
            If (foo1() == True) Then
                Return False;
            EndIf.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("foo1"),
        [VarDecl(Id("a"),[],None)],
        ([],
        [If([(BinaryOp("==",
        CallExpr(Id("foo2"),
        []),
        BooleanLiteral(False)),
        [],
        [Return(BooleanLiteral(True))])],
        ([],[]))])),
        FuncDecl(Id("foo2"),
        [VarDecl(Id("b"),[],None)],
        ([],
        [If([(BinaryOp("==",
        CallExpr(Id("foo1"),[]),BooleanLiteral(True)),[],
        [Return(BooleanLiteral(False))])],([],[]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,395))

    def test_random_case_11(self):
        input = """
        Function: foo
        Parameter: a[5], b
        Body:
            Var: i = 0;
            a[3 + foo(2)] = a[b[2][3]] + 4;
            While (i < 5) Do
                a[i] = b +. 1.0;
                i = i + 1;
            EndWhile.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("foo"),
        [VarDecl(Id("a"),[5],None),
        VarDecl(Id("b"),[],None)],
        ([VarDecl(Id("i"),[],IntLiteral(0))],
        [Assign(
        ArrayCell(Id("a"),
        [BinaryOp("+",IntLiteral(3),
        CallExpr(Id("foo"),[IntLiteral(2)]))]),
        BinaryOp("+",
        ArrayCell(Id("a"),
        [ArrayCell(Id("b"),[IntLiteral(2),IntLiteral(3)])]),IntLiteral(4))),
        While(BinaryOp("<",Id("i"),IntLiteral(5)),
        ([],
        [Assign(ArrayCell(Id("a"),[Id("i")]),
        BinaryOp("+.",Id("b"),FloatLiteral(1.0))),
        Assign(Id("i"),BinaryOp("+",Id("i"),IntLiteral(1)))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,396))

    def test_random_case_12(self):
        input = """
        Function: program1
        Parameter: e,f,g
        Body:
            For (e = 1, e < f, e = e + g ) Do
                f = f + g;
            EndFor.
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("program1"),
        [VarDecl(Id("e"),[],None),
        VarDecl(Id("f"),[],None),
        VarDecl(Id("g"),[],None)],
        ([],
        [For(Id("e"),IntLiteral(1),
        BinaryOp("<",Id("e"),Id("f")),Id("e"),
        BinaryOp("+",Id("e"),Id("g")),
        ([],
        [Assign(Id("f"),
        BinaryOp("+",Id("f"),Id("g")))]))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,397))

    def test_random_case_13(self):
        input = """
        Function: program1
        Parameter: x
        Body:
            x();
            foo(2+x,4./y);
            goo();
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("program1"),
        [VarDecl(Id("x"),[],None)],
        ([],
        [CallStmt(Id("x"),
        []),
        CallStmt(Id("foo"),
        [BinaryOp("+",IntLiteral(2),Id("x")),
        BinaryOp("/",FloatLiteral(4.0),Id("y"))]),
        CallStmt(Id("goo"),[])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,398))

    def test_random_case_14(self):
        input = """
        Function: program1
        Parameter: x,y[3],z[4][5]
        Body:
            z = 5;
            test(x,y[1],z[2][2] + 5,"string",True);
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("program1"),
        [VarDecl(Id("x"),[],None),
        VarDecl(Id("y"),[3],None),
        VarDecl(Id("z"),[4,5],None)],
        ([],
        [Assign(Id("z"),IntLiteral(5)),
        CallStmt(Id("test"),[Id("x"),
        ArrayCell(Id("y"),[IntLiteral(1)]),
        BinaryOp("+",
        ArrayCell(Id("z"),[IntLiteral(2),IntLiteral(2)]),IntLiteral(5)),
        StringLiteral("string"),BooleanLiteral(True)])]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,399))

    def test_random_case_15(self):
        input = """
        Function: justforfun
        Parameter: a[10], b[10], c[10], d[10]
        Body:
        a[10] = b[10] + c[10];
        b[10] = a[10] + c[10];
        c[10] = b[10] + d[10];
        d[10] = a[10] + b[10];
        EndBody.
        """
        expect = str(Program(
        [FuncDecl(Id("justforfun"),
        [VarDecl(Id("a"),[10],None),
        VarDecl(Id("b"),[10],None),
        VarDecl(Id("c"),[10],None),
        VarDecl(Id("d"),[10],None)],
        ([],
        [Assign(
        ArrayCell(Id("a"),[IntLiteral(10)]),
        BinaryOp("+",
        ArrayCell(Id("b"),[IntLiteral(10)]),
        ArrayCell(Id("c"),[IntLiteral(10)]))),
        Assign(ArrayCell(Id("b"),[IntLiteral(10)]),
        BinaryOp("+",
        ArrayCell(Id("a"),[IntLiteral(10)]),
        ArrayCell(Id("c"),[IntLiteral(10)]))),
        Assign(
        ArrayCell(Id("c"),[IntLiteral(10)]),
        BinaryOp("+",
        ArrayCell(Id("b"),[IntLiteral(10)]),
        ArrayCell(Id("d"),[IntLiteral(10)]))),
        Assign(
        ArrayCell(Id("d"),[IntLiteral(10)]),
        BinaryOp("+",
        ArrayCell(Id("a"),[IntLiteral(10)]),
        ArrayCell(Id("b"),[IntLiteral(10)])))]))]))
        self.assertTrue(TestAST.checkASTGen(input,expect,400))


    
    
    

    
    