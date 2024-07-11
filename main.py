import sys 
from antlr4 import *
from antlr4.tree.Trees import Trees
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from EvalMiniCVisitor import EvalMiniCVisitor 
from EvalMiniCVisitor import ThreeAddressCodeVisitor

input_stream = FileStream(sys.argv[1])

lexer = MiniCLexer(input_stream)

token_stream = CommonTokenStream(lexer)

parser = MiniCParser(token_stream)

tree = parser.program()

visitor = ThreeAddressCodeVisitor()
visitor.visit(tree)