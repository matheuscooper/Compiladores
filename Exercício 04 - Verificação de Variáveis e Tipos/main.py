from antlr4 import *
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
from EvalMiniCVisitor import EvalMiniCVisitor
import sys 

def main(argv):

    inputFile = FileStream(argv[1])
    lexer = MiniCLexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = MiniCParser(stream)
    arvore = parser.program()
    visitor = EvalMiniCVisitor()
    visitor.visitProgram(arvore)

    if visitor.erros:
        for e in visitor.erros:
            print(e)

    
if __name__ == '__main__':
    main(sys.argv)   