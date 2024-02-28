# Syntax Analyzer Logic
from grammar import cfg, first_set, follow_set, predict_set


# For checking the syntax of the program
def syntax_analysis(programs, output):
    results = []
    err = "E: Syntax Analyzer: "

    for program in programs:
        if program[0] == "<space>":
            programs.remove(program)

    programs.append(("EPSILON", "EPSILON"))

    lexeme, token = zip(*programs)

    i = 0

    # seed
    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<program>"]:
        output.insert("end", "I: seed found\n")
        i += 1
    else:
        output.insert("end", err + "seed not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]

    # <global> TODO: string assignment
    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<global>"]:
        output.insert("end", "I: global found\n")

        # floral
        if lexeme[i] != "EPSILON" and lexeme[i] == "floral":
            i += 1
        else:
            output.insert("end", err + "floral not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # <constant>
        if lexeme[i] != "EPSILON" and lexeme[i] == "hard":
            output.insert("end", "I: constant found\n")
            i += 1

        # <all-type>
        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
            output.insert("end", "I: all-types found\n")
            i += 1
        else:
            output.insert("end", err + "all-types not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # #identifier
        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
            output.insert("end", "I: identifier found\n")
            i += 2  # skip hashtag and identifier name
        else:
            output.insert("end", err + "identifier not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # <insert-variable>
        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-variable>"]:
            output.insert("end", "I: insert-variable found\n")

            # <all-assignment>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-assignment>"]:
                output.insert("end", "I: all-assignment found\n")
                i += 1
            else:
                output.insert("end", err + "all-assignment not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # <flora-tint-value>
            while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
                output.insert("end", "I: flora-tint-value found\n")

                # <insert-flora-tint>
                if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
                    output.insert("end", "I: insert-flora-tint found\n")

                    # tint literal
                    if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                        output.insert("end", "I: tint literal found\n")
                        i += 1
                    # flora literal
                    elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                        output.insert("end", "I: flora literal found\n")
                        i += 1
                    # identifer
                    elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                        output.insert("end", "I: identifier found\n")
                        i += 2

                        # <insert-func>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:
                            output.insert("end", "I: insert-func found\n")

                            # (
                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                output.insert("end", "I: ( found\n")
                                i += 1
                            else:
                                output.insert("end", err + "( not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                            # TODO: <argument>

                            # )
                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                output.insert("end", "I: ) found\n")
                                i += 1
                            else:
                                output.insert("end", err + ") not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                        # TODO: (wip) <instance-grab> TODO
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:
                            output.insert("end", "I: instance-grab found\n")

                            # identifier
                            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                output.insert("end", "I: identifier found\n")
                                i += 6  # #identifer().identifer
                            else:
                                output.insert(
                                    "end", err + "identifier not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]
                    # lent(<all-type-value>)
                    elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                        output.insert("end", "I: lent found\n")
                        i += 1

                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            output.insert("end", "I: ( found\n")
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]

                        # TODO: <all-type-value>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                            output.insert("end", "I: all-type-value found\n")

                        else:
                            output.insert(
                                "end", err + "all-type-value not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]

                        # )
                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                            output.insert("end", "I: ) found\n")
                            i += 1
                        else:
                            output.insert("end", err + ") not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]
                    else:
                        output.insert(
                            "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                        return [(lexeme[i], "SYNTAX ERROR")]

                # TODO: <operate-flora-tint>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operate-flora-tint>"]:
                    output.insert("end", "I: operate-flora-tint found\n")

                    # <operator>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                        output.insert("end", "I: operator found\n")
                        i += 1
                    else:
                        output.insert("end", err + "operator not found\n")
                        return [(lexeme[i], "SYNTAX ERROR")]

                    # <insert-operation>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:
                        output.insert("end", "I: insert-operation found\n")

                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            output.insert("end", "I: ( found\n")
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]

                        # <insert-flora-tint>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                            output.insert(
                                "end", "I: insert-flora-tint found\n")
                            i += 1

                            # tint literal
                            if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                output.insert("end", "I: tint literal found\n")
                                i += 1
                            # flora literal
                            elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                output.insert(
                                    "end", "I: flora literal found\n")
                                i += 1
                            # identifer
                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                output.insert("end", "I: identifier found\n")
                                i += 2

                                # <insert-func>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:
                                    output.insert(
                                        "end", "I: insert-func found\n")

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        output.insert("end", "I: ( found\n")
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + "( not found\n")
                                        return [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <argument>

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        output.insert("end", "I: ) found\n")
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + ") not found\n")
                                        return [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <instance-grab>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:
                                    output.insert(
                                        "end", "I: instance-grab found\n")

                                    # identifier
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                        output.insert(
                                            "end", "I: identifier found\n")
                                        i += 6  # #identifer().identifer
                                    else:
                                        output.insert(
                                            "end", err + "identifier not found\n")
                                        return [(lexeme[i], "SYNTAX ERROR")]
                            # lent(<all-type-value>)
                            elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                output.insert("end", "I: lent found\n")
                                i += 1

                                # (
                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                    output.insert("end", "I: ( found\n")
                                    i += 1
                                else:
                                    output.insert("end", err + "( not found\n")
                                    return [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <all-type-value>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                    output.insert(
                                        "end", "I: all-type-value found\n")

                                else:
                                    output.insert(
                                        "end", err + "all-type-value not found\n")
                                    return [(lexeme[i], "SYNTAX ERROR")]

                                # )
                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                    output.insert("end", "I: ) found\n")
                                    i += 1
                                else:
                                    output.insert("end", err + ") not found\n")
                                    return [(lexeme[i], "SYNTAX ERROR")]
                            else:
                                output.insert(
                                    "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                            # )
                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                output.insert("end", "I: ) found\n")
                                i += 1
                            else:
                                output.insert("end", err + ") not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                # ,
                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                    output.insert("end", "I: , found\n")
                    i += 1
                else:
                    break

        # ;
        if lexeme[i] != "EPSILON" and lexeme[i] == ";":
            output.insert("end", "I: ; found\n")
            i += 1
        else:
            output.insert("end", err + "; not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

    return results


# For displaying the Parse Tree
def display_tree():
    pass


# For displaying the token stream e.g., tint a; == reserved word identifier reserved symbol
def token_stream():
    pass
