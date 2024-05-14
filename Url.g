grammar Url;

url : protocol '://' domain (':' port)? '/' path ('?' query)? ('#' frag)?;
path : TOKEN ('/' TOKEN)* ('.' TOKEN)* ;
port : PORTA ;
domain : TOKEN ('.' TOKEN)* ;
query : PARAM ('&' PARAM)* ;
frag : TOKEN+ ('&' TOKEN)* ('#' TOKEN)?;

protocol : 'http' | 'https' | 'ftp' ;
PORTA : [0-9]+ ;
TOKEN : [0-9a-zA-Z]+ ;
PARAM : TOKEN '=' TOKEN ;

WS : [ \t\r\n]+ -> skip ;
