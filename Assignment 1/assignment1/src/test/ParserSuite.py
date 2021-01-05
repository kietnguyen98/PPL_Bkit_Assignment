import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_global_vardecl_1(self):
        input = """Var: x;"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,201))

    def test_global_vardecl_2(self):
        input = """Var: x;
                   Var: a,b,c;
                   Var: a[100];
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,202))

    def test_global_vardecl_3(self):
        input = """Var: a[100];
                   Var: b[10][200], c[9999], e[];
                """
        expect = "Error on line 2 col 47: ]"
        self.assertTrue(TestParser.checkParser(input,expect,203))

    def test_global_vardecl_4(self):
        input = """Var: x = (a + b - c / d * 100) % e;
                   Var: e[5];
                   Var: decArray[987654321], hexArray[0x123456789][0XABCDEF], octArray[0o1234567][0O5731321];
                """
        expect = "Error on line 1 col 9: ("
        self.assertTrue(TestParser.checkParser(input,expect,204))

    def test_global_vardecl_5(self):
        input = """ Var: a = 5;
                    Var: b[5][1][3][4][5];
                    Var: c, d = 6, e;
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,205))

    def test_funcdecl_1(self):
        input = """ Function: foo
                        Parameter: a
                        Body:
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,206))

    def test_funcdecl_2(self):
        input = """ Function: fact
                        Parameter:
                        Body:
                        If (n == 0) Then
                            Return 1;
                        Else
                            Return n * fact (n - 1);
                            EndIf.
                        EndBody.
                """
        expect = "Error on line 3 col 24: Body"
        self.assertTrue(TestParser.checkParser(input,expect,207))

    def test_funcdecl_3(self):
        input = """ Function: justforfun1
                        Parameter: n[1][2][3], abc
                        Body:
                        n[1][2][3] = abc * abc;
                        EndBody.
                    
                    Function: justforfun2
                        Parameter: n[3][4][5], fhg
                        Body:
                        n[3][4][5] = fhg * fhg;
                        EndBody.
                    
                    Function: justforfun3
                        Parameter: b[3][4],a1,b2,e3
                        Body:
                        b[3][1] = a1;
                        b[3][2] = b2;
                        b[3][3] = e3;
                        EndBody.
                    
                    Function: justforfun4
                        Parameter: a,b,c,e,d,f
                        Body:
                        a = b*c*e*d*f;
                        EndBody.
                    
                    Function: justforfun5
                        Parameter: a[10], b[10], c[10], d[10]
                        Body:
                        a[10] = b[10] + c[10];
                        b[10] = a[10] + c[10];
                        c[10] = b[10] + d[10];
                        d[10] = a[10] + b[10];
                        EndBody.         
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,208))

    def test_funcdecl_4(self):
        input = """ Function: main
                        Body:
                            For (i = 0, i < 10, i = i + 2) Do
                                writeln(i);
                            EndFor.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,209))

    def test_funcdecl_5(self):
        input = """  Var: x;

                    Function: fact
                        Parameter: n
                        Body:
                        If (n == 0) Then
                            Return 1;
                        Else
                            Return n * fact (n - 1);
                            EndIf.
                        EndBody.

                    Function: main
                        Body:
                            x = 10;
                            fact(x);
                        EndBody.
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,210))

    def test_vardecl_statement_1(self):
        input = """ Function: main
                        Body:
                        Var: r = 10., v;
                        v = (4. / 3.) *. 3.14 *. r *. r *. r;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,211))

    def test_vardecl_statement_2(self):
        input = """ Function: main
                        Body:
                        Var: a[10][50], string = "boom", bool = False;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,212))

    def test_vardecl_statement_3(self):
        input = """ Function: main
                        Body:
                        Var: a[2][3][4];
                        Var: string = "hello mice fence";
                        Var: checker = True || False;
                        EndBody.
                    """
        expect = "Error on line 5 col 44: ||"
        self.assertTrue(TestParser.checkParser(input,expect,213))

    def test_vardecl_statement_4(self):
        input = """ Function: main
                        Body:
                        Var: a = 10.0e-1000;
                        Var: d;
                        Var: f = 0x12347; 
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,214))

    def test_vardecl_statement_5(self):
        input = """ Function: main
                        Body:
                        Var: var = "var";
                        Var: If = 10000;
                        EndBody.
                    """
        expect = "Error on line 4 col 29: If"
        self.assertTrue(TestParser.checkParser(input,expect,215))

    def test_assign_statement_1(self):
        input = """ Function: main
                        Body:
                        Var: a;
                        a = 1000000000;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,216))

    def test_assign_statement_2(self):
        input = """ Function: main
                        Body:
                        Var: a, b, c;
                        a = False;
                        b = True;
                        c = a || b;
                        a = (!(b && c)||!(a && c)||!(a&&b)); 
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,217))

    def test_assign_statement_3(self):
        input = """ Function: main
                        Body:
                        Var: a[5][5][9], b = 1.55, c = 10;
                        a[1][2][3] = b * c;
                        a[2][3][4] = b / c;
                        a[3][4][5] = ((b + c) - (b*c))/(b*5 - c *. -8.e15 / (a[1][1][1] + b + c));
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,218))

    def test_assign_statement_4(self):
        input = """ Function: main
                        Body:
                        Var: a,b,c;
                        a = "hello my name is kiet";
                        b = "this is my testcase";
                        c = a + b;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,219))

    def test_assign_statement_5(self):
        input = """ Function: main
                        Body:
                        Var: a, b;
                        a = (a = b);
                        EndBody.
                    """
        expect = "Error on line 4 col 31: ="
        self.assertTrue(TestParser.checkParser(input,expect,220))
    
    def test_if_statement_1(self):
        input = """ Function: testIfStatement
                        Parameter: x
                        Body:
                            If(x == True) Then
                                x = False;
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,221))

    def test_if_statement_2(self):
        input = """ Function: testIfStatement
                        Parameter: x, a, b, c
                        Body:
                            If(x == ((False||True) && (a > b + c))) Then
                                a = b - c;
                            Else
                                a = b + c;
                                x = True;
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,222))

    def test_if_statement_3(self):
        input = """ Function: testIfStatement
                        Parameter: a, b, c, d
                        Body:
                            If (a == True) Then a = False;
                            ElseIf (b == True) Then b = False;
                            ElseIf (c == True) Then c = False;
                            Else d = False;
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,223))

    def test_if_statement_4(self):
        input = """ Function: testIfStatement
                        Parameter: x, y, z
                        Body:
                            If(x == True) Then 
                                If(y == False) Then
                                    If(z == False) Then
                                        x = True;
                                    Else
                                        x = False;
                                    EndIf.
                                Else
                                    y = False;
                                EndIf.
                            ElseIf((x || y || z ) == True) Then
                                x = False;
                                y = False;
                                z = False;
                            Else
                                x = True;
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_if_statement_5(self):
        input = """ Function: testIfStatement
                        Parameter: x, y, z
                        Body:
                            If(x == True) Then 
                                If(y == False) Then
                                    If(z == False) Then
                                    Else
                                    EndIf.
                                Else
                                EndIf.
                            ElseIf() Then
                                x = False;
                                y = False;
                                z = False;
                            Else
                                x = True;
                            EndIf.
                        EndBody.
                    """
        expect = "Error on line 11 col 35: )"
        self.assertTrue(TestParser.checkParser(input,expect,225))

    def test_For_statement_1(self):
        input = """ Function: testForStatement
                        Parameter: x
                        Body:
                            For (i = 1, i <= x*x*x, i = i + x ) Do
                                writeln(i);
                            EndFor.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,226))

    def test_For_statement_2(self):
        input = """ Function: testForStatement
                        Parameter: x
                        Body:
                            For (i = x, i <= x*x*x + x*x - x, i = i * x ) Do
                                writeln(i);
                            EndFor.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,227))

    def test_For_statement_3(self):
        input = """ Function: testForStatement
                        Parameter: x
                        Body:
                            For (i, i, i = i + 1 ) Do
                                writeln(i);
                            EndFor.
                        EndBody.
                    """
        expect = "Error on line 4 col 34: ,"
        self.assertTrue(TestParser.checkParser(input,expect,228))

    def test_For_statement_4(self):
        input = """ Function: testForStatement
                        Parameter: x
                        Body:
                            For (i = 1, i < x*x , i++ ) Do
                                writeln(i);
                            EndFor.
                        EndBody.
                    """
        expect = "Error on line 4 col 51: +"
        self.assertTrue(TestParser.checkParser(input,expect,229))

    def test_For_statement_5(self):
        input = """ Function: testForStatement
                        Parameter: x, array[10][10][10][10]
                        Body:
                            For (i = 1, i < x*x , i = i + 1 ) Do
                                For( j = 1, j < x*x , j = j + 1) Do
                                    For( k = 1, k < x*x , k = k + 1 ) Do
                                        For( l = 1 , l < x*x , l = l + 1) Do
                                            writeln(array[i][j][k][l]);
                                            l = l + 1;
                                            k = k + 1;
                                            j = j + 1;
                                            i = i + 1;
                                        EndFor.
                                    EndFor.
                                EndFor.
                            EndFor.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,230))

    def test_While_statement_1(self):
        input = """ Function: testWhileStatement
                        Parameter: x
                        Body:
                            While(1) Do
                            EndWhile.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,231))

    def test_While_statement_2(self):
        input = """ Function: testWhileStatement
                        Parameter: x
                        Body:
                            While(!x) Do
                                x = True;
                            EndWhile.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,232))

    def test_While_statement_3(self):
        input = """ Function: testWhileStatement
                        Parameter: x , a , b , c
                        Body:
                            While(!x) Do
                                x = True;
                                a = b + c;
                                b = a + c;
                                c = a + b;
                            EndWhile.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,233))

    def test_While_statement_4(self):
        input = """ Function: testWhileStatement
                        Parameter: x,a,b,c,d
                        Body:
                            While(x > a) Do
                                While(x > b) Do
                                    While(x > c) Do
                                        While(x > d) Do
                                            x = x - 1;
                                        EndWhile.
                                        x = x - 1;
                                    EndWhile.
                                    x = x - 1;
                                EndWhile.
                                x = x - 1;
                            EndWhile.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,234))

    def test_While_statement_5  (self):
        input = """ Function: testWhileStatement
                        Parameter: x
                        Body:
                            While((x > a) && (x < b)) Do
                                While((x >= b) || (x >= a)) Do
                                    While((x > c * b) && (x < b*b)) Do
                                        While(x > d) Do
                                            x = x - 1;
                                            d = d + 1;
                                        EndWhile.
                                        x = x - 1;
                                        c = 2 * c;
                                    EndWhile.
                                    x = x - 1;
                                    b = 3 * b;
                                EndWhile.
                                x = x - 1;
                                a = a + 1;
                                While( !False ) Do
                                    a = a * 1;
                                EndWhile.
                            EndWhile.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,235))


    def test_DoWhile_statement_1(self):
        input = """ Function: testDowhileStatement
                        Parameter: x
                        Body:
                            Do
                                x = x + 1;
                                writeln(x);
                            While(x < 100);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_DoWhile_statement_2(self):
        input = """ Function: testDowhilestatement
                        Parameter: x,a,b
                        Body:
                            Do
                                x = a + b;
                                writeln(x);
                            While(True || False || True || (a > b));
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,237))

    def test_DoWhile_statement_3(self):
        input = """ Function: testDoWhileStatement
                        Parameter: x,a,b[10][10]
                        Body:
                            Do
                                x = x + 1;
                                Do
                                    a = a + 2;
                                    Do
                                        b[10][10] = b[1][1] * b[2][2] * b[3][3] * b[4][4] * b[5][5]; 
                                    While(b[10][10] <= b[9][9] - b[8][8] - b[7][7] - b[6][6]);
                                While( a < 50);
                            While(x < 100);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,238))

    def test_DoWhile_statement_4(self):
        input = """ Function: testDoWhileStatement
                        Parameter: x
                        Body:
                            Do
                            While();
                        EndBody.
                    """
        expect = "Error on line 5 col 34: )"
        self.assertTrue(TestParser.checkParser(input,expect,239))

    def test_DoWhile_statement_5(self):
        input = """ Function: testDoWhileStatement
                        Parameter: x
                        Body:
                            Do
                                Do
                                    Do
                                    While(1);
                                While(2);
                                    Do
                                        Do
                                        While(3);
                                    While(4);
                                Do
                                    Do
                                        Do
                                        While(5);
                                    While(6);
                                While(7);
                                    Do
                                        Do
                                        While(a);
                                    While(b);  
                                Do
                                    Do 
                                        Do
                                        While(c);
                                    While(True);
                                While(False);
                            While(12E-789);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,240))

    def test_Break_statement_1(self):
        input = """ Break;
                    """
        expect = "Error on line 1 col 1: Break"
        self.assertTrue(TestParser.checkParser(input,expect,241))

    def test_Break_statement_2(self):
        input = """ Function: testBreakStatement
                        Parameter: x
                        Body:
                            Break;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,242))

    def test_Break_statement_3(self):
        input = """ Function: testBreakStatement
                        Parameter: x
                        Body:
                            For(i = 1, i <= 50, i = i + 1) Do
                                Break;
                            EndFor.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,243))

    def test_Break_statement_4(self):
        input = """ Function: testBreakStatement
                        Parameter: x
                        Body:
                            Do  
                                Break;
                            While(True);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,244))

    def test_Break_statement_5(self):
        input = """ Function: testBreakStatement
                        Parameter: x
                        Body:
                            Do
                                Do
                                    Do
                                        Do
                                            Break;
                                        While(2);
                                        Break;
                                    While(b);
                                    Break;
                                While(a);
                                Break;
                            While(1);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,245))

    def test_Continue_statement_1(self):
        input = """ Continue;
                    """
        expect = "Error on line 1 col 1: Continue"
        self.assertTrue(TestParser.checkParser(input,expect,246))

    def test_Continue_statement_2(self):
        input = """ Function: testContinueStatement
                        Parameter: x
                        Body:
                            Continue;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_Continue_statement_3(self):
        input = """ Function: testContinueStatement
                        Parameter: x
                        Body:
                            For(i = 1, i <= 50, i = i + 1) Do
                                Continue;
                            EndFor.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,248))

    def test_Continue_statement_4(self):
        input = """ Function: testContinueStatement
                        Parameter: x
                        Body:
                            Do  
                                Continue;
                            While(True);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,249))

    def test_Continue_statement_5(self):
        input = """ Function: testContinueStatement
                        Parameter: x
                        Body:
                            Do
                                Do
                                    Do
                                        Do
                                            Continue;
                                        While(2);
                                        Continue;
                                    While(b);
                                    Continue;
                                While(a);
                                Continue;
                            While(1);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,250))

    def test_Call_statement_1(self):
        input = """ test(a,b,c);
                    """
        expect = "Error on line 1 col 1: test"
        self.assertTrue(TestParser.checkParser(input,expect,251))

    def test_Call_statement_2(self):
        input = """ Function: testCallStatement
                        Parameter: x,y,z
                        Body:
                            test(x,y,z);
                        EndBody.
                        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,252))

    def test_Call_statement_3(self):
        input = """ Function: testCallStatement
                        Parameter: x,y[3],z[4][5]
                        Body:
                            z = 5;
                            test(x,y[1],z[2][2] + 5,"string",True);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,253))

    def test_Call_statement_4(self):
        input = """ Function: testCallStatement
                        Parameter: x,y,z
                        Body:
                            If(x > y) Then
                                sub(x,1);
                            Else
                                add(x,2);
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,254))

    def test_Call_statement_5(self):
        input = """ Function: testCallStatement
                        Parameter: x
                        Body:
                            x();
                            foo(2+x,4./y);
                            goo();
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,255))

    def test_Return_statement_1(self):
        input = """ Return;
                    """
        expect = "Error on line 1 col 1: Return"
        self.assertTrue(TestParser.checkParser(input,expect,256))

    def test_Return_statement_2(self):
        input = """ Function: testReturnStatement
                        Parameter: x
                        Body:
                            Return;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,257))

    def test_Return_statement_3(self):
        input = """ Function: testReturnStatement
                        Parameter: x
                        Body:
                            Return x;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,258))

    def test_Return_statement_4(self):
        input = """ Function: testReturnStatement
                        Parameter: x,y
                        Body:
                            If(x > y) Then
                                Return x;
                            Else
                                Return y
                            EndIf.
                        EndBody.
                    """
        expect = "Error on line 8 col 28: EndIf"
        self.assertTrue(TestParser.checkParser(input,expect,259))

    def test_Return_statement_5(self):
        input = """ Function: testReturnStatement
                        Parameter: x,y
                        Body:
                            Do  
                                Return foo(x,y);
                            While(True);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,260))

    def test_arithmetic_expression_1(self):
        input = """ Function: testarithmeticexpression
                        Parameter: x,y
                        Body:
                            x = x - x + y / y;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,261))

    def test_arithmetic_expression_2(self):
        input = """ Function: testarithmeticexpression
                        Parameter: x,y
                        Body:
                            x = x - x + y / y;
                            y = ( y \\ y * x - x ) % (x);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,262))

    def test_arithmetic_expression_3(self):
        input = """ Function: testarithmeticexpression
                        Parameter: x,y,z
                        Body:
                            x = 0x12A;
                            y = -3.5e-10;
                            z = 0o72;
                            x = y * . y / ( y -. z );
                            z = z * x;
                        EndBody.
                    """
        expect = "Error on line 7 col 36: ."
        self.assertTrue(TestParser.checkParser(input,expect,263))

    def test_arithmetic_expression_4(self):
        input = """ Function: testarithmeticexpression
                        Parameter: x,y,z,array[2][3]
                        Body:
                            x = 0x12A;
                            y = -3.5e-10;
                            z = 0o72;
                            array[1][1] = y *. y * array[2][2] / ( y -. z );
                            z = array[1][3] * x;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,264))
        
    def test_arithmetic_expression_5(self):
        input = """ Function: testarithmeticexpression
                        Parameter: x,y,ketqua
                        Body:
                            x = 0x12A;
                            y = -3.5e-10;
                            ketqua = (((((((((x - y) -. x) + y) +. x) * y) *. x) \\ y) / y) % (x));
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,265))

    def test_boolean_expression_1(self):
        input = """ Function: testbooleanexpression
                        Parameter: x,y,z
                        Body:
                            x = !(True);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,266))

    def test_boolean_expression_2(self):
        input = """ Function: testbooleanexpression
                        Parameter: x,y,z
                        Body:
                            x = !(True || False);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,267))

    def test_boolean_expression_3(self):
        input = """ Function: testbooleanexpression
                        Parameter: x,y,z
                        Body:
                            x = ( !(True) && False && ( y > z ));
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,268))

    def test_boolean_expression_4(self):
        input = """ Function: testbooleanexpression
                        Parameter: x,y,z
                        Body:
                            x = (!(True)) || False;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,269))

    def test_boolean_expression_5(self):
        input = """ Function: testbooleanexpression
                        Parameter: x,y,z
                        Body:
                            x = !(!(!(y) && z) || (x > 3) !(y < 2));
                        EndBody.
                    """
        expect = "Error on line 4 col 58: !"
        self.assertTrue(TestParser.checkParser(input,expect,270))

    def test_relational_expression_1(self):
        input = """ Function: testrelationalexpression
                        Parameter: x,y,z
                        Body:
                            If (x == y) Then
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,271))

    def test_relational_expression_2(self):
        input = """ Function: testrelationalexpression
                        Parameter: x,y,z
                        Body:
                            If (x == y) Then
                            EndIf.
                            a = (x != z);
                            z = (x < 3) && (y > 4);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,272))

    def test_relational_expression_3(self):
        input = """ Function: testrelationalexpression
                        Parameter: x,y,z
                        Body:
                            If(x =/= (y && True)) Then
                            EndIf. 
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,273))

    def test_relational_expression_4(self):
        input = """ Function: testrelationalexpression
                        Parameter: x,y,z
                        Body:
                            z = ((x <. y) && (x >. y)) || ((x <=. y) && (x >=. y)); 
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,274))

    def test_relational_expression_5(self):
        input = """ Function: testrelationalexpression
                        Parameter: x,y,z
                        Body:
                            If (x == y) Then
                                x = ((a > 2) || (x >. 2e-35));
                            EndIf.
                            a = (x != z);
                            z = (x < 3) && (y > 4);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,275))
    
    def test_index_expression_1(self):
        input = """ Function: testindexexpression
                        Parameter: a,b
                        Body:
                            a[3 + foo(2)] = a[b[2][3]] + 4;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,276))

    def test_index_expression_2(self):
        input = """ Function: testindexexpression
                        Parameter: a,b
                        Body:
                            a[[3 + foo(2)]] = a[b[2][3]] + 4;
                        EndBody.
                    """
        expect = "Error on line 4 col 30: ["
        self.assertTrue(TestParser.checkParser(input,expect,277))

    def test_index_expression_3(self):
        input = """ Function: testindexexpression
                        Parameter: a,b,c
                        Body:
                            a[a[3 + foo(2)][b]][b[b]] = a[b[2][3]] + 4;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,278))

    def test_index_expression_4(self):
        input = """ Function: testindexexpression
                        Parameter: a,b,c
                        Body:
                            a[a[3 + foo(2)][b]][b[b[a][a]]] = a[b[2][b[foo(2)][12E-9]*3]] + 4;
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,279))

    def test_index_expression_5(self):
        input = """ Function: testindexexpression
                        Parameter: a,b,c
                        Body:
                            a[a[3 + foo(2)][b][0xABDCD][0O766666]][b[c][b[a][a]]] = a[b[2][b[foo(2)][12E-9]*3]] + a[b[c[4]]*c[print(a,b,c)]];
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,280))

    def test_funcall_expression_1(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b
                        Body:
                            a = foo(a,b);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,281))

    def test_funcall_expression_2(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b
                        Body:
                            a = foo1(a) * foo2(b);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,282))

    def test_funcall_expression_3(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b
                        Body:
                            foo4(a) = foo1(foo2(foo3(b)));
                        EndBody.
                    """
        expect = "Error on line 4 col 36: ="
        self.assertTrue(TestParser.checkParser(input,expect,283))

    def test_funcall_expression_4(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b
                        Body:
                            foo1(foo2(foo3(foo4())));
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,284))

    def test_funcall_expression_5(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b,c
                        Body:
                            If (foo(a[b][a])) Then
                                change(foo(a[b][a]));
                            EndIf.
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,285))

    def test_funcall_expression_6(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b,c
                        Body:
                            foo(2.34,"string",-9.2e11);
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,286))

    def test_funcall_expression_7(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b,c
                        Body:
                            a = foo(foo(a),foo(a),foo(b));
                            b = foo1(foo1(b),"foo1");
                            c = foo2(foo2(c) + foo2(b));
                        EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,287))

    def test_funcall_expression_8(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b,c
                        Body:
                            foo;
                        EndBody.
                    """
        expect = "Error on line 4 col 31: ;"
        self.assertTrue(TestParser.checkParser(input,expect,288))
    def test_funcall_expression_9(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b,c
                        Body:
                            foo1(((((((())))))));
                        EndBody.
                    """
        expect = "Error on line 4 col 40: )"
        self.assertTrue(TestParser.checkParser(input,expect,289))

    def test_funcall_expression_10(self):
        input = """ Function: testfuncallexpression
                        Parameter: a,b,c
                        Body:
                            foo2((a(b(b(())))));
                        EndBody.
                    """
        expect = "Error on line 4 col 41: )"
        self.assertTrue(TestParser.checkParser(input,expect,290))

    def test_simple_program_1(self):
        input = """ Var : a;
                    Var : b[10][20];
                    Var : x,y;
                    
                    Function: program1
                    Parameter: e
                    Body:
                    EndBody.

                    Function: main
                    Body:
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,291))

    def test_simple_program_2(self):
        input = """ Var : a;
                    Var : b[10][20];
                    Var : x,y;
                    
                    Function: program1
                    Parameter: e,f,g
                    Body:
                        For (e = 1, e < f, e = e + g ) Do
                            f = f + g;
                        EndFor.
                    EndBody.

                    Function: main
                    Body:
                        program1(a);
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,292))

    def test_simple_program_3(self):
        input = """ Var : a;
                    Var : b[10][20];
                    Var : x,y;
                    
                    Function: program1
                    Parameter: e,f,g
                    Body:
                        While((a < 100)&&(x + y < f)) Do
                            If(b[1][1] == "string") Then
                                Return a;
                            EndIf.
                            x = x + 1;
                            y = y + 1;
                            a = a + 1;
                        EndWhile.
                    EndBody.

                    Function: main
                    Body:
                        Var : a1,b1,c1;
                        program1(a1,b1,c1);
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,293))

    def test_simple_program_4(self):
        input = """ Var : a;
                    Var : b[10][20];
                    Var : x,y;

                    Function: program2
                    Parameter: array[100][100][100]
                    Body:
                        For(i = 1, i < 100, i = i + 1) Do
                            For(j = 1, j < 100, j = j + 1) Do
                                For(k = 1, k < 100, k = k + 1) Do
                                    array[i][j][k] = (120 * 2e-55 \\ c) % a; 
                                EndFor.                                
                            EndFor.
                        EndFor.
                    EndBody.

                    Function: main
                    Body:
                        Var : a[100][100][100];
                        While(i < 100) Do
                            writeln(program2(a[100][100][100]));
                            i = i + 1;
                        EndWhile.
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,294))

    def test_simple_program_5(self):
        input = """ Function: foo
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,295))

    def test_simple_program_6(self):
        input = """ Function: foo1
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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,296))

    def test_simple_program_7(self):
        input = """ Function: foo
                    Parameter: a,b,c[10][20]
                    Body:
                        a = 123;
                        b = 324;
                        c[2][3]= a + b;
                        For(i = 1 , i < c[3][4] , i = i + 1) Do
                            If(!False) Then
                                print(a);
                                print(b);
                                print(c);
                            EndIf.
                            Break;
                        EndFor.
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,297))

    def test_simple_program_8(self):
        input = """ Var : a;
                    Var : b[10][20];
                    Var : x,y;
                    
                    Function: program1
                    Parameter: e
                    Body:
                        If (bool_of_string ("True")) Then
                            Var: r = 10., v;
                            v = (4. / 3.) *. 3.14 *. r *. r *. r;
                            a = int_of_string (read ());
                            b = float_of_int (a) +. 2.0;
                        EndIf.
                        Return a*b;
                    EndBody.

                    Function: main
                    Body:
                        Var : f,e;
                        Var : b;
                        b = program1(f);
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,298))

    def test_simple_program_9(self):
        input = """ Function: foo
                    Parameter: a,b,c[10][20]
                    Body:
                        a = 123;
                        b = 324;
                        c[2][3]= a + b;
                        For(i = 1 , i < c[3][4] , i = i + 1) Do
                            If(!False) Then
                                Do
                                    print(a);
                                    print(b);
                                    print(c);
                                    Continue;
                                While(True);
                                foo(a,b,c[10][20]);
                            EndIf.
                            Break;
                        EndFor.
                    EndBody.
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,299))

    def test_simple_program_10(self):
        input = """ Var : a;
                    Var : b[10][20];
                    Var : x,y;
                    
                    Function: program1
                    Parameter: e,f,g
                    Body:
                        While((a < 100)&&(x + y < f)) Do
                            If(b[1][1] == "string") Then
                                Return a;
                            EndIf.
                            For(i = 0, i < 200, i = i * i) Do
                                i = i*1.0e-9 / 12.2 * 0xABC - 0.00001;
                                i = i + 0o7541;
                                program1(i,"hello",False);
                                Break;
                            EndFor.
                        EndWhile.
                        Return program1("hello", i , True);
                    EndBody.

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
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,300))








        
    
    
    
    
    
    






