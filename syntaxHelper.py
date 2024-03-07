from grammar import cfg, first_set, follow_set, predict_set


def insert_index(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<insert-index>"]:
        # tint literal
        if token[i] == "tint literal":
            i += 1
        # string literal
        elif token[i] == "string literal":
            i += 1
        else:
            output.insert(
                "end", err + "tint or string literal not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
    return i, results


def D3_start_end_step(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    # <3D-start-end-step>
    if lexeme[i] in first_set["<3D-start-end-step>"]:
        # [
        if lexeme[i] != "[":
            output.insert(
                "end", err + "[ not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # <3D-insert-start>
        if lexeme[i] in first_set["<3D-insert-start>"]:
            # <insert-index>
            if lexeme[i] in first_set["<insert-index>"]:
                i, results = insert_index(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # :
                if lexeme[i] != ":":
                    output.insert(
                        "end", err + ": not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # <3D-close-start>
                if lexeme[i] in first_set["<3D-close-start>"]:
                    # <3D-close-end>
                    if lexeme[i] in first_set["<3D-close-end>"]:
                        # :
                        if lexeme[i] == ":":
                            i += 1
                            # tint literal
                            if token[i] != "tint literal":
                                output.insert(
                                    "end", err + "tint literal not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1

                        # ]
                        if lexeme[i] != "]":
                            output.insert(
                                "end", err + "] not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1
                    # <insert-index>
                    if lexeme[i] in first_set["<insert-index>"]:
                        i, results = insert_index(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # <3D-close-end>
                        if lexeme[i] in first_set["<3D-close-end>"]:
                            # :
                            if lexeme[i] == ":":
                                i += 1
                                # tint literal
                                if token[i] != "tint literal":
                                    output.insert(
                                        "end", err + "tint literal not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                                i += 1

                            # ]
                            if lexeme[i] != "]":
                                output.insert(
                                    "end", err + "] not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1
                    else:
                        output.insert(
                            "end", err + "3d-close-end or insert-index not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
            elif lexeme[i] == "[":
                i += 1

                # <3D-skip-start>
                if lexeme[i] in first_set["<3D-skip-start>"]:
                    # <insert-index>
                    if lexeme[i] in first_set["<insert-index>"]:
                        i, results = insert_index(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                    # <3D-close-end>
                    if lexeme[i] in first_set["<3D-close-end>"]:
                        # ]
                        if lexeme[i] == "]":
                            i += 1

                        # :
                        elif lexeme[i] == ":":
                            i += 1
                            # tint literal
                            if token[i] != "tint literal":
                                output.insert(
                                    "end", err + "tint literal not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1

                            # ]
                            if lexeme[i] != "]":
                                output.insert(
                                    "end", err + "] not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1
                        else:
                            output.insert(
                                "end", err + "] or : not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
            else:
                output.insert(
                    "end", err + "3D-insert-start error\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
    return i, results


def D2_start_end_step(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<2D-start-end-step>"]:
        # [
        if lexeme[i] != "[":
            output.insert(
                "end", err + "[ not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # <2D-insert-start>
        if lexeme[i] in first_set["<2D-insert-start>"]:
            # <insert-index>
            if lexeme[i] in first_set["<insert-index>"]:
                i, results = insert_index(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # :
                if lexeme[i] != ":":
                    output.insert(
                        "end", err + ": not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # <2D-close-start>
                if lexeme[i] in first_set["<2D-close-start>"]:
                    # <2D-close-end>
                    if lexeme[i] in first_set["<2D-close-end>"]:
                        # ]
                        if lexeme[i] == "]":
                            i += 1

                            # <3D-start-end-step>
                            i, results = D3_start_end_step(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                        # :
                        elif lexeme[i] == ":":
                            i += 1
                            # tint literal
                            if token[i] != "tint literal":
                                output.insert(
                                    "end", err + "tint literal not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # ]
                            if lexeme[i] != "]":
                                output.insert(
                                    "end", err + "] not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1

                            # <3D-start-end-step>
                            i, results = D3_start_end_step(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results
                        else:
                            output.insert(
                                "end", err + "] not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                    # <insert-index>
                    elif lexeme[i] in first_set["<insert-index>"]:
                        i, results = insert_index(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # <2D-close-end>
                        if lexeme[i] in first_set["<2D-close-end>"]:
                            # ]
                            if lexeme[i] == "]":
                                i += 1

                                # <3D-start-end-step>
                                i, results = D3_start_end_step(
                                    lexeme, token, i, output)
                                if "SYNTAX ERROR" in results:
                                    return i, results

                            # :
                            elif lexeme[i] == ":":
                                i += 1
                                # tint literal
                                if token[i] != "tint literal":
                                    output.insert(
                                        "end", err + "tint literal not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                                # ]
                                if lexeme[i] != "]":
                                    output.insert(
                                        "end", err + "] not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                                i += 1

                                # <3D-start-end-step>
                                i, results = D3_start_end_step(
                                    lexeme, token, i, output)
                                if "SYNTAX ERROR" in results:
                                    return i, results
                            else:
                                output.insert(
                                    "end", err + "] not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                        else:
                            output.insert(
                                "end", err + "2D-close-end not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                    else:
                        output.insert(
                            "end", err + "2D-close-start not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
            # :
            elif lexeme[i] == ":":
                i += 1

                # <2D-skip-start>
                if lexeme[i] in first_set["<2D-skip-start>"]:
                    # <insert-index>
                    if lexeme[i] in first_set["<insert-index>"]:
                        i, results = insert_index(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                    # <2D-close-end>
                    if lexeme[i] in first_set["<2D-close-end>"]:
                        # ]
                        if lexeme[i] == "]":
                            i += 1

                            # <3D-start-end-step>
                            i, results = D3_start_end_step(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                        # :
                        elif lexeme[i] == ":":
                            i += 1
                            # tint literal
                            if token[i] != "tint literal":
                                output.insert(
                                    "end", err + "tint literal not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # ]
                            if lexeme[i] != "]":
                                output.insert(
                                    "end", err + "] not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1

                            # <3D-start-end-step>
                            i, results = D3_start_end_step(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results
                        else:
                            output.insert(
                                "end", err + "] not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                    else:
                        output.insert(
                            "end", err + "2D-skip-start not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                # :
                elif lexeme[i] == ":":
                    i += 1
                    # tint literal
                    if token[i] != "tint literal":
                        output.insert(
                            "end", err + "tint literal not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # ]
                    if lexeme[i] != "]":
                        output.insert(
                            "end", err + "] not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                    # <3D-start-end-step>
                    i, results = D3_start_end_step(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results
                else:
                    output.insert(
                        "end", err + "2D-skip-start not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
            else:
                output.insert(
                    "end", err + "2D-insert-start not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

    return i, results


def start_end_step(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<start-end-step>"]:
        # [
        if lexeme[i] != "[":
            output.insert(
                "end", err + "[ not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # <insert-start>
        if lexeme[i] in first_set["<insert-start>"]:
            # <insert-index>
            if lexeme[i] in first_set["<insert-index>"]:
                i, results = insert_index(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # :
                if lexeme[i] != ":":
                    output.insert(
                        "end", err + ": not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # <close-start>
                if lexeme[i] in first_set["<close-start>"]:
                    # <insert-index>
                    if lexeme[i] in first_set["<insert-index>"]:
                        i, results = insert_index(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # :
                        if lexeme[i] != ":":
                            output.insert(
                                "end", err + ": not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # <close-start>
                        if lexeme[i] in first_set["<close-start>"]:
                            # <close-end>
                            if lexeme[i] in first_set["<close-end>"]:
                                # ]
                                if lexeme[i] == "]":
                                    i += 1

                                    # <2D-start-end-step>
                                    i, results = D2_start_end_step(
                                        lexeme, token, i, output)
                                    if "SYNTAX ERROR" in results:
                                        return i, results

                                # :
                                elif lexeme[i] == ":":
                                    i += 1
                                    # tint literal
                                    if token[i] != "tint literal":
                                        output.insert(
                                            "end", err + "tint literal not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]

                                    # ]
                                    if lexeme[i] != "]":
                                        output.insert(
                                            "end", err + "] not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                    i += 1

                                    # <2D-start-end-step>
                                    i, results = D2_start_end_step(
                                        lexeme, token, i, output)
                                    if "SYNTAX ERROR" in results:
                                        return i, results
                                else:
                                    output.insert(
                                        "end", err + "] not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]

                            # <insert-index>
                            elif lexeme[i] in first_set["<insert-index>"]:
                                i, results = insert_index(
                                    lexeme, token, i, output)
                                if "SYNTAX ERROR" in results:
                                    return i, results

                                # <close-end>
                                if lexeme[i] in first_set["<close-end>"]:
                                    # ]
                                    if lexeme[i] == "]":
                                        i += 1

                                        # <2D-start-end-step>
                                        i, results = D2_start_end_step(
                                            lexeme, token, i, output)
                                        if "SYNTAX ERROR" in results:
                                            return i, results

                                    # :
                                    elif lexeme[i] == ":":
                                        i += 1
                                        # tint literal
                                        if token[i] != "tint literal":
                                            output.insert(
                                                "end", err + "tint literal not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]

                                        # ]
                                        if lexeme[i] != "]":
                                            output.insert(
                                                "end", err + "] not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                        i += 1

                                        # <2D-start-end-step>
                                        i, results = D2_start_end_step(
                                            lexeme, token, i, output)
                                        if "SYNTAX ERROR" in results:
                                            return i, results
                                    else:
                                        output.insert(
                                            "end", err + "] not found\n")
                                        return i, [(lexeme[i], "SYNTAX ERROR")]
                                else:
                                    output.insert(
                                        "end", err + "close-end not found\n")
                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                            else:
                                output.insert(
                                    "end", err + "close-start not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                    # <close-end>
                    elif lexeme[i] in first_set["<close-end>"]:
                        # ]
                        if lexeme[i] == "]":
                            i += 1

                            # <2D-start-end-step>
                            i, results = D2_start_end_step(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                        # :
                        elif lexeme[i] == ":":
                            i += 1
                            # tint literal
                            if token[i] != "tint literal":
                                output.insert(
                                    "end", err + "tint literal not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # ]
                            if lexeme[i] != "]":
                                output.insert(
                                    "end", err + "] not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1

                            # <2D-start-end-step>
                            i, results = D2_start_end_step(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results
                        else:
                            output.insert(
                                "end", err + "] not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                    else:
                        output.insert(
                            "end", err + "close-start not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
            # :
            elif lexeme[i] == ":":
                i += 1

                # <skip-start>
                if lexeme[i] in first_set["<skip-start>"]:
                    # <insert-index>
                    if lexeme[i] in first_set["<insert-index>"]:
                        i, results = insert_index(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                    # <close-end>
                    if lexeme[i] in first_set["<close-end>"]:
                        # ]
                        if lexeme[i] == "]":
                            i += 1

                            # <2D-start-end-step>
                            i, results = D2_start_end_step(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                        # :
                        elif lexeme[i] == ":":
                            i += 1
                            # tint literal
                            if token[i] != "tint literal":
                                output.insert(
                                    "end", err + "tint literal not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]

                            # ]
                            if lexeme[i] != "]":
                                output.insert(
                                    "end", err + "] not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1

                            # <2D-start-end-step>
                            i, results = D2_start_end_step(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results
                        else:
                            output.insert(
                                "end", err + "] not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                    else:
                        output.insert(
                            "end", err + "skip-start not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                # :
                elif lexeme[i] == ":":
                    i += 1
                    # tint literal
                    if token[i] != "tint literal":
                        output.insert(
                            "end", err + "tint literal not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # ]
                    if lexeme[i] != "]":
                        output.insert(
                            "end", err + "] not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                    # <2D-start-end-step>
                    i, results = D2_start_end_step(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results
                else:
                    output.insert(
                        "end", err + "skip-start not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
            else:
                output.insert(
                    "end", err + "insert-start not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
    return i, results


def indexing(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "
    while True:
        if lexeme[i] not in first_set["<indexing>"]:
            break

        # [
        if lexeme[i] != "[":
            output.insert(
                "end", err + "[ not found\n")
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
        if lexeme[i] != "]":
            output.insert("end", err + "] not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
    return i, results


def string_value(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<string-value>"] or token[i] in first_set["<string-value>"]:
        print("string-value found")
        # "chard literal"
        if token[i] == "chard literal":
            i += 1
        # "string literal"
        elif token[i] == "string literal":
            i += 1
        # "bloom literal"
        elif token[i] == "bloom literal":
            i += 1
        # identifier
        elif lexeme[i] == "#":
            i += 2
            i, results = insert_func(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

            # <start-end-step>
            i, results = start_end_step(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

            # <indexing>
            i, results = indexing(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results
        else:
            output.insert(
                "end", err + "string-value not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
    return i, results


def common_data(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "
    if lexeme[i] in first_set["<common-data>"]:
        # <insert-flora-tint>
        if lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]:
            i, results = insert_flora_tint(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results
        # <string-value>
        elif lexeme[i] in first_set["<string-value>"]:
            i, results = string_value(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

            # <concatenate>
            while True:
                if lexeme[i] not in first_set["<concatenate>"]:
                    break

                # +
                if lexeme[i] != "+":
                    output.insert(
                        "end", err + "+ not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # <string-value>
                i, results = string_value(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results
        # <all-types>
        elif lexeme[i] in first_set["<all-types>"]:
            i += 1

            # (
            if lexeme[i] != "(":
                output.insert(
                    "end", err + "( not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

            # <all-type-value>
            i, results = all_type_value(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

            # )
            if lexeme[i] != ")":
                output.insert("end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
        # bare
        elif lexeme[i] == "bare":
            i += 1
        else:
            output.insert("end", err + "common-data not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]

        # <add-florist>
        while True:
            if lexeme[i] not in first_set["<add-florist>"]:
                break

            # indexing
            i, results = indexing(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

            # +
            if lexeme[i] != "+":
                output.insert("end", err + "+ not found\n")
                break
            i += 1

            # <all-type-value>
            i, results = all_type_value(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results
    return i, results


def all_type_value(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<all-type-value>"] or token[i] in first_set["<all-type-value>"]:
        # <common-data>
        if lexeme[i] in first_set["<common-data>"]:
            i, results = common_data(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results
        # <open-bracket>
        elif lexeme[i] in first_set["<open-bracket>"]:
            i += 1

            # <dirt>
            if lexeme[i] in first_set["<dirt>"]:
                # string literal
                if token[i] == "string literal":
                    i += 1
                # :
                if lexeme[i] != ":":
                    output.insert("end", err + ": not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

            # <sequence>
            if lexeme[i] in first_set["<sequence>"]:
                while True:
                    if lexeme[i] in first_set["<common-data>"]:
                        while True:
                            # <common-data>
                            if lexeme[i] not in first_set["<common-data>"]:
                                break

                            i, results = common_data(lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                            # ,
                            if lexeme[i] != ",":
                                break
                    # <open-bracket>
                    elif lexeme[i] in first_set["<open-bracket>"]:
                        i += 1
                        # <dirt>
                        if lexeme[i] in first_set["<dirt>"]:
                            # string literal
                            if token[i] == "string literal":
                                i += 1
                            # :
                            if lexeme[i] != ":":
                                output.insert("end", err + ": not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1

                        # <2D-sqnc>
                        if lexeme[i] in first_set["<2D-sqnc>"]:
                            while True:
                                if lexeme[i] in first_set["<common-data>"]:
                                    # <common-data>
                                    if lexeme[i] not in first_set["<common-data>"]:
                                        break

                                    i, results = common_data(
                                        lexeme, token, i, output)
                                    if "SYNTAX ERROR" in results:
                                        return i, results
                                # <open-bracket>
                                elif lexeme[i] in first_set["<open-bracket>"]:
                                    i += 1
                                    # <dirt>
                                    if lexeme[i] in first_set["<dirt>"]:
                                        # string literal
                                        if token[i] == "string literal":
                                            i += 1
                                        # :
                                        if lexeme[i] != ":":
                                            output.insert(
                                                "end", err + ": not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                        i += 1

                                        # <common-data>
                                        i, results = common_data(
                                            lexeme, token, i, output)
                                        if "SYNTAX ERROR" in results:
                                            return i, results

                                        # <next-3D-sqnc>
                                        if lexeme[i] in first_set["<next-3D-sqnc>"]:
                                            while True:
                                                if lexeme[i] not in first_set["<next-3D-sqnc>"]:
                                                    break

                                                # <common-data>
                                                i, results = common_data(
                                                    lexeme, token, i, output)
                                                if "SYNTAX ERROR" in results:
                                                    return i, results

                                                # ,
                                                if lexeme[i] != ",":
                                                    output.insert(
                                                        "end", err + ", not found\n")
                                                    return i, [(lexeme[i], "SYNTAX ERROR")]
                                                i += 1
                                        # <close-bracket>
                                        if lexeme[i] not in first_set["<close-bracket>"]:
                                            output.insert(
                                                "end", err + "close-bracket not found\n")
                                            return i, [(lexeme[i], "SYNTAX ERROR")]
                                        i += 1
                                # ,
                                if lexeme[i] != ",":
                                    break
                        # <close-bracket>
                        if lexeme[i] not in first_set["<close-bracket>"]:
                            output.insert(
                                "end", err + "close-bracket not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1
                    # ,
                    if lexeme[i] != ",":
                        break

                # <supply-dirt>
                if lexeme[i] in first_set["<supply-dirt>"]:
                    # getItems
                    if lexeme[i] == "getItems" or lexeme == "getKeys" or lexeme[i] == "getValues":
                        flag = True if lexeme[i] == "getValues" else False

                        # (
                        if lexeme[i] != "(":
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                        # identifier
                        if lexeme[i] != "#":
                            output.insert(
                                "end", err + "identifier not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 2

                        # <insert-func>
                        i, result = insert_func(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        if flag:
                            # indexing
                            i, results = indexing(lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                        # )
                        if lexeme[i] != ")":
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                    else:
                        output.insert(
                            "end", err + "getItems/getKeys/getValues not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                # inpetal
                if lexeme[i] == "inpetal":
                    i += 1

                    # (
                    if lexeme[i] != "(":
                        output.insert("end", err + "( not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                    # string literal
                    if token[i] != "string literal":
                        output.insert(
                            "end", err + "string literal not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                    # )
                    if lexeme[i] != ")":
                        output.insert("end", err + ") not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1
            # <close-bracket>
            if lexeme[i] not in first_set["<close-bracket>"]:
                output.insert("end", err + "close-bracket not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 1

        else:
            output.insert(
                "end", err + "open-bracket not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]

    return i, results


def insert_func(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "
    if lexeme[i] in first_set["<insert-func>"]:
        # (
        if lexeme[i] != "(":
            output.insert(
                "end", err + "( not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # <argument>
        if lexeme[i] in first_set["<argument>"]:
            # <insert-argument>
            if lexeme[i] in first_set["<insert-argument>"]:
                while True:
                    if lexeme[i] in first_set["<all-types>"]:
                        while True:
                            # <all-types>
                            if lexeme[i] not in first_set["<all-types>"]:
                                output.insert(
                                    "end", err + "all-types not found\n")
                                return i, [(lexeme[i], "SYNTAX ERROR")]
                            i += 1

                            # ,
                            if lexeme[i] != ",":
                                break
                            i += 1
                    elif lexeme[i] == "#":
                        i += 2
                        # (
                        if lexeme[i] != "(":
                            output.insert(
                                "end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # <2D-argument>
                        if lexeme[i] in first_set["<2D-argument>"]:
                            while True:
                                if lexeme[i] not in first_set["<2D-argument>"]:
                                    break
                                i += 1

                                # <all-type-value>
                                i, results = all_type_value(
                                    lexeme, token, i, output)
                                if "SYNTAX ERROR" in results:
                                    return i, results

                                # ,
                                if lexeme[i] != ",":
                                    break
                                i += 1
                    # ,
                    if lexeme[i] != ",":
                        break
            # <commond-data>
            elif lexeme[i] in first_set["<common-data>"]:
                i, results = common_data(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # identifier
                if lexeme[i] != "#":
                    output.insert(
                        "end", err + "identifier not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 2
        # )
        if lexeme[i] != ")":
            output.insert(
                "end", err + ") not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # <instance-grab>
        if lexeme[i] in first_set["<instance-grab>"]:
            # identifier
            if lexeme[i] != "#":
                output.insert(
                    "end", err + "identifier not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 2

            # (
            if lexeme[i] != "(":
                output.insert(
                    "end", err + "( not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 1

            # )
            if lexeme[i] != ")":
                output.insert(
                    "end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 1

            # identifier
            if lexeme[i] != "#":
                output.insert(
                    "end", err + "identifier not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 2

    return i, results


def insert_operation(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<insert-operation>"]:
        flag = False
        # (
        if lexeme[i] == "(":
            i += 1
            flag = True

        # <insert-flora-tint>
        if lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]:
            i, results = insert_flora_tint(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

            # <operate-flora-tint>
            i, results = operate_flora_tint(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

        if flag:
            # )
            if lexeme[i] != ")":
                output.insert("end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 1

            # <operate-flora-tint>
            i, results = operate_flora_tint(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

    return i, results


def operate_flora_tint(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<operate-flora-tint>"]:
        # <operator>
        if lexeme[i] in first_set["<operator>"]:
            i += 1

            # <insert-operation>
            i, results = insert_operation(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

    return i, results


def insert_flora_tint(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<insert-flora-tint>"] or token[i] in first_set["<insert-flora-tint>"]:

        # tint literal
        if token[i] == "tint literal":
            i += 1
        elif token[i] == "flora literal":
            i += 1
        elif lexeme[i] == "#":
            i += 2
            # <insert-func>
            i, results = insert_func(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, i, results

            # indexing
            i, results = indexing(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, i, results
        # lent
        elif lexeme[i] == "lent":
            i += 1

            # (
            if lexeme[i] != "(":
                output.insert("end", err + "( not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 1

            # <all-type-value>
            i, results = all_type_value(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, i, results

            # )
            if lexeme[i] != ")":
                output.insert("end", err + ") not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 1
    else:
        output.insert("end", err + "insert-flora-tint not found\n")
        return i, [(lexeme[i], "SYNTAX ERROR")]

    # <operate-flora-tint>
    if lexeme[i] in first_set["<operate-flora-tint>"]:
        i, results = operate_flora_tint(lexeme, token, i, output)
        if "SYNTAX ERROR" in results:
            return i, i, results

        # <insert-operation>
        i, results = insert_operation(lexeme, token, i, output)
        if "SYNTAX ERROR" in results:
            return i, i, results

    return i, results


def insert_variable(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "
    print("inside insert-variable")
    print("lexeme[i]: ", lexeme[i])

    # <all-assignment>
    if lexeme[i] in first_set["<all-assignment>"]:
        print("inside all-assignment")
        i += 1

        # <flora-tint-value>
        if lexeme[i] in first_set["<flora-tint-value>"] or token[i] in first_set["<flora-tint-value>"]:
            print("inside flora-tint-value")

            while True:
                if lexeme[i] not in first_set["<insert-flora-tint>"] and token[i] not in first_set["<insert-flora-tint>"]:
                    break
                print("inside while insert-flora-tint")

                i, results = insert_flora_tint(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                print("results: ", results)

                # ,
                if lexeme[i] != ",":
                    break
                i += 1

                print("more insert-flora-tint")

    # <string-assignment>
    elif lexeme[i] in first_set["<string-assignment>"]:
        i += 1

        # <all-type-value>
        i, results = all_type_value(lexeme, token, i, output)
        if "SYNTAX ERROR" in results:
            return i, results

    return i, results


def insert_condition(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    # <insert-condition>
    if lexeme[i] in first_set["<insert-condition>"]:
        i += 1
        # <all-cond-operator>
        if lexeme[i] in first_set["<all-cond-operator>"]:
            # <flora-tint-value>
            if lexeme[i] in first_set["<flora-tint-value>"] or token[i] in first_set["<flora-tint-value>"]:
                while True:
                    if lexeme[i] not in first_set["<flora-tint-value>"] and token[i] not in first_set["<flora-tint-value>"]:
                        break

                    i, results = insert_flora_tint(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results
            # <common-type>
            elif lexeme[i] in first_set["<common-type>"]:
                while True:
                    if lexeme[i] not in first_set["<common-type>"]:
                        break
                    i += 1

                    # ,
                    if lexeme[i] != ",":
                        break
        # <string-cond-op>
        if lexeme[i] in first_set["<string-cond-op>"]:
            i += 1

            # <string-operand>
            if lexeme[i] in first_set["<string-operand>"]:
                # <all-type-value>
                if lexeme[i] in first_set["<all-type-value>"]:
                    while True:
                        if lexeme[i] not in first_set["<all-type-value>"]:
                            break

                        i, results = all_type_value(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # ,
                        if lexeme[i] != ",":
                            break
                # <all-types>
                if lexeme[i] in first_set["<all-types>"]:
                    while True:
                        # <all-types>
                        if lexeme[i] not in first_set["<all-types>"]:
                            output.insert(
                                "end", err + "all-types not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # ,
                        if lexeme[i] != ",":
                            break
                        i += 1
            else:
                output.insert("end", err + "string-operand not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
        else:
            output.insert("end", err + "string-cond-op not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
    else:
        output.insert("end", err + "insert-condition not found\n")
        return i, [(lexeme[i], "SYNTAX ERROR")]

    return i, results


def more_condition(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<more-condition>"]:
        # eleaf
        if lexeme[i] != "eleaf":
            output.insert("end", err + "eleaf not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # (
        if lexeme[i] != "(":
            output.insert("end", err + "( not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # <all_type_value>
        if lexeme[i] in first_set["<all-type-value>"]:
            while True:
                if lexeme[i] not in first_set["<all-type-value>"]:
                    break

                # <all-type-value>
                i, results = all_type_value(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # ,
                if lexeme[i] != ",":
                    break

        # <insert-condition>
        i, results = insert_condition(lexeme, token, i, output)
        if "SYNTAX ERROR" in results:
            return i, results

        # )
        if lexeme[i] != ")":
            output.insert("end", err + ") not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # (
        if lexeme[i] != "(":
            output.insert("end", err + "( not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]
        i += 1

        # statement
        i, results = statement(lexeme, token, i, output)
        if "SYNTAX ERROR" in results:
            return i, results

        # )
        if lexeme[i] != ")":
            output.insert("end", err + ") not found\n")
            return i, [(lexeme[i], "SYNTAX ERROR")]

        i, results = more_condition(lexeme, token, i, output)

    return i, results


def statement(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<statement>"]:
        while True:
            # <constant>
            if lexeme[i] == "hard" or lexeme[i] in first_set["<all-types>"]:
                if lexeme[i] == "hard":
                    print("hard found")
                    i += 1

                # <all-types>
                if lexeme[i] not in first_set["<all-types>"]:
                    output.insert("end", err + "all-types not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("all-types found")

                print("lexeme[i]: ", lexeme[i])
                # identifier
                if lexeme[i] == "#":
                    i += 2
                    print("identifier found")
                    print("lexeme[i]: ", lexeme[i])
                else:
                    output.insert("end", err + "identifier not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <insert-variable>
                i, results = insert_variable(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results
                print("insert-variable found")

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                print("; found")

                continue

            # <i/o-statement>
            elif lexeme[i] in first_set["<i/o-statement>"]:
                # mint
                if lexeme[i] == "mint":
                    i += 1

                    # (
                    if lexeme[i] != "(":
                        output.insert("end", err + "( not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                    # <all-type-value>
                    i, results = all_type_value(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results

                    # )
                    if lexeme[i] != ")":
                        output.insert("end", err + ") not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                # <insert-inpetal>
                elif lexeme[i] in first_set["<insert-inpetal>"]:
                    # <all-types>
                    if lexeme[i] in first_set["<all-types>"]:
                        i += 1

                        # identifier
                        if lexeme[i] == "#":
                            i += 2

                            # <insert-func>
                            i, results = insert_func(lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results
                    else:
                        output.insert(
                            "end", err + "insert-inpetal not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]

                    # inpetal
                    if lexeme[i] == "inpetal":
                        i += 1

                        # (
                        if lexeme[i] != "(":
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # string literal
                        if token[i] != "string literal":
                            output.insert(
                                "end", err + "string literal not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # )
                        if lexeme[i] != ")":
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1
                else:
                    output.insert("end", err + "i/o-statement not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                continue

            # identifier
            elif lexeme[i] == "#":
                i += 2

                # <insert-func>
                i, results = insert_func(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # <more-id>
                while True:
                    if lexeme[i] not in first_set["<more-id>"]:
                        break

                    # ,
                    if lexeme[i] != ",":
                        break
                    i += 1

                    # identifier
                    if lexeme[i] != "#":
                        output.insert("end", err + "identifier not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 2

                    # <insert-func>
                    i, results = insert_func(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results

                    # indexing
                    i, results = indexing(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results

                # <insert-assignment>
                if lexeme[i] in first_set["<insert-assignment>"]:
                    i += 1

                    if lexeme[i] in first_set["<all-type-value>"]:
                        while True:
                            if lexeme[i] not in first_set["<all-type-value>"]:
                                break

                            # <all-type-value>
                            i, results = all_type_value(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                            # ,
                            if lexeme[i] != ",":
                                break
                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                continue

            # leaf
            elif lexeme[i] == "leaf":
                i += 1

                # (
                if lexeme[i] != "(":
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # <all_type_value>
                if lexeme[i] in first_set["<all-type-value>"]:
                    while True:
                        if lexeme[i] not in first_set["<all-type-value>"]:
                            break

                        # <all-type-value>
                        i, results = all_type_value(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # ,
                        if lexeme[i] != ",":
                            break
                else:
                    output.insert("end", err + "all-type-value not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]

                # <insert-condition>
                i, results = insert_condition(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # )
                if lexeme[i] != ")":
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # (
                if lexeme[i] != "(":
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # <statement>
                i, results = statement(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # )
                if lexeme[i] != ")":
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # <more-condition>
                i, results = more_condition(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # <else>
                if lexeme[i] in first_set["<else>"]:
                    # moss
                    if lexeme[i] == "moss":
                        i += 1

                        # (
                        if lexeme[i] != "(":
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # <statement>
                        i, results = statement(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # )
                        if lexeme[i] != ")":
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1
                    else:
                        output.insert("end", err + "moss not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                continue
            # <iterative>
            elif lexeme[i] in first_set["<iterative>"]:
                # fern
                if lexeme[i] == "fern":
                    i += 1

                    # (
                    if lexeme[i] != "(":
                        output.insert("end", err + "( not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                    # identifier
                    if lexeme[i] == "#":
                        i += 2

                        # =
                        if lexeme[i] != "=":
                            output.insert("end", err + "= not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # <insert-flora-tint>
                        i, results = insert_flora_tint(
                            lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # <all_type_value>
                        if lexeme[i] in first_set["<all-type-value>"]:
                            while True:
                                if lexeme[i] not in first_set["<all-type-value>"]:
                                    break

                                # <all-type-value>
                                i, results = all_type_value(
                                    lexeme, token, i, output)
                                if "SYNTAX ERROR" in results:
                                    return i, results

                                # ,
                                if lexeme[i] != ",":
                                    break

                        # insert-condition
                        i, results = insert_condition(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # ;
                        if lexeme[i] != ";":
                            output.insert("end", err + "; not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # identifier
                        if lexeme[i] != "#":
                            output.insert(
                                "end", err + "identifier not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 2

                        # <all-assignment>
                        if lexeme[i] not in first_set["<all-assignment>"]:
                            output.insert(
                                "end", err + "all-assignment not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # <insert-flora-tint>
                        i, results = insert_flora_tint(
                            lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # ;
                        if lexeme[i] != ";":
                            output.insert("end", err + "; not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # )
                        if lexeme[i] != ")":
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        # (
                        if lexeme[i] != "(":
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # statement
                        i, results = statement(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # )
                        if lexeme[i] != ")":
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                    # <common-data>
                    elif lexeme[i] in first_set["<common-data>"]:
                        while True:
                            i, results = common_data(lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                            # ,
                            if lexeme[i] != ",":
                                break

                        # at
                        if lexeme[i] != "at":
                            output.insert("end", err + "at not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # <all-type-value>
                        i, results = all_type_value(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # )
                        if lexeme[i] != ")":
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        # (
                        if lexeme[i] != "(":
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # statement
                        i, results = statement(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # )
                        if lexeme[i] != ")":
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]

                # willow
                if lexeme[i] == "willow":
                    i += 1

                    # (
                    if lexeme[i] != "(":
                        output.insert("end", err + "( not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                    # <all_type_value>
                    if lexeme[i] in first_set["<all-type-value>"]:
                        while True:
                            if lexeme[i] not in first_set["<all-type-value>"]:
                                break

                            # <all-type-value>
                            i, results = all_type_value(
                                lexeme, token, i, output)
                            if "SYNTAX ERROR" in results:
                                return i, results

                            # ,
                            if lexeme[i] != ",":
                                break

                    # <insert-condition>
                    i, results = insert_condition(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results

                    # )
                    if lexeme[i] != ")":
                        output.insert("end", err + ") not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    # (
                    if lexeme[i] != "(":
                        output.insert("end", err + "( not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 1

                    # statement
                    i, results = statement(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results

                    # )
                    if lexeme[i] != ")":
                        output.insert("end", err + ") not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                continue

            # tree
            elif lexeme[i] == "tree":
                i += 1

                # (
                if lexeme[i] != "(":
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # identifier
                if lexeme[i] != "#":
                    output.insert("end", err + "identifier not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 2

                # )
                if lexeme[i] != ")":
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # (
                if lexeme[i] != "(":
                    output.insert("end", err + "( not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # all-type-value
                i, results = all_type_value(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # <insert-branch>
                if lexeme[i] in first_set["<insert-branch>"]:
                    # :
                    if lexeme[i] == ":":
                        i += 1

                        # <statement>
                        i, results = statement(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                    # leaf
                    elif lexeme[i] == "leaf":

                        # <all_type_value>
                        if lexeme[i] in first_set["<all-type-value>"]:
                            while True:
                                if lexeme[i] not in first_set["<all-type-value>"]:
                                    break

                                # <all-type-value>
                                i, results = all_type_value(
                                    lexeme, token, i, output)
                                if "SYNTAX ERROR" in results:
                                    return i, results

                                # ,
                                if lexeme[i] != ",":
                                    break

                        # <insert-condition>
                        i, results = insert_condition(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # (
                        if lexeme[i] != "(":
                            output.insert("end", err + "( not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                        i += 1

                        # statement
                        i, results = statement(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                        # )
                        if lexeme[i] != ")":
                            output.insert("end", err + ") not found\n")
                            return i, [(lexeme[i], "SYNTAX ERROR")]
                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # <more-branch>
                if lexeme[i] in first_set["<more-branch>"]:
                    # branch
                    while True:
                        if lexeme[i] != "branch":
                            break
                        i += 1

                        # <all-type-value>
                        i, results = all_type_value(lexeme, token, i, output)
                        if "SYNTAX ERROR" in results:
                            return i, results

                # )
                if lexeme[i] != ")":
                    output.insert("end", err + ") not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                continue

            # clear
            elif lexeme[i] == "clear":
                i += 1

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                continue

            # break
            elif lexeme[i] == "break":
                i += 1

                # ;
                if lexeme[i] != ";":
                    output.insert("end", err + "; not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1
                continue

            # ,
            if lexeme[i] != ",":
                break
            else:
                output.insert("end", err + "insert-all-operand not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]

    return i, results


def next_D3_parameter(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<next-D3-parameter>"]:
        # <all-types>
        if lexeme[i] in first_set["<all-types>"]:
            while True:
                if lexeme[i] not in first_set["<all-types>"]:
                    break
                i += 1

                # <all-types>
                if lexeme[i] not in first_set["<all-types>"]:
                    output.insert("end", err + "all-types not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 1

                # identifier
                if lexeme[i] != "#":
                    output.insert(
                        "end", err + "identifier not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 2

                # insert_variable
                i, results = insert_variable(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # ,
                if lexeme[i] == ",":
                    i, results = next_D3_parameter(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results
    return i, results


def D2_parameter(lexeme, token, i, output):
    results = []
    err = "E: Syntax Analyzer: "

    if lexeme[i] in first_set["<D2-parameter>"]:
        # <keyword-param>
        if lexeme[i] in first_set["<keyword-param>"]:
            while True:
                if lexeme[i] not in first_set["<keyword-param>"]:
                    break
                if lexeme[i] in first_set["<common-type>"]:
                    i += 1

                    # identifier
                    if lexeme[i] != "*#":
                        output.insert(
                            "end", err + "identifier not found\n")
                        return i, [(lexeme[i], "SYNTAX ERROR")]
                    i += 3
                # identifier
                elif lexeme[i] != "**#":
                    output.insert(
                        "end", err + "identifier not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 4

        # <all-types>
        elif lexeme[i] in first_set["<all-types>"]:

            while True:
                if lexeme[i] not in first_set["<all-types>"]:
                    break
                i += 1

                # identifier
                if lexeme[i] != "#":
                    output.insert(
                        "end", err + "identifier not found\n")
                    return i, [(lexeme[i], "SYNTAX ERROR")]
                i += 2

                # insert_variable
                i, results = insert_variable(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results

                # ,
                if lexeme[i] == ",":
                    i, results = D2_parameter(lexeme, token, i, output)
                    if "SYNTAX ERROR" in results:
                        return i, results
        # identifier
        elif lexeme[i] == "#":
            i += 2

            # (
            if lexeme[i] != "(":
                output.insert("end", err + "( not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 1

            # <all-types>
            if lexeme[i] not in first_set["<all-types>"]:
                output.insert("end", err + "all-types not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 1

            # identifier
            if lexeme[i] != "#":
                output.insert("end", err + "identifier not found\n")
                return i, [(lexeme[i], "SYNTAX ERROR")]
            i += 2

            # insert_variable
            i, results = insert_variable(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

            i, results = next_D3_parameter(lexeme, token, i, output)
            if "SYNTAX ERROR" in results:
                return i, results

            # ,
            if lexeme[i] == ",":
                i, results = D2_parameter(lexeme, token, i, output)
                if "SYNTAX ERROR" in results:
                    return i, results
    return i, results
