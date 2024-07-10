import sys
from antlr4 import*
from SimpleLangLexer import SimpleLangLexer
from SimpleLangParser import SimpleLangParser
from ThreeAddressCodeVisitor import ThreeAddressCodeVisitor 

input_stream = FileStream(sys.argv[1])

lexer = SimpleLangLexer(input_stream)

token_stream = CommonTokenStream(lexer)

parser = SimpleLangParser(token_stream)

tree = parser.prog()

visitor = ThreeAddressCodeVisitor()
visitor.visit(tree)