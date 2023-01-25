import ply.lex as lex
import ply.yacc as yacc

# Define the list of tokens
tokens = ['VAR', 'OUTPUT', 'PLUS', 'EQUALS', 'INTEGER', 'ID']

# Define the lexer rules
def t_VAR(t):
    r'var'
    return t

def t_OUTPUT(t):
    r'output'
    return t

def t_PLUS(t):
    r'\+'
    return t

def t_EQUALS(t):
    r'='
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the parser rules
def p_program(p):
    '''program : statement
               | program statement'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

def p_statement(p):
    '''statement : var_declaration
                | output_statement'''
    p[0] = p[1]

def p_var_declaration(p):
    'var_declaration : VAR ID EQUALS INTEGER'
    p[0] = ('var_declaration', p[2], p[4])

def p_output_statement(p):
    'output_statement : OUTPUT ID'
    p[0] = ('output_statement', p[2])

def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

# Test the lexer and parser
data = 'var x = 5\noutput x'
lexer.input(data)
for token in lexer:
    print(token)

result = parser.parse(data)
print(result)
