import ply.yacc as yacc
import ply.lex as lex

# Lexer part (as you provided)
tokens = ('ID', 'PLUS', 'TIMES', 'LPAREN', 'RPAREN')

t_PLUS = r'\+'
t_TIMES = r'\*'
t_LPAREN = r'\('
t_RPAREN = r'\)'

def t_ID(t):
    r'id'
    t.value = "id"  # Handle identifier
    return t

def t_error(t):
    print("")
    t.lexer.skip(1)

lexer = lex.lex()

# Parser part
def p_expression_plus(p):
    'E : E PLUS T'
    p[0] = ('+', p[1], p[3])

def p_expression_E(p):
    'E : T'
    p[0] = p[1]

def p_term_times(p):
    'T : T TIMES F'
    p[0] = ('*', p[1], p[3])

def p_term_T(p):
    'T : F'
    p[0] = p[1]

def p_factor_expr(p):
    'F : LPAREN E RPAREN'
    p[0] = p[2]

def p_factor_id(p):
    'F : ID'
    p[0] = ('id', p[1])

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Test
data = "id + id * ( id )"
result = parser.parse(data)
print(result)
