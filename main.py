from antlr4 import *
from UrlLexer import UrlLexer
from UrlParser import UrlParser

input_text = InputStream(input('? '))
lexer = UrlLexer(input_text)
stream = CommonTokenStream(lexer)
parser = UrlParser(stream)

tree = parser.url()

print(tree.toStringTree(recog=parser))