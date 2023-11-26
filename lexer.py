
import ply.lex as lex
# List of token names. This is always required
tokens = (
   'ID',
   'PLUS',
   'TIMES',
   'LPAREN',
   'RPAREN',
)

# Regular expression rules for simple tokens
t_PLUS    = r'\+'
t_TIMES   = r'\*'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

# A regular expression rule with some action code
def t_ID(t):
    r'id'
    t.value = "id"  # You might want to do more sophisticated ID handling
    return t

# Error handling rule
def t_error(t):
    print(f"")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test it out
data = '''
id + id * ( id )
'''

# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
