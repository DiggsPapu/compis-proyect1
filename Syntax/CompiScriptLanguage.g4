grammar Compiscript;

program: declaration* EOF ;

declaration: 
    classDecl # classDecl
    |   funDecl # funDecl
    |   varDecl # varDecl
    |   statement # statement
    ;

classDecl: 'class' IDENTIFIER ('<' IDENTIFIER)? '{' function* '}'
;

funDecl: 'fun' function
;

varDecl: 'var' IDENTIFIER ('=' expression)? ';'
;

statement: 
    exprStmt # exprStmt
    | forStmt # forStmt
    | ifStmt # ifStmt
    | printStmt # printStmt
    | returnStmt # returnStmt
    | whileStmt # whileStmt
    | block # block
    ;

exprStmt:
    expression ';'
    ;

forStmt:
    'for' '(' (varDecl | exprStmt | ';') expression? ';' expression? ')' statement
    ;

ifStmt:
    'if' '(' expression ')' statement ('else' statement)?
    ;

printStmt: 
    'print' expression ';'
    ;

returnStmt: 
    'return' expression? ';'
    ;

whileStmt: 
    'while' '(' expression ')' statement
    ;

block: '{' '(' expression ')' '}' statement
    ;

expression:
    assignment
    ;

assignment:
    (call '.')? IDENTIFIER '=' assignment
    | logic_or
    ;

logic_or:
    logic_and ('or' logic_and)*
    ;

logic_and: 
    equality ('and' equality)*
    ;

equality: 
    comparison (( '!=' | '==' ) comparison)*
    ;

comparison: 
    term (( '>' | '>=' | '<' | '<=' ) term)*
    ;

term: 
    factor (( '-' | '+' ) factor)* 
    ;

factor: 
    unary (( '/' | '*' ) unary)* 
    ;

unary: 
    ( '!' | '-' ) unary
    | call 
    ;

call: 
    primary ( '(' arguments? ')' | '.' IDENTIFIER )*
    ;
primary: 
    'true'
    | 'false'
    | 'nil'
    | 'this'
    | NUMBER
    | STRING
    | IDENTIFIER
    | '(' expression ')'
    | 'super' '.' IDENTIFIER
    ;

function : 
    IDENTIFIER '(' parameters? ')' block
    ;

parameters: 
    IDENTIFIER ( ',' IDENTIFIER )*
    ;

arguments: 
    expression ( ',' expression )*
    ;

NUMBER: 
    DIGIT+ ( '.' DIGIT+ )?
    ;

STRING: 
    '"' (~["\\])* '"' 
    ;
IDENTIFIER:
    ALPHA ( ALPHA | DIGIT )* 
    ;
fragment ALPHA: 
    [a-zA-Z_]
    ;
    
fragment DIGIT: 
    [0-9] 
    ;

WS: 
    [ \t\r\n]+ -> skip 
    ;
