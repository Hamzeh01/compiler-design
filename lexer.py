import ply.lex as lex

# These tokens represent the different types of symbols that the lexer will recognize.
tokens = (
   'ID',     
   'PLUS',   
   'TIMES',  
   'LPAREN',
   'RPAREN', 
)

# Each of these definitions associates a token with a regular expression pattern
t_PLUS    = r'\+'   
t_TIMES   = r'\*'   
t_LPAREN  = r'\('   
t_RPAREN  = r'\)'   

# This function defines how to recognize and process 'ID' tokens
def t_ID(t):
    r'id'           
    t.value = "identifier" 
    return t  

# This function is invoked when an illegal character is encountered
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)  # Skip the illegal character and continue

# Build the lexer
lexer = lex.lex()

# Test cases
data_0 = 'id+id'
data_1 = 'id+id*(id)'
data_2 = 'id*id'
data_3 = 'id*id*id'
data_4 = '(id+id)*id'

# Input the test data to the lexer
lexer.input(data_1)

# Tokenize
# This loop reads tokens from the lexer and prints them until there are no more tokens
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)
