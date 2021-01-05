import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_identifier_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",101))
    
    def test_identifier_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("qwertyuiopasdfghjklzxcvbnm","qwertyuiopasdfghjklzxcvbnm,<EOF>",102))
    
    def test_identifier_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("qwertyuiopasdfghjklzxcvbnm1234567890","qwertyuiopasdfghjklzxcvbnm1234567890,<EOF>",103))
    
    def test_identifier_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("aaaaabbbb132132aaa123132BBBBBCCZZZ","aaaaabbbb132132aaa123132BBBBBCCZZZ,<EOF>",104))
    
    def test_identifier_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("a__1_____b___2_______c________3____d","a__1_____b___2_______c________3____d,<EOF>",105))
    
    def test_identifier_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("qwer_123_aaa_qwewqewq_jkrnfkjrwnciuwfalkdnasdiuwh124632tr832hr3829cmkl92","qwer_123_aaa_qwewqewq_jkrnfkjrwnciuwfalkdnasdiuwh124632tr832hr3829cmkl92,<EOF>",106))
   
    def test_identifier_7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("i9m9i9n9l9o9v9e9w9i9t9h9y9o9u9u9uu9u9u9u9uu9u9u9uu9","i9m9i9n9l9o9v9e9w9i9t9h9y9o9u9u9uu9u9u9u9uu9u9u9uu9,<EOF>",107))
    
    def test_identifier_8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc1232132sadassad79873512_________","abc1232132sadassad79873512_________,<EOF>",108))
    
    def test_identifier_9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("z123213ASDWQEHY____","z123213ASDWQEHY____,<EOF>",109))
   
    def test_identifier_10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("x_1223_ASDWRWQFWF","x_1223_ASDWRWQFWF,<EOF>",110))

    def test_all_keywords(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("Body Break Continue Do Else ElseIf EndBody EndIf EndFor EndWhile For Function If Parameter Return Then Var While True False","Body,Break,Continue,Do,Else,ElseIf,EndBody,EndIf,EndFor,EndWhile,For,Function,If,Parameter,Return,Then,Var,While,True,False,<EOF>",111))

    def test_operators_1(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("1+2=3","1,+,2,=,3,<EOF>",112))
   
    def test_operators_2(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("(1+2)*3/4 <= ((2+3*5-2)/9)%4","(,1,+,2,),*,3,/,4,<=,(,(,2,+,3,*,5,-,2,),/,9,),%,4,<EOF>",113))
  
    def test_operators_3(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("+ +. - -. * *. \\ / % ! && || =  == != < <. > >. <= <=. >= >=. =/=","+,+.,-,-.,*,*.,\\,/,%,!,&&,||,=,==,!=,<,<.,>,>.,<=,<=.,>=,>=.,=/=,<EOF>",114))
   
    def test_operators_4(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("(2*a+3*b<=5*x)||((8>=9-100)&&(3<9))","(,2,*,a,+,3,*,b,<=,5,*,x,),||,(,(,8,>=,9,-,100,),&&,(,3,<,9,),),<EOF>",115))
 
    def test_operators_5(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("2-3*a+5*x/y*abc == 5/9*7+3-4","2,-,3,*,a,+,5,*,x,/,y,*,abc,==,5,/,9,*,7,+,3,-,4,<EOF>",116))
   
    def test_operators_6(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("((-9 >=. -8) || (2 <= 3))&&(!(!(!(a && b) || c) && d) <=. e)","(,(,-,9,>=.,-,8,),||,(,2,<=,3,),),&&,(,!,(,!,(,!,(,a,&&,b,),||,c,),&&,d,),<=.,e,),<EOF>",117))
    
    def test_operators_7(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("(1234564 +878*231/51231 > 1231*89751) || ((True && False) || -999.999*a < -8.999b)","(,1234564,+,878,*,231,/,51231,>,1231,*,89751,),||,(,(,True,&&,False,),||,-,999.999,*,a,<,-,8.999,b,),<EOF>",118))
  
    def test_operators_8(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("s > b < c >= e <=. a/b + c - d * e && z +. l -. x *. f \\ s","s,>,b,<,c,>=,e,<=.,a,/,b,+,c,-,d,*,e,&&,z,+.,l,-.,x,*.,f,\\,s,<EOF>",119))
   
    def test_operators_9(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("z % a % b % c % d % e / b / c \\ e \\ x","z,%,a,%,b,%,c,%,d,%,e,/,b,/,c,\\,e,\\,x,<EOF>",120))
   
    def test_operators_10(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("!(ve && a * (ccc || False / (12 + 3 - 4 * 12 >=. -1.223)))","!,(,ve,&&,a,*,(,ccc,||,False,/,(,12,+,3,-,4,*,12,>=.,-,1.223,),),),<EOF>",121))
    
    def test_Separators_1(self):
        self.assertTrue(TestLexer.checkLexeme("[asdsad]","[,asdsad,],<EOF>",122))
    
    def test_Separators_2(self):
        self.assertTrue(TestLexer.checkLexeme("""[[(:.,;)]]""","[,[,(,:,.,,,;,),],],<EOF>",123))
    
    def test_Separators_3(self):
        self.assertTrue(TestLexer.checkLexeme("(1[+;2,=3)]","(,1,[,+,;,2,,,=,3,),],<EOF>",124))
    
    def test_Separators_4(self):
        self.assertTrue(TestLexer.checkLexeme("abc((123[asdsad))q,,weq.we;1231;];","abc,(,(,123,[,asdsad,),),q,,,,,weq,.,we,;,1231,;,],;,<EOF>",125))
    
    def test_Separators_5(self):
        self.assertTrue(TestLexer.checkLexeme("123fdf[[[asdsad]];asds;d,]][[qwewqr[","123,fdf,[,[,[,asdsad,],],;,asds,;,d,,,],],[,[,qwewqr,[,<EOF>",126))

    def test_integer_1(self):
        self.assertTrue(TestLexer.checkLexeme("123a123","123,a123,<EOF>",127))

    def test_integer_2(self):
        self.assertTrue(TestLexer.checkLexeme("123456a123456","123456,a123456,<EOF>",128))

    def test_integer_3(self):
        self.assertTrue(TestLexer.checkLexeme("123456789a123","123456789,a123,<EOF>",129))

    def test_integer_4(self):
        self.assertTrue(TestLexer.checkLexeme("1a2b3c4d5e6f7g8h9i","1,a2b3c4d5e6f7g8h9i,<EOF>",130))
    
    def test_integer_5(self):
        self.assertTrue(TestLexer.checkLexeme("1234567899876543210","1234567899876543210,<EOF>",131))
    
    def test_integer_6(self):
        self.assertTrue(TestLexer.checkLexeme("0xFF","0xFF,<EOF>",132))
    
    def test_integer_7(self):
        self.assertTrue(TestLexer.checkLexeme("0XABC","0XABC,<EOF>",133))
    
    def test_integer_8(self):
        self.assertTrue(TestLexer.checkLexeme("Var: z = 0x123ABC;","Var,:,z,=,0x123ABC,;,<EOF>",134))
    
    def test_integer_9(self):
        self.assertTrue(TestLexer.checkLexeme("b = 0x1A2B3C * 0X3D4E5F;","b,=,0x1A2B3C,*,0X3D4E5F,;,<EOF>",135))
    
    def test_integer_10(self):
        self.assertTrue(TestLexer.checkLexeme("0x0123456789ABCDEF 0XABCDEF0123456789 0x1A2B3C4D5E6F7890","0x0123456789ABCDEF,0XABCDEF0123456789,0x1A2B3C4D5E6F7890,<EOF>",136))
    
    def test_integer_11(self):
        self.assertTrue(TestLexer.checkLexeme("0o567","0o567,<EOF>",137))
    
    def test_integer_12(self):
        self.assertTrue(TestLexer.checkLexeme("0O77","0O77,<EOF>",138))
    
    def test_integer_13(self):
        self.assertTrue(TestLexer.checkLexeme("Var : z = 0o01234567, b = 0O1234567;","Var,:,z,=,0o01234567,,,b,=,0O1234567,;,<EOF>",139))
    
    def test_integer_14(self):
        self.assertTrue(TestLexer.checkLexeme("e = 0O76543210 + 0o76543210 * 0o1 / 0O2;","e,=,0O76543210,+,0o76543210,*,0o1,/,0O2,;,<EOF>",140))
    
    def test_integer_15(self):
        self.assertTrue(TestLexer.checkLexeme("((1320465789/0O6547132*0x75ADD)+0XAABF45454)/723453299-0o653127","(,(,1320465789,/,0O6547132,*,0x75ADD,),+,0XAABF45454,),/,723453299,-,0o653127,<EOF>",141))
    
    def test_float_1(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3","12.0e3,<EOF>",142))

    def test_float_2(self):
        self.assertTrue(TestLexer.checkLexeme("12e3","12e3,<EOF>",143))

    def test_float_3(self):
        self.assertTrue(TestLexer.checkLexeme("12.e5","12.e5,<EOF>",144))
    
    def test_float_4(self):
        self.assertTrue(TestLexer.checkLexeme("12.0e3","12.0e3,<EOF>",145))

    def test_float_5(self):
        self.assertTrue(TestLexer.checkLexeme("12000.","12000.,<EOF>",146))

    def test_float_6(self):
        self.assertTrue(TestLexer.checkLexeme("120000e-1","120000e-1,<EOF>",147))

    def test_float_7(self):
        self.assertTrue(TestLexer.checkLexeme("-5.0","-,5.0,<EOF>",148))

    def test_float_8(self):
        self.assertTrue(TestLexer.checkLexeme("-15.789","-,15.789,<EOF>",149))

    def test_float_9(self):
        self.assertTrue(TestLexer.checkLexeme("-684318.483186e549932102","-,684318.483186e549932102,<EOF>",150))

    def test_float_10(self):
        self.assertTrue(TestLexer.checkLexeme("89515463216E-68987203","89515463216E-68987203,<EOF>",151))

    def test_float_11(self):
        self.assertTrue(TestLexer.checkLexeme("54321e-846531","54321e-846531,<EOF>",152))

    def test_float_12(self):
        self.assertTrue(TestLexer.checkLexeme("33.e-1547","33.e-1547,<EOF>",153))

    def test_float_13(self):
        self.assertTrue(TestLexer.checkLexeme("-1.0e8765321897653213","-,1.0e8765321897653213,<EOF>",154))

    def test_float_14(self):
        self.assertTrue(TestLexer.checkLexeme("0.33E-3","0.33E-3,<EOF>",155))

    def test_float_15(self):
        self.assertTrue(TestLexer.checkLexeme("1.5e-97","1.5e-97,<EOF>",156))

    def test_boolean_1(self):
        self.assertTrue(TestLexer.checkLexeme("a=True","a,=,True,<EOF>",157))

    def test_boolean_2(self):
        self.assertTrue(TestLexer.checkLexeme("If(check = True)","If,(,check,=,True,),<EOF>",158))

    def test_boolean_3(self):
        self.assertTrue(TestLexer.checkLexeme("Return check = False;","Return,check,=,False,;,<EOF>",159))

    def test_boolean_4(self):
        self.assertTrue(TestLexer.checkLexeme("TrueFalseTrueFalseTrueFalse","True,False,True,False,True,False,<EOF>",160))

    def test_boolean_5(self):
        self.assertTrue(TestLexer.checkLexeme("If(check = False) Then a = True ; Return a ;","If,(,check,=,False,),Then,a,=,True,;,Return,a,;,<EOF>",161))

    def test_string_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",162))

    def test_string_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" "asdsadf$$2134" ""","""asdsadf$$2134,<EOF>""",163))

    def test_string_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" "aa123215e##b124fge" ""","aa123215e##b124fge,<EOF>",164))

    def test_string_4(self):
        self.assertTrue(TestLexer.checkLexeme(""" "hello \n hi \n howareyou \n imfine" """,'Error Token "',165))

    def test_string_5(self):
        self.assertTrue(TestLexer.checkLexeme(""" "This is a string containing tab \t" """, """This is a string containing tab 	,<EOF>""",166))

    def test_string_6(self):
        self.assertTrue(TestLexer.checkLexeme(""" "ab'"c\\n def"  ""","""ab'"c\\n def,<EOF>""",167))

    def test_string_7(self):
        self.assertTrue(TestLexer.checkLexeme("""  "He asked me: Where is John?"  ""","""He asked me: Where is John?,<EOF>""",168))

    def test_string_8(self):
        self.assertTrue(TestLexer.checkLexeme(""" "h21398xy2QWEXWQ HTHY1y89yr39 81h4D FGREGS813yx18u23 8912u38210ax" ""","""h21398xy2QWEXWQ HTHY1y89yr39 81h4D FGREGS813yx18u23 8912u38210ax,<EOF>""",169))

    def test_string_9(self):
        self.assertTrue(TestLexer.checkLexeme(""" "saidh\\n3hq\\nqwreeedsf4324213sad" ""","""saidh\\n3hq\\nqwreeedsf4324213sad,<EOF>""" ,170))

    def test_string_10(self):
        self.assertTrue(TestLexer.checkLexeme(""" "abc def  ""","""Unclosed String: abc def  """,171))

    def test_blockcomment_1(self):
        self.assertTrue(TestLexer.checkLexeme(""" **this is a comment**  ""","""<EOF>""",172))

    def test_blockcomment_2(self):
        self.assertTrue(TestLexer.checkLexeme(""" ** this an expression b = ((a+b=c+d/2*3 >= f)&&(True||False));**  ""","""<EOF>""",173))

    def test_blockcomment_3(self):
        self.assertTrue(TestLexer.checkLexeme(""" **hello !
                                                   *hiii !
                                                   *how are you?
                                                   *i'm fine, thank you. And you? 
                                                   *i'm fine**"""
                                                   ,"""<EOF>""",174))

    def test_blockcomment_4(self):
        self.assertTrue(TestLexer.checkLexeme("""****""","""<EOF>""",175))

    def test_blockcomment_5(self):
        self.assertTrue(TestLexer.checkLexeme("""** ** ** *** ** ** **""","""*,*,*,<EOF>""",176))

    def test_complex_string_tokens_1(self):
        self.assertTrue(TestLexer.checkLexeme("**comment**\n=!<>!_=>","=,!,<,>,!,Error Token _", 177))
    
    def test_complex_string_tokens_2(self):
        self.assertTrue(TestLexer.checkLexeme("indeE_,nti/fy;com<>plx+while+do","indeE_,,,nti,/,fy,;,com,<,>,plx,+,while,+,do,<EOF>", 178))

    def test_complex_string_tokens_3(self):
        self.assertTrue(TestLexer.checkLexeme("e16355156.51111ksBF + ----4p+ 25^4","e16355156,.,51111,ksBF,+,-,-,-,-,4,p,+,25,Error Token ^", 179))

    def test_complex_string_tokens_4(self):
        self.assertTrue(TestLexer.checkLexeme("123.2222e+123XTZ%supercomplex","123.2222e+123,Error Token X", 180))

    def test_complex_string_tokens_5(self):
        self.assertTrue(TestLexer.checkLexeme("123.2222e+123 * 13E-98715 / supervariable;","123.2222e+123,*,13E-98715,/,supervariable,;,<EOF>", 181))

    def test_complex_string_tokens_6(self):
        self.assertTrue(TestLexer.checkLexeme("** every think in here is comment! sure?","*,*,every,think,in,here,is,comment,!,sure,Error Token ?", 182))

    def test_complex_string_tokens_7(self):
        self.assertTrue(TestLexer.checkLexeme("** every think in here is comment! sure? yes!**","<EOF>", 183))

    def test_complex_string_tokens_8(self):
        self.assertTrue(TestLexer.checkLexeme(">-<! <- this * is * symbol * 3.14 **to be continue**",">,-,<,!,<,-,this,*,is,*,symbol,*,3.14,<EOF>", 184))

    def test_complex_string_tokens_9(self):
        self.assertTrue(TestLexer.checkLexeme("1.1244/40xABD*1.00000000e-325","1.1244,/,40xABD,*,1.00000000e-325,<EOF>", 185))
    
    def test_complex_string_tokens_10(self):
        self.assertTrue(TestLexer.checkLexeme("float sudo = 25632552.............e5511515;","float,sudo,=,25632552.,.,.,.,.,.,.,.,.,.,.,.,.,e5511515,;,<EOF>", 186))

    def test_vardecl_1(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a;
                                                 Var: b;
                                                 Var: c,e,d,f,g;""","""Var,:,a,;,Var,:,b,;,Var,:,c,,,e,,,d,,,f,,,g,;,<EOF>""",187))
    
    def test_vardecl_2(self):
        self.assertTrue(TestLexer.checkLexeme("""
                                                 Var: a[5];
                                                 Var: b[2][3];
                                                 """,
                                                 """Var,:,a,[,5,],;,Var,:,b,[,2,],[,3,],;,<EOF>""",188))

    def test_vardecl_3(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a[b][ex] = b[zz][e];""",
                                              """Var,:,a,[,b,],[,ex,],=,b,[,zz,],[,e,],;,<EOF>""",189))

    def test_vardecl_4(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a = 10e+599;
                                                 Var: b[1][2][3] = (True||(False &&(12 >= b)))""",
                                                 """Var,:,a,=,10e+599,;,Var,:,b,[,1,],[,2,],[,3,],=,(,True,||,(,False,&&,(,12,>=,b,),),),<EOF>""",190))

    def test_vardecl_5(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: a = -1000;Var: b = +1000; Var: toilakiet1711861;""",
                                              """Var,:,a,=,-,1000,;,Var,:,b,=,+,1000,;,Var,:,toilakiet1711861,;,<EOF>""",191))

    def test_funcdecl_1(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo
                                                 Parameter: a,b;
                                                 Body:
                                                 EndBody.""",
                                                 """Function,:,foo,Parameter,:,a,,,b,;,Body,:,EndBody,.,<EOF>""",192))

    def test_funcdecl_2(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo
                                                 Parameter: a,b;
                                                 Body:
                                                 a = 123;
                                                 b = 324;
                                                 c = a + b;
                                                 print(a,b,c);
                                                 EndBody.""",
                                                 """Function,:,foo,Parameter,:,a,,,b,;,Body,:,a,=,123,;,b,=,324,;,c,=,a,+,b,;,print,(,a,,,b,,,c,),;,EndBody,.,<EOF>""",193))

    def test_funcdecl_3(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo
                                                 Parameter: a,b,c[10][20];
                                                 Body:
                                                 a = 123;
                                                 b = 324;
                                                 c[2][3]= a + b;
                                                 For(i = 1; i < c[3][4] ; i = i + 1) Do
                                                 print(a);
                                                 print(b);
                                                 print(c);
                                                 EndFor.
                                                 EndBody.""",
                                                 """Function,:,foo,Parameter,:,a,,,b,,,c,[,10,],[,20,],;,Body,:,a,=,123,;,b,=,324,;,c,[,2,],[,3,],=,a,+,b,;,For,(,i,=,1,;,i,<,c,[,3,],[,4,],;,i,=,i,+,1,),Do,print,(,a,),;,print,(,b,),;,print,(,c,),;,EndFor,.,EndBody,.,<EOF>""",194))

    def test_funcdecl_4(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo1
                                                 Parameter: a;
                                                 Body:
                                                 EndBody.
                                                 
                                                 Function: foo2
                                                 Parameter: b;
                                                 Body:
                                                 EndBody.
                                                 
                                                 Function: foo3
                                                 Parameter: c;
                                                 Body:
                                                 EndBody.""",
                                                 """Function,:,foo1,Parameter,:,a,;,Body,:,EndBody,.,Function,:,foo2,Parameter,:,b,;,Body,:,EndBody,.,Function,:,foo3,Parameter,:,c,;,Body,:,EndBody,.,<EOF>""",195))

    def test_funcdecl_5(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo1
                                                 Parameter:;
                                                 Body:
                                                    If (foo2() == False)
                                                        Return True;
                                                    EndIf.
                                                 EndBody.
                                                 
                                                 Function: foo2
                                                 Parameter:;
                                                 Body:
                                                    If (foo1() == True)
                                                        Return False;
                                                    EndIf.
                                                 EndBody.""",
                                                 """Function,:,foo1,Parameter,:,;,Body,:,If,(,foo2,(,),==,False,),Return,True,;,EndIf,.,EndBody,.,Function,:,foo2,Parameter,:,;,Body,:,If,(,foo1,(,),==,True,),Return,False,;,EndIf,.,EndBody,.,<EOF>""",196))
    
    def test_Random_Lexer_1(self):
        self.assertTrue(TestLexer.checkLexeme("""Function: foo
                                                 Parameter: a[5], b;
                                                 Body:
                                                    Var: i = 0;
                                                    a[3 + foo(2)] = a[b[2][3]] + 4;
                                                        While (i < 5)
                                                            a[i] = b +. 1.0;
                                                            i = i + 1;
                                                        EndWhile.
                                                 EndBody.""",
                                                 """Function,:,foo,Parameter,:,a,[,5,],,,b,;,Body,:,Var,:,i,=,0,;,a,[,3,+,foo,(,2,),],=,a,[,b,[,2,],[,3,],],+,4,;,While,(,i,<,5,),a,[,i,],=,b,+.,1.0,;,i,=,i,+,1,;,EndWhile,.,EndBody,.,<EOF>""",197))

    def test_Random_Lexer_2(self):
        self.assertTrue(TestLexer.checkLexeme("""Var: x;
                                                 Function: fact
                                                 Parameter: n
                                                 Body:
                                                    If (n == 0)
                                                        Return 1;
                                                    Else
                                                        Return n * fact (n - 1);
                                                    EndIf.
                                                 EndBody.
                                                
                                                 Function: main
                                                 Body:
                                                    x = 10;
                                                    fact (x);
                                                 EndBody.""",
                                                 """Var,:,x,;,Function,:,fact,Parameter,:,n,Body,:,If,(,n,==,0,),Return,1,;,Else,Return,n,*,fact,(,n,-,1,),;,EndIf,.,EndBody,.,Function,:,main,Body,:,x,=,10,;,fact,(,x,),;,EndBody,.,<EOF>""",198))

    def test_Random_Lexer_3(self):
        self.assertTrue(TestLexer.checkLexeme("""For (i = 0, i < 10, i = i + 2) Do
                                                 writeln(i);
                                                 foo (2 + x, 4. /. y);
                                                 goo ();
                                                 EndFor.""",
                                                 """For,(,i,=,0,,,i,<,10,,,i,=,i,+,2,),Do,writeln,(,i,),;,foo,(,2,+,x,,,4.,/,.,y,),;,goo,(,),;,EndFor,.,<EOF>""",199))

    def test_Random_Lexer_4(self):
        self.assertTrue(TestLexer.checkLexeme("""If (bool_of_string ("True")) Then
                                                 Var: r = 10., v;
                                                 v = (4. / 3.) *. 3.14 *. r *. r *. r;
                                                 a = int_of_string (read ());
                                                 b = float_of_int (a) +. 2.0;
                                                 EndIf.""",
                                                 """If,(,bool_of_string,(,True,),),Then,Var,:,r,=,10.,,,v,;,v,=,(,4.,/,3.,),*.,3.14,*.,r,*.,r,*.,r,;,a,=,int_of_string,(,read,(,),),;,b,=,float_of_int,(,a,),+.,2.0,;,EndIf,.,<EOF>""",200))
