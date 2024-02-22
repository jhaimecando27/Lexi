# Syntax Analyzer Logic
from grammar import cfg, first_set, follow_set, predict_set


# For checking the syntax of the program
def syntax_analysis(programs):
    results = []
    err = "SYNTAX ERROR"

    for program in programs:
        if program[0] == "<space>":
            programs.remove(program)

    programs.append(("EPSILON", "EPSILON"))

    lexeme, token = zip(*programs)

    print(programs)
    print(lexeme)
    print(token)

    print(len(lexeme))

    i = 0
    if lexeme[i] == "seed":
        print(str(i) + ": have seed")
        i += 1

        # Global
        while True:
            # puro global
            if i < len(lexeme) and lexeme[i] == "floral":
                print(str(i) + ": have floral")
                i += 1
                if i < len(lexeme) and lexeme[i][0] == "#":
                    print(str(i) + ": have global")
                    i += 3
                else:
                    results.append(("floral error", err))
                    return results
            else:
                break

        # garden () (
        if i < len(lexeme) and lexeme[i] == "garden":
            print(str(i) + ": have garden")
            i += 2
            if i < len(lexeme) and lexeme[i] == "(":
                i += 1

                # <statement>
                while True:
                    # <local-variable>
                    if program[i] in first_set["<local-variable>"]:

                        # identifier
                        if i < len(lexeme) and lexeme[i][0] == "#":
                            print(str(i) + ": have local")
                            i += 2

                            # value
                            if program[i] == "=":
                                i += 1
                                if "LIT" in token[i]:
                                    i += 1
                                else:
                                    results.append(("literal error", err))
                                    return results
                        else:
                            results.append(("local error", err))
                            return results

                        while True:
                            # identifier
                            if i < len(lexeme) and lexeme[i][0] == "#":
                                print(str(i) + ": have local")
                                i += 2

                                # value
                                if program[i] == "=":
                                    i += 1
                                    if "LIT" in token[i]:
                                        i += 1
                                    else:
                                        results.append(("literal error", err))
                                        return results
                            else:
                                break

        print(str(i) + ": end = " + lexeme[i])
    else:
        results.append(("seed missing", err))

    return results

# For displaying the Parse Tree


def display_tree():
    pass

# For displaying the token stream e.g., tint a; == reserved word identifier reserved symbol


def token_stream():
    pass
