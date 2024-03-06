# Syntax Analyzer Logic
from grammar import cfg, first_set, follow_set, predict_set
from syntaxHelper import statement, insert_flora_tint, insert_variable, D2_parameter, all_type_value, common_data


# For checking the syntax of the program
def syntax_analysis(programs, output):
    results = []
    err = "E: Syntax Analyzer: "

    programs.append(("EPSILON", "EPSILON"))
    print(programs)

    # remove "<--", "-->", "<space> from the list of tuple in programs
    programs = [program for program in programs if program[0] != "<--" and program[0]
                != "-->" and program[0] != "<space>" and program[0] != "?"]

    lexeme, token = zip(*programs)

    print(programs)

    i = 0

    # ---------- # seed # ---------- #
    if lexeme[0] != "seed":
        output.insert("end", err + "seed not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]
    i += 1
    print("seed found")

    # ---------- # <global> # ---------- #
    if lexeme[i] != "EPSILON" and lexeme[i] == "floral":
        print("floral found")
        while True:
            # floral
            if lexeme[i] == "floral":
                i += 1

                # <constant>
                if lexeme[i] == "hard":
                    print("hard found")
                    i += 1

                # <all-types>
                if lexeme[i] not in first_set["<all-types>"]:
                    output.insert("end", err + "all-types not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("all-types found")

                # #identifier
                if lexeme[i] != "#":
                    output.insert("end", err + "identifier not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 2  # skip hashtag and identifier name
                print("identifier found")

                # <insert-variable>
                i, results = insert_variable(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return results
                print("insert-variable found")

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("; found")
            else:
                break

    # ---------- # garden # ---------- #
    if lexeme[i] == "garden":
        i += 1

        # (
        if lexeme[i] != "(":
            output.insert("end", err + "( not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]
        i += 1
        print("( found")

        # )
        if lexeme[i] != ")":
            output.insert("end", err + ") not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]
        i += 1
        print(") found")

        # (
        if lexeme[i] != "(":
            output.insert("end", err + "( not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]
        i += 1
        print("( found")

        # <statement>
        i, results = statement(lexeme, token, i, output)
        if "SYNTAX ERROR" in results:
            return results
        print("statement found")

        # )
        if lexeme[i] != ")":
            output.insert("end", err + ") not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]
        i += 1
        print(") found")

        # ;
        if lexeme[i] != ";":
            output.insert("end", err + "; not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]
        i += 1
        print("; found")
    else:
        output.insert("end", err + "garden not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # <function> # ---------- #
    if lexeme[i] in first_set["<function>"]:
        print("function found")
        while True:
            if lexeme[i] not in first_set["<function>"]:
                break

            if lexeme[i] in first_set["<common-type>"]:
                i += 1
                print("common-type found")

                # identifier
                if lexeme[i] != "#":
                    output.insert("end", err + "identifier not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 2
                print("identifier found")

                # (
                if lexeme[i] != "(":
                    output.insert("end", err + "( not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("( found")

                # <insert-parameter>
                if lexeme[i] in first_set["<insert-parameter>"]:
                    print("insert-parameter found")
                    # <keyword-param>
                    if lexeme[i] in first_set["<keyword-param>"]:
                        print("keyword-param found")
                        while True:
                            if lexeme[i] not in first_set["<keyword-param>"]:
                                break
                            if lexeme[i] in first_set["<common-type>"]:
                                print("common-type found")
                                i += 1

                                # identifier
                                if lexeme[i] != "*#":
                                    output.insert(
                                        "end", err + "identifier not found\n")
                                    return [(lexeme[i], "SYNTAX ERROR")]
                                i += 3
                                print("identifier found")
                            # identifier
                            elif lexeme[i] != "**#":
                                output.insert(
                                    "end", err + "identifier not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]
                            i += 4
                            print("identifier found")

                    # <all-types>
                    elif lexeme[i] in first_set["<all-types>"]:
                        print("all-types found")

                        while True:
                            if lexeme[i] not in first_set["<all-types>"]:
                                break
                            i += 1

                            # identifier
                            if lexeme[i] != "#":
                                output.insert(
                                    "end", err + "identifier not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]
                            i += 2
                            print("identifier found")

                            # ,
                            if lexeme[i] != ",":
                                output.insert("end", err + ", not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]
                            i += 1
                            print(", found")

                    # identifier
                    elif lexeme[i] == "#":
                        print("identifier found")
                        i += 2

                        # (
                        if lexeme[i] != "(":
                            output.insert("end", err + "( not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]
                        i += 1
                        print("( found")

                        # <2D-parameter>
                        if lexeme[i] in first_set["<2D-parameter>"]:
                            print("2D-parameter found")
                            i, results = D2_parameter(lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return results
                            print("2D-parameter found")
                else:
                    output.insert("end", err + "parameter not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]

                # )
                if lexeme[i] != ")":
                    output.insert("end", err + ") not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print(") found")

                # (
                if lexeme[i] != "(":
                    output.insert("end", err + "( not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("( found")

                # <statement>
                i, results = statement(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return results
                print("statement found")

                # regrow
                if lexeme[i] != "regrow":
                    output.insert("end", err + "regrow not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("regrow found")

                # <insert-regrow>
                if lexeme[i] in first_set["<insert-regrow>"]:
                    print("insert-regrow found")

                    # <all-type-value>
                    if lexeme[i] in first_set["<all-type-value>"]:
                        print("all-type-value found")

                        i, results = all_type_value(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return results
                        print("all-type-value found")

                    # <common-data>
                    elif lexeme[i] in first_set["<common-data>"]:
                        print("common-data found")

                        i, results = common_data(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return results
                        print("common-data found")

                        # at
                        if lexeme[i] != "at":
                            output.insert("end", err + "at not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]
                        i += 1
                        print("at found")

                        # <all-type-value>
                        i, results = all_type_value(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return results
                        print("all-type-value found")

                else:
                    output.insert("end", err + "insert-regrow not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("; found")

                # )
                if lexeme[i] != ")":
                    output.insert("end", err + ") not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print(") found")

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("; found")

            # viola
            elif lexeme[i] == "viola":
                print("viola found")
                i += 1

                # identifier
                if lexeme[i] != "#":
                    output.insert("end", err + "identifier not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 2
                print("identifier found")

                # (
                if lexeme[i] != "(":
                    output.insert("end", err + "( not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("( found")

                # <keyword-param>
                if lexeme[i] in first_set["<keyword-param>"]:
                    print("keyword-param found")
                    while True:
                        if lexeme[i] not in first_set["<keyword-param>"]:
                            break
                        if lexeme[i] in first_set["<common-type>"]:
                            print("common-type found")
                            i += 1

                            # identifier
                            if lexeme[i] != "*#":
                                output.insert(
                                    "end", err + "identifier not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]
                            i += 3
                            print("identifier found")

                        # identifier
                        elif lexeme[i] != "**#":
                            output.insert(
                                "end", err + "identifier not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]
                        i += 4
                        print("identifier found")

                # )
                if lexeme[i] != ")":
                    output.insert("end", err + ") not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print(") found")

                # (
                if lexeme[i] != "(":
                    output.insert("end", err + "( not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("( found")

                # <statement>
                i, results = statement(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return results

                # )
                if lexeme[i] != ")":
                    output.insert("end", err + ") not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print(") found")

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("; found")

    # ---------- # plant # ---------- #
    if lexeme[-2] != "plant":
        output.insert("end", err + "plant not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]
    i += 1
    print("plant found")

    if lexeme[i] != "EPSILON":
        output.insert("end", err + "EPSILON found\n")
    else:
        output.insert("end", "SyntaxAnalyser: No Error Found.\n")
        return results


# For displaying the Parse Tree
def display_tree():
    pass


# For displaying the token stream e.g., tint a; == reserved word identifier reserved symbol
def token_stream():
    pass
