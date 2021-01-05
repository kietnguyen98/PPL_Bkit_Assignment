#update: 6/06/2020
from abc import ABC
from dataclasses import dataclass
from AST import *

class Kind(ABC):
    pass

class Function(Kind):
    def __str__(self):
        return "Method"

class Parameter(Kind):
    def __str__(self):
        return "Parameter"

class Variable(Kind):
    def __str__(self):
        return "Variable"

class Identifier(Kind):
    def __str__(self):
        return "Identifier"

class StaticError(Exception):
    pass
@dataclass
class Undeclared(StaticError):
    k: Kind
    n: str  # name of identifier
    
    def __str__(self):
        return  "Undeclared "+ str(self.k) + ": " + self.n

@dataclass
class Redeclared(StaticError):
    k: Kind
    n: str # name of identifier 
    
    def __str__(self):
        return  "Redeclared "+ str(self.k) + ": " + self.n

@dataclass
class TypeMismatchInExpression(StaticError):
    exp: Expr

    def __str__(self):
        return  "Type Mismatch In Expression: "+ str(self.exp)

@dataclass
class TypeMismatchInStatement(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Type Mismatch In Statement: "+ str(self.stmt)

@dataclass
class TypeCannotBeInferred(StaticError):
    stmt: Stmt

    def __str__(self):
        return "Type Cannot Be Inferred: "+ str(self.stmt)




