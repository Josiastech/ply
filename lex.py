#------------------------------------------------------------
# lex.py
#
# tokenizer
# ------------------------------------------------------------

import ply.lex as lex

# List of token names.   
tokens = ('QUOTE', 'SIMB', 'NUM', 'LPAREN', 'RPAREN', \
'NIL', 'TRUE', 'FALSE', 'TEXT')

# Reserved words
reserved = {
    'nil' : 'NIL',
}

# Regular expression rules for simple tokens
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_QUOTE = r'\''
t_TRUE = r'\#t'
t_FALSE = r'\#f'

def t_NUM(t):
    r'\d+'
    try:
        t.value = int(t.value)    
    except ValueError:
        print "Line %d: Number %s is too large!" % (t.lineno,t.value)
        t.value = 0
    return t

def t_SIMB(t):
    r'[a-zA-Z_+=\*\-][a-zA-Z0-9_+\*\-]*'
    t.type = reserved.get(t.value,'SIMB')    # Check for reserved words
    return t

def t_TEXT(t):
    r'\'[a-zA-Z0-9_+\*\- :,]*\''
    t.type = reserved.get(t.value,'TEXT')    # Check for reserved words
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print "Illegal character '%s'" % t.value[0]
    t.lexer.skip(1)

# Build the lexer
lex.lex()

if __name__ == '__main__':
    lex.runmain()
