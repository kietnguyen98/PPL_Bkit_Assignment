grammar BKIT;

/*
Nguyen Han Manh Kiet
mssv : 1711861
*/

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    if tk == self.UNCLOSE_STRING:       
        result = super().emit();
        raise UncloseString(result.text);
    elif tk == self.ILLEGAL_ESCAPE:
        result = super().emit();
        raise IllegalEscape(result.text);
    elif tk == self.ERROR_CHAR:
        result = super().emit();
        raise ErrorToken(result.text); 
    else:
        return super().emit();
}

options{
	language=Python3;
}
//...............................................................................//
//.....................................Parser....................................//
//...............................................................................//

program : globalVardecl globalFuncdecl EOF ;

//variable declaration
globalVardecl : varDecl globalVardecl
              | varDecl
              |
              ;

varDecl : VAR COLON varList SEMI;

varList: var COMMA varList
       | var;

var: (basicVar | arrayVar)
   | (basicVar | arrayVar) EQUAL_ASSIGN initialValue;

initialValue : INTLIT | FLOATLIT | STRINGLIT | booleanLit;

arrayVar : ID multiDimension;

multiDimension: dimension multiDimension 
              | dimension;

dimension: LSB INTLIT RSB;

basicVar : ID;

//function declaration
globalFuncdecl : funcDecl globalFuncdecl
               | funcDecl
               |
               ;

funcDecl: mainFuncDecl | nonMainFuncDecl ;

mainFuncDecl: FUNCTION COLON 'main' (PARAMETER COLON varList)? BODY COLON globalVardecl statementList ENDBODY DOT;

nonMainFuncDecl: FUNCTION COLON funcName (PARAMETER COLON varList)? BODY COLON globalVardecl statementList ENDBODY DOT;

funcName: ID;

//Statements
statementList : statement statementList
              | statement 
              |
              ;

statement: assignStmt
         | ifStmt
         | forStmt
         | whileStmt
         | dowhileStmt
         | breakStmt
         | continueStmt
         | callStmt
         | returnStmt
         ;

assignStmt: variable EQUAL_ASSIGN expression SEMI;

variable : ID
         | indexExpression;

ifStmt: IF expression THEN globalVardecl statementList (ELSEIF expression THEN globalVardecl statementList)* (ELSE globalVardecl statementList)? ENDIF DOT;

forStmt: FOR LB ID EQUAL_ASSIGN expression COMMA expression COMMA ID EQUAL_ASSIGN expression RB DO globalVardecl statementList ENDFOR DOT;

whileStmt: WHILE expression DO globalVardecl statementList ENDWHILE DOT;

dowhileStmt: DO globalVardecl statementList WHILE expression SEMI;

breakStmt: BREAK SEMI;

continueStmt: CONTINUE SEMI;

callStmt: funcName LB argumentList RB SEMI;

returnStmt: RETURN expression? SEMI;

//Expression
expression: expression INT_EQUAL expression1
          | expression INT_NOT_EQUAL expression1
          | expression INT_LESS_THAN expression1
          | expression INT_MORE_THAN expression1
          | expression INT_LESS_OR_EQUAL expression1
          | expression INT_MORE_OR_EQUAL expression1
          | expression FLOAT_NOT_EQUAL expression1
          | expression FLOAT_LESS_THAN expression1
          | expression FLOAT_MORE_THAN expression1
          | expression FLOAT_LESS_OR_EQUAL expression1
          | expression FLOAT_MORE_OR_EQUAL expression1
          | expression1;

expression1: expression1 AND expression2
           | expression1 OR expression2
           | expression2;

expression2: expression2 INT_ADD expression3
           | expression2 INT_SUB expression3
           | expression2 FLOAT_ADD expression3
           | expression2 FLOAT_SUB expression3
           | expression3;

expression3: expression3 INT_MUL expression4
           | expression3 FLOAT_MUL expression4
           | expression3 INT_DIV expression4
           | expression3 FLOAT_DIV expression4
           | expression3 INT_MOD expression4
           | expression4 ;

expression4: NOT expression5
           | expression5; 

expression5: INT_SUB expression6
           | FLOAT_SUB expression6
           | expression6;

expression6: indexExpression
           | funccallExpression
           | LB expression RB
           | ID
           | INTLIT
           | FLOATLIT
           | booleanLit
           | STRINGLIT
           ;

booleanLit: TRUE | FALSE;

funccallExpression: funcName LB argumentList RB;

argumentList: expression manyArgument
            |;

manyArgument: COMMA expression manyArgument
            |;

indexExpression : ID indexOperator;

indexOperator : LSB expression RSB indexOperator
              | LSB expression RSB;

//...............................................................................//
//.....................................LEXER.....................................//
//...............................................................................//

//Comment
BLOCKCOMMENT : '**' .*? '**' -> skip;

//Keywords
BODY : 'Body';

BREAK : 'Break';

CONTINUE : 'Continue';

DO : 'Do';

ELSE : 'Else';

ELSEIF : 'ElseIf';

ENDBODY : 'EndBody';

ENDIF :'EndIf';

ENDFOR : 'EndFor';

ENDWHILE : 'EndWhile';

FOR : 'For';

FUNCTION : 'Function';

IF : 'If';

PARAMETER : 'Parameter';

RETURN : 'Return';

THEN : 'Then';

VAR: 'Var';

WHILE : 'While';

TRUE : 'True';

FALSE : 'False';

//Operators

INT_ADD : '+';

FLOAT_ADD: '+.';

INT_SUB : '-';

FLOAT_SUB : '-.';

INT_MUL : '*';

FLOAT_MUL : '*.';

INT_DIV : '\\';

FLOAT_DIV : '/';

INT_MOD : '%';

NOT : '!';

AND : '&&';

OR : '||';

EQUAL_ASSIGN: '=';

INT_EQUAL : '==';

INT_NOT_EQUAL : '!=';

INT_LESS_THAN : '<';

FLOAT_LESS_THAN : '<.';

INT_MORE_THAN : '>';

FLOAT_MORE_THAN : '>.';

INT_LESS_OR_EQUAL : '<=';

FLOAT_LESS_OR_EQUAL : '<=.';

INT_MORE_OR_EQUAL : '>=';

FLOAT_MORE_OR_EQUAL : '>=.';

FLOAT_NOT_EQUAL : '=/=';

//Separators

LB: '(' ;

RB: ')' ;

LSB: '[';

RSB: ']';

COLON: ':' ;

DOT : '.';

COMMA: ',';

SEMI: ';';

WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

//Identifiers

ID: [a-z][a-zA-Z0-9_]* ;

//Literals

INTLIT : (DEC | HEX | OC)+ ;

fragment DEC : [0-9];

fragment HEX : '0'[xX][0-9A-F]+;

fragment OC : '0'[oO][0-7]+;

FLOATLIT : INT_PART DEC_PART EXPO_PART
         | INT_PART DEC_PART
         | INT_PART EXPO_PART
         ;

fragment DIGITS : [0-9];

fragment INT_PART: DIGITS+;

fragment DEC_PART:  DOT DIGITS*;

fragment EXPO_PART: [eE] (INT_ADD|INT_SUB)? DIGITS+;

BOOLEANLIT : TRUE | FALSE;

fragment ESCAPE_SEQUENCES: '\\' [bftrn'\\] ;

STRINGLIT
	: '"' ( ESCAPE_SEQUENCES | ('\'"') | ~[\n\r'\\] )* '"'
		{
			self.text = self.text[1:len(self.text)-1]
		}
	;	

ERROR_CHAR
	: .
        { 
            raise ErrorToken(self.text[0:]) 
        }
    ;
	
UNCLOSE_STRING
    :  '"' (ESCAPE_SEQUENCES | ~["\r\n])* ('\n'| EOF)
        {
            if self.text[-1]=='\n':
                 raise UncloseString(self.text[1:-1])
            else:
                raise UncloseString(self.text[1:])
        }
    ;
	
ILLEGAL_ESCAPE
	: '"' (ESCAPE_SEQUENCES | ~["\\])* ([\\] ~[bfrnt'"\\]) 
        {
           raise IllegalEscape(self.text[1:])
        }	
    ;