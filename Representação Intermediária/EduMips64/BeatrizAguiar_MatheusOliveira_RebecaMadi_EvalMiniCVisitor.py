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
        tipo = ""
        if ctx.tipo():
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
            return self.visitExpression(ctx.expression(), nm)
        
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
    def __init__(self):
        self.temp_count = 0
        self.label_count = 0
        self.values = []
        self.code = []

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def visitDefinition(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.DefinitionContext):
        if ctx.data_definition():
            self.visit(ctx.data_definition())
        elif ctx.function_definition():
            self.visit(ctx.function_definition())

    def visitData_definition(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Data_definitionContext):
        tipo = ctx.tipo().getText()
        for declarator in ctx.declarator():
            var_name = declarator.getText()
            self.code.append(f"{var_name} : {tipo}")
            

    def visitFunction_definition(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Function_definitionContext):
        func_name = ctx.function_header().declarator().getText()
        self.code.append(f"func {func_name} begin")
        self.visit(ctx.function_body())
        self.code.append(f"func {func_name} end")

    def visitFunction_body(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Function_bodyContext):
        for data_def in ctx.data_definition():
            self.visit(data_def)
        for statement in ctx.statement():
            self.visit(statement)

    def visitStatement(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatementContext):
        #print(ctx.getText())
        
        if ctx.getText()[0:2] == "if" or ctx.getText()[0:6]=="elseif":
            self.visitIf(ctx)
        elif ctx.getText()[0:5] == "while" or ctx.getText()[0:9]=="elsewhile":
            self.visitWhile(ctx)
        elif ctx.getText()[0:6] == "return" or ctx.getText()[0:10]=="elsereturn":
            value = self.visit(ctx.expression())
            self.code.append(f"return {value}")
        else:
            if ctx.expression():
                self.visit(ctx.expression())

    def visitIf(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatementContext):
        cond = self.visit(ctx.expression())
        label_true = self.new_temp()
        label_end = self.new_temp()
        self.code.append(f"if {cond} goto {label_true}")
        self.code.append(f"goto {label_end}")
        self.code.append(f"{label_true}:")
        self.visit(ctx.statement(0))
        #print("aaa", ctx.statement(0).getText())
        i = 1
        while(ctx.statement(i)):
            label_else = self.new_label()
            self.code.append(f"goto {label_else}")
            self.code.append(f"{label_end}:")
            self.visit(ctx.statement(i))
            self.code.append(f"{label_else}:")
            i += 1
            
        if i == 1:
            self.code.append(f"{label_end}:")

    def visitWhile(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.StatementContext):
        label_begin = self.new_temp()
        label_true = self.new_temp()
        label_end = self.new_temp()
        self.code.append(f"{label_begin}:")
        cond = self.visit(ctx.expression())
        self.code.append(f"if {cond} goto {label_true}")
        self.code.append(f"goto {label_end}")
        self.code.append(f"{label_true}:")
        i = 0
        while(ctx.statement(i)):
            self.visit(ctx.statement(i))
            i += 1
        self.code.append(f"goto {label_begin}")
        self.code.append(f"{label_end}:")

    def visitExpression(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.ExpressionContext):
        results = [self.visit(binary) for binary in ctx.binary()]
        #print(results)
        return results[0] if len(results) == 1 else results

    def visitBinary(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.BinaryContext):
        cs1 = [c for c in ctx.getChildren()]
        cs = [csi.getText() for csi in cs1]
        c0 = []
        if '=' in cs[0]:
            c0 = cs[0].split("=")
            cs.pop(0)
            c0 = [c0[0], "=", c0[1]]
            cs = c0 + cs
        if len(cs)>2:
            #print(cs)
            left = cs[0]
            right = cs[2]
            op = cs[1]
            if op == "=":
                #print(cs, ctx.getChild(2).getText())
                
                if len(cs)>3:
                    #print([c.getText() for c in cs1])
                    x1 = self.visit(cs1[0])
                    x2 = self.visit(cs1[-1])
                    #print(f"{left} = {x1} {cs[3]} {x2}")
                    temp = self.new_temp()
                    #print(temp, "=", cs[2])
                    self.code.append(f"{temp} = {x1} {cs[3]} {x2}")
                    self.code.append(f"{cs[0][0]} = {temp}")
                    return temp
                elif len(cs) == 3:
                    if cs[2][:2] == "++":
                        temp = self.new_temp()
                        ident = cs[2][2:]
                        self.code.append(f"{temp} = {ident} + 1")
                        self.code.append(f"{cs[0]} = {temp}")
                        return temp
                    elif cs[2][:2] == "--":
                        temp = self.new_temp()
                        ident = cs[2][2:]
                        self.code.append(f"{temp} = {ident} - 1")
                        self.code.append(f"{cs[0]} = {temp}")
                        return temp
                    else:
                        self.code.append(f"{cs[0]} = {self.visit(ctx.getChild(2))}")
                        return self.visit(ctx.getChild(2))
            elif len(op)>1:
                #print(cs)
                temp = self.new_temp()
                self.code.append(f"{temp} = {cs[0]} {op[0]} {cs[2]}")
                self.code.append(f"{cs[0]} = {temp}")
                return temp
            else:
                temp = self.new_temp()
                #print(f"{temp} = {self.visit(cs1[0])} {op} {self.visit(cs1[2])}")
                self.code.append(f"{temp} = {self.visit(cs1[0])} {op} {self.visit(cs1[2])}")
                return temp
        elif len(ctx.binary()) > 1:
            #print("c2: ", cs)
            left = self.visit(ctx.binary(0))
            right = self.visit(ctx.binary(1))
            op = ctx.getChild(1).getText()
            temp = self.new_temp()
            #print(f"{temp} = !{cs[0]}")
            self.code.append(f"{temp} = {left} {op} {right}")
            return temp
        else:
            return cs[0]

    def visitUnary(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.UnaryContext):
        if ctx.Identifier():
            if ctx.getText()[-2:] == "++":
                ident = ctx.Identifier().getText()
                self.code.append(f"{ident} = {ident} + 1")
                return ident
            elif ctx.getText()[-2:] == "--":
                ident = ctx.Identifier().getText()
                self.code.append(f"{ident} = {ident} - 1")
                return ident
            else:
                return ctx.Identifier().getText()
        else:
            return self.visit(ctx.primary())

    def visitPrimary(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.PrimaryContext):
        if ctx.Identifier():
            if ctx.getChildCount() == 1:
                return ctx.Identifier().getText()
            else:
                func_name = ctx.Identifier().getText()
                args = self.visit(ctx.argument_list()) if ctx.argument_list() else []
                arg_list = ", ".join(args)
                temp = self.new_temp()
                self.code.append(f"{temp} = call {func_name}({arg_list})")
                return temp
        elif ctx.CONSTANT_INT():
            return ctx.CONSTANT_INT().getText()
        elif ctx.CONSTANT_CHAR():
            return ctx.CONSTANT_CHAR().getText()
        elif ctx.expression():
            return self.visit(ctx.expression())

    def visitArgument_list(self, ctx: BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniCParser.Argument_listContext):
        k = [self.visit(binary) for binary in ctx.binary()]
        print(k)
        return k
    

def EduMIPS64(codigo):
    data = []
    code = []
    registradores = []
    mapa_registradores = {}
    labels = []
    
    for i in range(31):
        registradores.append("t"+str(i))
        mapa_registradores["t"+str(i)] = "vazio"
    
    mapa_variaveis = {}
    label_counter = 0

    def nova_label():
        nonlocal label_counter
        label = f"label{label_counter}"
        label_counter += 1
        labels.append(label)
        return label

    def declaracao(v, vl, tipo):
        if tipo == "int":
            data.append(f"{v}: .word {vl}")
        else:
            data.append(f"{v}: .asciiz {vl}")
        mapa_variaveis[v] = "vazio"
    
    def prox():
        chaves = mapa_registradores.keys()
        for c in chaves:
            if mapa_registradores[c] == "vazio":
                mapa_registradores[c] = "ocupado"
                return c

    def carrega(a, var, ant="zero"):
        print(a, var)
        if a.isdigit():
            if var in mapa_registradores.keys():
                code.append(f"addi ${var}, ${ant}, {a}")
                return var
            else:
                if var not in mapa_variaveis.keys():
                    declaracao(a, 0, "int")
                reg = prox()
                mapa_registradores[reg] = var
                mapa_variaveis[var] = reg
                code.append(f"lw ${reg}, {var}($zero)")
                code.append(f"addi ${reg}, ${ant}, {a}")
                return reg
        else:
            if a not in mapa_registradores.keys():
                if a not in mapa_variaveis.keys():
                    declaracao(a, 0, "int")
                elif mapa_variaveis[a] == "vazio":
                    return mapa_variaveis[a]
                reg = prox()
                mapa_registradores[reg] = a
                mapa_variaveis[a] = reg
                code.append(f"lw ${reg}, {a}($zero)")
                return reg
            else:
                return a

    def atribuicoes(words):
        words[0] = words[0].replace(" ", "")
        words[1] = words[1].replace(" ", "")
        words[0] = words[0].replace("\n", "")
        words[1] = words[1].replace("\n", "")
        var = words[0]
        if var in mapa_registradores.keys():
            mapa_registradores[var] = "ocupado"
        if "+" in words[1]:
            a = words[1].split("+")[0]
            b = words[1].split("+")[1]
            a = a.replace(" ", "")
            b = b.replace(" ", "")
            r1 = carrega(a, var, ant="zero")
            if r1 == var:
                r2 = carrega(b, var, ant=r1)
            else:
                r2 = carrega(b, var)
            if r1 != r2:
                code.append(f"add ${var}, ${r1}, ${r2}")
            if var not in mapa_registradores.keys():  
                r = prox()
                code.append(f"sw ${r}, {var}($zero)")
                mapa_variaveis[var] = r
                mapa_registradores[r] = var
        elif "-" in words[1]:
            a = words[1].split("-")[0]
            b = words[1].split("-")[1]
            a = a.replace(" ", "")
            b = b.replace(" ", "")
            r1 = carrega(a, var, ant="zero")
            r2 = carrega(b, var)
            if r1 != r2:
                code.append(f"sub ${var}, ${r1}, ${r2}")
            if var not in mapa_registradores.keys():  
                r = prox()
                code.append(f"sw ${r}, {var}($zero)")
                mapa_variaveis[var] = r
                mapa_registradores[r] = var
        elif "*" in words[1]:
            a = words[1].split("*")[0]
            b = words[1].split("*")[1]
            a = a.replace(" ", "")
            b = b.replace(" ", "")
            r1 = carrega(a, var, ant="zero")
            r2 = carrega(b, var)
            if r1 != r2:
                code.append(f"dmult ${r1}, ${r2}")
                if var in mapa_registradores.keys():
                    code.append(f"mflo ${var}")
                else:
                    r = prox()
                    code.append(f"mflo ${r}")
                    code.append(f"sw ${r}, {var}($zero)")
                    mapa_variaveis[var] = r
                    mapa_registradores[r] = var
                mapa_registradores[r1] = "vazio"
                mapa_registradores[r2] = "vazio"
        elif "/" in words[1]:
            a = words[1].split("/")[0]
            b = words[1].split("/")[1]
            a = a.replace(" ", "")
            b = b.replace(" ", "")
            r1 = carrega(a, var, ant="zero")
            r2 = carrega(b, var)
            if r1 != r2:
                code.append(f"div ${r1}, ${r2}")
                if var in mapa_registradores.keys():
                    code.append(f"mflo ${var}")
                else:
                    r = prox()
                    code.append(f"mflo ${r}")
                    code.append(f"sw ${r}, {var}($zero)")
                    mapa_variaveis[var] = r
                    mapa_registradores[r] = var
                    mapa_registradores[r1] = "vazio"
                    mapa_registradores[r2] = "vazio"
        elif "%" in words[1]:
            a = words[1].split("%")[0]
            b = words[1].split("%")[1]
            a = a.replace(" ", "")
            b = b.replace(" ", "")
            r1 = carrega(a, var, ant="zero")
            r2 = carrega(b, var)
            if r1 != r2:
                code.append(f"div ${r1}, ${r2}")
                if var in mapa_registradores.keys():
                    code.append(f"mfhi ${var}")
                else:
                    r = prox()
                    code.append(f"mfhi ${r}")
                    code.append(f"sw ${r}, {var}($zero)")
                    mapa_variaveis[var] = r
                    mapa_registradores[r] = var
                mapa_registradores[r1] = "vazio"
                mapa_registradores[r2] = "vazio"
        elif ">" in words[1] or "<" in words[1]:
            if ">" in words[1]:
                a = words[1].split(">")[0]
                b = words[1].split(">")[1]
            else:
                a = words[1].split("<")[0]
                b = words[1].split("<")[1]
            a = a.replace(" ", "")
            b = b.replace(" ", "")
            r1 = carrega(a, var, ant="zero")
            r2 = carrega(b, var)
            if r1 != r2:
                if var in mapa_registradores.keys():
                    code.append(f"slt ${var}, ${r1}, ${r2}")
                else:
                    r = prox()
                    code.append(f"slt ${r}, ${r1}, ${r2}")
                    code.append(f"sw ${r}, {var}($zero)")
                    mapa_variaveis[var] = r
                    mapa_registradores[r] = var
                mapa_registradores[r1] = "vazio"
                mapa_registradores[r2] = "vazio"
        elif "==" in words[1] or "!=" in words[1]:
            if "==" in words[1]:
                a = words[1].split("==")[0]
                b = words[1].split("==")[1]
            else:
                a = words[1].split("!=")[0]
                b = words[1].split("!=")[1]
            a = a.replace(" ", "")
            b = b.replace(" ", "")
            r1 = carrega(a, var, ant="zero")
            r2 = carrega(b, var)
            if r1 != r2:
                if var in mapa_registradores.keys():
                    code.append(f"xor ${var}, ${r1}, ${r2}")
                else:
                    r = prox()
                    code.append(f"xor ${r}, ${r1}, ${r2}")
                    code.append(f"sw ${r}, {var}($zero)")
                    mapa_variaveis[var] = r
                    mapa_registradores[r] = var
                mapa_registradores[r1] = "vazio"
                mapa_registradores[r2] = "vazio"
        else:
            print(words, var)
            if words[1] in mapa_registradores.keys():
                if var not in mapa_variaveis.keys():
                    declaracao(var, 0, "int")
                code.append(f"sw ${words[1]}, {var}($zero)")
                mapa_variaveis[var] = words[1]
                mapa_registradores[words[1]] = var
            else:
                if var not in mapa_variaveis.keys():
                    declaracao(var, 0, "int")
                r = carrega(words[1], var)
                code.append(f"sw ${r}, {var}($zero)")
                mapa_variaveis[var] = r
                mapa_registradores[r] = var
                    
    for linha, i in zip(codigo, range(len(codigo))):
        linha = linha.replace("\n", "")
        
        if "begin" in linha or (":" in linha and "int" not in linha and "char" not in linha):
            if ":" in linha:
                code.append("\n")
                if linha[-1] not in labels:
                    labels.append(linha[-1])
                    code.append(linha)
                else:
                    code.append(linha)
            else:
                l = linha.split(" ")
                code.append(l[1]+":")
            #a implementar
            continue
        elif " = " in linha:
            atribuicoes(linha.split("="))
        elif "if" in linha:
            linha = linha.replace(")", " ")
            linha = linha.replace("(", " ")
            linha = linha.replace("go to", "goto")
            words = linha.split(" ")
            words = [w for w in words if w != ""]
            print(words)
            p = codigo[i+1]
            if "go" in p:
                p = p.replace("go to", "goto")
                p = p.replace("\n", "")
                pw = p.split(" ")
                code.append(f"beq ${words[1]}, $zero, {pw[1]}")
            else:
                code.append(f"beq ${words[1]}, $zero, else")
                code.append("else:")
                code.append(f"NOP")
        elif "go" in linha:
            p = codigo[i-1]
            if "if" not in p:
                linha = linha.replace(")", " ")
                linha = linha.replace("(", " ")
                linha = linha.replace("go to", "goto")
                words = linha.split(" ")
                code.append(f"b {words[1]}")
            continue
    code.append("SYSCALL 0")        
    return data, code