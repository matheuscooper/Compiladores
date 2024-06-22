# Generated from Html.g by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,100,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,1,0,1,0,
        1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,
        1,3,1,4,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,4,8,75,8,
        8,11,8,12,8,76,1,9,1,9,5,9,81,8,9,10,9,12,9,84,9,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,11,1,11,5,11,94,8,11,10,11,12,11,97,9,11,1,11,1,
        11,0,0,12,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,
        12,1,0,4,1,0,48,57,1,0,34,34,3,0,9,10,13,13,32,32,2,0,10,10,13,13,
        102,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,
        0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
        0,21,1,0,0,0,0,23,1,0,0,0,1,25,1,0,0,0,3,31,1,0,0,0,5,42,1,0,0,0,
        7,56,1,0,0,0,9,61,1,0,0,0,11,67,1,0,0,0,13,69,1,0,0,0,15,71,1,0,
        0,0,17,74,1,0,0,0,19,78,1,0,0,0,21,87,1,0,0,0,23,91,1,0,0,0,25,26,
        5,84,0,0,26,27,5,69,0,0,27,28,5,88,0,0,28,29,5,84,0,0,29,30,5,79,
        0,0,30,2,1,0,0,0,31,32,5,69,0,0,32,33,5,83,0,0,33,34,5,67,0,0,34,
        35,5,79,0,0,35,36,5,76,0,0,36,37,5,72,0,0,37,38,5,65,0,0,38,39,5,
        85,0,0,39,40,5,77,0,0,40,41,5,65,0,0,41,4,1,0,0,0,42,43,5,69,0,0,
        43,44,5,83,0,0,44,45,5,67,0,0,45,46,5,79,0,0,46,47,5,76,0,0,47,48,
        5,72,0,0,48,49,5,65,0,0,49,50,5,86,0,0,50,51,5,65,0,0,51,52,5,82,
        0,0,52,53,5,73,0,0,53,54,5,65,0,0,54,55,5,83,0,0,55,6,1,0,0,0,56,
        57,5,77,0,0,57,58,5,69,0,0,58,59,5,78,0,0,59,60,5,85,0,0,60,8,1,
        0,0,0,61,62,5,66,0,0,62,63,5,79,0,0,63,64,5,84,0,0,64,65,5,65,0,
        0,65,66,5,79,0,0,66,10,1,0,0,0,67,68,5,40,0,0,68,12,1,0,0,0,69,70,
        5,44,0,0,70,14,1,0,0,0,71,72,5,41,0,0,72,16,1,0,0,0,73,75,7,0,0,
        0,74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,18,
        1,0,0,0,78,82,5,34,0,0,79,81,8,1,0,0,80,79,1,0,0,0,81,84,1,0,0,0,
        82,80,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,82,1,0,0,0,85,86,5,
        34,0,0,86,20,1,0,0,0,87,88,7,2,0,0,88,89,1,0,0,0,89,90,6,10,0,0,
        90,22,1,0,0,0,91,95,5,35,0,0,92,94,8,3,0,0,93,92,1,0,0,0,94,97,1,
        0,0,0,95,93,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,95,1,0,0,0,98,
        99,6,11,0,0,99,24,1,0,0,0,4,0,76,82,95,1,6,0,0
    ]

class HtmlLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    NUMERO = 9
    STRING = 10
    IGNORE = 11
    COMMENT = 12

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'TEXTO'", "'ESCOLHAUMA'", "'ESCOLHAVARIAS'", "'MENU'", "'BOTAO'", 
            "'('", "','", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMERO", "STRING", "IGNORE", "COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "NUMERO", "STRING", "IGNORE", "COMMENT" ]

    grammarFileName = "Html.g"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


