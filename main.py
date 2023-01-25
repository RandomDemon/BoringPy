from interpreter import *

# Define a symbol table to store variable values
symbol_table = {}

def execute(ast):
    for node in ast:
        if node[0] == 'var_declaration':
            symbol_table[node[1]] = node[2]
        elif node[0] == 'output_statement':
            print(symbol_table[node[1]])
        # Additional code for handling loop and x += y statements here

if __name__ == '__main__':
    with open('test.boring', 'r') as f:
        data = f.read()
    ast = parser.parse(data)
    execute(ast)
