import ply.yacc as yacc
import ply.lex as lex
import json

# Lexer part (as you provided)

tokens = (
   'ID',     
   'PLUS',   
   'TIMES',  
   'LPAREN',
   'RPAREN', 
)

t_PLUS    = r'\+'   
t_TIMES   = r'\*'   
t_LPAREN  = r'\('   
t_RPAREN  = r'\)'   

def t_ID(t):
    r'id'           
    t.value = "identifier" 
    return t  

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)  

lexer = lex.lex()

# Parser part

# Parser rule for addition
def p_expression_plus(p):
    'E : E PLUS T'     
    p[0] = {"type": "binary-op", "op": "+", "left": p[1], "right": p[3]}  

def p_expression_E(p):
    'E : T'            
    p[0] = p[1]         

# Parser rule for multiplication
def p_term_times(p):
    'T : T TIMES F'     
    p[0] = {"type": "binary-op", "op": "*", "left": p[1], "right": p[3]}  

def p_term_T(p):
    'T : F'             
    p[0] = p[1]         

def p_factor_expr(p):
    'F : LPAREN E RPAREN'   
    p[0] = p[2]             

def p_factor_id(p):
    'F : ID'            
    p[0] = {"type": "id", "value": p[1]}  

# This function is called when the parser encounters a syntax error
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Test
data = "(id+id)*id"

# Parsing the test data
result = parser.parse(data)

# Outputting the result as a formatted JSON string to visualize the Abstract Syntax Tree (AST)
json_output = json.dumps(result, indent=2)
print(json_output)

