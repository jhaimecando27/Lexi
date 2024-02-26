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
                    print(str(i) + ": have " + lexeme[i][0])
                    i += 2
                else:
                    results.append(("floral identifier error", err))
                    return results

                # insert variable
                while True:
                    # <all-assignment> <flora-tint-value> <more-flora-tint>

                    # <all-assignment>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-assignment>"]:
                        print(str(i) + ": have all-assignment")
                        i += 1
                    else:
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-assignment>"]:
                            print(str(i) + ": have string-assignment")
                            i += 1
                        else:
                            results.append(("assignment error", err))
                            return results

                    # <flora-tint-value>
                    if i < len(lexeme) and lexeme[i] in first_set["<flora-tint-value>"]:
                        i += 1

                        # <insert-flora-tint> <operate-flora-tint>
                        if i < len(lexeme) and lexeme[i] in first_set["<insert-flora-tint>"]:
                            i += 1
                            # TODO (wip) identifier
                            if i < len(lexeme) and lexeme[i - 1] == "#":
                                print(str(i) + ": have " + lexeme[i - 1][0])
                                i += 1

                            # lent
                            elif i < len(lexeme) and lexeme[i - 1] == "lent":
                                print(str(i) + ": have lent")
                                if i < len(lexeme) and lexeme[i] == "(":
                                    print(str(i) + ": have (")
                                    i += 1

                                    # TODO: all-type-values

                                    if i < len(lexeme) and lexeme[i] == ")":
                                        print(str(i) + ": have )")
                                        i += 1
                                    else:
                                        results.append(("lent", err))
                                        return results
                                else:
                                    results.append(("lent", err))
                                    return results

                            # TODO <operate-flora-tint>
                            if i < len(lexeme) and lexeme[i] in first_set["<operate-flora-tint>"]:
                                i += 1

                        else:
                            results.append(("flora-tint-value error", err))
                            return results
                    else:
                        results.append(("flora-tint-value error", err))
                        return results

                    # more-flora-tint
                    if i < len(lexeme) and lexeme[i] == ",":
                        print(str(i) + ": have ,")
                        i += 1
                    else:
                        break

                while True:
                    # identifier
                    if i < len(lexeme) and lexeme[i][0] == "#":
                        print(str(i) + ": have " + lexeme[i][0])
                        i += 2

                # identifier
                if i < len(lexeme) and lexeme[i] == ";":
                    print(str(i) + ": have ;")
                    i += 2
                else:
                    print(lexeme[i])
                    results.append(("floral identifier error", err))
                    return results

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

            # --- Statement starts here ---
            while True:
                # <statement>

                # 1. <constant> <all-types> #identifer <insert-variable>;
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
                    print(str(i) + ": have " + lexeme[i][0])
                    i += 2
                else:
                    results.append(("floral identifier error", err))
                    return results

                # insert variable
                while True:
                    # <all-assignment> <flora-tint-value> <more-flora-tint>

                    # <all-assignment>
                    if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<all-assignment>"]:
                        print(str(i) + ": have all-assignment")
                        i += 1
                    else:
                        if lexeme[i] != "EPSILON" and lexeme[i] in first_set["<string-assignment>"]:
                            print(str(i) + ": have string-assignment")
                            i += 1
                        else:
                            results.append(("assignment error", err))
                            return results

                    # <flora-tint-value>
                    if i < len(lexeme) and lexeme[i] in first_set["<flora-tint-value>"]:
                        i += 1

                        # <insert-flora-tint> <operate-flora-tint>
                        if i < len(lexeme) and lexeme[i] in first_set["<insert-flora-tint>"]:
                            i += 1
                            # TODO (wip) identifier
                            if i < len(lexeme) and lexeme[i - 1] == "#":
                                print(str(i) + ": have " + lexeme[i - 1][0])
                                i += 1

                            # lent
                            elif i < len(lexeme) and lexeme[i - 1] == "lent":
                                print(str(i) + ": have lent")
                                if i < len(lexeme) and lexeme[i] == "(":
                                    print(str(i) + ": have (")
                                    i += 1

                                    # TODO: all-type-values

                                    if i < len(lexeme) and lexeme[i] == ")":
                                        print(str(i) + ": have )")
                                        i += 1
                                    else:
                                        results.append(("lent", err))
                                        return results
                                else:
                                    results.append(("lent", err))
                                    return results

                            # TODO <operate-flora-tint>
                            if i < len(lexeme) and lexeme[i] in first_set["<operate-flora-tint>"]:
                                i += 1

                        else:
                            results.append(("flora-tint-value error", err))
                            return results
                    else:
                        results.append(("flora-tint-value error", err))
                        return results

                    # more-flora-tint
                    if i < len(lexeme) and lexeme[i] == ",":
                        print(str(i) + ": have ,")
                        i += 1
                    else:
                        break

                while True:
                    # identifier
                    if i < len(lexeme) and lexeme[i][0] == "#":
                        print(str(i) + ": have " + lexeme[i][0])
                        i += 2

                # identifier
                if i < len(lexeme) and lexeme[i] == ";":
                    print(str(i) + ": have ;")
                    i += 2
                else:
                    print(lexeme[i])
                    results.append(("floral identifier error", err))
                    return results


                # 2. <i/o-statement>;
                # mint(<all-type-value>)
                if i < len(lexeme) and lexeme[i] == "mint":
                    print(str(i) + ": have mint")
                    i += 1

                    if i < len(lexeme) and lexeme[i] == "(":
                        print(str(i) + ": have (")
                        i += 1
                    else:
                        results.append(("mint error", err))
                        return results

                    # <all-type-value>
                    if i < len(lexeme) and lexeme[i] in first_set["<all-type-value>"]:
                        print(str(i) + ": have all-type-value")
                        i += 1

                    if i < len(lexeme) and lexeme[i] == ")":
                        print(str(i) + ": have )")
                        i += 1
                    else:
                        results.append(("mint error", err))
                        return results

                    if i < len(lexeme) and lexeme[i] == ";":
                        print(str(i) + ": have ;")
                        i += 1
                    else:
                        results.append(("mint error", err))
                        return results

                # <insert-inpetal> inpetal(string literal)
                # 3. #identifier <insert-func> <more-id> <insert-assignment>;
                # 4. leaf(<all-type-value>) <more-all> <insert-condition) (<statement>);
                # 5. <iterative>;
                # 6. tree(#identifier) (branch <all-type-value> <insert-branch>; <more-branch);
                # 7. clear;
                # 8. break;

            if i < len(lexeme) and lexeme[i] == ")":
                print(str(i) + ": have )")
                i += 1
                if i < len(lexeme) and lexeme[i] == ";":
                    print(str(i) + ": have ;")
                    i += 1
                else:
                    results.append(("function error: expecting ;", err))
                    return results

        # ----- function -----
        while True:
            # <common-type>
            if i < len(lexeme) and lexeme[i] in first_set["<common-type>"]:
                print(str(i) + ": have common-type")
                i += 1

                # identifier
                if i < len(lexeme) and lexeme[i][0] == "#":
                    print(str(i) + ": have " + lexeme[i][0])
                    i += 2
                    # parameter
                    if i < len(lexeme) and lexeme[i] == "(":
                        print(str(i) + ": have (")
                        i += 1

                        # <insert-parameter>
                        # <keyword-param> <more-key-param>
                        # <common-type>
                        # all-types
                        if i < len(lexeme) and lexeme[i] in first_set["<common-type>"]:
                            print(str(i) + ": have common-type")
                            i += 1
                        else:
                            # No (
                            results.append(
                                ("function error: common-type", err))
                            return results

                        if i < len(lexeme) and lexeme[i][0] == "*":
                            print(str(i) + ": have common-type")
                            i += 1
                            if i < len(lexeme) and lexeme[i][1] == "*":
                                print(str(i) + ": have common-type")
                                i += 1
                        # identifier
                        if i < len(lexeme) and lexeme[i][0] == "#":
                            print(str(i) + ": have " + lexeme[i][0])
                            i += 2

                            # more identifier
                            while True:
                                if i < len(lexeme) and lexeme[i] == ",":
                                    i += 1
                                    if i < len(lexeme) and lexeme[i] in first_set["<common-type>"]:
                                        print(str(i) + ": have common-type")
                                        i += 1

                                        if i < len(lexeme) and lexeme[i] == "*":
                                            print(str(i) + ": have common-type")
                                            i += 1
                                            if i < len(lexeme) and lexeme[i] == "*":
                                                print(
                                                    str(i) + ": have common-type")
                                                i += 1
                                        # identifier
                                        if i < len(lexeme) and lexeme[i][0] == "#":
                                            print(str(i) + ": have " +
                                                  lexeme[i][0])
                                            i += 2
                                else:
                                    break

                            if i < len(lexeme) and lexeme[i] == ")":
                                print(str(i) + ": have )")
                                i += 1
                                if i < len(lexeme) and lexeme[i] == "(":
                                    print(str(i) + ": have (")
                                    i += 1

                                    # Statement

                                    if i < len(lexeme) and lexeme[i] == ")":
                                        print(str(i) + ": have )")
                                        i += 1

                                        if i < len(lexeme) and lexeme[i] == ";":
                                            print(str(i) + ": have ;")
                                            i += 1
                                        else:
                                            # No ;
                                            results.append(
                                                ("function error: expecting ;", err))
                                            return results
                                    else:
                                        # No )
                                        results.append(
                                            ("function error: expecting )", err))
                                        return results
                                else:
                                    # No (
                                    results.append(
                                        ("function error: expecting (", err))
                                    return results
                            else:
                                # No )
                                results.append(
                                    ("function error: expecting )", err))
                                return results

                    else:
                        # No (
                        results.append(("function error: expecting (", err))
                        return results

                else:
                    # No hash
                    results.append(("function error: identifier error", err))
                    return results

                print(str(i) + ": function created")
            else:
                # No <common-type> (have EPSILON)
                break

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
