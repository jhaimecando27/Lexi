# Syntax Analyzer Logic
from grammar import cfg, first_set, follow_set, predict_set


def statement(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<statement>"]:

        # Variable Declaration
        # <constant>
        if lexeme[i] != "EPSILON" and lexeme[i] == "hard":
            i += 1

        # <all-type>
        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
            i += 1

            # #identifier
            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                i += 2  # skip hashtag and identifier name
            else:
                output.insert("end", err + "identifier not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <insert-variable>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-variable>"]:

                # <all-assignment>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-assignment>"]:
                    i += 1
                else:
                    output.insert(
                        "end", err + "all-assignment not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <flora-tint-value>
                while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                    # <insert-flora-tint>
                    if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                        # tint literal
                        if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                            i += 1
                        # flora literal
                        elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                            i += 1
                        # identifer
                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                            i += 2

                            # <insert-func>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                # (
                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                    i += 1
                                else:
                                    output.insert(
                                        "end", err + "( not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <argument>

                                # )
                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                    i += 1
                                else:
                                    output.insert(
                                        "end", err + ") not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                            # TODO: (wip) <instance-grab> TODO
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                # identifier
                                if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                    i += 6  # #identifer().identifer
                                else:
                                    output.insert(
                                        "end", err + "identifier not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                        # lent(<all-type-value>)
                        elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                            i += 1

                            # (
                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                i += 1
                            else:
                                output.insert("end", err + "( not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # TODO: <all-type-value>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                pass
                            else:
                                output.insert(
                                    "end", err + "all-type-value not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # )
                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                i += 1
                            else:
                                output.insert("end", err + ") not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                        else:
                            output.insert(
                                "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                    # TODO: <operate-flora-tint>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operate-flora-tint>"]:

                        # <operator>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                            i += 1
                        else:
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <insert-operation>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:

                            # (
                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                i += 1
                            else:
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # <insert-flora-tint>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                                i += 1

                                # tint literal
                                if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                    i += 1
                                # flora literal
                                elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                    i += 1
                                # identifer
                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                    i += 2

                                    # <insert-func>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                        # (
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                            i += 1
                                        else:
                                            output.insert(
                                                "end", err + "( not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # TODO: <argument>

                                        # )
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                            i += 1
                                        else:
                                            output.insert(
                                                "end", err + ") not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <instance-grab>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                        # identifier
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                            i += 6  # #identifer().identifer
                                        else:
                                            output.insert(
                                                "end", err + "identifier not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                # lent(<all-type-value>)
                                elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                    i += 1

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + "( not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <all-type-value>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                        pass
                                    else:
                                        output.insert(
                                            "end", err + "all-type-value not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + ") not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                else:
                                    output.insert(
                                        "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # )
                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                    i += 1
                                else:
                                    output.insert(
                                        "end", err + ") not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]
            # ;
            if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                i += 1
            else:
                output.insert("end", err + "; not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

        # <i/o-statement>;
        elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<i/o-statement>"]:

            # mint(<all-type-value>);
            if lexeme[i] != "EPSILON" and lexeme[i] == "mint":
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # TODO: <all-type-value>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    i += 1
                else:
                    output.insert("end", err + "all-type-value not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")

                    return i, [(lexeme[i], "SYNTAX ERROR")]

            # <insert-inpetal>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-inpetal>"]:

                # <all-types>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                    i += 1

                # #identifier
                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                    i += 2  # skip hashtag and identifier name

                    # <insert-func>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # TODO: <argument>

                        # )
                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                            i += 1
                        else:
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                else:
                    output.insert("end", err + "inpetal error\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # inpetal
                if lexeme[i] != "EPSILON" and lexeme[i] == "inpetal":
                    i += 1
                else:
                    output.insert("end", err + "inpetal not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # string literal
                if lexeme[i] != "EPSILON" and token[i] == "string literal":
                    i += 1
                else:
                    output.insert("end", err + "string literal not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

        # #identifier
        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
            i += 2  # skip hashtag and identifier name

            # <insert-func>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # TODO: <argument>

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
            else:
                output.insert("end", err + "identifier error\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <more-id>
            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<more-id>"]:

                # <indexing>
                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<indexing>"]:

                    # [
                    if lexeme[i] != "EPSILON" and lexeme[i] == "[":
                        i += 1
                    else:
                        output.insert("end", err + "[ not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <insert-index>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-index>"]:
                        # tint literal
                        if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                            i += 1
                        # string literal
                        if lexeme[i] != "EPSILON" and token[i] == "string literal":
                            i += 1

                    # ]
                    if lexeme[i] != "EPSILON" and lexeme[i] == "]":
                        i += 1
                    else:
                        output.insert("end", err + "] not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                # ,
                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                    i += 1
                else:
                    output.insert("end", err + ", not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # #identifier
                if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                    i += 2
                else:
                    output.insert("end", err + "identifier not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <insert-func>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                    # (
                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                        i += 1
                    else:
                        output.insert("end", err + "( not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # TODO: <argument>

                    # )
                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                        i += 1
                    else:
                        output.insert("end", err + ") not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                else:
                    output.insert("end", err + "<insert-func> not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <indexing>
                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<indexing>"]:

                    # [
                    if lexeme[i] != "EPSILON" and lexeme[i] == "[":
                        i += 1
                    else:
                        output.insert("end", err + "[ not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <insert-index>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-index>"]:
                        # tint literal
                        if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                            i += 1
                        # string literal
                        if lexeme[i] != "EPSILON" and token[i] == "string literal":
                            i += 1

                    # ]
                    if lexeme[i] != "EPSILON" and lexeme[i] == "]":
                        i += 1
                    else:
                        output.insert("end", err + "] not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

        # leaf
        elif lexeme[i] != "EPSILON" and lexeme[i] == "leaf":
            i += 1

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                i += 1
            else:
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <all-type-value>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                i += 1
            else:
                output.insert("end", err + "all-type-value not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <more-all>
            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<more-all>"]:

                # ,
                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                    i += 1
                else:
                    output.insert("end", err + ", not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <all-type-value>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    i += 1
                else:
                    return i, [(lexeme[i], "SYNTAX ERROR")]

            # <insert-condition>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:

                # <all-cond-operator>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                    i += 1

                    # <insert-all-operand>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:

                        # <flora-tint-value>
                        if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
                            while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                # <insert-flora-tint>
                                if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                    # tint literal
                                    if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                                        i += 1
                                    # flora literal
                                    elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                                        i += 1
                                    # identifer
                                    elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                        i += 2

                                        # <insert-func>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                i += 1
                                            else:
                                                output.insert("end", err + "( not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <argument>

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                i += 1
                                            else:
                                                output.insert("end", err + ") not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # TODO: (wip) <instance-grab> TODO
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                            # identifier
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                i += 6  # #identifer().identifer
                                            else:
                                                output.insert(
                                                    "end", err + "identifier not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]
                                    # lent(<all-type-value>)
                                    elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                        i += 1

                                        # (
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                            i += 1
                                        else:
                                            output.insert("end", err + "( not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # TODO: <all-type-value>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:

                                        else:
                                            output.insert(
                                                "end", err + "all-type-value not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # )
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                            i += 1
                                        else:
                                            output.insert("end", err + ") not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                    else:
                                        output.insert(
                                            "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <operate-flora-tint>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operate-flora-tint>"]:

                                    # <operator>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                        i += 1
                                    else:
                                        output.insert("end", err + "operator not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # <insert-operation>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:

                                        # (
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                            i += 1
                                        else:
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # <insert-flora-tint>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                                            i += 1

                                            # tint literal
                                            if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                                i += 1
                                            # flora literal
                                            elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                                i += 1
                                            # identifer
                                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                i += 2

                                                # <insert-func>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <argument>

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + ") not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # TODO: <instance-grab>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                                    # identifier
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                        i += 6  # #identifer().identifer
                                                    else:
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                            # lent(<all-type-value>)
                                            elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                                i += 1

                                                # (
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                    i += 1
                                                else:
                                                    output.insert("end", err + "( not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # TODO: <all-type-value>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        "end", "I: all-type-value found\n")

                                                else:
                                                    output.insert(
                                                        "end", err + "all-type-value not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                                            else:
                                                output.insert(
                                                    "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                i += 1
                                            else:
                                                output.insert("end", err + ") not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    i += 1
                                else:
                                    break

                        # <common-type>
                        elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                i += 1

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    i += 1
                                else:
                                    break
                        else:
                            output.insert(
                                "end", err + "insert-all-operand not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                    else:
                        output.insert(
                            "end", err + "insert-all-operand not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                # <string-cond-op>
                elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-cond-op>"]:
                    i += 1

                    # <string-operand>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:

                        # TODO: <all-type-value>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                i += 1

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    i += 1
                                else:
                                    break
                        # <all-types>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                i += 1

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    i += 1
                                else:
                                    break
                        else:
                            output.insert("end", err + "string-op error\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                    else:
                        output.insert("end", err + "string-operand not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # statement
            i, results = statement(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return results

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # ;
            if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                i += 1
            else:
                output.insert("end", err + "; not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # eleaf
            while lexeme[i] != "EPSILON" and lexeme[i] == "eleaf":
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <all-type-value>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    i += 1
                else:
                    output.insert("end", err + "all-type-value not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <more-all>
                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<more-all>"]:

                    # ,
                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                        i += 1
                    else:
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <all-type-value>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                        i += 1
                    else:
                        output.insert("end", err + "all-type-value not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                # <insert-condition>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:

                    # <all-cond-operator>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                        i += 1

                        # <insert-all-operand>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:

                            # <flora-tint-value>
                            if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
                                while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                    # <insert-flora-tint>
                                    if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                        # tint literal
                                        if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                                            i += 1
                                        # flora literal
                                        elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                                            i += 1
                                        # identifer
                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                            i += 2

                                            # <insert-func>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                                # (
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                    i += 1
                                                else:
                                                    output.insert("end", err + "( not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # TODO: <argument>

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: (wip) <instance-grab> TODO
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                                # identifier
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                    i += 6  # #identifer().identifer
                                                else:
                                                    output.insert(
                                                        "end", err + "identifier not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                                        # lent(<all-type-value>)
                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                            i += 1

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                i += 1
                                            else:
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <all-type-value>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:

                                            else:
                                                output.insert(
                                                    "end", err + "all-type-value not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                i += 1
                                            else:
                                                output.insert("end", err + ") not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]
                                        else:
                                            output.insert(
                                                "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <operate-flora-tint>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operate-flora-tint>"]:

                                        # <operator>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                            i += 1
                                        else:
                                            output.insert("end", err + "operator not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # <insert-operation>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                i += 1
                                            else:
                                                output.insert("end", err + "( not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # <insert-flora-tint>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                                                    "end", "I: insert-flora-tint found\n")
                                                i += 1

                                                # tint literal
                                                if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                                    i += 1
                                                # flora literal
                                                elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                                    i += 1
                                                # identifer
                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                    i += 2

                                                    # <insert-func>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                                        # (
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                            i += 1
                                                        else:
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # TODO: <argument>

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <instance-grab>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                                        # identifier
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                            i += 6  # #identifer().identifer
                                                        else:
                                                            output.insert(
                                                                "end", err + "identifier not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                                # lent(<all-type-value>)
                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                                    i += 1

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        pass

                                                    else:
                                                        output.insert(
                                                            "end", err + "all-type-value not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + ") not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                                else:
                                                    output.insert(
                                                        "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        i += 1
                                    else:
                                        break

                            # <common-type>
                            elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        i += 1
                                    else:
                                        break
                            else:
                                output.insert(
                                    "end", err + "insert-all-operand not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                        else:
                            output.insert(
                                "end", err + "insert-all-operand not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <string-cond-op>
                    elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-cond-op>"]:
                        i += 1

                        # <string-operand>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:

                            # TODO: <all-type-value>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        i += 1
                                    else:
                                        break
                            # <all-types>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        i += 1
                                    else:
                                        break
                            else:
                                output.insert("end", err + "string-op error\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                        else:
                            output.insert("end", err + "string-operand not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    i += 1
                else:
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # statement
                i, results = statement(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return results

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # ;
                if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                    i += 1
                else:
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
            # <else>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<else>"]:
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # statement
                i, results = statement(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return results

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

        # TODO: loops
        # <iterative>
        elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<iterative>"]:
            i += 1

            # fern
            if lexeme[i] != "EPSILON" and lexeme[i] == "fern":
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <insert-fern>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-fern>"]:

                    # #identifer = <insert-flora-tint>; <all-type-value> <more-all> <insert-condition>; #identifer <all-assignment> <insert-flora-tint>;)
                    if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                        i += 2

                        # =
                        if lexeme[i] != "EPSILON" and lexeme[i] == "=":
                            i += 1
                        else:
                            output.insert("end", err + "= not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <flora-tint-value>
                        while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                            # <insert-flora-tint>
                            if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                # tint literal
                                if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                                    i += 1
                                # flora literal
                                elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                                    i += 1
                                # identifer
                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                    i += 2

                                    # <insert-func>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                        # (
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                            i += 1
                                        else:
                                            output.insert("end", err + "( not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # TODO: <argument>

                                        # )
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                            i += 1
                                        else:
                                            output.insert("end", err + ") not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: (wip) <instance-grab> TODO
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                        # identifier
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                            i += 6  # #identifer().identifer
                                        else:
                                            output.insert(
                                                "end", err + "identifier not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                # lent(<all-type-value>)
                                elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                    i += 1

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        i += 1
                                    else:
                                        output.insert("end", err + "( not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <all-type-value>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:

                                    else:
                                        output.insert(
                                            "end", err + "all-type-value not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        i += 1
                                    else:
                                        output.insert("end", err + ") not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                else:
                                    output.insert(
                                        "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                            # TODO: <operate-flora-tint>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operate-flora-tint>"]:

                                # <operator>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                    i += 1
                                else:
                                    output.insert("end", err + "operator not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # <insert-operation>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        i += 1
                                    else:
                                        output.insert("end", err + "( not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # <insert-flora-tint>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                                        i += 1

                                        # tint literal
                                        if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                            i += 1
                                        # flora literal
                                        elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                            i += 1
                                        # identifer
                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                            i += 2

                                            # <insert-func>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                                # (
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                    i += 1
                                                else:
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # TODO: <argument>

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    i += 1
                                                else:
                                                    output.insert(
                                                        "end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <instance-grab>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                                # identifier
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                    i += 6  # #identifer().identifer
                                                else:
                                                    output.insert(
                                                        "end", err + "identifier not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                                        # lent(<all-type-value>)
                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                            i += 1

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                i += 1
                                            else:
                                                output.insert("end", err + "( not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <all-type-value>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                pass
                                            else:
                                                output.insert(
                                                    "end", err + "all-type-value not found\n")

                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                i += 1
                                            else:
                                                output.insert("end", err + ") not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]
                                        else:
                                            output.insert(
                                                "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # )
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                            i += 1
                                        else:
                                            output.insert("end", err + ") not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                            # ,
                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                i += 1
                            else:
                                break

                        # ;
                        if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                            i += 1
                        else:
                            output.insert("end", err + "; not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # TODO: <all-type-value>
                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                            i += 1

                            # ,
                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                i += 1
                            else:
                                break

                        # <insert-condition>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:

                            # <all-cond-operator>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                                i += 1

                                # <insert-all-operand>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:

                                    # <flora-tint-value>
                                    if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
                                        while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                            # <insert-flora-tint>
                                            if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                                # tint literal
                                                if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                                                    i += 1
                                                # flora literal
                                                elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                                                    i += 1
                                                # identifer
                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                    i += 2

                                                    # <insert-func>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                                        # (
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                            i += 1
                                                        else:
                                                            output.insert("end", err + "( not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # TODO: <argument>

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            i += 1
                                                        else:
                                                            output.insert("end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: (wip) <instance-grab> TODO
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                                        # identifier
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                            i += 6  # #identifer().identifer
                                                        else:
                                                            output.insert(
                                                                "end", err + "identifier not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                                # lent(<all-type-value>)
                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                                    i += 1

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        pass
                                                    else:
                                                        output.insert(
                                                            "end", err + "all-type-value not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + ") not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                                else:
                                                    output.insert(
                                                        "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <operate-flora-tint>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operate-flora-tint>"]:

                                                # <operator>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                                    i += 1
                                                else:
                                                    output.insert("end", err + "operator not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # <insert-operation>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # <insert-flora-tint>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                                                        i += 1

                                                        # tint literal
                                                        if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                                            i += 1
                                                        # flora literal
                                                        elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                                            i += 1
                                                        # identifer
                                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                            i += 2

                                                            # <insert-func>
                                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                                                # (
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + "( not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # TODO: <argument>

                                                                # )
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ") not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # TODO: <instance-grab>
                                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                                                # identifier
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                    i += 6  # #identifer().identifer
                                                                else:
                                                                    output.insert(
                                                                        "end", err + "identifier not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                                                        # lent(<all-type-value>)
                                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                                            i += 1

                                                            # (
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                i += 1
                                                            else:
                                                                output.insert("end", err + "( not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # TODO: <all-type-value>
                                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                    "end", "I: all-type-value found\n")

                                                            else:
                                                                output.insert(
                                                                    "end", err + "all-type-value not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # )
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                i += 1
                                                            else:
                                                                output.insert("end", err + ") not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]
                                                        else:
                                                            output.insert(
                                                                "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            i += 1
                                                        else:
                                                            output.insert("end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                i += 1
                                            else:
                                                break

                                    # <common-type>
                                    elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                i += 1
                                            else:
                                                break
                                    else:
                                        output.insert(
                                            "end", err + "insert-all-operand not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                else:
                                    output.insert(
                                        "end", err + "insert-all-operand not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                            # <string-cond-op>
                            elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-cond-op>"]:
                                i += 1

                                # <string-operand>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:

                                    # TODO: <all-type-value>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                i += 1
                                            else:
                                                break
                                    # <all-types>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                i += 1
                                            else:
                                                break
                                    else:
                                        output.insert("end", err + "string-op error\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                else:
                                    output.insert("end", err + "string-operand not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]



                        # ;
                        if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                            i += 1
                        else:
                            output.insert("end", err + "; not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # #identifer
                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                            i += 2
                        else:
                            output.insert("end", err + "identifier not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <all-assignment>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-assignment>"]:
                            i += 1
                        else:
                            output.insert("end", err + "all-assignment not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <insert-flora-tint>
                        if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                            # tint literal
                            if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                                i += 1
                            # flora literal
                            elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                                i += 1
                            # identifer
                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                i += 2

                                # <insert-func>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        i += 1
                                    else:
                                        output.insert("end", err + "( not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <argument>

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        i += 1
                                    else:
                                        output.insert("end", err + ") not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: (wip) <instance-grab> TODO
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                    # identifier
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                        i += 6  # #identifer().identifer
                                    else:
                                        output.insert(
                                            "end", err + "identifier not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                            # lent(<all-type-value>)
                            elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                i += 1

                                # (
                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                    i += 1
                                else:
                                    output.insert("end", err + "( not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <all-type-value>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:

                                else:
                                    output.insert(
                                        "end", err + "all-type-value not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # )
                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                    i += 1
                                else:
                                    output.insert("end", err + ") not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                            else:
                                output.insert(
                                    "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                        # ;
                        if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                            i += 1
                        else:
                            output.insert("end", err + "; not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # )
                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                            i += 1
                        else:
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # statement
                        i, results = statement(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return results

                        # )
                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                            i += 1
                        else:
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <common-data>
                    elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-data>"]:
                        i += 1

                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
            # willow
            elif lexeme[i] != "EPSILON" and lexeme[i] == "willow":
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # TODO: all-type-value and more-all
                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    i += 1

                    # ,
                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                        i += 1
                    else:
                        break

                # <insert-condition>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:

                    # <all-cond-operator>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                        i += 1

                        # <insert-all-operand>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:

                            # <flora-tint-value>
                            if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
                                while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                    # <insert-flora-tint>
                                    if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                                        # tint literal
                                        if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                                            i += 1
                                        # flora literal
                                        elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                                            i += 1
                                        # identifer
                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                            i += 2

                                            # <insert-func>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                                # (
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                    i += 1
                                                else:
                                                    output.insert("end", err + "( not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # TODO: <argument>

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: (wip) <instance-grab> TODO
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                                # identifier
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                    i += 6  # #identifer().identifer
                                                else:
                                                    output.insert(
                                                        "end", err + "identifier not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                                        # lent(<all-type-value>)
                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                            i += 1

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                i += 1
                                            else:
                                                output.insert("end", err + "( not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <all-type-value>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                pass

                                            else:
                                                output.insert(
                                                    "end", err + "all-type-value not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                i += 1
                                            else:
                                                output.insert("end", err + ") not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]
                                        else:
                                            output.insert(
                                                "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <operate-flora-tint>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operate-flora-tint>"]:

                                        # <operator>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                            i += 1
                                        else:
                                            output.insert("end", err + "operator not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # <insert-operation>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                i += 1
                                            else:
                                                output.insert("end", err + "( not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # <insert-flora-tint>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                                                i += 1

                                                # tint literal
                                                if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                                    i += 1
                                                # flora literal
                                                elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                                    i += 1
                                                # identifer
                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                    i += 2

                                                    # <insert-func>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                                        # (
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + "( not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # TODO: <argument>

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <instance-grab>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                                        # identifier
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                            i += 6  # #identifer().identifer
                                                        else:
                                                            output.insert(
                                                                "end", err + "identifier not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                                # lent(<all-type-value>)
                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                                    i += 1

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        pass
                                                    else:
                                                        output.insert(
                                                            "end", err + "all-type-value not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + ") not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                                else:
                                                    output.insert(
                                                        "end", err + "tint literal, flora literal, identifier, or lent not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        i += 1
                                    else:
                                        break

                            # <common-type>
                            elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        i += 1
                                    else:
                                        break
                            else:
                                output.insert(
                                    "end", err + "insert-all-operand not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                        else:
                            output.insert(
                                "end", err + "insert-all-operand not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <string-cond-op>
                    elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-cond-op>"]:
                        i += 1

                        # <string-operand>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:

                            # TODO: <all-type-value>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        i += 1
                                    else:
                                        break
                            # <all-types>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        i += 1
                                    else:
                                        break
                            else:
                                output.insert("end", err + "string-op error\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                        else:
                            output.insert("end", err + "string-operand not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
            else:
                output.insert("end", err + "iterative not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

        # TODO: tree

        # clear
        elif lexeme[i] != "EPSILON" and lexeme[i] == "clear":
            i += 1

        # break
        elif lexeme[i] != "EPSILON" and lexeme[i] == "break":
            i += 1
    return i, [("", "")]


# For checking the syntax of the program
def syntax_analysis(programs, output):
    results = []
    err = "E: Syntax Analyzer: "

    programs.append(("EPSILON", "EPSILON"))
    print(programs)

    # remove "<--", "-->", "<space> from the list of tuple in programs
    programs = [program for program in programs if program[0] != "<--" and program[0] != "-->" and program[0] != "<space>" and program[0] != "?"]

    lexeme, token = zip(*programs)

    print(programs)

    i = 0

    # ---------- # seed # ---------- #
    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<program>"]:
        i += 1
    else:
        return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # <global> TODO: string assignment # ---------- #
    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<global>"]:

        # floral
        if lexeme[i] != "EPSILON" and lexeme[i] == "floral":
            i += 1
        else:
            output.insert("end", err + "floral not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # <constant>
        if lexeme[i] != "EPSILON" and lexeme[i] == "hard":
            i += 1

        # <all-types>
        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
            i += 1
        else:
            output.insert("end", err + "all-types not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # #identifier
        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
            i += 2  # skip hashtag and identifier name
        else:
            output.insert("end", err + "identifier not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # <insert-variable>
        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-variable>"]:

            # <all-assignment>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-assignment>"]:
                i += 1
            else:
                output.insert("end", err + "all-assignment not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # <flora-tint-value>
            while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<flora-tint-value>>"] or token[i] in first_set["<insert-flora-tint>"]):

                # <insert-flora-tint>
                if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):

                    # tint literal
                    if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                        i += 1
                    # flora literal
                    elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
                        i += 1
                    # identifer
                    elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                        i += 2

                        # <insert-func>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                            # (
                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                i += 1
                            else:
                                output.insert("end", err + "( not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                            # TODO: <argument>

                            # )
                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                i += 1
                            else:
                                output.insert("end", err + ") not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                        # TODO: (wip) <instance-grab> TODO
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                            # identifier
                            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                i += 6  # #identifer().identifer
                            else:
                                output.insert(
                                    "end", err + "identifier not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]
                    # lent(<all-type-value>)
                    elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                        i += 1

                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]

                        # TODO: <all-type-value>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:

                        else:
                            output.insert(
                                "end", err + "all-type-value not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]

                        # )
                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
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

                    # <operator>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                        i += 1
                    else:
                        output.insert("end", err + "operator not found\n")
                        return [(lexeme[i], "SYNTAX ERROR")]

                    # <insert-operation>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:

                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]

                        # <insert-flora-tint>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                            i += 1

                            # tint literal
                            if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                i += 1
                            # flora literal
                            elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                i += 1
                            # identifer
                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                i += 2

                                # <insert-func>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + "( not found\n")
                                        return [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <argument>

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + ") not found\n")
                                        return [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <instance-grab>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<instance-grab>"]:

                                    # identifier
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                        i += 6  # #identifer().identifer
                                    else:
                                        output.insert(
                                            "end", err + "identifier not found\n")
                                        return [(lexeme[i], "SYNTAX ERROR")]
                            # lent(<all-type-value>)
                            elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                i += 1

                                # (
                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                    i += 1
                                else:
                                    output.insert("end", err + "( not found\n")
                                    return [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <all-type-value>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                    pass
                                else:
                                    output.insert(
                                        "end", err + "all-type-value not found\n")
                                    return [(lexeme[i], "SYNTAX ERROR")]

                                # )
                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
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
                                i += 1
                            else:
                                output.insert("end", err + ") not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                # ,
                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                    i += 1
                else:
                    break

        # ;
        if lexeme[i] != "EPSILON" and lexeme[i] == ";":
            i += 1
        else:
            output.insert("end", err + "; not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # garden # ---------- #
    if lexeme[i] != "EPSILON" and lexeme[i] == "garden":
        i += 1

        # (
        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
            i += 1
        else:
            output.insert("end", err + "( not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # )
        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
            i += 1
        else:
            output.insert("end", err + ") not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # (
        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
            i += 1
        else:
            output.insert("end", err + "( not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # statement
        i, results = statement(lexeme, token, i, output)
        if "SYNTAX ERROR" in results:
            return results

        # )
        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
            i += 1
        else:
            output.insert("end", err + ") not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]
        # ;
        if lexeme[i] != "EPSILON" and lexeme[i] == ";":
            i += 1
        else:
            output.insert("end", err + "; not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # TODO: <function> # ---------- #
    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<function>"]:
        output.insert("end", "I: function found\n")

        # <common-type>
        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
            # #identifier
            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                i += 2
            else:
                output.insert("end", err + "identifier not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # TODO: <insert_parameter>

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # <statement>
            i, results = statement(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return results

            # regrow
            if lexeme[i] != "EPSILON" and lexeme[i] == "regrow":
                i += 1

                # TODO: <insert-regrow>
                # <all-type-value>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    pass

                # TODO: <common-data>


            else:
                output.insert("end", err + "regrow not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]


            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # ;
            if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                i += 1
            else:
                output.insert("end", err + "; not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]
        # viola
        elif lexeme[i] != "EPSILON" and lexemi[i] == "viola":
            output.insert("end", "I: viola found\n")
            i += 1

            # #identifier
            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                i += 2
            else:
                output.insert("end", err + "identifier not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # TODO: <keyword-param>

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # <statement>
            i, results = statement(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return results

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # ;
            if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                i += 1
            else:
                output.insert("end", err + "; not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # plant # ---------- #
    if lexeme[i] != "EPSILON" and lexeme[-1] == "plant":
        i += 1
    else:
        output.insert("end", err + "plant not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]

    output.insert("end", "SyntaxAnalyser: No Errod Found.\n")

    return results


# For displaying the Parse Tree
def display_tree():
    pass


# For displaying the token stream e.g., tint a; == reserved word identifier reserved symbol
def token_stream():
    pass
