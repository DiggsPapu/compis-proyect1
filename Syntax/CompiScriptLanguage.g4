grammar CompiScriptLanguage;

program: declaration* EOF ;

declaration: 
    classDecl
    |   funDecl
    |   varDecl
    |   statement
    ;

classDecl: 'class' IDENTIFIER ('<' IDENTIFIER)? '{' function* '}'
;

funDecl: 'fun' function
;

varDecl: 'var' IDENTIFIER ('=' expression)? ';'
;

statement: 
    exprStmt
    | forStmt
    | ifStmt
    | printStmt
    | returnStmt
    | whileStmt
    | block
    ;

exprStmt: expression ';' ;

forStmt: 'for' '(' (varDecl | exprStmt | ';') expression? ';' expression? ')' statement ;

ifStmt: 'if' '(' expression ')' statement ('else' statement)? ;

printStmt: 'print' expression ';' ;

returnStmt: 'return' expression? ';' ;

whileStmt: 'while' '(' expression ')' statement ;

block: '{' declaration* '}' ;

expression: (call '.')? IDENTIFIER '=' expression | logic  ;

logic: comparison (( 'and'| 'or' ) comparison)* ;

comparison: term (( '>' | '>=' | '<' | '<='| '!=' | '==' ) term)* ;

term: unary (( '-' | '+' | '/' | '*' | '%' ) unary)* ;

unary: ( '!' | '-' ) unary | call ;

call: primary ( '(' arguments? ')' | '.' IDENTIFIER )* ;

primary: 'true' | 'false' | 'nil' | 'this' | NUMBER | STRING | IDENTIFIER | '(' expression ')' | 'super' '.' IDENTIFIER ;

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
