import argparse
from antlr4 import *
from HtmlLexer import HtmlLexer
from HtmlParser import HtmlParser
from Visitor import Visitor

def main():
    parser = argparse.ArgumentParser(description='Processar um arquivo HTML.')
    parser.add_argument('file', help='O caminho para o arquivo HTML.')
    args = parser.parse_args()

    input_stream = FileStream(args.file, encoding='utf-8')


    lexer = HtmlLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = HtmlParser(token_stream)
    tree = parser.root()
    visitor = Visitor()
    visitor.visit(tree)

# Para testa precisa de um arquivo de entrada ex: main.py entrada.txt
if __name__== '__main__':
    main()