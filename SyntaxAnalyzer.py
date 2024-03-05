# Syntax Analyzer Logic
from grammar import cfg, first_set, follow_set, predict_set


def statement(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<statement>"]:
        output.insert("end", "I: statement found\n")

        # Variable Declaration
        # <constant>
        if lexeme[i] != "EPSILON" and lexeme[i] == "hard":
            output.insert("end", "I: constant found\n")
            i += 1

        # <all-type>
        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
            output.insert("end", "I: all-types found\n")
            i += 1

            # #identifier
            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                output.insert("end", "I: identifier found\n")
                i += 2  # skip hashtag and identifier name
            else:
                output.insert("end", err + "identifier not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <insert-variable>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-variable>"]:
                output.insert("end", "I: insert-variable found\n")

                # <all-assignment>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-assignment>"]:
                    output.insert("end", "I: all-assignment found\n")
                    i += 1
                else:
                    output.insert(
                        "end", err + "all-assignment not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <flora-tint-value>
                while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
                    output.insert("end", "I: flora-tint-value found\n")

                    # <insert-flora-tint>
                    if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
                        output.insert(
                            "end", "I: insert-flora-tint found\n")

                        # tint literal
                        if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                            output.insert("end", "I: tint literal found\n")
                            i += 1
                        # flora literal
                        elif lexeme[i] != "EPSILON" and token[i] == "flora literal":
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
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # <argument>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                    output.insert(
                                        "end", "I: argument found\n")

                                    # <insert-argument>
                                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                        output.insert(
                                            "end", "I: insert-argument found\n")

                                        # TODO: <all-type-value>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                            output.insert(
                                                "end", "I: all-type-value found\n")
                                            # <common-data>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-data>"]:
                                                output.insert(
                                                    "end", "I: common-data found\n")
                                                i += 1

                                        # # identifier
                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                            output.insert(
                                                "end", "I: identifier found\n")
                                            i += 2

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                output.insert("end", "I: ( found\n")
                                                i += 1
                                            else:
                                                output.insert(
                                                    "end", err + "( not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <2D-argument>

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                output.insert("end", "I: ) found\n")
                                                i += 1
                                            else:
                                                output.insert(
                                                    "end", err + ") not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                        else:
                                            output.insert(
                                                "end", err + "insert-argument not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # ,
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                            output.insert("end", "I: , found\n")
                                            i += 1
                                        else:
                                            output.insert(
                                                "end", err + ", not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                    else:
                                        output.insert(
                                            "end", err + "insert-argument not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                # )
                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                    output.insert("end", "I: ) found\n")
                                    i += 1
                                else:
                                    output.insert(
                                        "end", err + ") not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                            # TODO: (wip) <instance-grab> TODO
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
                                    return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # TODO: <all-type-value>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                output.insert(
                                    "end", "I: all-type-value found\n")

                            else:
                                output.insert(
                                    "end", err + "all-type-value not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # )
                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                output.insert("end", "I: ) found\n")
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
                        output.insert(
                            "end", "I: operate-flora-tint found\n")

                        # <operator>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                            output.insert("end", "I: operator found\n")
                            i += 1
                        else:
                            output.insert(
                                "end", err + "operator not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <insert-operation>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:
                            output.insert(
                                "end", "I: insert-operation found\n")

                            # (
                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                output.insert("end", "I: ( found\n")
                                i += 1
                            else:
                                output.insert("end", err + "( not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # <insert-flora-tint>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-flora-tint>"]:
                                output.insert(
                                    "end", "I: insert-flora-tint found\n")
                                i += 1

                                # tint literal
                                if lexeme[i] != "EPSILON" and token[i] == "TINT LIT":
                                    output.insert(
                                        "end", "I: tint literal found\n")
                                    i += 1
                                # flora literal
                                elif lexeme[i] != "EPSILON" and token[i] == "FLORA LIT":
                                    output.insert(
                                        "end", "I: flora literal found\n")
                                    i += 1
                                # identifer
                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                    output.insert(
                                        "end", "I: identifier found\n")
                                    i += 2

                                    # <insert-func>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:
                                        output.insert(
                                            "end", "I: insert-func found\n")

                                        # (
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                            output.insert(
                                                "end", "I: ( found\n")
                                            i += 1
                                        else:
                                            output.insert(
                                                "end", err + "( not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # <argument>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                            output.insert(
                                                "end", "I: argument found\n")

                                            # <insert-argument>
                                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                output.insert(
                                                    "end", "I: insert-argument found\n")

                                                # <all-type-value>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                    output.insert(
                                                        "end", "I: all-type-value found\n")
                                                    i += 1
                                                # # identifier
                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                    output.insert(
                                                        "end", "I: identifier found\n")
                                                    i += 2

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        output.insert("end", "I: ( found\n")
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <2D-argument>

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        output.insert("end", "I: ) found\n")
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + ") not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                else:
                                                    output.insert(
                                                        "end", err + "insert-argument not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # ,
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                    output.insert("end", "I: , found\n")
                                                    i += 1
                                                else:
                                                    output.insert(
                                                        "end", err + ", not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                            else:
                                                output.insert(
                                                    "end", err + "insert-argument not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # -----

                                        # )
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                            output.insert(
                                                "end", "I: ) found\n")
                                            i += 1
                                        else:
                                            output.insert(
                                                "end", err + ") not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                # lent(<all-type-value>)
                                elif lexeme[i] != "EPSILON" and lexeme[i] == "lent":
                                    output.insert("end", "I: lent found\n")
                                    i += 1

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        output.insert(
                                            "end", "I: ( found\n")
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + "( not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <all-type-value>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                        output.insert(
                                            "end", "I: all-type-value found\n")

                                    else:
                                        output.insert(
                                            "end", err + "all-type-value not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        output.insert(
                                            "end", "I: ) found\n")
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
                                    output.insert("end", "I: ) found\n")
                                    i += 1
                                else:
                                    output.insert(
                                        "end", err + ") not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]
            # ;
            if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                output.insert("end", "I: ; found\n")
                i += 1
            else:
                output.insert("end", err + "; not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

        # <i/o-statement>;
        elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<i/o-statement>"]:
            output.insert("end", "I: i/o-statement found\n")

            # mint(<all-type-value>);
            if lexeme[i] != "EPSILON" and lexeme[i] == "mint":
                output.insert("end", "I: mint found\n")
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # TODO: <all-type-value>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    output.insert("end", "I: all-type-value found\n")
                    i += 1
                else:
                    output.insert("end", err + "all-type-value not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    output.insert("end", "I: ) found\n")
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

            # <insert-inpetal>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-inpetal>"]:
                output.insert("end", "I: insert-inpetal found\n")

                # <all-types>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                    output.insert("end", "I: all-types found\n")
                    i += 1

                # #identifier
                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                    output.insert("end", "I: identifier found\n")
                    i += 2  # skip hashtag and identifier name

                    # <insert-func>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:
                        output.insert("end", "I: insert-func found\n")

                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            output.insert("end", "I: ( found\n")
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <argument>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                            output.insert(
                                "end", "I: argument found\n")

                            # <insert-argument>
                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                output.insert(
                                    "end", "I: insert-argument found\n")

                                # <all-type-value>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                    output.insert(
                                        "end", "I: all-type-value found\n")
                                    i += 1
                                # # identifier
                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                    output.insert(
                                        "end", "I: identifier found\n")
                                    i += 2

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        output.insert("end", "I: ( found\n")
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + "( not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <2D-argument>

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        output.insert("end", "I: ) found\n")
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + ") not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                else:
                                    output.insert(
                                        "end", err + "insert-argument not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    output.insert("end", "I: , found\n")
                                    i += 1
                                else:
                                    output.insert(
                                        "end", err + ", not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                            else:
                                output.insert(
                                    "end", err + "insert-argument not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                # -----

                        # )
                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                            output.insert("end", "I: ) found\n")
                            i += 1
                        else:
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                else:
                    output.insert("end", err + "inpetal error\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # inpetal
                if lexeme[i] != "EPSILON" and lexeme[i] == "inpetal":
                    output.insert("end", "I: inpetal found\n")
                    i += 1
                else:
                    output.insert("end", err + "inpetal not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # string literal
                if lexeme[i] != "EPSILON" and token[i] == "string literal":
                    output.insert("end", "I: string literal found\n")
                    i += 1
                else:
                    output.insert("end", err + "string literal not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    output.insert("end", "I: ) found\n")
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

        # #identifier
        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
            output.insert("end", "I: identifier found\n")
            i += 2  # skip hashtag and identifier name

            # <insert-func>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:
                output.insert("end", "I: insert-func found\n")

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <argument>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                    output.insert(
                        "end", "I: argument found\n")

                    # <insert-argument>
                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                        output.insert(
                            "end", "I: insert-argument found\n")

                        # <all-type-value>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                            output.insert(
                                "end", "I: all-type-value found\n")
                            i += 1
                        # # identifier
                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                            output.insert(
                                "end", "I: identifier found\n")
                            i += 2

                            # (
                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                output.insert("end", "I: ( found\n")
                                i += 1
                            else:
                                output.insert(
                                    "end", err + "( not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # TODO: <2D-argument>

                            # )
                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                output.insert("end", "I: ) found\n")
                                i += 1
                            else:
                                output.insert(
                                    "end", err + ") not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                        else:
                            output.insert(
                                "end", err + "insert-argument not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # ,
                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                            output.insert("end", "I: , found\n")
                            i += 1
                        else:
                            output.insert(
                                "end", err + ", not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                    else:
                        output.insert(
                            "end", err + "insert-argument not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                        # -----


                # )
                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                    output.insert("end", "I: ) found\n")
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
            else:
                output.insert("end", err + "identifier error\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <more-id>
            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<more-id>"]:
                output.insert("end", "I: more-id found\n")

                # <indexing>
                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<indexing>"]:
                    output.insert("end", "I: indexing found\n")

                    # [
                    if lexeme[i] != "EPSILON" and lexeme[i] == "[":
                        output.insert("end", "I: [ found\n")
                        i += 1
                    else:
                        output.insert("end", err + "[ not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <insert-index>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-index>"]:
                        output.insert("end", err + "[ not found\n")
                        # tint literal
                        if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                            output.insert("end", "I: tint literal found\n")
                            i += 1
                        # string literal
                        if lexeme[i] != "EPSILON" and token[i] == "string literal":
                            output.insert("end", "I: tint literal found\n")
                            i += 1

                    # ]
                    if lexeme[i] != "EPSILON" and lexeme[i] == "]":
                        output.insert("end", "I: ] found\n")
                        i += 1
                    else:
                        output.insert("end", err + "] not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                # ,
                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                    output.insert("end", "I: , found\n")
                    i += 1
                else:
                    output.insert("end", err + ", not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # #identifier
                if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                    output.insert("end", "I: identifier found\n")
                    i += 2
                else:
                    output.insert("end", err + "identifier not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <insert-func>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-func>"]:
                    output.insert("end", "I: insert-func found\n")

                    # (
                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                        output.insert("end", "I: ( found\n")
                        i += 1
                    else:
                        output.insert("end", err + "( not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <argument>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                        output.insert(
                            "end", "I: argument found\n")

                        # <insert-argument>
                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                            output.insert(
                                "end", "I: insert-argument found\n")

                            # <all-type-value>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                output.insert(
                                    "end", "I: all-type-value found\n")
                                i += 1
                            # # identifier
                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                output.insert(
                                    "end", "I: identifier found\n")
                                i += 2

                                # (
                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                    output.insert("end", "I: ( found\n")
                                    i += 1
                                else:
                                    output.insert(
                                        "end", err + "( not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <2D-argument>

                                # )
                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                    output.insert("end", "I: ) found\n")
                                    i += 1
                                else:
                                    output.insert(
                                        "end", err + ") not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                            else:
                                output.insert(
                                    "end", err + "insert-argument not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # ,
                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                output.insert("end", "I: , found\n")
                                i += 1
                            else:
                                output.insert(
                                    "end", err + ", not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                        else:
                            output.insert(
                                "end", err + "insert-argument not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                            # -----


                    # )
                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                        output.insert("end", "I: ) found\n")
                        i += 1
                    else:
                        output.insert("end", err + ") not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                else:
                    output.insert("end", err + "<insert-func> not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <indexing>
                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<indexing>"]:
                    output.insert("end", "I: indexing found\n")

                    # [
                    if lexeme[i] != "EPSILON" and lexeme[i] == "[":
                        output.insert("end", "I: [ found\n")
                        i += 1
                    else:
                        output.insert("end", err + "[ not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <insert-index>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-index>"]:
                        output.insert("end", err + "[ not found\n")
                        # tint literal
                        if lexeme[i] != "EPSILON" and token[i] == "tint literal":
                            output.insert("end", "I: tint literal found\n")
                            i += 1
                        # string literal
                        if lexeme[i] != "EPSILON" and token[i] == "string literal":
                            output.insert("end", "I: tint literal found\n")
                            i += 1

                    # ]
                    if lexeme[i] != "EPSILON" and lexeme[i] == "]":
                        output.insert("end", "I: ] found\n")
                        i += 1
                    else:
                        output.insert("end", err + "] not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

        # leaf
        elif lexeme[i] != "EPSILON" and lexeme[i] == "leaf":
            output.insert("end", "I: leaf found\n")
            i += 1

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                output.insert("end", "I: ( found\n")
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <all-type-value>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                output.insert("end", "I: all-type-value found\n")
                i += 1
            else:
                output.insert("end", err + "all-type-value not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <more-all>
            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<more-all>"]:
                output.insert("end", "I: more-all found\n")

                # ,
                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                    output.insert("end", "I: , found\n")
                    i += 1
                else:
                    output.insert("end", err + ", not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <all-type-value>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    output.insert("end", "I: all-type-value found\n")
                    i += 1
                else:
                    output.insert("end", err + "all-type-value not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

            # <insert-condition>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:
                output.insert("end", "I: insert-condition found\n")

                # <all-cond-operator>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                    output.insert("end", "I: all-cond-operator found\n")
                    i += 1

                    # <insert-all-operand>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:
                        output.insert("end", "I: insert-all-operand found\n")

                        # <flora-tint-value>
                        if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
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
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # <argument>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                output.insert(
                                                    "end", "I: argument found\n")

                                                # <insert-argument>
                                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                    output.insert(
                                                        "end", "I: insert-argument found\n")

                                                    # <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        output.insert(
                                                            "end", "I: all-type-value found\n")
                                                        i += 1
                                                    # # identifier
                                                    elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                        output.insert(
                                                            "end", "I: identifier found\n")
                                                        i += 2

                                                        # (
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                            output.insert("end", "I: ( found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + "( not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # TODO: <2D-argument>

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            output.insert("end", "I: ) found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    else:
                                                        output.insert(
                                                            "end", err + "insert-argument not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # ,
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                        output.insert("end", "I: , found\n")
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + ", not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                else:
                                                    output.insert(
                                                        "end", err + "insert-argument not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # -----


                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                output.insert("end", "I: ) found\n")
                                                i += 1
                                            else:
                                                output.insert("end", err + ") not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # TODO: <all-type-value>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                            output.insert("end", "I: all-type-value found\n")

                                        else:
                                            output.insert(
                                                "end", err + "all-type-value not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # )
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                            output.insert("end", "I: ) found\n")
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
                                    output.insert("end", "I: operate-flora-tint found\n")

                                    # <operator>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                        output.insert("end", "I: operator found\n")
                                        i += 1
                                    else:
                                        output.insert("end", err + "operator not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # <insert-operation>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:
                                        output.insert("end", "I: insert-operation found\n")

                                        # (
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                            output.insert("end", "I: ( found\n")
                                            i += 1
                                        else:
                                            output.insert("end", err + "( not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # <argument>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                        output.insert(
                                                            "end", "I: argument found\n")

                                                        # <insert-argument>
                                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                            output.insert(
                                                                "end", "I: insert-argument found\n")

                                                            # <all-type-value>
                                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                output.insert(
                                                                    "end", "I: all-type-value found\n")
                                                                i += 1
                                                            # # identifier
                                                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                output.insert(
                                                                    "end", "I: identifier found\n")
                                                                i += 2

                                                                # (
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                    output.insert("end", "I: ( found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + "( not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # TODO: <2D-argument>

                                                                # )
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                    output.insert("end", "I: ) found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ") not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            else:
                                                                output.insert(
                                                                    "end", err + "insert-argument not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # ,
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                                output.insert("end", "I: , found\n")
                                                                i += 1
                                                            else:
                                                                output.insert(
                                                                    "end", err + ", not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        else:
                                                            output.insert(
                                                                "end", err + "insert-argument not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # -----

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        output.insert("end", "I: ) found\n")
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + ") not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # TODO: <all-type-value>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                    output.insert(
                                                        "end", "I: all-type-value found\n")

                                                else:
                                                    output.insert(
                                                        "end", err + "all-type-value not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    output.insert("end", "I: ) found\n")
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
                                                output.insert("end", "I: ) found\n")
                                                i += 1
                                            else:
                                                output.insert("end", err + ") not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    output.insert("end", "I: , found\n")
                                    i += 1
                                else:
                                    break

                        # <common-type>
                        elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                output.insert("end", "I: common-type found\n")
                                i += 1

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    output.insert("end", "I: , found\n")
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
                    output.insert("end", "I: string-cond-op found\n")
                    i += 1

                    # <string-operand>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:
                        output.insert("end", "I: string-operand found\n")

                        # TODO: <all-type-value>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                output.insert("end", "I: all-type-value found\n")
                                i += 1

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    output.insert("end", "I: , found\n")
                                    i += 1
                                else:
                                    break
                        # <all-types>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                output.insert("end", "I: all-types found\n")
                                i += 1

                                # ,
                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                    output.insert("end", "I: , found\n")
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
                output.insert("end", "I: ) found\n")
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                output.insert("end", "I: ( found\n")
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
                output.insert("end", "I: ) found\n")
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # ;
            if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                output.insert("end", "I: ; found\n")
                i += 1
            else:
                output.insert("end", err + "; not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # eleaf
            while lexeme[i] != "EPSILON" and lexeme[i] == "eleaf":
                output.insert("end", "i: eleaf found\n")
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <all-type-value>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    output.insert("end", "I: all-type-value found\n")
                    i += 1
                else:
                    output.insert("end", err + "all-type-value not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <more-all>
                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<more-all>"]:
                    output.insert("end", "I: more-all found\n")

                    # ,
                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                        output.insert("end", "I: , found\n")
                        i += 1
                    else:
                        output.insert("end", err + ", not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <all-type-value>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                        output.insert("end", "I: all-type-value found\n")
                        i += 1
                    else:
                        output.insert("end", err + "all-type-value not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                # <insert-condition>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:
                    output.insert("end", "I: insert-condition found\n")

                    # <all-cond-operator>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                        output.insert("end", "I: all-cond-operator found\n")
                        i += 1

                        # <insert-all-operand>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:
                            output.insert("end", "I: insert-all-operand found\n")

                            # <flora-tint-value>
                            if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
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
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # <argument>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                    output.insert(
                                                        "end", "I: argument found\n")

                                                    # <insert-argument>
                                                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                        output.insert(
                                                            "end", "I: insert-argument found\n")

                                                        # <all-type-value>
                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                            output.insert(
                                                                "end", "I: all-type-value found\n")
                                                            i += 1
                                                        # # identifier
                                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                            output.insert(
                                                                "end", "I: identifier found\n")
                                                            i += 2

                                                            # (
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                output.insert("end", "I: ( found\n")
                                                                i += 1
                                                            else:
                                                                output.insert(
                                                                    "end", err + "( not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # TODO: <2D-argument>

                                                            # )
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                output.insert("end", "I: ) found\n")
                                                                i += 1
                                                            else:
                                                                output.insert(
                                                                    "end", err + ") not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        else:
                                                            output.insert(
                                                                "end", err + "insert-argument not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # ,
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                            output.insert("end", "I: , found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ", not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    else:
                                                        output.insert(
                                                            "end", err + "insert-argument not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # -----

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    output.insert("end", "I: ) found\n")
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <all-type-value>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                output.insert("end", "I: all-type-value found\n")

                                            else:
                                                output.insert(
                                                    "end", err + "all-type-value not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                output.insert("end", "I: ) found\n")
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
                                        output.insert("end", "I: operate-flora-tint found\n")

                                        # <operator>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                            output.insert("end", "I: operator found\n")
                                            i += 1
                                        else:
                                            output.insert("end", err + "operator not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # <insert-operation>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:
                                            output.insert("end", "I: insert-operation found\n")

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                output.insert("end", "I: ( found\n")
                                                i += 1
                                            else:
                                                output.insert("end", err + "( not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # <argument>
                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                            output.insert(
                                                                "end", "I: argument found\n")

                                                            # <insert-argument>
                                                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                                output.insert(
                                                                    "end", "I: insert-argument found\n")

                                                                # <all-type-value>
                                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                    output.insert(
                                                                        "end", "I: all-type-value found\n")
                                                                    i += 1
                                                                # # identifier
                                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                    output.insert(
                                                                        "end", "I: identifier found\n")
                                                                    i += 2

                                                                    # (
                                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                        output.insert("end", "I: ( found\n")
                                                                        i += 1
                                                                    else:
                                                                        output.insert(
                                                                            "end", err + "( not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                    # TODO: <2D-argument>

                                                                    # )
                                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                        output.insert("end", "I: ) found\n")
                                                                        i += 1
                                                                    else:
                                                                        output.insert(
                                                                            "end", err + ") not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                else:
                                                                    output.insert(
                                                                        "end", err + "insert-argument not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # ,
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                                    output.insert("end", "I: , found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ", not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            else:
                                                                output.insert(
                                                                    "end", err + "insert-argument not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # -----

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            output.insert("end", "I: ) found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        output.insert(
                                                            "end", "I: all-type-value found\n")

                                                    else:
                                                        output.insert(
                                                            "end", err + "all-type-value not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        output.insert("end", "I: ) found\n")
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
                                                    output.insert("end", "I: ) found\n")
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
                                        i += 1
                                    else:
                                        break

                            # <common-type>
                            elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                    output.insert("end", "I: common-type found\n")
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
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
                        output.insert("end", "I: string-cond-op found\n")
                        i += 1

                        # <string-operand>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:
                            output.insert("end", "I: string-operand found\n")

                            # TODO: <all-type-value>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                    output.insert("end", "I: all-type-value found\n")
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
                                        i += 1
                                    else:
                                        break
                            # <all-types>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                    output.insert("end", "I: all-types found\n")
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
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
                    output.insert("end", "I: ) found\n")
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
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
                    output.insert("end", "I: ) found\n")
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # ;
                if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                    output.insert("end", "I: ; found\n")
                    i += 1
                else:
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
            # <else>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<else>"]:
                output.insert("end", "I: else found\n")
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
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
                    output.insert("end", "I: ) found\n")
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

        # TODO: loops
        # <iterative>
        elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<iterative>"]:
            output.insert("end", "I: iterative found\n")
            i += 1

            # fern
            if lexeme[i] != "EPSILON" and lexeme[i] == "fern":
                output.insert("end", "I: fern found\n")
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <insert-fern>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-fern>"]:
                    output.insert("end", "I: insert-fern found\n")

                    # #identifer = <insert-flora-tint>; <all-type-value> <more-all> <insert-condition>; #identifer <all-assignment> <insert-flora-tint>;)
                    if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                        output.insert("end", "I: identifier found\n")
                        i += 2

                        # =
                        if lexeme[i] != "EPSILON" and lexeme[i] == "=":
                            output.insert("end", "I: = found\n")
                            i += 1
                        else:
                            output.insert("end", err + "= not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # <argument>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                            output.insert(
                                                "end", "I: argument found\n")

                                            # <insert-argument>
                                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                output.insert(
                                                    "end", "I: insert-argument found\n")

                                                # <all-type-value>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                    output.insert(
                                                        "end", "I: all-type-value found\n")
                                                    i += 1
                                                # # identifier
                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                    output.insert(
                                                        "end", "I: identifier found\n")
                                                    i += 2

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        output.insert("end", "I: ( found\n")
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <2D-argument>

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        output.insert("end", "I: ) found\n")
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + ") not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                else:
                                                    output.insert(
                                                        "end", err + "insert-argument not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # ,
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                    output.insert("end", "I: , found\n")
                                                    i += 1
                                                else:
                                                    output.insert(
                                                        "end", err + ", not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                            else:
                                                output.insert(
                                                    "end", err + "insert-argument not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # -----

                                        # )
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                            output.insert("end", "I: ) found\n")
                                            i += 1
                                        else:
                                            output.insert("end", err + ") not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                            return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # TODO: <all-type-value>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                        output.insert("end", "I: all-type-value found\n")

                                    else:
                                        output.insert(
                                            "end", err + "all-type-value not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        output.insert("end", "I: ) found\n")
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
                                output.insert("end", "I: operate-flora-tint found\n")

                                # <operator>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                    output.insert("end", "I: operator found\n")
                                    i += 1
                                else:
                                    output.insert("end", err + "operator not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # <insert-operation>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:
                                    output.insert("end", "I: insert-operation found\n")

                                    # (
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                        output.insert("end", "I: ( found\n")
                                        i += 1
                                    else:
                                        output.insert("end", err + "( not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # <argument>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                    output.insert(
                                                        "end", "I: argument found\n")

                                                    # <insert-argument>
                                                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                        output.insert(
                                                            "end", "I: insert-argument found\n")

                                                        # <all-type-value>
                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                            output.insert(
                                                                "end", "I: all-type-value found\n")
                                                            i += 1
                                                        # # identifier
                                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                            output.insert(
                                                                "end", "I: identifier found\n")
                                                            i += 2

                                                            # (
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                output.insert("end", "I: ( found\n")
                                                                i += 1
                                                            else:
                                                                output.insert(
                                                                    "end", err + "( not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # TODO: <2D-argument>

                                                            # )
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                output.insert("end", "I: ) found\n")
                                                                i += 1
                                                            else:
                                                                output.insert(
                                                                    "end", err + ") not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        else:
                                                            output.insert(
                                                                "end", err + "insert-argument not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # ,
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                            output.insert("end", "I: , found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ", not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    else:
                                                        output.insert(
                                                            "end", err + "insert-argument not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # -----

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    output.insert("end", "I: ) found\n")
                                                    i += 1
                                                else:
                                                    output.insert(
                                                        "end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <all-type-value>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                output.insert(
                                                    "end", "I: all-type-value found\n")

                                            else:
                                                output.insert(
                                                    "end", err + "all-type-value not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                output.insert("end", "I: ) found\n")
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
                                            output.insert("end", "I: ) found\n")
                                            i += 1
                                        else:
                                            output.insert("end", err + ") not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # TODO: <all-type-value>
                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                            output.insert("end", "I: all-type-value found\n")
                            i += 1

                            # ,
                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                output.insert("end", "I: , found\n")
                                i += 1
                            else:
                                break

                        # <insert-condition>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:
                            output.insert("end", "I: insert-condition found\n")

                            # <all-cond-operator>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                                output.insert("end", "I: all-cond-operator found\n")
                                i += 1

                                # <insert-all-operand>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:
                                    output.insert("end", "I: insert-all-operand found\n")

                                    # <flora-tint-value>
                                    if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
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
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # <argument>
                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                            output.insert(
                                                                "end", "I: argument found\n")

                                                            # <insert-argument>
                                                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                                output.insert(
                                                                    "end", "I: insert-argument found\n")

                                                                # <all-type-value>
                                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                    output.insert(
                                                                        "end", "I: all-type-value found\n")
                                                                    i += 1
                                                                # # identifier
                                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                    output.insert(
                                                                        "end", "I: identifier found\n")
                                                                    i += 2

                                                                    # (
                                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                        output.insert("end", "I: ( found\n")
                                                                        i += 1
                                                                    else:
                                                                        output.insert(
                                                                            "end", err + "( not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                    # TODO: <2D-argument>

                                                                    # )
                                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                        output.insert("end", "I: ) found\n")
                                                                        i += 1
                                                                    else:
                                                                        output.insert(
                                                                            "end", err + ") not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                else:
                                                                    output.insert(
                                                                        "end", err + "insert-argument not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # ,
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                                    output.insert("end", "I: , found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ", not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            else:
                                                                output.insert(
                                                                    "end", err + "insert-argument not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # -----

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            output.insert("end", "I: ) found\n")
                                                            i += 1
                                                        else:
                                                            output.insert("end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        output.insert("end", "I: all-type-value found\n")

                                                    else:
                                                        output.insert(
                                                            "end", err + "all-type-value not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        output.insert("end", "I: ) found\n")
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
                                                output.insert("end", "I: operate-flora-tint found\n")

                                                # <operator>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                                    output.insert("end", "I: operator found\n")
                                                    i += 1
                                                else:
                                                    output.insert("end", err + "operator not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # <insert-operation>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:
                                                    output.insert("end", "I: insert-operation found\n")

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        output.insert("end", "I: ( found\n")
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # <argument>
                                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                                    output.insert(
                                                                        "end", "I: argument found\n")

                                                                    # <insert-argument>
                                                                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                                        output.insert(
                                                                            "end", "I: insert-argument found\n")

                                                                        # <all-type-value>
                                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                            output.insert(
                                                                                "end", "I: all-type-value found\n")
                                                                            i += 1
                                                                        # # identifier
                                                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                            output.insert(
                                                                                "end", "I: identifier found\n")
                                                                            i += 2

                                                                            # (
                                                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                                output.insert("end", "I: ( found\n")
                                                                                i += 1
                                                                            else:
                                                                                output.insert(
                                                                                    "end", err + "( not found\n")
                                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                            # TODO: <2D-argument>

                                                                            # )
                                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                                output.insert("end", "I: ) found\n")
                                                                                i += 1
                                                                            else:
                                                                                output.insert(
                                                                                    "end", err + ") not found\n")
                                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                        else:
                                                                            output.insert(
                                                                                "end", err + "insert-argument not found\n")
                                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                        # ,
                                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                                            output.insert("end", "I: , found\n")
                                                                            i += 1
                                                                        else:
                                                                            output.insert(
                                                                                "end", err + ", not found\n")
                                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                    else:
                                                                        output.insert(
                                                                            "end", err + "insert-argument not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                        # -----

                                                                # )
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                    output.insert("end", "I: ) found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ") not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # TODO: <all-type-value>
                                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                output.insert(
                                                                    "end", "I: all-type-value found\n")

                                                            else:
                                                                output.insert(
                                                                    "end", err + "all-type-value not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # )
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                output.insert("end", "I: ) found\n")
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
                                                            output.insert("end", "I: ) found\n")
                                                            i += 1
                                                        else:
                                                            output.insert("end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
                                                i += 1
                                            else:
                                                break

                                    # <common-type>
                                    elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                            output.insert("end", "I: common-type found\n")
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
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
                                output.insert("end", "I: string-cond-op found\n")
                                i += 1

                                # <string-operand>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:
                                    output.insert("end", "I: string-operand found\n")

                                    # TODO: <all-type-value>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                            output.insert("end", "I: all-type-value found\n")
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
                                                i += 1
                                            else:
                                                break
                                    # <all-types>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                            output.insert("end", "I: all-types found\n")
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
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
                            output.insert("end", "I: ; found\n")
                            i += 1
                        else:
                            output.insert("end", err + "; not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # #identifer
                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                            output.insert("end", "I: identifier found\n")
                            i += 2
                        else:
                            output.insert("end", err + "identifier not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <all-assignment>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-assignment>"]:
                            output.insert("end", "I: all-assignment found\n")
                            i += 1
                        else:
                            output.insert("end", err + "all-assignment not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # <argument>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                        output.insert(
                                            "end", "I: argument found\n")

                                        # <insert-argument>
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                            output.insert(
                                                "end", "I: insert-argument found\n")

                                            # <all-type-value>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                output.insert(
                                                    "end", "I: all-type-value found\n")
                                                i += 1
                                            # # identifier
                                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                output.insert(
                                                    "end", "I: identifier found\n")
                                                i += 2

                                                # (
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                    output.insert("end", "I: ( found\n")
                                                    i += 1
                                                else:
                                                    output.insert(
                                                        "end", err + "( not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # TODO: <2D-argument>

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    output.insert("end", "I: ) found\n")
                                                    i += 1
                                                else:
                                                    output.insert(
                                                        "end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                            else:
                                                output.insert(
                                                    "end", err + "insert-argument not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
                                                i += 1
                                            else:
                                                output.insert(
                                                    "end", err + ", not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                        else:
                                            output.insert(
                                                "end", err + "insert-argument not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # -----

                                    # )
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                        output.insert("end", "I: ) found\n")
                                        i += 1
                                    else:
                                        output.insert("end", err + ") not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                        return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # TODO: <all-type-value>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                    output.insert("end", "I: all-type-value found\n")

                                else:
                                    output.insert(
                                        "end", err + "all-type-value not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # )
                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                    output.insert("end", "I: ) found\n")
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
                            output.insert("end", "I: ; found\n")
                            i += 1
                        else:
                            output.insert("end", err + "; not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # )
                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                            output.insert("end", "I: ) found\n")
                            i += 1
                        else:
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            output.insert("end", "I: ( found\n")
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
                            output.insert("end", "I: ) found\n")
                            i += 1
                        else:
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                    # TODO: <common-data>
                    elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-data>"]:
                        output.insert("end", "I: common-data found\n")
                        i += 1

                        # (
                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                            output.insert("end", "I: ( found\n")
                            i += 1
                        else:
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
            # willow
            elif lexeme[i] != "EPSILON" and lexeme[i] == "willow":
                output.insert("end", "I: willow found\n")
                i += 1

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
                    i += 1
                else:
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # TODO: all-type-value and more-all
                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    output.insert("end", "I: all-type-value found\n")
                    i += 1

                    # ,
                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                        output.insert("end", "I: , found\n")
                        i += 1
                    else:
                        break

                # <insert-condition>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:
                    output.insert("end", "I: insert-condition found\n")

                    # <all-cond-operator>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                        output.insert("end", "I: all-cond-operator found\n")
                        i += 1

                        # <insert-all-operand>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:
                            output.insert("end", "I: insert-all-operand found\n")

                            # <flora-tint-value>
                            if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
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
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # <argument>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                    output.insert(
                                                        "end", "I: argument found\n")

                                                    # <insert-argument>
                                                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                        output.insert(
                                                            "end", "I: insert-argument found\n")

                                                        # <all-type-value>
                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                            output.insert(
                                                                "end", "I: all-type-value found\n")
                                                            i += 1
                                                        # # identifier
                                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                            output.insert(
                                                                "end", "I: identifier found\n")
                                                            i += 2

                                                            # (
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                output.insert("end", "I: ( found\n")
                                                                i += 1
                                                            else:
                                                                output.insert(
                                                                    "end", err + "( not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # TODO: <2D-argument>

                                                            # )
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                output.insert("end", "I: ) found\n")
                                                                i += 1
                                                            else:
                                                                output.insert(
                                                                    "end", err + ") not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        else:
                                                            output.insert(
                                                                "end", err + "insert-argument not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # ,
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                            output.insert("end", "I: , found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ", not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    else:
                                                        output.insert(
                                                            "end", err + "insert-argument not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # -----

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    output.insert("end", "I: ) found\n")
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # TODO: <all-type-value>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                output.insert("end", "I: all-type-value found\n")

                                            else:
                                                output.insert(
                                                    "end", err + "all-type-value not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # )
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                output.insert("end", "I: ) found\n")
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
                                        output.insert("end", "I: operate-flora-tint found\n")

                                        # <operator>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                            output.insert("end", "I: operator found\n")
                                            i += 1
                                        else:
                                            output.insert("end", err + "operator not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # <insert-operation>
                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:
                                            output.insert("end", "I: insert-operation found\n")

                                            # (
                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                output.insert("end", "I: ( found\n")
                                                i += 1
                                            else:
                                                output.insert("end", err + "( not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # <argument>
                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                            output.insert(
                                                                "end", "I: argument found\n")

                                                            # <insert-argument>
                                                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                                output.insert(
                                                                    "end", "I: insert-argument found\n")

                                                                # <all-type-value>
                                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                    output.insert(
                                                                        "end", "I: all-type-value found\n")
                                                                    i += 1
                                                                # # identifier
                                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                    output.insert(
                                                                        "end", "I: identifier found\n")
                                                                    i += 2

                                                                    # (
                                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                        output.insert("end", "I: ( found\n")
                                                                        i += 1
                                                                    else:
                                                                        output.insert(
                                                                            "end", err + "( not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                    # TODO: <2D-argument>

                                                                    # )
                                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                        output.insert("end", "I: ) found\n")
                                                                        i += 1
                                                                    else:
                                                                        output.insert(
                                                                            "end", err + ") not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                else:
                                                                    output.insert(
                                                                        "end", err + "insert-argument not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # ,
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                                    output.insert("end", "I: , found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ", not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            else:
                                                                output.insert(
                                                                    "end", err + "insert-argument not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # -----

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            output.insert("end", "I: ) found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        output.insert(
                                                            "end", "I: all-type-value found\n")

                                                    else:
                                                        output.insert(
                                                            "end", err + "all-type-value not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        output.insert("end", "I: ) found\n")
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
                                                    output.insert("end", "I: ) found\n")
                                                    i += 1
                                                else:
                                                    output.insert("end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
                                        i += 1
                                    else:
                                        break

                            # <common-type>
                            elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                    output.insert("end", "I: common-type found\n")
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
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
                        output.insert("end", "I: string-cond-op found\n")
                        i += 1

                        # <string-operand>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:
                            output.insert("end", "I: string-operand found\n")

                            # TODO: <all-type-value>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                    output.insert("end", "I: all-type-value found\n")
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
                                        i += 1
                                    else:
                                        break
                            # <all-types>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                    output.insert("end", "I: all-types found\n")
                                    i += 1

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
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
                    output.insert("end", "I: ) found\n")
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
            else:
                output.insert("end", err + "iterative not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

        # TODO: tree
        if lexeme[i] != "EPSILON" and lexeme[i] == "tree":
            output.insert("end", "I: tree found\n")

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                output.insert("end", "I: ( found\n")
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # #identifier
            if lexeme[i] != "EPSILON" and lexeme[i] == "#identifier":
                output.insert("end", "I: identifier found\n")
                i += 2
            else:
                output.insert("end", err + "identifier not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                output.insert("end", "I: ) found\n")
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                output.insert("end", "I: ( found\n")
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # branch
            if lexeme[i] != "EPSILON" and lexeme[i] == "branch":
                output.insert("end", "I: branch found\n")
                i += 1
            else:
                output.insert("end", err + "branch not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <all-type-value>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                output.insert("end", "I: all-type-value found\n")
                i += 1
            else:
                output.insert("end", err + "all-type-value not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <insert-branch>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-branch>"]:
                output.insert("end", "I: insert-branch found\n")

                # :
                if lexeme[i] != "EPSILON" and lexeme[i] == ":":
                    output.insert("end", "I: : found\n")
                    i += 1
                    # statement
                    i, results = statement(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return results
                # leaf
                elif lexeme[i] != "EPSILON" and lexeme[i] == "leaf":
                    output.insert("end", "I: leaf found\n")
                    i += 1

                    # <all-type-value>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                        output.insert("end", "I: all-type-value found\n")
                        i += 1
                    else:
                        output.insert("end", err + "all-type-value not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <more-all>
                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<more-all>"]:
                        output.insert("end", "I: more-all found\n")

                        # ,
                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                            output.insert("end", "I: , found\n")
                            i += 1
                        else:
                            output.insert("end", err + ", not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <all-type-value>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                            output.insert("end", "I: all-type-value found\n")
                            i += 1
                        else:
                            output.insert("end", err + "all-type-value not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # <insert-condition>
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-condition>"]:
                            output.insert("end", "I: insert-condition found\n")

                            # <all-cond-operator>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-cond-operator>"]:
                                output.insert("end", "I: all-cond-operator found\n")
                                i += 1

                                # <insert-all-operand>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-all-operand>"]:
                                    output.insert("end", "I: insert-all-operand found\n")

                                    # <flora-tint-value>
                                    if lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]):
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
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # <argument>
                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                            output.insert(
                                                                "end", "I: argument found\n")

                                                            # <insert-argument>
                                                            while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                                output.insert(
                                                                    "end", "I: insert-argument found\n")

                                                                # <all-type-value>
                                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                    output.insert(
                                                                        "end", "I: all-type-value found\n")
                                                                    i += 1
                                                                # # identifier
                                                                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                    output.insert(
                                                                        "end", "I: identifier found\n")
                                                                    i += 2

                                                                    # (
                                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                        output.insert("end", "I: ( found\n")
                                                                        i += 1
                                                                    else:
                                                                        output.insert(
                                                                            "end", err + "( not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                    # TODO: <2D-argument>

                                                                    # )
                                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                        output.insert("end", "I: ) found\n")
                                                                        i += 1
                                                                    else:
                                                                        output.insert(
                                                                            "end", err + ") not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                else:
                                                                    output.insert(
                                                                        "end", err + "insert-argument not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # ,
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                                    output.insert("end", "I: , found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ", not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            else:
                                                                output.insert(
                                                                    "end", err + "insert-argument not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # -----


                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            output.insert("end", "I: ) found\n")
                                                            i += 1
                                                        else:
                                                            output.insert("end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # TODO: <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        output.insert("end", "I: all-type-value found\n")

                                                    else:
                                                        output.insert(
                                                            "end", err + "all-type-value not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # )
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                        output.insert("end", "I: ) found\n")
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
                                                output.insert("end", "I: operate-flora-tint found\n")

                                                # <operator>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<operator>"]:
                                                    output.insert("end", "I: operator found\n")
                                                    i += 1
                                                else:
                                                    output.insert("end", err + "operator not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # <insert-operation>
                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-operation>"]:
                                                    output.insert("end", "I: insert-operation found\n")

                                                    # (
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                        output.insert("end", "I: ( found\n")
                                                        i += 1
                                                    else:
                                                        output.insert("end", err + "( not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # <argument>
                                                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                                    output.insert(
                                                                        "end", "I: argument found\n")

                                                                    # <insert-argument>
                                                                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                                        output.insert(
                                                                            "end", "I: insert-argument found\n")

                                                                        # <all-type-value>
                                                                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                            output.insert(
                                                                                "end", "I: all-type-value found\n")
                                                                            i += 1
                                                                        # # identifier
                                                                        elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                            output.insert(
                                                                                "end", "I: identifier found\n")
                                                                            i += 2

                                                                            # (
                                                                            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                                output.insert("end", "I: ( found\n")
                                                                                i += 1
                                                                            else:
                                                                                output.insert(
                                                                                    "end", err + "( not found\n")
                                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                            # TODO: <2D-argument>

                                                                            # )
                                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                                output.insert("end", "I: ) found\n")
                                                                                i += 1
                                                                            else:
                                                                                output.insert(
                                                                                    "end", err + ") not found\n")
                                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                        else:
                                                                            output.insert(
                                                                                "end", err + "insert-argument not found\n")
                                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                        # ,
                                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                                            output.insert("end", "I: , found\n")
                                                                            i += 1
                                                                        else:
                                                                            output.insert(
                                                                                "end", err + ", not found\n")
                                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                    else:
                                                                        output.insert(
                                                                            "end", err + "insert-argument not found\n")
                                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                        # -----

                                                                # )
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                    output.insert("end", "I: ) found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ") not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

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
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
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
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # TODO: <all-type-value>
                                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                output.insert(
                                                                    "end", "I: all-type-value found\n")

                                                            else:
                                                                output.insert(
                                                                    "end", err + "all-type-value not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # )
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                output.insert("end", "I: ) found\n")
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
                                                            output.insert("end", "I: ) found\n")
                                                            i += 1
                                                        else:
                                                            output.insert("end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
                                                i += 1
                                            else:
                                                break

                                    # <common-type>
                                    elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                            output.insert("end", "I: common-type found\n")
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
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
                                output.insert("end", "I: string-cond-op found\n")
                                i += 1

                                # <string-operand>
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-operand>"]:
                                    output.insert("end", "I: string-operand found\n")

                                    # TODO: <all-type-value>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                            output.insert("end", "I: all-type-value found\n")
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
                                                i += 1
                                            else:
                                                break
                                    # <all-types>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                                            output.insert("end", "I: all-types found\n")
                                            i += 1

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
                                                i += 1
                                            else:
                                                break
                                    else:
                                        output.insert("end", err + "string-op error\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                else:
                                    output.insert("end", err + "string-operand not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # (
                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                    output.insert("end", "I: ( found\n")
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
                    output.insert("end", "I: ) found\n")
                    i += 1
                else:
                    output.insert("end", err + ") not found\n")
                    return [(lexeme[i], "SYNTAX ERROR")]


                # --
            else:
                output.insert("end", err + "insert-branch not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            # ;
            # <more-branch>

            # statement
            i, results = statement(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return results

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                output.insert("end", "I: ) found\n")
                i += 1

        # clear
        elif lexeme[i] != "EPSILON" and lexeme[i] == "clear":
            output.insert("end", "I: clear found\n")
            i += 1

        # break
        elif lexeme[i] != "EPSILON" and lexeme[i] == "break":
            output.insert("end", "I: break found\n")
            i += 1
            break

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
    if lexeme[i] != "EPSILON" and lexeme[0] == "seed":
        output.insert("end", "I: seed found\n")
        i += 1
    else:
        output.insert("end", err + "seed not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # <global> TODO: string assignment # ---------- #
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

        # <all-types>
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
            while lexeme[i] != "EPSILON" and (lexeme[i] in first_set["<flora-tint-value>"] or token[i] in first_set["<insert-flora-tint>"]):
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

                            # <argument>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                output.insert(
                                    "end", "I: argument found\n")

                                # <insert-argument>
                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                    output.insert(
                                        "end", "I: insert-argument found\n")

                                    # <all-type-value>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                        output.insert(
                                            "end", "I: all-type-value found\n")
                                        i += 1
                                    # # identifier
                                    elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                        output.insert(
                                            "end", "I: identifier found\n")
                                        i += 2

                                        # (
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                            output.insert("end", "I: ( found\n")
                                            i += 1
                                        else:
                                            output.insert(
                                                "end", err + "( not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # TODO: <2D-argument>

                                        # )
                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                            output.insert("end", "I: ) found\n")
                                            i += 1
                                        else:
                                            output.insert(
                                                "end", err + ") not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                    else:
                                        output.insert(
                                            "end", err + "insert-argument not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # ,
                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                        output.insert("end", "I: , found\n")
                                        i += 1
                                    else:
                                        output.insert(
                                            "end", err + ", not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                else:
                                    output.insert(
                                        "end", err + "insert-argument not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # -----

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

                                    # <argument>
                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                        output.insert(
                                            "end", "I: argument found\n")

                                        # <insert-argument>
                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                            output.insert(
                                                "end", "I: insert-argument found\n")

                                            # <all-type-value>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                output.insert(
                                                    "end", "I: all-type-value found\n")
                                                i += 1
                                            # # identifier
                                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                output.insert(
                                                    "end", "I: identifier found\n")
                                                i += 2

                                                # (
                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                    output.insert("end", "I: ( found\n")
                                                    i += 1
                                                else:
                                                    output.insert(
                                                        "end", err + "( not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                # TODO: <2D-argument>

                                                # )
                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                    output.insert("end", "I: ) found\n")
                                                    i += 1
                                                else:
                                                    output.insert(
                                                        "end", err + ") not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                            else:
                                                output.insert(
                                                    "end", err + "insert-argument not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # ,
                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                output.insert("end", "I: , found\n")
                                                i += 1
                                            else:
                                                output.insert(
                                                    "end", err + ", not found\n")
                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                        else:
                                            output.insert(
                                                "end", err + "insert-argument not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                            # -----

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

    # ---------- # garden # ---------- #
    if lexeme[i] != "EPSILON" and lexeme[i] == "garden":
        output.insert("end", "I: garden found\n")
        i += 1

        # (
        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
            output.insert("end", "I: ( found\n")
            i += 1
        else:
            output.insert("end", err + "( not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # )
        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
            output.insert("end", "I: ) found\n")
            i += 1
        else:
            output.insert("end", err + ") not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]

        # (
        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
            output.insert("end", "I: ( found\n")
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
            output.insert("end", "I: ) found\n")
            i += 1
        else:
            output.insert("end", err + ") not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]
        # ;
        if lexeme[i] != "EPSILON" and lexeme[i] == ";":
            output.insert("end", "I: ; found\n")
            i += 1
        else:
            output.insert("end", err + "; not found\n")
            return [(lexeme[i], "SYNTAX ERROR")]
    else:
        output.insert("end", err + "garden or floral not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # TODO: <function> # ---------- #
    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<function>"]:
        output.insert("end", "I: function found\n")

        # <common-type>
        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
            # #identifier
            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                output.insert("end", "I: identifier found\n")
                i += 2
            else:
                output.insert("end", err + "identifier not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                output.insert("end", "I: ( found\n")
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # <insert-parameter>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["insert-parameter"]:
                # <keyword-param>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<keyword-param>"]:

                    while True:
                        # <common-type> *#identifier
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                            i += 1
                            if lexeme[i] != "EPSILON" and lexeme[i] == "*":
                                if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                    i += 2
                            else:
                                output.insert("end", err + "identifier not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                        # **#identifier
                        elif lexeme[i] != "EPSILON" and lexeme[i] == "**":
                            i += 1
                            if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                i += 2
                            else:
                                output.insert("end", err + "identifier not found\n")
                                return [(lexeme[i], "SYNTAX ERROR")]

                        # ,
                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                            i += 1
                        else:
                            break

                # <all-types>
                elif lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                    while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-types>"]:
                        i += 1

                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                            i += 2
                        else:
                            output.insert("end", err + "identifier not found\n")
                            return [(lexeme[i], "SYNTAX ERROR")]

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

                                            # <argument>
                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                output.insert(
                                                    "end", "I: argument found\n")

                                                # <insert-argument>
                                                while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                    output.insert(
                                                        "end", "I: insert-argument found\n")

                                                    # <all-type-value>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                        output.insert(
                                                            "end", "I: all-type-value found\n")
                                                        i += 1
                                                    # # identifier
                                                    elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                        output.insert(
                                                            "end", "I: identifier found\n")
                                                        i += 2

                                                        # (
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                            output.insert("end", "I: ( found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + "( not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        # TODO: <2D-argument>

                                                        # )
                                                        if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                            output.insert("end", "I: ) found\n")
                                                            i += 1
                                                        else:
                                                            output.insert(
                                                                "end", err + ") not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    else:
                                                        output.insert(
                                                            "end", err + "insert-argument not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # ,
                                                    if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                        output.insert("end", "I: , found\n")
                                                        i += 1
                                                    else:
                                                        output.insert(
                                                            "end", err + ", not found\n")
                                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                                else:
                                                    output.insert(
                                                        "end", err + "insert-argument not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                    # -----

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

                                                    # <argument>
                                                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<argument>"]:
                                                        output.insert(
                                                            "end", "I: argument found\n")

                                                        # <insert-argument>
                                                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<insert-argument>"]:
                                                            output.insert(
                                                                "end", "I: insert-argument found\n")

                                                            # <all-type-value>
                                                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                                                                output.insert(
                                                                    "end", "I: all-type-value found\n")
                                                                i += 1
                                                            # # identifier
                                                            elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                                                output.insert(
                                                                    "end", "I: identifier found\n")
                                                                i += 2

                                                                # (
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                                                                    output.insert("end", "I: ( found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + "( not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                                # TODO: <2D-argument>

                                                                # )
                                                                if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                                                                    output.insert("end", "I: ) found\n")
                                                                    i += 1
                                                                else:
                                                                    output.insert(
                                                                        "end", err + ") not found\n")
                                                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            else:
                                                                output.insert(
                                                                    "end", err + "insert-argument not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # ,
                                                            if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                                                                output.insert("end", "I: , found\n")
                                                                i += 1
                                                            else:
                                                                output.insert(
                                                                    "end", err + ", not found\n")
                                                                return i, [(lexeme[i], "SYNTAX ERROR")]

                                                        else:
                                                            output.insert(
                                                                "end", err + "insert-argument not found\n")
                                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                                            # -----

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

                        # ,
                        if lexeme[i] != "EPSILON" and lexeme[i] == ",":
                            i += 1
                        else:
                            break
                # #identifer
                elif lexeme[i] != "EPSILON" and lexeme[i] == "#":
                    i += 2
                    # (
                    if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                        i += 1
                    else:
                        output.insert("end", err + "( not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <2D-parameter>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<2D-parameter>"]:
                        while lexeme[i] != "EPSILON" and lexeme[i] in first_set["<2D-parameter>"]:
                            # <keyword-param>
                            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<keyword-param>"]:

                                # <common-type> *#identifier
                                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                                    i += 1
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "*":
                                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                            i += 2
                                    else:
                                        output.insert("end", err + "identifier not found\n")
                                        return [(lexeme[i], "SYNTAX ERROR")]

                                # **#identifier
                                elif lexeme[i] != "EPSILON" and lexeme[i] == "**":
                                    i += 1
                                    if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                                        i += 2
                                    else:
                                        output.insert("end", err + "identifier not found\n")
                                        return [(lexeme[i], "SYNTAX ERROR")]
                    # TODO: while <all-types> #identifier <insert-variable> ,
                    # TODO: while #identifer (<all-types> #identifier <insert-variable> <next-3D-param>) ,


                    else:
                        output.insert("end", err + "2D-parameter not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # )
                    if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                        i += 1
                    else:
                        output.insert("end", err + ") not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
            else:
                output.insert("end", err + "common-type or all-types not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                output.insert("end", "I: ) found\n")
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                output.insert("end", "I: ( found\n")
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
                output.insert("end", "I: regrow found\n")
                i += 1

                # TODO: <insert-regrow>
                # <all-type-value>
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-type-value>"]:
                    output.insert(
                        "end", "I: all-type-value found\n")
                # TODO: <common-data>

            else:
                output.insert("end", err + "regrow not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                output.insert("end", "I: ) found\n")
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # ;
            if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                output.insert("end", "I: ; found\n")
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
                output.insert("end", "I: identifier found\n")
                i += 2
            else:
                output.insert("end", err + "identifier not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                output.insert("end", "I: ( found\n")
                i += 1
            else:
                output.insert("end", err + "( not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # <keyword-param>
            if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<keyword-param>"]:

                # <common-type> *#identifier
                if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<common-type>"]:
                    i += 1
                    if lexeme[i] != "EPSILON" and lexeme[i] == "*":
                        if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                            i += 2
                    else:
                        output.insert("end", err + "identifier not found\n")
                        return [(lexeme[i], "SYNTAX ERROR")]

                # **#identifier
                elif lexeme[i] != "EPSILON" and lexeme[i] == "**":
                    i += 1
                    if lexeme[i] != "EPSILON" and lexeme[i] == "#":
                        output.insert("end", "I: **#id found\n")
                        i += 2
                    else:
                        output.insert("end", err + "identifier not found\n")
                        return [(lexeme[i], "SYNTAX ERROR")]

            # )
            if lexeme[i] != "EPSILON" and lexeme[i] == ")":
                output.insert("end", "I: ) found\n")
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # (
            if lexeme[i] != "EPSILON" and lexeme[i] == "(":
                output.insert("end", "I: ( found\n")
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
                output.insert("end", "I: ) found\n")
                i += 1
            else:
                output.insert("end", err + ") not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

            # ;
            if lexeme[i] != "EPSILON" and lexeme[i] == ";":
                output.insert("end", "I: ; found\n")
                i += 1
            else:
                output.insert("end", err + "; not found\n")
                return [(lexeme[i], "SYNTAX ERROR")]

    # ---------- # plant # ---------- #
    if lexeme[i] != "EPSILON" and lexeme[-2] == "plant":
        output.insert("end", "I: plant found\n")
        i += 1
    else:
        output.insert("end", err + "plant not found\n")
        return [(lexeme[i], "SYNTAX ERROR")]

    output.insert("end", "SyntaxAnalyser: No Error Found.\n")
    return results


# For displaying the Parse Tree
def display_tree():
    pass


# For displaying the token stream e.g., tint a; == reserved word identifier reserved symbol
def token_stream():
    pass
