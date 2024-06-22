from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from EvalListener import EvalListener

input_stream = InputStream(input('? '))
lexer = ExprLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = ExprParser(token_stream)
tree = parser.root()
eval_listener = EvalListener()
#listener.visit(tree)
walker = ParseTreeWalker()
walker.walk(eval_listener, tree)
print(eval_listener.getResult())