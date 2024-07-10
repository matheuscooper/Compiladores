from antlr4 import *
from antlr4.tree.Trees import Trees
from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCLexer import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCLexer
from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser
from BeatrizAguiar_MatheusOliveira_RebecaMadi_EvalMiniCVisitor import EvalBeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor
import sys 

def main(argv):

    inputFile = FileStream(argv[1])
    lexer = BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCLexer(inputFile)
    stream = CommonTokenStream(lexer)
    parser = BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser(stream)
    arvore = parser.program()
    print(Trees.toStringTree(arvore, None, parser))
    visitor = EvalBeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor()
    visitor.visitProgram(arvore)
    if visitor.erros:
        for e in visitor.erros:
            print(e)

    
if __name__ == '__main__':
    main(sys.argv)   