from antlr4 import *
from antlr4.tree.Trees import Trees
from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCLexer import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCLexer
from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser
from BeatrizAguiar_MatheusOliveira_RebecaMadi_EvalMiniCVisitor import EvalBeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor, ThreeAddressCodeVisitor, EduMIPS64
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
        print("O códico contém erros!")
    else:
        print("\nTE:")
        visitor = ThreeAddressCodeVisitor()
        visitor.visit(arvore)
        for v in visitor.code:
            print(v)
        print(visitor.code)
        ds, ts = EduMIPS64(visitor.code)
        print(".data")
        for line in ds:
            print(line)

        print("\n.text")
        for line in ts:
            print(line)
        


    
if __name__ == '__main__':
    main(sys.argv)   