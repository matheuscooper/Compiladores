grammar SimpleLang;

prog: stat+ ;

stat: ifStat
    | whileStat
    | assignStat
    | exprStat
    ;

ifStat: 'if' '(' expr ')' 'then' stat ; 

whileStat: 'while' '(' expr ')' stat;

assignStat: Ident '=' expr ';';

exprStat: expr ';';

expr: expr ('*' |'/') expr 
    | expr ('+' |'-') expr
    | expr ('<' | '>' | '==' | '!=') expr
    | expr ('&&' | '||') expr
    | '!=' expr
    | Ident
    | INT
    | '(' expr ')'
    ;

    Ident: [a-zA-Z_] [a-zA-Z_0-9]* ;
    INT: [0-9]+ ;
    WS : [ \t\r\n]+ -> skip; 