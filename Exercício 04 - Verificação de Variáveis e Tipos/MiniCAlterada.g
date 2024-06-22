grammar MiniC;

program
    : definition+ ;

definition
    : data_definition
    | function_definition ;

data_definition
    : ('int' | 'char') declarator (',' declarator)* ';' ;

declarator
    : Identifier ;

function_definition
    : ('int' | 'char')? function_header function_body ; // tipos de retorno int ou char

function_header
    : declarator parameter_list ;

parameter_list
    : '(' (parameter_declaration (',' parameter_declaration)*)? ')' ;

parameter_declaration
    : ('int' | 'char') declarator ;

function_body
    : '{' data_definition* statement* '}' ;

statement
    : (expression? ';' 
    | 'if' '(' expression ')' statement ( 'else' statement )?
    | 'while' '(' expression ')' statement
    | 'break' ';'
    | 'continue' ';'
    | 'return' expression? ';' ) ;

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
    : '++' Identifier 
    | '--' Identifier 
    | primary ;

primary
    : Identifier
    | CONSTANT_INT
    | CONSTANT_CHAR
    | '(' expression ')'
    | Identifier '(' (argument_list)? ')' ;

argument_list
    : binary (',' binary)* ;

Identifier
    : [a-zA-Z_][a-zA-Z0-9_]* ;

CONSTANT_INT
    : [0-9]+ ;
## na anterior eu nao sabia que a constante era assim a gente ver isso no slide 4 de Semantica
CONSTANT_CHAR
    : '\'' . '\'' ;

WS
    : [ \t\r\n]+ -> skip ;
