# Syntax Analyzer Logic
from grammar import first_set
from syntaxHelper import insert_variable, statement, function

errors = []
ERR = "E: Syntax Analyzer: "


# For checking the syntax of the program
def syntax_analysis(programs, output):

    programs.append(("EPSILON", "EPSILON"))
    print(programs)

    # remove "<--", "-->", "<space> from the list of tuple in programs
    programs = [
        program
        for program in programs
        if program[0] != "<--"
        and program[0] != "-->"
        and program[0] != "<space>"
        and program[0] != "?"
    ]

    lexeme, token = zip(*programs)

    print(programs)
    print(lexeme)
    print(token)

    i = 0

    # ---------- # seed # ---------- #
    if lexeme[0] == "seed":
        i += 1
        print("1: seed")
    else:
        errors.append(ERR + "seed not found")
        return errors

    # ---------- # <global> # ---------- #
    if lexeme[i] == "floral":

        while True:
            # floral
            if lexeme[i] == "floral":
                print("2: floral")
                i += 1
            else:
                break

            # <constant>
            if lexeme[i] == "hard":
                print("4: hard")
                i += 1
            else:
                print("5: EPSILON")

            # <insert-variable>
            i = insert_variable(lexeme, token, i)

            # ;
            if lexeme[i] == ";":
                i += 1
                print("2: ;")
            else:
                errors.append(ERR + "; not found")
                return errors

    # ---------- # garden # ---------- #
    if lexeme[i] == "garden":
        print("1: garden")
        i += 1

        # (
        if lexeme[i] == "(":
            print("1: (")
            i += 1
        else:
            errors.append(ERR + "( not found")
            return errors

        # )
        if lexeme[i] == ")":
            print("1: )")
            i += 1
        else:
            errors.append(ERR + ") not found")
            return errors

        # (
        if lexeme[i] == "(":
            print("1: (")
            i += 1
        else:
            errors.append(ERR + "( not found")
            return errors

        # <statement>
        if lexeme[i] in first_set["<statement>"]:
            print("1: statement")
            i = statement(lexeme, token, i)

        # )
        if lexeme[i] == ")":
            print("1: )")
            i += 1
        else:
            errors.append(ERR + ") not found")
            return errors
        # ;
        if lexeme[i] == ";":
            i += 1
            print("1: ;")
        else:
            errors.append(ERR + "; not found")
            return errors
    else:
        output.insert("end", ERR + "garden not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # <function> # ---------- #
    if lexeme[i] in first_set["<function>"]:
        i = function(lexeme, token, i)

    # ---------- # plant # ---------- #
    if lexeme[i] == "plant":
        i += 1
        print("plant found")
    else:
        output.insert("end", ERR + "plant not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]

    if lexeme[i] != "EPSILON":
        output.insert("end", ERR + "Excess Code \n")


# For displaying the Parse Tree
def display_tree():
    pass


# For displaying the token stream e.g., tint a; == reserved word identifier reserved symbol
def token_stream():
    pass
