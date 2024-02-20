# Syntax Analyzer Logic
from grammar import cfg, first_set, follow_set, predict_set


# For checking the syntax of the program
def syntax_analysis(program):
    results = []
    lexeme, token = zip(*program)

    print(program)
    print(lexeme)
    print(token)

    return results

# For displaying the Parse Tree
def display_tree():
    pass

# For displaying the token stream e.g., tint a; == reserved word identifier reserved symbol
def token_stream():
    pass
