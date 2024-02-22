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
    if lexeme[i] in first_set["<program>"]:
        print(str(i) + ": have <program>")
        i += 1

        # Global
        while True:
            # puro global
            if i < len(lexeme) and lexeme[i] == "floral":
                print(str(i) + ": have floral")
                i += 1

                # constant
                if i < len(lexeme) and lexeme[i] in first_set["<constant>"]:
                    print(str(i) + ": have ")
                    i += 1

                # all-types
                if i < len(lexeme) and lexeme[i] in first_set["<common-type>"]:
                    print(str(i) + ": have common-type")
                    i += 1
                elif i < len(lexeme) and lexeme[i] in first_set["<sqnc-type>"]:
                    print(str(i) + ": have sqnc-type")
                    i += 1
                else:
                    results.append(("all-types error", err))
                    return results

                # identifier
                if i < len(lexeme) and lexeme[i][0] == "#":
                    print(str(i) + ": have identifier")
                    i += 2
                else:
                    results.append(("floral identifier error", err))
                    return results

                while True:
                    # insert variable
                    if lexeme[i] in first_set["<all-assignment>"]:
                        i += 1
                        # flora tint value
                        if "LIT" in lexeme[i]:
                            i += 1
                            # more flora tint
                            while True:
                                if lexeme[i] == ",":
                                    i += 1
                                    if "LIT" in lexeme[i]:
                                        i += 1
                                    else:
                                        results.append(
                                            ("floral more error", err))
                                        return results
                    # string assignment
                    elif lexeme[i] in first_set["<string-assignment>"]:
                        i += 1
                        # all-types
                        if i < len(lexeme) and lexeme[i] in first_set["<common-type>"]:
                            print(str(i) + ": have common-type")
                            i += 1
                        elif i < len(lexeme) and lexeme[i] in first_set["<sqnc-type>"]:
                            print(str(i) + ": have sqnc-type")
                            i += 1
                        else:
                            results.append(("all-types error", err))
                            return results
                    # Insert Variable
                    else:
                        break

            # Global
            else:
                break

        # garden ()
        if i < len(lexeme) and lexeme[i] == "garden":
            print(str(i) + ": have garden")
            i += 1

            if i < len(lexeme) and lexeme[i] == "(":
                print(str(i) + ": have (")
                i += 1
            else:
                results.append(("garden error", err))
                return results

            if i < len(lexeme) and lexeme[i] == ")":
                print(str(i) + ": have )")
                i += 1
            else:
                results.append(("garden error", err))
                return results
        else:
            results.append(("garden error", err))
            return results

        # Statement
        if i < len(lexeme) and lexeme[i] == "(":
            print(str(i) + ": have (")
            i += 1

            # Statement starts here

            if i < len(lexeme) and lexeme[i] == ")":
                print(str(i) + ": have )")
                i += 1
                if i < len(lexeme) and lexeme[i] == ";":
                    print(str(i) + ": have ;")
                    i += 1
    else:
        results.append(("seed missing", err))

    # plant
    if i < len(lexeme) and lexeme[i] == "plant":
        print(str(i) + ": have plant")
        i += 1
    else:
        results.append(("plant error", err))
        return results

    print(str(i) + ": end = " + lexeme[i])

    return results

# For displaying the Parse Tree


def display_tree():
    pass

# For displaying the token stream e.g., tint a; == reserved word identifier reserved symbol


def token_stream():
    pass
