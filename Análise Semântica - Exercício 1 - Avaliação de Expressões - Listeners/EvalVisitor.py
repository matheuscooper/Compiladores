from ExprVisitor import ExprVisitor
from math import fabs

def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x-1)

class EvalVisitor(ExprVisitor):
    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        print(self.visit(l[0]))
        return self.visit(l[0])

    def visitNumber(self, ctx):
        return int(ctx.NUM().getText())

    def visitFact(self, ctx):
        l = list(ctx.getChildren())
        return fatorial(int(self.visit(l[2])))
    
    def visitAbs_(self, ctx):
        l = list(ctx.getChildren())
        return fabs(self.visit(l[2]))

    def visitPot(self, ctx):
        l = list(ctx.getChildren())
        return int(self.visit(l[0])) ** int(self.visit(l[2]))

    def visitSomaSub(self, ctx):
        l = list(ctx.getChildren())
        left = self.visit(l[0])
        right = self.visit(l[2])
        if ctx.getChild(1).getText() == '+':
            return left + right
        else:
            return left - right

    def visitMultDiv(self, ctx):
        l = list(ctx.getChildren())
        left = self.visit(l[0])
        right = self.visit(l[2])
        if ctx.getChild(1).getText() == '/':
            return left / right
        else:
            return left * right

    def visitParent(self, ctx):
        return self.visit(ctx.expr())
