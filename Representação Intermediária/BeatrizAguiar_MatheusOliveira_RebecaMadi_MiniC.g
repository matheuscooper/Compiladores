grammar BeatrizAguiar_MatheusOliveira_RebecaMadi_MiniC;

program
    : definition+ 
    | stat+ ;

definition
    : data_definition
    | function_definition ;

data_definition
    : tipo declarator (',' declarator)* ';' ;

declarator
    : Identifier ;

function_definition
    : (tipo)? function_header function_body ;

function_header
    : declarator parameter_list ;

parameter_list
    : '(' (parameter_declaration (',' declarator)*)? ')' ;

parameter_declaration
    : tipo declarator ;

function_body
    : '{' data_definition* statement* '}' ;

statement
    : expression? ';'
    | 'if' '(' expression ')' statement ('else' statement)?
    | 'while' '(' expression ')' (statement)
    | 'break' ';'
    | 'continue' ';'
    | 'return' expression? ';' ;

expression
    : binary (',' binary)* ;

binary
    : Identifier '=' binary
    | Identifier '+=' binary
    | Identifier '-=' binary
    | Identifier '*=' binary
    | Identifier '/=' binary
    | Identifier '%=' binary
    | binary '==' binary
    | binary '!=' binary
    | binary '<' binary
    | binary '<=' binary
    | binary '>=' binary
    | binary '>' binary
    | binary '+' binary
    | binary '-' binary
    | binary '*' binary
    | binary '/' binary
    | binary '%' binary
    | unary ;

unary
    : Identifier '++' 
    | Identifier '--' 
    | primary ;

primary
    : Identifier
    | CONSTANT_INT
    | CONSTANT_CHAR
    | '(' expression ')'
    | Identifier '(' (argument_list)? ')' ;

tipo
    : 'int'
    | 'char' ;

argument_list
    : binary (',' binary)* ;

Identifier
    : [a-zA-Z_][a-zA-Z0-9_]* ;

value
    : CONSTANT_INT
    | CONSTANT_CHAR ;


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
    
CONSTANT_INT
    : [0-9]+ ;

CONSTANT_CHAR
    : '\'' . '\'' ;

WS
    : [ \t\r\n]+ -> skip ;