from MiniCParser import MiniCParser
from MiniCVisitor import MiniCVisitor

class EvalMiniCVisitor(MiniCVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.function_table = {}
        self.symbol_table_escopo = {}
        self.erros = []
    
    def add_error(self, message, ctx):
        line = ctx.start.line
        column = ctx.start.column
        self.erros.append(f"Line [{line}:{column}]: {message}")

    def visitProgram(self, ctx:MiniCParser.ProgramContext):
        for li in ctx.definition():
            self.visitDefinition(li)
            

    def visitDefinition(self, ctx):
        for li in ctx.getChildren():
            if isinstance(li, MiniCParser.Data_definitionContext):
                self.visitData_definition(li, self.symbol_table)
            elif isinstance(li, MiniCParser.Function_definitionContext):
                #self.symbol_table_escopo = {}
                self.visitFunction_definition(li)

    def visitData_definition(self, ctx, table):
        tipo = ctx.tipo().getText()
        nomes = []
        for n in ctx.declarator():
            nomes.append(n.getText())
        for nome in nomes:
            """if ctx.value():
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
            """
            if nome in table:
                self.add_error(f"Error: Variable '{nome}' already declared.", ctx)
            else:
                table[nome] = tipo
            
        return table

    def visitFunction_definition(self, ctx):
        if ctx.tipo():
            tipo = ctx.tipo().getText()
        
        self.symbol_table_escopo = {}
        self.visitFunction_header(ctx.function_header(), tipo)
        self.visitFunction_body(ctx.function_body(), tipo)
        #print(self.symbol_table_escopo)
        return None

    def visitFunction_header(self, ctx: MiniCParser.Function_headerContext, tipo):
        nome = ctx.declarator()
        nome = nome.getText()
        if nome in self.symbol_table or nome in self.function_table:
            self.add_error(f"Error: Variable '{nome}' already declared.", ctx)
        else:
            self.function_table[nome] = (tipo, self.visitParameter_list(ctx.parameter_list()))            
        return None

    def visitFunction_body(self, ctx: MiniCParser.Function_bodyContext, tipo):
        l = list(ctx.getChildren())
        for li in l:
            if isinstance(li, MiniCParser.Data_definitionContext):
                self.symbol_table_escopo = self.visitData_definition(li, self.symbol_table_escopo)
            elif isinstance(li, MiniCParser.StatementContext):
                self.visitStatement(li, tipo)
        return None
    
    def visitParameter_list(self, ctx: MiniCParser.Parameter_listContext):
        if ctx.parameter_declaration():
            for li in ctx.parameter_declaration():
                self.visitParameter_declarationn(li)
        return None
    
    def visitParameter_declarationn(self, ctx):
        tipo = ctx.tipo().getText()
        nome = ctx.declarator()
        nome = nome.getText()
        if nome in self.symbol_table_escopo:
            self.add_error(f"Error: Variable '{nome}' already declared.", ctx)
        else:
            self.symbol_table_escopo[nome] = tipo
        return self.symbol_table_escopo

    def visitStatement(self, ctx: MiniCParser.StatementContext, tipo):
        if ctx.expression():
            self.visitExpression(ctx.expression())
        if ctx.statement():
            self.visitStatement(ctx.statement(), tipo)
        if ctx.expression() :
            v = 0
            for r in ctx.getChildren():
                if v == 1:
                    rt = r.getText()
                    ob = r
                    break
                if r.getText() == "return":
                    v = 1
                
            if v:
                if rt != ";":
                    if rt in self.symbol_table_escopo:
                        if self.symbol_table_escopo[rt] != tipo:
                            self.add_error(f"Error: Type mismatch in return of variable '{rt}'.", ctx)
                    elif rt in self.symbol_table:
                        if self.symbol_table[rt] != tipo:
                                self.add_error(f"Error: Type mismatch in return of variable '{rt}'.", ctx)
                        else:
                            self.add_error(f"Error: Variable '{rt}' not declared.", ctx)
                    else:
                        if tipo != self.visitExpression(ob):
                            self.add_error(f"Error: Type mismatch in return of expression '{ob.getText()}'.", ctx)
        return None
    
    def visitExpression(self, ctx: MiniCParser.ExpressionContext):
        t = ""
        for li in ctx.binary():
            t = self.visitBinary(li)
        return t
    
    def visitBinary(self, ctx: MiniCParser.BinaryContext):
        l = []
        lc = []
        for b in ctx.binary():
            l.append(b.getText())
            lc.append(b)
        #se só precisar validar o tipo da esquerda e da direita
        if ctx.Identifier():
            i = ctx.Identifier().getText()
            if i in self.symbol_table_escopo:
                if self.symbol_table_escopo[i] != self.visitBinary(lc[0]):
                    self.add_error(f"Error: Type mismatch in expressions '{i}' and '{l[0]}'.", ctx)
                    return False
                else:
                    return self.symbol_table_escopo[i]
            elif i in self.symbol_table:
                if self.symbol_table[i] != self.visitBinary(lc[0]):
                    self.add_error(f"Error: Type mismatch in expressions '{i}' and '{l[0]}'.", ctx)
                    return False
                else:
                    return self.symbol_table[i]
            else:
                self.add_error(f"Error: Variable '{i}' not declared.", ctx)
                return False

        else:
            if ctx.unary():
                return self.visitUnary(ctx.unary())
            else:
                aux = self.visitBinary(lc[0])
                if aux != self.visitBinary(lc[1]):
                    self.add_error(f"Error: Type mismatch in expression'{l[0]}' and '{l[1]}'.", ctx)
                    return False
                else:
                    return aux
            """
            Se precisar validar q as variaveis são inteiras:
            if l[1] == "+=" or l[1] == "-=" or l[1] =="/="or l[1] == "*=" or l[1] == "+" or l[1] =="-" or l[1] == "*" or l[1] =="/" or l[1] == "%" or l[1] =="%=":
                return
            elif l[1] == "==" or l[1] == "!=" or l[1] ==">=" or l[i]
            """
    
    def visitUnary(self, ctx: MiniCParser.UnaryContext):
        if ctx.Identifier():
            t = ctx.Identifier().getText()
            if t not in self.symbol_table_escopo and t not in self.symbol_table:
                self.add_error(f"Error: Variable '{t}' not declared.", ctx)
            else:
                if t in self.symbol_table_escopo:
                    return self.symbol_table_escopo[t]
                else:
                    return self.symbol_table[t]
        else:
            return self.visitPrimary(ctx.primary())
    
    def visitPrimary(self, ctx: MiniCParser.PrimaryContext):
        if ctx.Identifier():
            t = ctx.Identifier().getText()
            if ctx.getChildCount() == 1:
                if t not in self.symbol_table_escopo and t not in self.symbol_table:
                    self.add_error(f"Error: Variable '{t}' not declared.", ctx)
                else:
                    if t in self.symbol_table_escopo:
                        return self.symbol_table_escopo[t]
                    else:
                        return self.symbol_table[t]
            else:
                if t not in self.function_table:
                    self.add_error(f"Error: Function '{t}' not declared.", ctx)
                    return None
                if ctx.argument_list():
                    self.visitArgument_list(ctx.argument_list())
                    return self.function_table[t][0]
        elif ctx.CONSTANT_INT():
            return "int"
        elif ctx.CONSTANT_CHAR():
            return "char"
        elif ctx.expression():
            #resolver
            return self.visitExpression(ctx.expression())
        
    def visitArgument_list(self, ctx: MiniCParser.Argument_listContext):
        if ctx.binary():
            for a in ctx.binary():
                r = self.visitBinary(a)
                if r == False:
                    self.add_error(f"Error: Type mismatch in function call of variable '{a.getText()}'.", ctx)
        return None
    