import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """
        Var: x = 3, y = 2, z;
        Function: main
        Body:
            Var: t;
            Var: a;
            t = a;
        EndBody.  
        """
        expect = str(Program([VarDecl(Id("x"),[],None)]))
        self.assertTrue(TestAST.checkASTGen(input,expect,300))

   