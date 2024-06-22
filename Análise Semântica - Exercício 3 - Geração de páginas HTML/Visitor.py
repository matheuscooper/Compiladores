from HtmlParser import HtmlParser
from HtmlVisitor import HtmlVisitor


class HtmlOutput():
    def __init__(self):
        self.conteudo = ""
        self.count = 0

    def HtmlOutput(self):
        self.count = 0
        self.conteudo = "<html>\n"
        self.conteudo += "<head><title>Formulario</title></head>\n"
        self.conteudo += "<body>\n"
        self.conteudo += "<form>\n"

    def addText(self, cols, rows, s):
        self.conteudo += s + "<br>\n"
        self.conteudo += "<textarea name='Q" + str(self.count) + "' cols='" + str(cols) + "' rows='" + str(rows) + "'></textarea><br>\n"
        self.conteudo += "<br>\n\n"
        self.count += 1
    
    def addRadio(self, s, options):
        self.conteudo += s + "<br>\n"
        for val in options:
            self.conteudo += "<input type='radio' name='Q" + str(self.count) + "' "
            self.conteudo += "value='" + val + "'>" + val + "<br>\n"
        
        self.conteudo += "<br>\n\n"
        self.count+=1
    
    def addCheckBox(self, s , options):
        self.conteudo += s + "<br>\n"
        
        for val in options: 
            self.conteudo += "<input type='checkbox' name='Q" + str(self.count) + "' "
            self.conteudo += "value='" + val + "'>" + val + "<br>\n"
        self.count+=1    
        
        self.conteudo += "<br>\n\n"

    def addBotao(self, label, alert ):
          self.conteudo += f'<button type="button" onclick="alert(\'{alert}\')">{label}</button><br>\n\n'
          #self.conteudo += hello_world(label,alert)
    
    
    def addCheckMenuBox(self, s, options):
        self.conteudo+= f'<label for="Q{self.count}">{s}</label><br>\n'
        self.conteudo+= f'<select name="Q{self.count}" id="Q{self.count}">\n'

        for i in options:
            self.conteudo += f'<option value="{i}">{i}</option>\n' 
            
        self.conteudo +='</select><br>\n\n'
        self.count+=1  

    def close(self):
        self.conteudo += "</form>\n"
        self.conteudo += "</body>\n"
        self.conteudo += "</html>\n"
        self.geraArquivoHtml('queroDezRomulo.html')
        print(self.conteudo)
        
    #Função que gera o arquivo de saida Html 
    def geraArquivoHtml(self, arquivo):
        with open(arquivo, 'w') as filename:
            filename.write(self.conteudo)

class Visitor(HtmlVisitor):

    def __init__(self):
        self.html = HtmlOutput()

    def visitRoot(self, ctx):
        l = list(ctx.getChildren())
        for questao in l:
            self.visit(questao)

        self.html.close()
       
    def visitQTexto(self, ctx):
        l = list(ctx.getChildren())
        
        if(len(l) == 4):
            cols = l[1].getText()
            rows = l[2].getText()
            string = self.visit(l[3])
            
            self.html.addText(cols, rows, string)

    def visitQRadioBox(self, ctx):
        l = list(ctx.getChildren())
        
        if(len(l) == 3):
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addRadio(string, opcoes)
    
    def visitQCheckBox(self, ctx: HtmlParser.QCheckBoxContext):
        l = list(ctx.getChildren())
        
        if(len(l) == 3):
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addCheckBox(string, opcoes)

    def visitOpcoes(self, ctx):
        l = list(ctx.getChildren())
        qtdStr = (len(l) - 2) // 2 # retirando os '()' e ','
        opcoes = []
        
        for i in range(qtdStr + 1):
            opcoes.append(self.visit(ctx.str_(i)))
        
        return opcoes

    def visitQMenu(self, ctx):
        l = list(ctx.getChildren())
        if(len(l) == 3):
            string = self.visit(l[1])
            opcoes = self.visit(l[2])
            self.html.addCheckMenuBox(string, opcoes)
    
    def visitQBotao(self, ctx):
        l = list(ctx.getChildren())
        if(len(l) == 3):
            label = self.visit(l[1])
            alert = self.visit(l[2])
            self.html.addBotao(label, alert)

    def visitStr_(self, ctx):
        l = list(ctx.getChildren())
        string = l[0].getText().replace('"','')
        return string
