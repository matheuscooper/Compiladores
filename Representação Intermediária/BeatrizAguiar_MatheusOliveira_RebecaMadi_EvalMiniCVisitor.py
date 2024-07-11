from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser
from BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor import BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor

class EvalBeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor(BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor):
    def __init__(self):
        self.symbol_table = {}
        self.function_table = {}
        self.symbol_table_escopo = {}
        self.erros = []
    
    def add_error(self, message, ctx):
        line = ctx.start.line
        column = ctx.start.column
        e = f"Line [{line}:{column}]: {message}"
        if e not in self.erros:
            self.erros.append(e)

    def visitProgram(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ProgramContext):
        for li in ctx.definition():
            self.visitDefinition(li)
            

    def visitDefinition(self, ctx):
        for li in ctx.getChildren():
            if isinstance(li, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Data_definitionContext):
                self.visitData_definition(li, self.symbol_table)
            elif isinstance(li, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Function_definitionContext):
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
        self.symbol_table_escopo = {}
        tipo = ""
        if ctx.tipo():
            tipo = ctx.tipo().getText()
        #print(tipo)
        nome = self.visitFunction_header(ctx.function_header(), tipo)
        self.visitFunction_body(ctx.function_body(), tipo, nome)

        
        #print(self.symbol_table_escopo)
        return None

    def visitFunction_header(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Function_headerContext, tipo):
        nome = ctx.declarator()
        nome = nome.getText()
        if nome in self.symbol_table or nome in self.function_table:
            self.add_error(f"Error: Variable '{nome}' already declared.", ctx)
        else:
            aux = self.visitParameter_list(ctx.parameter_list())
            aux1 = {}
            if aux == None:
                aux = {}
            for a in aux.keys():
                aux1[a] = aux[a]
            self.function_table[nome] = (tipo, aux1)  
        return nome

    def visitFunction_body(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Function_bodyContext, tipo, nm):
        l = list(ctx.getChildren())
        for li in l:
            if isinstance(li, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Data_definitionContext):
                self.symbol_table_escopo = self.visitData_definition(li, self.symbol_table_escopo)
            elif isinstance(li, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatementContext):
                if li.getChildCount() >=1:
                    self.visitStatement(li, tipo, nm)
        return None
    
    def visitParameter_list(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Parameter_listContext):
        if ctx.parameter_declaration():
            a = self.visitParameter_declarationn(ctx.parameter_declaration())
        else:
            return None
        if ctx.declarator():
            for d in ctx.declarator():
                if d.getText() in self.symbol_table_escopo:
                    self.add_error(f"Error: Variable '{d.getText()}' already declared.", ctx)
                else:
                    self.symbol_table_escopo[d.getText()] = a[1]
        return self.symbol_table_escopo
    
    def visitParameter_declarationn(self, ctx):
        tipo = ctx.tipo().getText()
        nome = ctx.declarator()
        nome = nome.getText()
        if nome in self.symbol_table_escopo:
            self.add_error(f"Error: Variable '{nome}' already declared.", ctx)
        else:
            self.symbol_table_escopo[nome] = tipo
        return [self.symbol_table_escopo, tipo]

    def visitStatement(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatementContext, tipo, nm):
        v = 0
        if type(ctx) == list:
            ctx = ctx[0]
        if not ctx.isEmpty():
            for c in ctx.getChildren():
                if isinstance(c, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExpressionContext):
                    #print(f"c: {c.getText()} expression")
                    self.visitExpression(ctx.expression(), nm)
                    if v == 1:
                        rt = c.getText()
                        ob = c
                elif isinstance(c, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatementContext):
                    #print(f"c: {c.getText()} statement")
                    self.visitStatement(ctx.statement(), tipo, nm)
                if c.getText() =="return":
                    v = 1
        else:
            print(ctx.getChild(0))
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
                    if tipo != self.visitExpression(ob, nm):
                        self.add_error(f"Error: Type mismatch in return of expression '{ob.getText()}'.", ctx)

                
            return None
    
    def visitExpression(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExpressionContext, nm):
        t = ""
        for li in ctx.binary():
            t = self.visitBinary(li, nm)
        return t
    
    def visitBinary(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.BinaryContext, nm):
        l = []
        lc = []
        for b in ctx.binary():
            l.append(b.getText())
            lc.append(b)
        
        #se só precisar validar o tipo da esquerda e da direita
        if ctx.Identifier():
            i = ctx.Identifier().getText()
            e = [ei for ei in ctx.getChildren() if not isinstance(ei, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.BinaryContext) and not isinstance(ei, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.UnaryContext) and ei != ctx.Identifier()]
            e = e[0]
            if i in self.symbol_table_escopo:
                if self.symbol_table_escopo[i] != self.visitBinary(lc[0], nm):
                    self.add_error(f"Error: Type mismatch in expressions ('{i}' {e} '{l[0]}').", ctx)
                    return False
                else:
                    return self.symbol_table_escopo[i]
            elif i in self.symbol_table:
                if self.symbol_table[i] != self.visitBinary(lc[0], nm):
                    self.add_error(f"Error: Type mismatch in expressions ('{i}' {e} '{l[0]}').", ctx)
                    return False
                else:
                    return self.symbol_table[i]
            else:
                self.add_error(f"Error: Variable '{i}' not declared.", ctx)
                return False

        else:
            if ctx.unary():
                return self.visitUnary(ctx.unary(), nm)
            else:
                e = [ei for ei in ctx.getChildren() if not isinstance(ei, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.BinaryContext) and not isinstance(ei, BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.UnaryContext) and ei != ctx.Identifier()]
                e = e[0]
                aux = self.visitBinary(lc[0], nm)
                if aux != self.visitBinary(lc[1], nm):
                    self.add_error(f"Error: Type mismatch in expression ('{l[0]}' {e} '{l[1]}').", ctx)
                    return False
                else:
                    return aux
            """
            Se precisar validar q as variaveis são inteiras:
            if l[1] == "+=" or l[1] == "-=" or l[1] =="/="or l[1] == "*=" or l[1] == "+" or l[1] =="-" or l[1] == "*" or l[1] =="/" or l[1] == "%" or l[1] =="%=":
                return
            elif l[1] == "==" or l[1] == "!=" or l[1] ==">=" or l[i]
            """
    
    def visitUnary(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.UnaryContext, nm):
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
            return self.visitPrimary(ctx.primary(), nm)
    
    def visitPrimary(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.PrimaryContext, nm):
        if ctx.Identifier():
            t = ctx.Identifier().getText()
            if ctx.getChildCount() == 1:
               # print(self.symbol_table_escopo,  self.function_table[nm], self.symbol_table, t)
                if t not in self.symbol_table_escopo and t not in self.symbol_table and t not in self.function_table[nm]:
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
                    self.visitArgument_list(ctx.argument_list(), t)
                    return self.function_table[t][0]
        elif ctx.CONSTANT_INT():
            return "int"
        elif ctx.CONSTANT_CHAR():
            return "char"
        elif ctx.expression():
            #resolver
            return self.visitExpression(ctx.expression())
        
    def visitArgument_list(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Argument_listContext, t):
        if ctx.binary():
            v = self.function_table[t][1].values()
            v = [vi for vi in v]
            tam = len(v)
            i = 0
            for a in ctx.binary():
                i +=1
                r = self.visitBinary(a, t)
                if r == False or r!=v[i-1]:
                    self.add_error(f"Error: Type mismatch in function call of variable '{a.getText()}' in function '{t}'.", ctx)
            if i!=tam:
                self.add_error(f"Error: Argmument mismatch in function call '{t}'.", ctx)
        return None
    
class ThreeAddressCodeVisitor(BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCVisitor):
    temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def visitProgram(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ProgramContext): ## Adaptar depois por que eu gerei sem compilar a
        for stat in ctx.stat():
            self.visit(stat)
    
    def visitStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatContext):
        return self.visitChildren(ctx)
    
    def visitIfStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.IfStatContext):
        cond = self.visit(ctx.expr())
        then_label = self.new_temp()
        end_label = self.new_temp()
        print(f"if {cond} goto {then_label}\ngoto {end_label}\n{then_label}:\n")
        self.visit(ctx.stat())
        print(f"{end_label}:\n")
        return
    def visitWhileStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.WhileStatContext):
        start_label = self.new_temp()
        middle_label = self.new_temp()
        end_label = self.new_temp()
        print(f"{start_label}:\n")
        cond = self.visit(ctx.expr())
        print(f"if {cond} goto {middle_label}\ngoto {end_label}\n{middle_label}:\n")
        self.visit(ctx.stat())
        print(f"goto {start_label}\n{end_label}:\n")
        return
    
    def visitAssignStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExprStatContext):
        value = self.visit(ctx.expr())
        code = f"{ctx.Ident().getText()}= {value};"
        print(code)
        return code
    
    def visitExprStat(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExprStatContext):
        expr = self.visit(ctx.expr())
        print(expr)
        return expr
    
    def visitExpr(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExprContext):
        if len(ctx.expr()) == 2:
            left = self.visit(ctx.expr(0))
            right = self.visit(ctx.expr(1))
            op = ctx.getChild(1).getText()
            temp = self.new_temp()
            print(f"{temp} = {left} {op} {right}")
            return temp
        elif ctx.getChildCount() == 2:
            expr = self.visit(ctx.expr(0))
            temp = self.new_temp()
            print(f"{temp} = !{expr}")
            return temp
        elif ctx.Ident():
            return ctx.Ident().getText()
        elif ctx.INT():
            return ctx.INT().getText()
        else:
            return self.visit(ctx.expr(0))
    
    def visitIdentExpr(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExprContext):
        return ctx.Ident().getText()
    
    def visitIntExpr(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExprContext):
        return ctx.INT().getText()
    
    def visitParentExpr(self, ctx:BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExprContext):
        return self.visit(ctx.expr())