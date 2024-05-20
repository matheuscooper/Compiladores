from antlr4 import *
from antlr4.tree.Trees import Trees
from MiniCLexer import MiniCLexer
from MiniCParser import MiniCParser
import sys 

def main(argv):
    if len(argv) < 2:
        print("python ,<script> ,<arquivo>")
        return

    inputFile = FileStream(argv[1])

    lexer = MiniCLexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = MiniCParser(stream)

    arvore = parser.program()


    print(Trees.toStringTree(arvore, None, parser))

    
if __name__ == '__main__':
    main(sys.argv)    
