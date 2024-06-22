from ExprListener import ExprListener
from math import fabs

def fatorial(x):
    if x == 0:
        return 1
    return x * fatorial(x-1)

class EvalListener(ExprListener):
    def __init__(self):
        self.stack = []

    def exitMultDiv(self, ctx):
        right = int(self.stack.pop())
        left = int(self.stack.pop())
        if ctx.getChild(1).getText() == '/':
            self.stack.append(left / right)
        else:
            self.stack.append(left * right)

    def exitSomaSub(self, ctx):
        right = int(self.stack.pop())
        left = int(self.stack.pop())
        if ctx.getChild(1).getText() == '+':
            self.stack.append(left + right)
        else:
            self.stack.append(left - right)

    def exitPot(self, ctx):
        right = int(self.stack.pop())
        left = int(self.stack.pop())
        self.stack.append(left ** right)

    def exitAbs_(self, ctx):
        x = self.stack.pop()
        self.stack.append(fabs(x))

    def exitFact(self, ctx):
        x = self.stack.pop()
        self.stack.append(fatorial(int(x)))  
        
    def exitNumber(self, ctx):
        self.stack.append(int(ctx.NUM().getText()))

    def getResult(self):
        return self.stack[0] if self.stack else None
