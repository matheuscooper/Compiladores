grammar MiniC;

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
    : '(' (parameter_declaration (',' parameter_declaration)*)? ')' ;

parameter_declaration
    : tipo declarator ;

function_body
    : '{' data_definition* statement* '}' ;

stat: ifStat
    | whileStat
    | assignStat
    | exprStat
    ;

ifStat: 'if' '(' expr ')' 'then' stat ; 

whileStat: 'while' '(' expr ')' stat;

assignStat: Identifier '=' expr ';';

exprStat: expr ';';

statement
    :expression? ';'
    | 'if' '(' expression ')' statement ('then' statement)?
    | 'while' '(' expression ')' (statement)
    | 'break' ';'
    | 'continue' ';'
    | 'return' expression? ';'
    ;

expr
    : expr ('*' |'/') expr
    | expr ('+' |'-') expr
    | expr ('<' | '>' | '==' | '!=') expr
    | expr ('&&' | '||') expr
    | '!=' expr
    | Identifier
    | CONSTANT_INT
    | CONSTANT_CHAR
    | '(' expr ')'
    ;

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

CONSTANT_INT
    : [0-9]+ ;

CONSTANT_CHAR
    : '\'' . '\'' ;

INT: [0-9]+ ;

WS
    : [ \t\r\n]+ -> skip ;