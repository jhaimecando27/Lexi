from grammar import first_set

errors = []
ERR = "E: Syntax Analyzer: "

def D3_start_end_step(lexeme, token, i):
    if lexeme[i] in first_set["<3D-start-end-step>"]:
        # [
        if lexeme[i] != "[":
            return i
        print("162: [")
        i += 1

        # <3D-insert-start>
        if lexeme[i] not in first_set["<3D-insert-start>"]:
            errors.append(ERR + "<3D-insert-start> not found")
            return i
        print("162: <3D-insert-start>")

        # tint literal
        if token[i] == "tint literal":
            print("164: tint literal")
            i += 1

            # :
            if lexeme[i] != ":":
                errors.append(ERR + ": not found")
                return i
            print("164: :")
            i += 1

            # <3D-close-start>
            if lexeme[i] in first_set["<3D-close-start>"]:
                # tint literal
                if token[i] == "tint literal":
                    print("167: tint literal")
                    i += 1

                # <3D-close-end>
                if lexeme[i] in first_set["<3D-close-end>"]:
                    print("166/167: <3D-close-end>")
                    # :
                    if lexeme[i] == ":":
                        print("169: :")
                        i += 1

                        # tint literal
                        if token[i] == "tint literal":
                            print("169: tint literal")
                            i += 1

                    # ]
                    if lexeme[i] == "]":
                        print("168/169: ]")
                        i += 1
                    else:
                        errors.append(ERR + "] not found")
                        return i
        # :
        elif lexeme[i] == ":":
            print("165: :")
            i += 1

            # tint literal
            if token[i] == "tint literal":
                print("170: tint literal")
                i += 1

                # <3D-close-end>
                if lexeme[i] in first_set["<3D-close-end>"]:
                    print("170: <3D-close-end>")
                    # :
                    if lexeme[i] == ":":
                        print("169: :")
                        i += 1

                        # tint literal
                        if token[i] == "tint literal":
                            print("169: tint literal")
                            i += 1

                    # ]
                    if lexeme[i] == "]":
                        print("168/169: ]")
                        i += 1
                    else:
                        errors.append(ERR + "] not found")
                        return i
            # :
            elif lexeme[i] == ":":
                print("171: :")
                i += 1

                # tint literal
                if token[i] == "tint literal":
                    print("171: tint literal")
                    i += 1
                else:
                    errors.append(ERR + "tint literal not found")
                    return i

                # ]
                if lexeme[i] == "]":
                    print("171: ]")
                    i += 1
                else:
                    errors.append(ERR + "] not found")
                    return i

            else:
                errors.append(ERR + "tint literal or : not found")
                return i
        else:
            errors.append(ERR + "tint literal or : not found")
    else:
        print("153: EPSILON")

    return i


def D2_start_end_step(lexeme, token, i):
    if lexeme[i] in first_set["<2D-start-end-step>"]:
        # [
        if lexeme[i] != "[":
            return i
        print("152: [")
        i += 1

        # <2D-insert-start>
        if lexeme[i] not in first_set["<2D-insert-start>"]:
            errors.append(ERR + "<2D-insert-start> not found")
            return i
        print("152: <2D-insert-start>")

        # tint literal
        if token[i] == "tint literal":
            print("154: tint literal")
            i += 1

            # :
            if lexeme[i] != ":":
                errors.append(ERR + ": not found")
                return i
            print("154: :")
            i += 1

            # <2D-close-start>
            if lexeme[i] in first_set["<2D-close-start>"]:
                # tint literal
                if token[i] == "tint literal":
                    print("157: tint literal")
                    i += 1

                # <2D-close-end>
                if lexeme[i] in first_set["<2D-close-end>"]:
                    print("156/157: <2D-close-end>")
                    # :
                    if lexeme[i] == ":":
                        print("159: :")
                        i += 1

                        # tint literal
                        if token[i] == "tint literal":
                            print("159: tint literal")
                            i += 1

                    # ]
                    if lexeme[i] == "]":
                        print("158/159: ]")
                        i += 1
                    else:
                        errors.append(ERR + "] not found")
                        return i

                    # D2_start_end_step
                    i = D3_start_end_step(lexeme, token, i)
        # :
        elif lexeme[i] == ":":
            print("155: :")
            i += 1

            # tint literal
            if token[i] == "tint literal":
                print("160: tint literal")
                i += 1

                # <2D-close-end>
                if lexeme[i] in first_set["<2D-close-end>"]:
                    print("160: <2D-close-end>")
                    # :
                    if lexeme[i] == ":":
                        print("159: :")
                        i += 1

                        # tint literal
                        if token[i] == "tint literal":
                            print("159: tint literal")
                            i += 1

                    # ]
                    if lexeme[i] == "]":
                        print("158/159: ]")
                        i += 1
                    else:
                        errors.append(ERR + "] not found")
                        return i

                    # D2_start_end_step
                    print("158/159: 3D start end step")
                    i = D3_start_end_step(lexeme, token, i)
            # :
            elif lexeme[i] == ":":
                print("161: :")
                i += 1

                # tint literal
                if token[i] == "tint literal":
                    print("161: tint literal")
                    i += 1
                else:
                    errors.append(ERR + "tint literal not found")
                    return i

                # ]
                if lexeme[i] == "]":
                    print("161: ]")
                    i += 1
                else:
                    errors.append(ERR + "] not found")
                    return i

                # D3_start_end_step
                print("161: 3D start end step")
                i = D3_start_end_step(lexeme, token, i)
            else:
                errors.append(ERR + "tint literal or : not found")
                return i

        else:
            errors.append(ERR + "tint literal or : not found")
    else:
        print("153: EPSILON")

    return i


def start_end_step(lexeme, token, i):
    if lexeme[i] in first_set["<start-end-step>"]:
        # [
        if lexeme[i] != "[":
            return i
        print("142: [")
        i += 1

        # <insert-start>
        if lexeme[i] not in first_set["<insert-start>"]:
            errors.append(ERR + "<insert-start> not found")
            return i
        print("142: <insert-start>")

        # tint literal
        if token[i] == "tint literal":
            print("142: tint literal")
            i += 1

            # :
            if lexeme[i] != ":":
                errors.append(ERR + ": not found")
                return i
            print("144: :")
            i += 1

            # <close-start>
            if lexeme[i] in first_set["<close-start>"]:
                # tint literal
                if token[i] == "tint literal":
                    print("147: tint literal")
                    i += 1

                # <close-end>
                if lexeme[i] in first_set["<close-end>"]:
                    print("146/147: <close-end>")
                    # :
                    if lexeme[i] == ":":
                        print("149: :")
                        i += 1

                        # tint literal
                        if token[i] == "tint literal":
                            print("149: tint literal")
                            i += 1

                    # ]
                    if lexeme[i] == "]":
                        print("148/149: ]")
                        i += 1
                    else:
                        errors.append(ERR + "] not found")
                        return i

                    # D2_start_end_step
                    i = D2_start_end_step(lexeme, token, i)
        # :
        elif lexeme[i] == ":":
            print("145: :")
            i += 1

            # tint literal
            if token[i] == "tint literal":
                print("143: tint literal")
                i += 1

                # <close-end>
                if lexeme[i] in first_set["<close-end>"]:
                    print("146/147: <close-end>")
                    # :
                    if lexeme[i] == ":":
                        print("149: :")
                        i += 1

                        # tint literal
                        if token[i] == "tint literal":
                            print("149: tint literal")
                            i += 1

                    # ]
                    if lexeme[i] == "]":
                        print("148/149: ]")
                        i += 1
                    else:
                        errors.append(ERR + "] not found")
                        return i

                    # D2_start_end_step
                    print("148/149: 2D start end step")
                    i = D2_start_end_step(lexeme, token, i)
            # :
            elif lexeme[i] == ":":
                print("151: :")
                i += 1

                # tint literal
                if token[i] == "tint literal":
                    print("151: tint literal")
                    i += 1
                else:
                    errors.append(ERR + "tint literal not found")
                    return i

                # ]
                if lexeme[i] == "]":
                    print("151: ]")
                    i += 1
                else:
                    errors.append(ERR + "] not found")
                    return i

                # D2_start_end_step
                print("151: 2D start end step")
                i = D2_start_end_step(lexeme, token, i)
            else:
                errors.append(ERR + "tint literal or : not found")
                return i

        else:
            errors.append(ERR + "tint literal or : not found")

    return i


def tint_literals(lexeme, token, i):
    if (
        lexeme[i] in first_set["<tint-literals>"]
        or token[i] in first_set["<tint-literals>"]
    ):
        print("28: <tint-literals>")

        if token[i] == "tint literal":
            print("30: tint literal")
            i += 1

        elif lexeme[i] == "#":
            print("31: #identifier")
            i += 2

            i = insert_func(lexeme, token, i)

            i = indexing(lexeme, token, i)

        elif lexeme[i] == "lent":
            print("32: lent")
            i += 1

            # (
            if lexeme[i] == "(":
                print("32: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            # identifier
            if lexeme[i] == "#":
                print("32: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            # insert-func
            if lexeme[i] in first_set["<insert-func>"]:
                print("32: insert-func")
                i = insert_func(lexeme, token, i)

            # indexing
            if lexeme[i] in first_set["<indexing>"]:
                print("32: indexing")
                i = indexing(lexeme, token, i)

            # )
            if lexeme[i] == ")":
                print("32: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i

        elif lexeme[i] == "tint":
            print("33: tint")
            i += 1

            # (
            if lexeme[i] == "(":
                print("33: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            # #identifier
            if lexeme[i] == "#":
                print("33: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            # insert-func
            if lexeme[i] in first_set["<insert-func>"]:
                print("33: insert-func")
                i = insert_func(lexeme, token, i)

            # indexing
            if lexeme[i] in first_set["<indexing>"]:
                print("33: indexing")
                i = indexing(lexeme, token, i)

            # )
            if lexeme[i] == ")":
                print("33: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i
    return i


def flora_literals(lexeme, token, i):
    if (
        lexeme[i] in first_set["<flora-literals>"]
        or token[i] in first_set["<flora-literals>"]
    ):
        print("36: <flora-literals>")

        if token[i] == "flora literal":
            print("40: flora literal")
            i += 1

        elif lexeme[i] == "flora":
            print("41: flora")
            i += 1

            # (
            if lexeme[i] == "(":
                print("41: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            # #identifier
            if lexeme[i] == "#":
                print("41: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            # insert-func
            if lexeme[i] in first_set["<insert-func>"]:
                print("41: insert-func")
                i = insert_func(lexeme, token, i)

            # indexing
            if lexeme[i] in first_set["<indexing>"]:
                print("41: indexing")
                i = indexing(lexeme, token, i)

            # )
            if lexeme[i] == ")":
                print("41: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i
        # tint-literals
        elif (
            lexeme[i] in first_set["<tint-literals>"]
            or token[i] in first_set["<tint-literals>"]
        ):
            print("36: <tint-literals>")
            i = tint_literals(lexeme, token, i)
    else:
        errors.append(ERR + "36: <flora-literals> not found")
    return i


def arithmetic(lexeme, token, i):
    if (
        lexeme[i] in first_set["<arithmetic>"]
        or token[i] in first_set["<arithmetic>"]
    ):
        print("29: <arithmetic>")

        # <numerics>
        if lexeme[i] in first_set["<numerics>"]:
            print("35: <numerics>")

            # <tint-literals>
            if (
                lexeme[i] in first_set["<tint-literals>"]
                or token[i] in first_set["<tint-literals>"]
            ):
                i = tint_literals(lexeme, token, i)
            # <flora-literals>
            elif (
                lexeme[i] in first_set["<flora-literals>"]
                or token[i] in first_set["<flora-literals>"]
            ):
                print("36: <flora-literals>")
                i = flora_literals(lexeme, token, i)
            else:
                errors.append(ERR + "35: <numerics> not found")
                return i

            # <operate-number>
            if lexeme[i] in first_set["<operate-number>"]:
                print("38: <operate-number>")

                # <operator>
                if lexeme[i] in first_set["<operator>"]:
                    print("43: <operator>")
                    i += 1

                    # <arithmetic>
                    if lexeme[i] in first_set["<arithmetic>"]:
                        print("43: <arithmetic>")
                        i = arithmetic(lexeme, token, i)
                    else:
                        errors.append(ERR + "43: <arithmetic> not found")
                        return i
                else:
                    print("44: EPSILON")
        # (
        elif lexeme[i] == "(":
            print("39: (")
            i += 1

            # <numerics>
            if lexeme[i] in first_set["<numerics>"]:
                print("39: <numerics>")

                # <tint-literals>
                if (
                    lexeme[i] in first_set["<tint-literals>"]
                    or token[i] in first_set["<tint-literals>"]
                ):
                    i = tint_literals(lexeme, token, i)
                # <flora-literals>
                elif (
                    lexeme[i] in first_set["<flora-literals>"]
                    or token[i] in first_set["<flora-literals>"]
                ):
                    i = flora_literals(lexeme, token, i)
                else:
                    errors.append(ERR + "35: <numerics> not found")
                    return i

            # <operator>
            if lexeme[i] in first_set["<operator>"]:
                print("39: <operator>")
                i += 1
            else:
                errors.append(ERR + "<operator> not found")
                return i

            # <arithmetic>
            if lexeme[i] in first_set["<arithmetic>"]:
                print("39: <arithmetic>")
                i = arithmetic(lexeme, token, i)
            else:
                errors.append(ERR + "39: <arithmetic> not found")
                return i

            # )
            if lexeme[i] == ")":
                print("39: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i

            # <operate-number>
            if lexeme[i] in first_set["<operate-number>"]:
                print("39: <operate-number>")

                # <operator>
                if lexeme[i] in first_set["<operator>"]:
                    print("43: <operator>")
                    i += 1

                    # <arithmetic>
                    if lexeme[i] in first_set["<arithmetic>"]:
                        print("43: <arithmetic>")
                        i = arithmetic(lexeme, token, i)
                    else:
                        errors.append(ERR + "43: <arithmetic> not found")
                        return i
                else:
                    print("44: EPSILON")
        else:
            errors.append(ERR + "39: <numerics> not found")
            return i
    else:
        errors.append(ERR + "29: <arithmetic> not found")
    return i


def tint(lexeme, token, i):

    if lexeme[i] in first_set["<tint>"] or token[i] in first_set["<tint>"]:

        if (
            lexeme[i] in first_set["<tint-literals>"]
            or token[i] in first_set["<tint-literals>"]
        ):
            i = tint_literals(lexeme, token, i)

        elif (
            lexeme[i] in first_set["<arithmetic>"]
            or token[i] in first_set["<arithmetic>"]
        ):
            print("29: <arithmetic>")
            i = arithmetic(lexeme, token, i)

    else:
        errors.append(ERR + "26: <tint> not found")

    return i


def flora(lexeme, token, i):

    if lexeme[i] in first_set["<flora>"] or token[i] in first_set["<flora>"]:

        if (
            lexeme[i] in first_set["<flora-literals>"]
            or token[i] in first_set["<flora-literals>"]
        ):
            print("36: <flora-literals>")
            i = flora_literals(lexeme, token, i)

        elif (
            lexeme[i] in first_set["<arithmetic>"]
            or token[i] in first_set["<arithmetic>"]
        ):
            print("37: <arithmetic>")
            i = arithmetic(lexeme, token, i)

    else:
        errors.append(ERR + "27: <flora> not found")
    return i


def chard(lexeme, token, i):
    if lexeme[i] in first_set["<chard>"] or token[i] in first_set["<chard>"]:
        if token[i] == "chard literal":
            print("56: chard literal")
            i += 1

        # #identifier
        elif lexeme[i] == "#":
            print("57: #identifier")
            i += 2

            # insert-func
            if lexeme[i] in first_set["<insert-func>"]:
                print("57: insert-func")
                i = insert_func(lexeme, token, i)

            # indexing
            if lexeme[i] in first_set["<indexing>"]:
                print("57: indexing")
                i = indexing(lexeme, token, i)

        # chard
        elif lexeme[i] == "chard":
            print("58: chard")
            i += 1

            # (
            if lexeme[i] == "(":
                print("58: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            # #identifier
            if lexeme[i] == "#":
                print("58: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            # insert-func
            if lexeme[i] in first_set["<insert-func>"]:
                print("58: insert-func")
                i = insert_func(lexeme, token, i)

            # indexing
            if lexeme[i] in first_set["<indexing>"]:
                print("58: indexing")
                i = indexing(lexeme, token, i)

            # )
            if lexeme[i] == ")":
                print("58: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i

    else:
        errors.append(ERR + "<chard> not found")
    return i


def concatenate(lexeme, token, i):
    if lexeme[i] in first_set["<concatenate>"] or token[i] in first_set["<concatenate>"]:
        # indexing
        if lexeme[i] in first_set["<indexing>"]:
            print("59: indexing")
            i = indexing(lexeme, token, i)
        else:
            errors.append(ERR + "59: <indexing> not found")
            return i

        # +
        if lexeme[i] == "+":
            print("59: +")
            i += 1
        else:
            errors.append(ERR + "+ not found")
            return i

        # string
        i = string(lexeme, token, i)

        print("59: concatenate")
        concatenate(lexeme, token, i)

    return i


def string(lexeme, token, i):
    if lexeme[i] in first_set["<string>"] or token[i] in first_set["<string>"]:
        if token[i] == "string literal":
            print("61: string literal")
            i += 1

        # #identifier
        elif lexeme[i] == "#":
            print("62: #identifier")
            i += 2

            # insert-func
            if lexeme[i] in first_set["<insert-func>"]:
                print("62: insert-func")
                i = insert_func(lexeme, token, i)

            # indexing
            if lexeme[i] in first_set["<indexing>"]:
                print("62: indexing")
                i = indexing(lexeme, token, i)

            # <start-end-step>
            if lexeme[i] in first_set["<start-end-step>"]:
                print("62: start-end-step")
                i = start_end_step(lexeme, token, i)
        # string
        elif lexeme[i] == "string":
            print("63: string")
            i += 1

            # (
            if lexeme[i] == "(":
                print("63: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            # #identifier
            if lexeme[i] == "#":
                print("63: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            # insert-func
            if lexeme[i] in first_set["<insert-func>"]:
                print("63: insert-func")
                i = insert_func(lexeme, token, i)

            # indexing
            if lexeme[i] in first_set["<indexing>"]:
                print("63: indexing")
                i = indexing(lexeme, token, i)

            # <start-end-step>
            if lexeme[i] in first_set["<start-end-step>"]:
                print("63: start-end-step")
                i = start_end_step(lexeme, token, i)

            # )
            if lexeme[i] == ")":
                print("63: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i

    else:
        errors.append(ERR + "<string> not found")
    return i


def bloom_literals(lexeme, token, i):
    if (
        lexeme[i] in first_set["<bloom-literals>"]
        or token[i] in first_set["<bloom-literals>"]
    ):
        print("64: <bloom-literals>")

        if token[i] == "bloom literal":
            print("65: bloom literal")
            i += 1
        elif lexeme[i] == "bloom":
            print("66: bloom")
            i += 1

            # (
            if lexeme[i] == "(":
                print("66: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            # #identifier
            if lexeme[i] == "#":
                print("66: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            # insert-func
            if lexeme[i] in first_set["<insert-func>"]:
                print("66: insert-func")
                i = insert_func(lexeme, token, i)

            # indexing
            if lexeme[i] in first_set["<indexing>"]:
                print("66: indexing")
                i = indexing(lexeme, token, i)

            # )
            if lexeme[i] == ")":
                print("66: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i
        elif lexeme[i] in first_set["<tint>"]:
            print("72: tint")
            i = tint(lexeme, token, i)
        elif lexeme[i] in first_set["<flora>"]:
            print("73: flora")
            i = flora(lexeme, token, i)
        elif lexeme[i] in first_set["<chard>"]:
            print("74: chard")
            i = chard(lexeme, token, i)
        elif lexeme[i] in first_set["<string>"]:
            print("75: string")
            i = string(lexeme, token, i)
        elif lexeme[i] in first_set["<sqnc>"]:
            print("76: sqnc")
            i = sqnc(lexeme, token, i)
        elif lexeme[i] == "bare":
            print("77: bare")
            i += 1
        else:
            errors.append(ERR + "64: <bloom-literals> not found")
            return i

    return i


def bloom(lexeme, token, i):
    if lexeme[i] in first_set["<bloom>"] or token[i] in first_set["<bloom>"]:
        if token[i] == "bloom literal":
            print("65: bloom literal")
            i = bloom_literals(lexeme, token, i)

            # <operate-logic>
            if lexeme[i] in first_set["<operate-logic>"]:
                print("68: <operate-logic>")

                # <cond-operator>
                if lexeme[i] in first_set["<cond-operator>"]:
                    print("78: <cond-operator>")
                    i += 1

                    # <bloom>
                    if lexeme[i] in first_set["<bloom>"]:
                        print("79: <bloom>")
                        i = bloom(lexeme, token, i)
                    else:
                        errors.append(ERR + "79: <bloom> not found")
                        return i
                else:
                    print("79: EPSILON")
        elif lexeme[i] == "(":
            print("69: (")
            i += 1

            # bloom-literals
            if lexeme[i] in first_set["<bloom-literals>"]:
                print("69: <bloom-literals>")
                i = bloom_literals(lexeme, token, i)
            else:
                errors.append(ERR + "69: <bloom-literals> not found")
                return i

            # <cond-operator>
            if lexeme[i] in first_set["<cond-operator>"]:
                print("78: <cond-operator>")
                i += 1

                # <bloom>
                if lexeme[i] in first_set["<bloom>"]:
                    print("79: <bloom>")
                    i = bloom(lexeme, token, i)
                else:
                    errors.append(ERR + "79: <bloom> not found")
                    return i
            else:
                print("79: EPSILON")


            # <bloom>
            if lexeme[i] in first_set["<bloom>"]:
                print("80: <bloom>")
                i = bloom(lexeme, token, i)
            else:
                errors.append(ERR + "80: <bloom> not found")
                return i

            # )
            if lexeme[i] == ")":
                print("80: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i

            # <operate-logic>
            if lexeme[i] in first_set["<operate-logic>"]:
                print("69: <operate-logic>")

                # <cond-operator>
                if lexeme[i] in first_set["<cond-operator>"]:
                    print("78: <cond-operator>")
                    i += 1

                    # <bloom>
                    if lexeme[i] in first_set["<bloom>"]:
                        print("79: <bloom>")
                        i = bloom(lexeme, token, i)
                    else:
                        errors.append(ERR + "79: <bloom> not found")
                        return i
                else:
                    print("79: EPSILON")

    else:
        errors.append(ERR + "<bloom> not found")
    return i


def common_data(lexeme, token, i):
    if lexeme[i] in first_set["<common-data>"]:
        if lexeme[i] in first_set["<tint>"]:
            print("129: tint")
            i = tint(lexeme, token, i)
        elif lexeme[i] in first_set["<flora>"]:
            print("130: flora")
            i = flora(lexeme, token, i)
        elif lexeme[i] in first_set["<chard>"]:
            print("131: chard")
            i = chard(lexeme, token, i)
        elif lexeme[i] in first_set["<string>"]:
            print("132: string")
            i = string(lexeme, token, i)
        elif lexeme[i] in first_set["<bloom>"]:
            print("133: bloom")
            i = bloom(lexeme, token, i)
        else:
            errors.append(ERR + "129-133: <common-data> not found")
            return i


def dirt(lexeme, token, i):

    if lexeme[i] in first_set["<dirt>"]:
        print("114: <dirt>")

        if token[i] == "string literal":
            print("123: string literal")
            i += 1
        else:
            errors.append(ERR + "string literal not found")
            return i

        if lexeme[i] == ":":
            print("123: :")
            i += 1
        else:
            errors.append(ERR + ": not found")
            return i


def sequence(lexeme, token, i):

    while lexeme[i] in first_set["<sequence>"]:
        print("114: sequence")

        if lexeme[i] in first_set["<common-data>"]:
            i = common_data(lexeme, token, i)

            i = next_sqnc(lexeme, token, i)

        elif lexeme[i] in first_set["<open>"]:
            print("128: open")

            if lexeme[i] in first_set["<dirt>"]:
                i = dirt(lexeme, token, i)

            while lexeme[i] in first_set["<2D-sqnc>"]:

                if lexeme[i] in first_set["<common-data>"]:
                    i = common_data(lexeme, token, i)

                elif lexeme[i] in first_set["<open>"]:
                    print("137: open")
                    i += 1

                    i = dirt(lexeme, token, i)

                    if lexeme[i] in first_set["<common-data>"]:
                        i = common_data(lexeme, token, i)

                    while True:
                        # <next-3D-sqnc>
                        if lexeme[i] == ",":
                            print("140: ,")
                            i += 1
                        else:
                            print("141: EPSILON")
                            break

                        if lexeme[i] in first_set["<common-data>"]:
                            i = common_data(lexeme, token, i)

                    if lexeme[i] in first_set["<close>"]:
                        print("137: close")
                        i += 1
                    else:
                        errors.append(ERR + "close not found")
                        return i

                # <next-2D-sqnc>
                if lexeme[i] == ",":
                    print("138: ,")
                    i += 1
                else:
                    print("139: EPSILON")
                    break

        if lexeme[i] in first_set["<close>"]:
            print("128: close")
            i += 1
        else:
            errors.append(ERR + "close not found")
            return i

        # <next-sqnc>
        if lexeme[i] == ",":
            print("134: ,")
            i += 1
        else:
            print("135: EPSILON")
            return i



def indexing(lexeme, token, i):
    if lexeme[i] in first_set["<indexing>"]:
        # [
        if lexeme[i] == "[":
            print("94: [")
            i += 1
        else:
            errors.append(ERR + "[ not found")
            return i

        # <insert-index>
        if token[i] in first_set["<insert-index>"]:
            if token[i] == "tint literal":
                print("96: tint literal")
                i += 1
            elif token[i] == "string literal":
                print("97: string literal")
                i += 1
            else:
                errors.append(ERR + "tint or string literal not found")
                return i

        # ]
        if lexeme[i] == "]":
            print("94: ]")
            i += 1
        else:
            errors.append(ERR + "] not found")
            return i

        print("94: indexing")
        i = indexing(lexeme, token, i)

    return i

def sqnc(lexeme, token, i):
    if lexeme[i] in first_set["<sqnc>"]:
        print("173: sqnc")

        if lexeme[i] in first_set["<open>"]:
            print("114: <open>")
            i += 1

            if lexeme[i] in first_set["<dirt>"]:
                i = dirt(lexeme, token, i)

            if lexeme[i] in first_set["<sequence>"]:
                print("114: sequence")

                i = sequence(lexeme, token, i)

            if lexeme[i] in first_set["<close>"]:
                print("114: close")
                i += 1
            else:
                errors.append(ERR + "close not found")
                return i

        elif lexeme[i] in first_set["<supply-dirt>"]:

            if lexeme[i] == "getItems":
                print("118: getItems")
                i += 1
            elif lexeme[i] == "getKeys":
                print("119: getKeys")
                i += 1
            elif lexeme[i] == "getValues":
                print("120: getValues")
                i += 1
            else:
                errors.append(ERR + "supply-dirt not found")
                return i

            if lexeme[i] == "(":
                print("115: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            if lexeme[i] == "#":
                print("115: #identifer")
                i += 1
            else:
                errors.append(ERR + "#identifer not found")
                return i

            if lexeme[i] in first_set["<insert-func>"]:
                i = insert_func(lexeme, token, i)
    return i


def all_type_value(lexeme, token, i):
    if lexeme[i] in first_set["<all-type-value>"]:
        if lexeme[i] in first_set["<common-data>"]:
            print("172: common-data")
            i = common_data(lexeme, token, i)

        elif lexeme[i] in first_set["<sqnc>"]:
            print("173: sqnc")
            i = sqnc(lexeme, token, i)
        elif lexeme[i] == "inpetal":
            print("174: inpetal")
            i += 1

            # (
            if lexeme[i] == "(":
                print("174: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            # string literal
            if token[i] == "string literal":
                print("174: string literal")
                i += 1
            else:
                errors.append(ERR + "string literal not found")
                return i

            # )
            if lexeme[i] == ")":
                print("174: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i

    return i


def D3_argument(lexeme, token, i):
    if lexeme[i] in first_set["<3D-argument>"]:
        if lexeme[i] in first_set["<all-type-value>"]:
            print("286: <all-type-value>")
            i = all_type_value(lexeme, token, i)

            # <add-3D-argument>
            if lexeme[i] == ",":
                print("286: ,")
                i += 1

                # <argument>
                if lexeme[i] in first_set["<2D-argument>"]:
                    print("286: <2D-argument>")
                    i = D3_argument(lexeme, token, i)
    return i


def D2_argument(lexeme, token, i):
    if lexeme[i] in first_set["<2D-argument>"]:
        if lexeme[i] in first_set["<all-type-value>"]:
            print("286: <all-type-value>")
            i = all_type_value(lexeme, token, i)

            # <add-2D-argument>
            if lexeme[i] == ",":
                print("286: ,")
                i += 1

                # <argument>
                if lexeme[i] in first_set["<2D-argument>"]:
                    print("286: <2D-argument>")
                    i = D2_argument(lexeme, token, i)
        elif lexeme[i] == "#":
            print("287: #identifier")
            i += 2

            # (
            if lexeme[i] == "(":
                print("287: (")
                i += 1
            else:
                errors.append(ERR + "( not found")
                return i

            # <3D-argument>
            if lexeme[i] in first_set["<3D-argument>"]:
                print("287: <3D-argument>")
                i = D3_argument(lexeme, token, i)

            # )
            if lexeme[i] == ")":
                print("287: )")
                i += 1
            else:
                errors.append(ERR + ") not found")
                return i

            # <add-2D-argument>
            if lexeme[i] == ",":
                print("286: ,")
                i += 1

                # <argument>
                if lexeme[i] in first_set["<2D-argument>"]:
                    print("286: <2D-argument>")
                    i = D2_argument(lexeme, token, i)
    return i


def insert_kwargs(lexeme, token, i):
    if lexeme[i] in first_set["<insert-kwargs>"]:
        # tint value
        if lexeme[i] == "tint":
            print("16: tint")
            i += 1
            while True:
                if lexeme[i] == "#":
                    print("16: #identifier")
                    i += 2
                else:
                    errors.append(ERR + "#identifier not found")
                    return i

                if lexeme[i] == "=":
                    print("26: =")
                    i += 1

                    i = tint(lexeme, token, i)

                    # <more-tint>
                    if lexeme[i] == ",":
                        print("98: ,")
                        i += 1
                    else:
                        print("99: EPSILON")
                        break
                else:
                    print("26: EPSILON")
                    break
        # flora value
        elif lexeme[i] == "flora":
            print("17: flora")
            i += 1
            while True:
                if lexeme[i] == "#":
                    print("17: #identifier")
                    i += 2
                else:
                    errors.append(ERR + "#identifier not found")
                    return i

                if lexeme[i] == "=":
                    print("34: =")
                    i += 1

                    i = flora(lexeme, token, i)

                    # <more-flora>
                    if lexeme[i] == ",":
                        print("100: ,")
                        i += 1
                    else:
                        print("101: EPSILON")
                        break
                else:
                    print("35: EPSILON")
                    break
        # chard value
        elif lexeme[i] == "chard":
            print("18: chard")
            i += 1
            while True:
                if lexeme[i] == "#":
                    print("18: #identifier")
                    i += 2
                else:
                    errors.append(ERR + "#identifier not found")
                    return i

                if lexeme[i] == "=":
                    print("54: =")
                    i += 1

                    i = chard(lexeme, token, i)

                    # <more-chard>
                    if lexeme[i] == ",":
                        print("102: ,")
                        i += 1
                    else:
                        print("103: EPSILON")
                        break
                else:
                    print("37: EPSILON")
                    break

        # string value
        elif lexeme[i] == "string":
            print("19: string")
            i += 1

            while True:

                if lexeme[i] == "#":
                    print("19: #identifier")
                    i += 2
                else:
                    errors.append(ERR + "#identifier not found")
                    return i

                if lexeme[i] == "=":
                    print("59: =")
                    i += 1

                    print("59: string")
                    i = string(lexeme, token, i)

                    print("59: concatenate")
                    i = concatenate(lexeme, token, i)

                    if lexeme[i] == ",":
                        print("104: ,")
                        i += 1
                    else:
                        print("105: EPSILON")
                        break
                else:
                    print("60: EPSILON")
                    break

        # bloom value
        elif lexeme[i] == "bloom":
            print("20: bloom")
            i += 1

            while True:

                if lexeme[i] == "#":
                    print("20: #identifier")
                    i += 2
                else:
                    errors.append(ERR + "#identifier not found")
                    return i

                if lexeme[i] == "=":
                    print("64: =")
                    i += 1

                    i = bloom(lexeme, token, i)

                    if lexeme[i] == ",":
                        print("106: ,")
                        i += 1
                    else:
                        print("107: EPSILON")
                        break
                else:
                    print("65: EPSILON")
                    break
        elif lexeme[i] in first_set["<sqnc-type>"]:
            print("21: sqnc-type")
            i += 1

            while True:
                if lexeme[i] == "#":
                    print("21: #identifier")
                    i += 2
                else:
                    errors.append(ERR + "#identifier not found")
                    return i

                if lexeme[i] == "=":
                    print("108: =")
                    i += 1

                    if lexeme[i] in first_set["<sqnc>"]:
                        print("108: sqnc")
                        i = sqnc(lexeme, token, i)

                    print("108: concatenate")
                    i = concatenate(lexeme, token, i)

                    if lexeme[i] == ",":
                        print("110: ,")
                        i += 1
                    else:
                        print("111: EPSILON")
                        break
                else:
                    print("109: EPSILON")
                    break

    return i



def argument(lexeme, token, i):
    if lexeme[i] in first_set["<argument>"]:

        # <insert-argument>
        if lexeme[i] in first_set["<insert-argument>"]:
            print("286: <insert-argument>")

            # <all-type-value>
            if lexeme[i] in first_set["<all-type-value>"]:
                print("286: <all-type-value>")
                i = all_type_value(lexeme, token, i)

                # <add-argument>
                if lexeme[i] == ",":
                    print("286: ,")
                    i += 1

                    # <argument>
                    if lexeme[i] in first_set["<argument>"]:
                        print("286: <argument>")
                        i = argument(lexeme, token, i)
            # #identifier
            elif lexeme[i] == "#":
                print("287: #identifier")
                i += 2

                # (
                if lexeme[i] == "(":
                    print("287: (")
                    i += 1
                else:
                    errors.append(ERR + "( not found")
                    return i

                # <2D-argument>
                if lexeme[i] in first_set["<2D-argument>"]:
                    print("287: <2D-argument>")
                    i = D2_argument(lexeme, token, i)

                # )
                if lexeme[i] == ")":
                    print("287: )")
                    i += 1
                else:
                    errors.append(ERR + ") not found")
                    return i

                # <add-argument>
                if lexeme[i] == ",":
                    print("286: ,")
                    i += 1

                    # <argument>
                    if lexeme[i] in first_set["<argument>"]:
                        print("286: <argument>")
                        i = argument(lexeme, token, i)

        elif lexeme[i] in first_set["<insert**kwargs>"]:
            print("286: <insert**kwargs>")

            # <insert-kwargs>
            if lexeme[i] in first_set["<insert-kwargs>"]:
                print("286: <insert-kwargs>")
                i = insert_kwargs(lexeme, token, i)

    return i



def insert_func(lexeme, token, i):
    if lexeme[i] in first_set["<insert-func>"]:
        if lexeme[i] == "(":
            print("90: (")
            i += 1
        else:
            errors.append(ERR + "( not found")
            return i

        # <argument>
        if lexeme[i] in first_set["<argument>"]:
            print("90: argument")
            i = argument(lexeme, token, i)

        # )
        if lexeme[i] == ")":
            print("90: )")
            i += 1
        else:
            errors.append(ERR + ") not found")
            return i

        # .
        if lexeme[i] == ".":
            print("90: .")
            i += 1

            # identifier
            if lexeme[i] == "#":
                print("90: #identifier")
                i += 1
            else:
                errors.append(ERR + "#identifier not found")
                return i


def insert_variable(lexeme, token, i):

    # tint value
    if lexeme[i] == "tint":
        print("16: tint")
        i += 1
        while True:
            if lexeme[i] == "#":
                print("16: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            if lexeme[i] == "=":
                print("26: =")
                i += 1

                i = tint(lexeme, token, i)

            # <more-tint>
            if lexeme[i] == ",":
                print("98: ,")
                i += 1
            else:
                print("99: EPSILON")
                break
    # flora value
    elif lexeme[i] == "flora":
        print("17: flora")
        i += 1
        while True:
            if lexeme[i] == "#":
                print("17: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            if lexeme[i] == "=":
                print("34: =")
                i += 1

                i = flora(lexeme, token, i)

            # <more-flora>
            if lexeme[i] == ",":
                print("100: ,")
                i += 1
            else:
                print("101: EPSILON")
                break

    # chard value
    elif lexeme[i] == "chard":
        print("18: chard")
        i += 1
        while True:
            if lexeme[i] == "#":
                print("18: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            if lexeme[i] == "=":
                print("54: =")
                i += 1

                i = chard(lexeme, token, i)

            # <more-chard>
            if lexeme[i] == ",":
                print("102: ,")
                i += 1
            else:
                print("103: EPSILON")
                break

    # string value
    elif lexeme[i] == "string":
        print("19: string")
        i += 1

        while True:

            if lexeme[i] == "#":
                print("19: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            if lexeme[i] == "=":
                print("59: =")
                i += 1

                print("59: string")
                i = string(lexeme, token, i)

                print("59: concatenate")
                i = concatenate(lexeme, token, i)

            if lexeme[i] == ",":
                print("104: ,")
                i += 1
            else:
                print("105: EPSILON")
                break

    # bloom value
    elif lexeme[i] == "bloom":
        print("20: bloom")
        i += 1

        while True:

            if lexeme[i] == "#":
                print("20: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            if lexeme[i] == "=":
                print("64: =")
                i += 1

                i = bloom(lexeme, token, i)

            if lexeme[i] == ",":
                print("106: ,")
                i += 1
            else:
                print("107: EPSILON")
                break
    elif lexeme[i] in first_set["<sqnc-type>"]:
        print("21: sqnc-type")
        i += 1

        while True:
            if lexeme[i] == "#":
                print("21: #identifier")
                i += 2
            else:
                errors.append(ERR + "#identifier not found")
                return i

            if lexeme[i] == "=":
                print("108: =")
                i += 1

                if lexeme[i] in first_set["<sqnc>"]:
                    print("108: sqnc")
                    i = sqnc(lexeme, token, i)

                print("108: concatenate")
                i = concatenate(lexeme, token, i)

            if lexeme[i] == ",":
                print("110: ,")
                i += 1
            else:
                print("111: EPSILON")
                break

    else:
        errors.append(ERR + "16-20: <insert-variable> not found")
        return i

    return i


def statement(lexeme, token, i):
    if lexeme[i] in first_set["<statement>"]:
        pass

    return i
