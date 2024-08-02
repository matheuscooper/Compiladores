from antlr4 import *
from antlr4.tree.Trees import Trees
from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCLexer import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCLexer
from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser
from BeatrizAguiar_MatheusOliveira_RebecaMadi_EvalMiniCVisitor import EvalBeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor, ThreeAddressCodeVisitor, EduMIPS64
import sys 

def main(argv):
    if argv[1] == "minic":
        inputFile = FileStream(argv[2])
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
            func(ds + ts)
    elif argv[1] == "te":
        te = []
        with open(argv[2], 'r', encoding='utf-8') as arquivo:
            for linha in arquivo:
                te.append(linha)
        #["func main begin", "t0 = 1 + 2", "t1 = t0 * 3", "x = t1", "func main end"]
        ds, ts = EduMIPS64(te)
        print(".data")
        for line in ds:
            print(line)

        print("\n.text")
        for line in ts:
            print(line)
        func(ds + ts)


    
def func(lista):
    with open("./resultados/resultado.txt", 'w', encoding='utf-8') as arquivo:
            for linha in lista:
                arquivo.write(linha)
                arquivo.write("\n")

if __name__ == '__main__':
    main(sys.argv)   