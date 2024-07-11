from SimpleLangParser import SimpleLangParser
from SimpleLangVisitor import SimpleLangVisitor


class ThreeAddressCodeVisitor(SimpleLangVisitor):
    temp_count = 0

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"
    
    def visitProg(self, ctx:SimpleLangParser.ProgContext): ## Adaptar depois por que eu gerei sem compilar a
        for stat in ctx.stat():
            self.visit(stat)
    
    def visitStat(self, ctx:SimpleLangParser.StatContext):
        return self.visitChildren(ctx)
    
    def visitIfStat(self, ctx:SimpleLangParser.IfStatContext):
        cond = self.visit(ctx.expr())
        then_label = self.new_temp()
        end_label = self.new_temp()
        print(f"if {cond} goto {then_label}\ngoto {end_label}\n{then_label}:\n")
        self.visit(ctx.stat())
        print(f"{end_label}:\n")
        return
    def visitWhileStat(self, ctx:SimpleLangParser.WhileStatContext):
        start_label = self.new_temp()
        middle_label = self.new_temp()
        end_label = self.new_temp()
        print(f"{start_label}:\n")
        cond = self.visit(ctx.expr())
        print(f"if {cond} goto {middle_label}\ngoto {end_label}\n{middle_label}:\n")
        self.visit(ctx.stat())
        print(f"goto {start_label}\n{end_label}:\n")
        return
    
    def visitAssignStat(self, ctx:SimpleLangParser.ExprStatContext):
        value = self.visit(ctx.expr())
        code = f"{ctx.Ident().getText()}= {value};"
        print(code)
        return code
    
    def visitExprStat(self, ctx:SimpleLangParser.ExprStatContext):
        expr = self.visit(ctx.expr())
        print(expr)
        return expr
    
    def visitExpr(self, ctx: SimpleLangParser.ExprContext):
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
            #print(f"{temp} = !{expr}")
            return temp
        elif ctx.Ident():
            return ctx.Ident().getText()
        elif ctx.INT():
            return ctx.INT().getText()
        else:
            return self.visit(ctx.expr(0))
    
    def visitIdentExpr(self, ctx:SimpleLangParser.ExprContext):
        return ctx.Ident().getText()
    
    def visitIntExpr(self, ctx:SimpleLangParser.ExprContext):
        return ctx.INT().getText()
    
    def visitParentExpr(self, ctx:SimpleLangParser.ExprContext):
        return self.visit(ctx.expr())