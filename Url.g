grammar Url;
url : protocol '://' domain (':' port)? '/' path ('?' query)? ('#' frag)?;
path : TOKEN ('/' TOKEN)* (~'http' | ~'https' | ~'ftp')? ;
port : PORTA ;
domain : TOKEN ('.' TOKEN)* (~'http' | ~'https' | ~'ftp')? ;
query : TOKEN '=' TOKEN ('&' query)? (~'http' | ~'https' | ~'ftp')? ;
frag : TOKEN (~'http' | ~'https' | ~'ftp')? ;

protocol : 'http' | 'https' | 'ftp' ;
PORTA : [0-9]+ ;

TOKEN : [0-9a-zA-Z]+ ;
WS : [ \t\r\n]+ -> skip ;
