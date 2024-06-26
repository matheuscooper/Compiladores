from MiniCParser import MiniCParser
from MiniCVisitor import MiniCVisitor

class EvalMiniCVisitor(MiniCVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.erros = []
    
    def add_error(self, message, ctx):
        line = ctx.start.line
        self.erros.append(f"Line {line}: {message}")

    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        l = list(ctx.definition())
        for li in l:
            self.visitDefinition(li)

    def visitDefinition(self, ctx):
        if isinstance(ctx, MiniCParser.Data_definitionContext):
            return self.visitData_definition(ctx.data_definition())
        else:
            return self.visitFunction_definition(ctx.function_definition())

    def visitData_definition(self, ctx):
        valor = ctx.value().getText()
        tipo = ctx.type_().getText()
        nome = ctx.declarator()
        nome = nome[0].getText()
        print(tipo, nome, valor)
        if ctx.value().getText():
            valor = ctx.value().getText()
            #print(nome, valor, type(valor))
            if tipo == 'int':
                try:
                    int(valor)
                except:
                    self.add_error(f"Error: Type mismatch in initialization of variable '{nome}'.", ctx)
            elif tipo == 'char':
                if valor[0] != "'" or valor[2] != "'" or len(valor) != 3:
                    self.add_error(f"Error: Type mismatch in initialization of variable '{nome}'.", ctx)
        if nome in self.symbol_table:
            self.add_error(f"Error: Variable '{nome}' already declared.", ctx)
        else:
            self.symbol_table[nome] = tipo
            
        return None