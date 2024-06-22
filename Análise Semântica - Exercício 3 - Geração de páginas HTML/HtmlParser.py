# Generated from Html.g by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,65,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,1,1,1,1,1,
        1,3,1,29,8,1,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,5,7,56,8,7,10,7,
        12,7,59,9,7,1,7,1,7,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,0,
        61,0,19,1,0,0,0,2,28,1,0,0,0,4,30,1,0,0,0,6,35,1,0,0,0,8,39,1,0,
        0,0,10,43,1,0,0,0,12,47,1,0,0,0,14,51,1,0,0,0,16,62,1,0,0,0,18,20,
        3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,
        22,1,1,0,0,0,23,29,3,4,2,0,24,29,3,6,3,0,25,29,3,8,4,0,26,29,3,10,
        5,0,27,29,3,12,6,0,28,23,1,0,0,0,28,24,1,0,0,0,28,25,1,0,0,0,28,
        26,1,0,0,0,28,27,1,0,0,0,29,3,1,0,0,0,30,31,5,1,0,0,31,32,5,9,0,
        0,32,33,5,9,0,0,33,34,3,16,8,0,34,5,1,0,0,0,35,36,5,2,0,0,36,37,
        3,16,8,0,37,38,3,14,7,0,38,7,1,0,0,0,39,40,5,3,0,0,40,41,3,16,8,
        0,41,42,3,14,7,0,42,9,1,0,0,0,43,44,5,4,0,0,44,45,3,16,8,0,45,46,
        3,14,7,0,46,11,1,0,0,0,47,48,5,5,0,0,48,49,3,16,8,0,49,50,3,16,8,
        0,50,13,1,0,0,0,51,52,5,6,0,0,52,57,3,16,8,0,53,54,5,7,0,0,54,56,
        3,16,8,0,55,53,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,
        58,60,1,0,0,0,59,57,1,0,0,0,60,61,5,8,0,0,61,15,1,0,0,0,62,63,5,
        10,0,0,63,17,1,0,0,0,3,21,28,57
    ]

class HtmlParser ( Parser ):

    grammarFileName = "Html.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'TEXTO'", "'ESCOLHAUMA'", "'ESCOLHAVARIAS'", 
                     "'MENU'", "'BOTAO'", "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "NUMERO", "STRING", "IGNORE", "COMMENT" ]

    RULE_root = 0
    RULE_questao = 1
    RULE_qTexto = 2
    RULE_qRadioBox = 3
    RULE_qCheckBox = 4
    RULE_qMenu = 5
    RULE_qBotao = 6
    RULE_opcoes = 7
    RULE_str_ = 8

    ruleNames =  [ "root", "questao", "qTexto", "qRadioBox", "qCheckBox", 
                   "qMenu", "qBotao", "opcoes", "str_" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    NUMERO=9
    STRING=10
    IGNORE=11
    COMMENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def questao(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HtmlParser.QuestaoContext)
            else:
                return self.getTypedRuleContext(HtmlParser.QuestaoContext,i)


        def getRuleIndex(self):
            return HtmlParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = HtmlParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.questao()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 62) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QuestaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def qTexto(self):
            return self.getTypedRuleContext(HtmlParser.QTextoContext,0)


        def qRadioBox(self):
            return self.getTypedRuleContext(HtmlParser.QRadioBoxContext,0)


        def qCheckBox(self):
            return self.getTypedRuleContext(HtmlParser.QCheckBoxContext,0)


        def qMenu(self):
            return self.getTypedRuleContext(HtmlParser.QMenuContext,0)


        def qBotao(self):
            return self.getTypedRuleContext(HtmlParser.QBotaoContext,0)


        def getRuleIndex(self):
            return HtmlParser.RULE_questao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQuestao" ):
                listener.enterQuestao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQuestao" ):
                listener.exitQuestao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQuestao" ):
                return visitor.visitQuestao(self)
            else:
                return visitor.visitChildren(self)




    def questao(self):

        localctx = HtmlParser.QuestaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_questao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 23
                self.qTexto()
                pass
            elif token in [2]:
                self.state = 24
                self.qRadioBox()
                pass
            elif token in [3]:
                self.state = 25
                self.qCheckBox()
                pass
            elif token in [4]:
                self.state = 26
                self.qMenu()
                pass
            elif token in [5]:
                self.state = 27
                self.qBotao()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QTextoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self, i:int=None):
            if i is None:
                return self.getTokens(HtmlParser.NUMERO)
            else:
                return self.getToken(HtmlParser.NUMERO, i)

        def str_(self):
            return self.getTypedRuleContext(HtmlParser.Str_Context,0)


        def getRuleIndex(self):
            return HtmlParser.RULE_qTexto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQTexto" ):
                listener.enterQTexto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQTexto" ):
                listener.exitQTexto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQTexto" ):
                return visitor.visitQTexto(self)
            else:
                return visitor.visitChildren(self)




    def qTexto(self):

        localctx = HtmlParser.QTextoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_qTexto)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(HtmlParser.T__0)
            self.state = 31
            self.match(HtmlParser.NUMERO)
            self.state = 32
            self.match(HtmlParser.NUMERO)
            self.state = 33
            self.str_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QRadioBoxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_(self):
            return self.getTypedRuleContext(HtmlParser.Str_Context,0)


        def opcoes(self):
            return self.getTypedRuleContext(HtmlParser.OpcoesContext,0)


        def getRuleIndex(self):
            return HtmlParser.RULE_qRadioBox

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQRadioBox" ):
                listener.enterQRadioBox(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQRadioBox" ):
                listener.exitQRadioBox(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQRadioBox" ):
                return visitor.visitQRadioBox(self)
            else:
                return visitor.visitChildren(self)




    def qRadioBox(self):

        localctx = HtmlParser.QRadioBoxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_qRadioBox)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(HtmlParser.T__1)
            self.state = 36
            self.str_()
            self.state = 37
            self.opcoes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QCheckBoxContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_(self):
            return self.getTypedRuleContext(HtmlParser.Str_Context,0)


        def opcoes(self):
            return self.getTypedRuleContext(HtmlParser.OpcoesContext,0)


        def getRuleIndex(self):
            return HtmlParser.RULE_qCheckBox

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQCheckBox" ):
                listener.enterQCheckBox(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQCheckBox" ):
                listener.exitQCheckBox(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQCheckBox" ):
                return visitor.visitQCheckBox(self)
            else:
                return visitor.visitChildren(self)




    def qCheckBox(self):

        localctx = HtmlParser.QCheckBoxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_qCheckBox)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(HtmlParser.T__2)
            self.state = 40
            self.str_()
            self.state = 41
            self.opcoes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QMenuContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_(self):
            return self.getTypedRuleContext(HtmlParser.Str_Context,0)


        def opcoes(self):
            return self.getTypedRuleContext(HtmlParser.OpcoesContext,0)


        def getRuleIndex(self):
            return HtmlParser.RULE_qMenu

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQMenu" ):
                listener.enterQMenu(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQMenu" ):
                listener.exitQMenu(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQMenu" ):
                return visitor.visitQMenu(self)
            else:
                return visitor.visitChildren(self)




    def qMenu(self):

        localctx = HtmlParser.QMenuContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_qMenu)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.match(HtmlParser.T__3)
            self.state = 44
            self.str_()
            self.state = 45
            self.opcoes()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class QBotaoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HtmlParser.Str_Context)
            else:
                return self.getTypedRuleContext(HtmlParser.Str_Context,i)


        def getRuleIndex(self):
            return HtmlParser.RULE_qBotao

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterQBotao" ):
                listener.enterQBotao(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitQBotao" ):
                listener.exitQBotao(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitQBotao" ):
                return visitor.visitQBotao(self)
            else:
                return visitor.visitChildren(self)




    def qBotao(self):

        localctx = HtmlParser.QBotaoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_qBotao)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(HtmlParser.T__4)
            self.state = 48
            self.str_()
            self.state = 49
            self.str_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OpcoesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def str_(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HtmlParser.Str_Context)
            else:
                return self.getTypedRuleContext(HtmlParser.Str_Context,i)


        def getRuleIndex(self):
            return HtmlParser.RULE_opcoes

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOpcoes" ):
                listener.enterOpcoes(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOpcoes" ):
                listener.exitOpcoes(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOpcoes" ):
                return visitor.visitOpcoes(self)
            else:
                return visitor.visitChildren(self)




    def opcoes(self):

        localctx = HtmlParser.OpcoesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_opcoes)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(HtmlParser.T__5)
            self.state = 52
            self.str_()
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7:
                self.state = 53
                self.match(HtmlParser.T__6)
                self.state = 54
                self.str_()
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 60
            self.match(HtmlParser.T__7)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Str_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(HtmlParser.STRING, 0)

        def getRuleIndex(self):
            return HtmlParser.RULE_str_

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStr_" ):
                listener.enterStr_(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStr_" ):
                listener.exitStr_(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStr_" ):
                return visitor.visitStr_(self)
            else:
                return visitor.visitChildren(self)




    def str_(self):

        localctx = HtmlParser.Str_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_str_)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 62
            self.match(HtmlParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





