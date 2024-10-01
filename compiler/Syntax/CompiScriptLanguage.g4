grammar CompiScriptLanguage;

program: declaration* EOF ;

declaration: 
    classDecl
    |   funDecl
    |   varDecl
    |   statement
    ;

classDecl: 'class' IDENTIFIER ('extends' IDENTIFIER)? '{' function* '}'
;

funDecl: 'fun' function
;

varDecl: 'var' IDENTIFIER ('=' expression)? ';'
;

statement: 
    exprStmt
    | ifStmt
    | forStmt
    | whileStmt
    | printStmt
    | returnStmt
    | block
    ;

exprStmt: expression ';' ;

ifStmt: 'if' '(' expression ')' block ('else if' '(' expression ')' block)* ('else' block)? ;

forStmt: 'for' '(' (varDecl | exprStmt | ';') expression? ';' expression? ')' block ;

whileStmt: 'while' '(' expression ')' block ;

printStmt: 'print' expression ';' ;

returnStmt: 'return' expression? ';' ;

block: '{' declaration* '}' ;

expression: (call '.')? IDENTIFIER '=' ( expression | logic | array ) ;

array: '[' (logic)* ']' ;

logic: comparison (( 'and'| 'or' ) comparison)* ;

comparison: term (( '>' | '>=' | '<' | '<='| '!=' | '==' ) term)* ;

term: unary (( '-' | '+' | '/' | '*' | '%' ) unary)* ;

unary: ( '!' | '-' ) unary | call ;

call: 'new'? primary ( '(' arguments? ')' | '.' IDENTIFIER )* ;

primary: 'true' | 'false' | 'nil' | 'this' | 'break' | 'continue' | NUMBER | STRING | IDENTIFIER | '(' expression ')' | 'super' '.' IDENTIFIER ;

function : IDENTIFIER '(' parameters? ')' block ;

parameters: IDENTIFIER ( ',' IDENTIFIER )* ;

arguments: expression ( ',' expression )* ;

NUMBER: DIGIT+ ( '.' DIGIT+ )? ;

STRING: '"' (~["\\])* '"' ;

IDENTIFIER: ALPHA ( ALPHA | DIGIT )* ;

fragment ALPHA: [a-zA-Z_] ;

fragment DIGIT: [0-9] ;

WS: [ \t\r\n]+ -> skip ;

// Captura cualquier otro carácter no válido
MALFORMED: . ;
