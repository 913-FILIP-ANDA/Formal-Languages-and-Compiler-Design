%{
#include <stdio.h>
#include <stdlib.h>
#define YYDEBUG 1

%}

%token READ
%token DISPLAY
%token DEFINE
%token INT
%token START
%token STRING
%token CHARACTER
%token IF
%token END
%token THEN
%token DO
%token WHILE
%token STOP
%token ELSE
%token FOR 

%token ASSIGNMENT
%token EQ
%token LT
%token LTE
%token GT
%token GTE
%token NE
%token AND
%token OR
%token NOT


%token IDENTIFIER
%token CONSTANT

%left '+' '-' '*' '/'

%token ADD 
%token SUB
%token DIV 
%token MOD 
%token MUL
%token INCR

%token OPEN_CURLY_BRACKET
%token CLOSED_CURLY_BRACKET 
%token OPEN_ROUND_BRACKET
%token CLOSED_ROUND_BRACKET
%token OPEN_RIGHT_BRACKET
%token CLOSED_RIGHT_BRACKET 

%token COMMA 
%token SEMI_COLON
%token COLON

%start program
%error-verbose

%%

program : START OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET END 
		;
statement_list : statement | statement statement_list 
			   ;
statement : simple_statement | if_stmt | while_stmt | for_stmt
		  ;	  
simple_statement : declaration | io_stmt | assignment_stmt
				 ;
declaration : DEFINE type COLON IDENTIFIER SEMI_COLON
			;		
type : simple_type
	;
simple_type : INT | STRING | CHARACTER
			;
io_stmt : READ COLON IDENTIFIER SEMI_COLON | DISPLAY OPEN_ROUND_BRACKET IDENTIFIER CLOSED_ROUND_BRACKET SEMI_COLON | DISPLAY OPEN_ROUND_BRACKET CONSTANT CLOSED_ROUND_BRACKET SEMI_COLON
		;
assignment_stmt : IDENTIFIER ASSIGNMENT expression SEMI_COLON
				;
expression : expression ADD term | expression SUB term | expression INCR term | expression MUL term | term
		   ;
term : term MUL factor | term DIV factor | term MOD factor | factor
	 ;
factor : OPEN_ROUND_BRACKET expression CLOSED_ROUND_BRACKET | IDENTIFIER | CONSTANT
	   ;
if_stmt : IF condition THEN OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET | IF condition THEN OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET ELSE OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET
		;
condition : expression relation expression
		  ;
relation : EQ | NE | LT | LTE | GT | GTE | AND | OR | NOT 
		 ;
while_stmt : WHILE OPEN_ROUND_BRACKET condition CLOSED_ROUND_BRACKET DO OPEN_CURLY_BRACKET statement_list CLOSED_CURLY_BRACKET STOP
		   ;
for_stmt : FOR IDENTIFIER ASSIGNMENT CONSTANT COMMA IDENTIFIER COMMA CONSTANT COLON statement_list
		 ;
%%

yyerror(char *s)
{
  printf("%s\n", s);
}

extern FILE *yyin;

main(int argc, char **argv)
{
  if(argc>1) yyin = fopen(argv[1], "r");
  if((argc>2)&&(!strcmp(argv[2],"-d"))) yydebug = 1;
  if(!yyparse()) fprintf(stderr,"\tO.K.\n");
}