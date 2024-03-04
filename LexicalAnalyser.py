# Lexical Analyser Logic
import redef as rd
from helper import Errors
from helper import esc, skip, skipV1 # Walang escape characters na nachechek sa string



def lexical_analysis(programs):
    rw = "RESERVED WORD"
    rs = "RESERVED SYMBOL"
    tint_lit = "tint literal"
    flora_lit = "flora literal"
    str_lit = "string literal"
    ch_lit = "chard literal"
    Id = "IDENTIFIER"
    cmnt = "COMMENT"
    results = []

    isComment = False

    for program in programs:
        i = 0

        program += "\n"

        while i < len(program) and program[i] != '\n':

            if isComment:
                print("in comment: " + str(i))
                tmp_wrd = ""
                while i < len(program) and program[i] != '\n':
                    print("in while: " + str(i) + " " + program[i])
                    if i < len(program) and program[i] == '-':
                        i += 1
                        if i < len(program) and program[i] == '-':
                            i += 1
                            if i < len(program) and program[i] == '>':
                                i += 1
                                if i < len(program) and program[i] in rd.delim2:
                                    results.append(("-->", rs))
                                    isComment = False
                                    break
                    tmp_wrd += program[i]
                    i += 1

                print("end comment, i = " + str(i))
                continue

            # ---------------------- Reserved Word ---------------------- #
            # AT delim4
            if i < len(program) and program[i] == 'a':
                i += 1
                tmp_wrd = "a"
                if i < len(program) and program[i] == 't':
                    i += 1
                    tmp_wrd = "at"
                    if i < len(program) and program[i] in rd.delim4:
                        results.append(("at", rw))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim4))
                        i = skip(i, program)
                        continue
            elif i < len(program) and program[i] == 'b':
                tmp_wrd = "b"
                i += 1
                # BARE
                if i < len(program) and program[i] == 'a':
                    i += 1
                    tmp_wrd = "ba"
                    if i < len(program) and program[i] == 'r':
                        i += 1
                        tmp_wrd = "bar"
                        if i < len(program) and program[i] == 'e':
                            i += 1
                            tmp_wrd = "bare"
                            if i < len(program) and program[i] in rd.delim1:
                                results.append(("bare", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim1))
                                i = skip(i, program)
                                continue
                # BLOOM
                elif i < len(program) and program[i] == 'l':
                    i += 1
                    tmp_wrd = "bl"
                    if i < len(program) and program[i] == 'o':
                        i += 1
                        tmp_wrd = "blo"
                        if i < len(program) and program[i] == 'o':
                            i += 1
                            tmp_wrd = "bloo"
                            if i < len(program) and program[i] == 'm':
                                i += 1
                                tmp_wrd = "bloom"
                                if i < len(program) and program[i] in rd.delim3:
                                    results.append(("bloom", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim3))
                                    i = skip(i, program)
                                    continue
                elif i < len(program) and program[i] == 'r':
                    i += 1
                    tmp_wrd = "br"
                    # BRANCH delim27
                    if i < len(program) and program[i] == 'a':
                        i += 1
                        tmp_wrd = "bra"
                        if i < len(program) and program[i] == 'n':
                            i += 1
                            tmp_wrd = "bran"
                            if i < len(program) and program[i] == 'c':
                                i += 1
                                tmp_wrd = "branc"
                                if i < len(program) and program[i] == 'h':
                                    i += 1
                                    tmp_wrd = "branch"
                                    if i < len(program) and program[i] in rd.delim27:
                                        results.append(("branch", rw))
                                        continue
                                    else:
                                        # Finish whole word if error
                                        results.append(Errors.delim(
                                            i, tmp_wrd, program[i], rd.delim27))
                                        i = skip(i, program)
                                        continue
                    # BREAK
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        tmp_wrd = "bre"
                        if i < len(program) and program[i] == 'a':
                            i += 1
                            tmp_wrd = "brea"
                            if i < len(program) and program[i] == 'k':
                                i += 1
                                tmp_wrd = "break"
                                if i < len(program) and program[i] in rd.delim1:
                                    results.append(("break", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim1))
                                    i = skip(i, program)
                                    continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # CHARD
            elif i < len(program) and program[i] == 'c':
                i += 1
                tmp_wrd = "c"
                if i < len(program) and program[i] == 'h':
                    i += 1
                    tmp_wrd = "ch"
                    if i < len(program) and program[i] == 'a':
                        i += 1
                        tmp_wrd = "cha"
                        if i < len(program) and program[i] == 'r':
                            i += 1
                            tmp_wrd = "char"
                            if i < len(program) and program[i] == 'd':
                                i += 1
                                tmp_wrd = "chard"
                                if i < len(program) and program[i] in rd.delim3:
                                    results.append(("chard", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim3))
                                    i = skip(i, program)
                                    continue
                # CLEAR
                elif i < len(program) and program[i] == 'l':
                    i += 1
                    tmp_wrd = "cl"
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        tmp_wrd = "cle"
                        if i < len(program) and program[i] == 'a':
                            i += 1
                            tmp_wrd = "clea"
                            if i < len(program) and program[i] == 'r':
                                i += 1
                                tmp_wrd = "clear"
                                if i < len(program) and program[i] in rd.delim4:
                                    results.append(("clear", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim4))
                                    i = skip(i, program)
                                    continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # DIRT
            elif i < len(program) and program[i] == 'd':
                i += 1
                tmp_wrd = "d"
                if i < len(program) and program[i] == 'i':
                    i += 1
                    tmp_wrd = "di"
                    if i < len(program) and program[i] == 'r':
                        i += 1
                        tmp_wrd = "dir"
                        if i < len(program) and program[i] == 't':
                            i += 1
                            tmp_wrd = "dirt"
                            if i < len(program) and program[i] in rd.delim3:
                                results.append(("dirt", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim3))
                                i = skip(i, program)
                                continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # ELEAF
            elif i < len(program) and program[i] == 'e':
                i += 1
                tmp_wrd = "e"
                if i < len(program) and program[i] == 'l':
                    i += 1
                    tmp_wrd = "el"
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        tmp_wrd = "ele"
                        if i < len(program) and program[i] == 'a':
                            i += 1
                            tmp_wrd = "elea"
                            if i < len(program) and program[i] == 'f':
                                i += 1
                                tmp_wrd = "eleaf"
                                if i < len(program) and program[i] in rd.delim24:
                                    results.append(("eleaf", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim24))
                                    i = skip(i, program)
                                    continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # FALSE
            elif i < len(program) and program[i] == 'f':
                i += 1
                tmp_wrd = "f"
                if i < len(program) and program[i] == 'a':
                    i += 1
                    tmp_wrd = "fa"
                    if i < len(program) and program[i] == 'l':
                        i += 1
                        tmp_wrd = "fal"
                        if i < len(program) and program[i] == 's':
                            i += 1
                            tmp_wrd = "fals"
                            if i < len(program) and program[i] == 'e':
                                i += 1
                                tmp_wrd = "false"
                                if i < len(program) and program[i] in rd.delimb:
                                    results.append(("false", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delimb))
                                    i = skip(i, program)
                                    continue
                # FERN
                if i < len(program) and program[i] == 'e':
                    i += 1
                    tmp_wrd = "fe"
                    if i < len(program) and program[i] == 'r':
                        i += 1
                        tmp_wrd = "fer"
                        if i < len(program) and program[i] == 'n':
                            i += 1
                            tmp_wrd = "fern"
                            if i < len(program) and program[i] in rd.delim3:
                                results.append(("fern", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim3))
                                i = skip(i, program)
                                continue

                # FLORA
                if i < len(program) and program[i] == 'l':
                    i += 1
                    tmp_wrd = "fl"
                    if i < len(program) and program[i] == 'o':
                        i += 1
                        tmp_wrd = "flo"
                        if i < len(program) and program[i] == 'r':
                            i += 1
                            tmp_wrd = "flor"
                            if i < len(program) and program[i] == 'a':
                                i += 1
                                tmp_wrd = "flora"
                                if i < len(program) and program[i] in rd.delim3:
                                    results.append(("flora", rw))
                                    continue

                                # FLORAL
                                elif i < len(program) and program[i] == 'l':
                                    i += 1
                                    tmp_wrd = "floral"
                                    if i < len(program) and program[i] in rd.delim3:
                                        results.append(("floral", rw))
                                        continue
                                    else:
                                        # Finish whole word if error
                                        results.append(Errors.delim(
                                            i, tmp_wrd, program[i], rd.delim4))
                                        i = skip(i, program)
                                        continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim4))
                                    i = skip(i, program)
                                    continue

                            # FLORIST
                            elif i < len(program) and program[i] == 'i':
                                i += 1
                                tmp_wrd = "flori"
                                if i < len(program) and program[i] == 's':
                                    i += 1
                                    tmp_wrd = "floris"
                                    if i < len(program) and program[i] == 't':
                                        i += 1
                                        tmp_wrd = "florist"
                                        if i < len(program) and program[i] in rd.delim3:
                                            results.append(("florist", rw))
                                            continue
                                        else:
                                            # Finish whole word if error
                                            results.append(Errors.delim(
                                                i, tmp_wrd, program[i], rd.delim3))
                                            i = skip(i, program)
                                            continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # GARDEN
            elif i < len(program) and program[i] == 'g':
                i += 1
                tmp_wrd = "g"
                if i < len(program) and program[i] == 'a':
                    i += 1
                    tmp_wrd = "ga"
                    if i < len(program) and program[i] == 'r':
                        i += 1
                        tmp_wrd = "gar"
                        if i < len(program) and program[i] == 'd':
                            i += 1
                            tmp_wrd = "gard"
                            if i < len(program) and program[i] == 'e':
                                i += 1
                                tmp_wrd = "garde"
                                if i < len(program) and program[i] == 'n':
                                    i += 1
                                    tmp_wrd = "garden"
                                    if i < len(program) and program[i] in rd.delim3:
                                        results.append(("garden", rw))
                                        continue
                                    else:
                                        # Finish whole word if error
                                        results.append(Errors.delim(
                                            i, tmp_wrd, program[i], rd.delim3))
                                        i = skip(i, program)
                                        continue
                # GETITEM delim24
                elif i < len(program) and program[i] == 'e':
                    i += 1
                    tmp_wrd = "ge"
                    if i < len(program) and program[i] == 't':
                        i += 1
                        tmp_wrd = "get"
                        if i < len(program) and program[i] == 'I':
                            i += 1
                            tmp_wrd = "getI"
                            if i < len(program) and program[i] == 't':
                                i += 1
                                tmp_wrd = "getIt"
                                if i < len(program) and program[i] == 'e':
                                    i += 1
                                    tmp_wrd = "getIte"
                                    if i < len(program) and program[i] == 'm':
                                        i += 1
                                        tmp_wrd = "getItem"
                                        if i < len(program) and program[i] == 's':
                                            i += 1
                                            tmp_wrd = "getItems"
                                            if i < len(program) and program[i] in rd.delim24:
                                                results.append(("getitem", rw))
                                                continue
                                            else:
                                                # Finish whole word if error
                                                results.append(Errors.delim(
                                                    i, tmp_wrd, program[i], rd.delim24))
                                                i = skip(i, program)
                                                continue
                        # GETKEYS, GETVALUES delim24
                        elif i < len(program) and program[i] == 'k':
                            i += 1
                            tmp_wrd = "getk"
                            if i < len(program) and program[i] == 'e':
                                i += 1
                                tmp_wrd = "getke"
                                if i < len(program) and program[i] == 'y':
                                    i += 1
                                    tmp_wrd = "getkey"
                                    if i < len(program) and program[i] == 's':
                                        i += 1
                                        tmp_wrd = "getKeys"
                                        if i < len(program) and program[i] in rd.delim24:
                                            results.append(("getkeys", rw))
                                            continue
                                        else:
                                            # Finish whole word if error
                                            results.append(Errors.delim(
                                                i, tmp_wrd, program[i], rd.delim24))
                                            i = skip(i, program)
                                            continue
                        elif i < len(program) and program[i] == 'V':
                            i += 1
                            tmp_wrd = "getV"
                            if i < len(program) and program[i] == 'a':
                                i += 1
                                tmp_wrd = "getVa"
                                if i < len(program) and program[i] == 'l':
                                    i += 1
                                    tmp_wrd = "getVal"
                                    if i < len(program) and program[i] == 'u':
                                        i += 1
                                        tmp_wrd = "getValu"
                                        if i < len(program) and program[i] == 'e':
                                            i += 1
                                            tmp_wrd = "getValue"
                                            if i < len(program) and program[i] == 's':
                                                i += 1
                                                tmp_wrd = "getValues"
                                                if i < len(program) and program[i] in rd.delim24:
                                                    results.append(("getValues", rw))
                                                    continue
                                                else:
                                                    # Finish whole word if error
                                                    results.append(Errors.delim(
                                                        i, tmp_wrd, program[i], rd.delim24))
                                                    i = skip(i, program)
                                                    continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # HARD
            elif i < len(program) and program[i] == 'h':
                i += 1
                tmp_wrd = "h"
                if i < len(program) and program[i] == 'a':
                    i += 1
                    tmp_wrd = "ha"
                    if i < len(program) and program[i] == 'r':
                        i += 1
                        tmp_wrd = "har"
                        if i < len(program) and program[i] == 'd':
                            i += 1
                            tmp_wrd = "hard"
                            if i < len(program) and program[i] in rd.delim4:
                                results.append(("hard", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim4))
                                i = skip(i, program)
                                continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # INPETAL
            elif i < len(program) and program[i] == 'i':
                i += 1
                tmp_wrd = "i"
                if i < len(program) and program[i] == 'n':
                    i += 1
                    tmp_wrd = "in"
                    if i < len(program) and program[i] == 'p':
                        i += 1
                        tmp_wrd = "inp"
                        if i < len(program) and program[i] == 'e':
                            i += 1
                            tmp_wrd = "inpe"
                            if i < len(program) and program[i] == 't':
                                i += 1
                                tmp_wrd = "inpet"
                                if i < len(program) and program[i] == 'a':
                                    i += 1
                                    tmp_wrd = "inpeta"
                                    if i < len(program) and program[i] == 'l':
                                        i += 1
                                        tmp_wrd = "inpetal"
                                        if i < len(program) and program[i] in rd.delim3:
                                            results.append(("inpetal", rw))
                                            continue
                                        else:
                                            # Finish whole word if error
                                            results.append(Errors.delim(
                                                i, tmp_wrd, program[i], rd.delim3))
                                            i = skip(i, program)
                                            continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # LEAF
            elif i < len(program) and program[i] == 'l':
                i += 1
                tmp_wrd = "l"
                if i < len(program) and program[i] == 'e':
                    i += 1
                    tmp_wrd = "le"
                    if i < len(program) and program[i] == 'a':
                        i += 1
                        tmp_wrd = "lea"
                        if i < len(program) and program[i] == 'f':
                            i += 1
                            tmp_wrd = "leaf"
                            if i < len(program) and program[i] in rd.delim23:
                                results.append(("leaf", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim23))
                                i = skip(i, program)
                                continue
                    # LENT delim23
                    elif i < len(program) and program[i] == 'n':
                        i += 1
                        tmp_wrd = "len"
                        if i < len(program) and program[i] == 't':
                            i += 1
                            tmp_wrd = "lent"
                            if i < len(program) and program[i] in rd.delim3:
                                results.append(("lent", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim3))
                                i = skip(i, program)
                                continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # MINT
            elif i < len(program) and program[i] == 'm':
                i += 1
                tmp_wrd = "m"
                if i < len(program) and program[i] == 'i':
                    i += 1
                    tmp_wrd = "mi"
                    if i < len(program) and program[i] == 'n':
                        i += 1
                        tmp_wrd = "min"
                        if i < len(program) and program[i] == 't':
                            i += 1
                            tmp_wrd = "mint"
                            if i < len(program) and program[i] in rd.delim3:
                                results.append(("mint", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim3))
                                i = skip(i, program)
                                continue
                # MOSS
                elif i < len(program) and program[i] == 'o':
                    i += 1
                    tmp_wrd = "mo"
                    if i < len(program) and program[i] == 's':
                        i += 1
                        tmp_wrd = "mos"
                        if i < len(program) and program[i] == 's':
                            i += 1
                            tmp_wrd = "moss"
                            if i < len(program) and program[i] in rd.delim21:
                                results.append(("moss", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim21))
                                i = skip(i, program)
                                continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # NUT delim4
            elif i < len(program) and program[i] == 'n':
                i += 1
                tmp_wrd = "n"
                if i < len(program) and program[i] == 'u':
                    i += 1
                    tmp_wrd = "nu"
                    if i < len(program) and program[i] == 't':
                        i += 1
                        tmp_wrd = "nut"
                        if i < len(program) and program[i] in rd.delim4:
                            results.append(("nut", rw))
                            continue
                        else:
                            # Finish whole word if error
                            results.append(Errors.delim(
                                i, tmp_wrd, program[i], rd.delim4))
                            i = skip(i, program)
                            continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # PLANT
            elif i < len(program) and program[i] == 'p':
                i += 1
                tmp_wrd = "p"
                if i < len(program) and program[i] == 'l':
                    i += 1
                    tmp_wrd = "pl"
                    if i < len(program) and program[i] == 'a':
                        i += 1
                        tmp_wrd = "pla"
                        if i < len(program) and program[i] == 'n':
                            i += 1
                            tmp_wrd = "plan"
                            if i < len(program) and program[i] == 't':
                                i += 1
                                tmp_wrd = "plant"
                                if i < len(program) and program[i] in rd.delim2:
                                    results.append(("plant", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim2))
                                    i = skip(i, program)
                                    continue
            # REGROW
            elif i < len(program) and program[i] == 'r':
                i += 1
                tmp_wrd = "r"
                if i < len(program) and program[i] == 'e':
                    i += 1
                    tmp_wrd = "re"
                    if i < len(program) and program[i] == 'g':
                        i += 1
                        tmp_wrd = "reg"
                        if i < len(program) and program[i] == 'r':
                            i += 1
                            tmp_wrd = "regr"
                            if i < len(program) and program[i] == 'o':
                                i += 1
                                tmp_wrd = "regro"
                                if i < len(program) and program[i] == 'w':
                                    i += 1
                                    tmp_wrd = "regrow"
                                    if i < len(program) and program[i] in rd.delim4:
                                        results.append(("regrow", rw))
                                        continue
                                    else:
                                        # Finish whole word if error
                                        results.append(Errors.delim(
                                            i, tmp_wrd, program[i], rd.delim4))
                                        i = skip(i, program)
                                        continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # SEED
            elif i < len(program) and program[i] == 's':
                i += 1
                tmp_wrd = "s"
                if i < len(program) and program[i] == 'e':
                    i += 1
                    tmp_wrd = "se"
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        tmp_wrd = "see"
                        if i < len(program) and program[i] == 'd':
                            i += 1
                            tmp_wrd = "seed"
                            if i < len(program) and program[i] in rd.delim16:
                                results.append(("seed", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim16))
                                i = skip(i, program[i])
                                continue
                # STEM
                elif i < len(program) and program[i] == 't':
                    i += 1
                    tmp_wrd = "st"
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        tmp_wrd = "ste"
                        if i < len(program) and program[i] == 'm':
                            i += 1
                            tmp_wrd = "stem"
                            if i < len(program) and program[i] in rd.delim3:
                                results.append(("stem", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim3))
                                i = skip(i, program)
                                continue
                    # STRING
                    elif i < len(program) and program[i] == 'r':
                        i += 1
                        tmp_wrd = "str"
                        if i < len(program) and program[i] == 'i':
                            i += 1
                            tmp_wrd = "stri"
                            if i < len(program) and program[i] == 'n':
                                i += 1
                                tmp_wrd = "strin"
                                if i < len(program) and program[i] == 'g':
                                    i += 1
                                    tmp_wrd = "string"
                                    if i < len(program) and program[i] in rd.delim3:
                                        results.append(("string", rw))
                                        continue
                                    else:
                                        # Finish whole word if error
                                        results.append(Errors.delim(
                                            i, tmp_wrd, program[i], rd.delim3))
                                        i = skip(i, program)
                                        continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # TINT
            elif i < len(program) and program[i] == 't':
                i += 1
                tmp_wrd = "t"
                if i < len(program) and program[i] == 'i':
                    i += 1
                    tmp_wrd = "ti"
                    if i < len(program) and program[i] == 'n':
                        i += 1
                        tmp_wrd = "tin"
                        if i < len(program) and program[i] == 't':
                            i += 1
                            tmp_wrd = "tint"
                            if i < len(program) and program[i] in rd.delim3:
                                results.append(("tint", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim3))
                                i = skip(i, program)
                                continue
                # TULIP
                elif i < len(program) and program[i] == 'u':
                    i += 1
                    tmp_wrd = "tu"
                    if i < len(program) and program[i] == 'l':
                        i += 1
                        tmp_wrd = "tul"
                        if i < len(program) and program[i] == 'i':
                            i += 1
                            tmp_wrd = "tuli"
                            if i < len(program) and program[i] == 'p':
                                i += 1
                                tmp_wrd = "tulip"
                                if i < len(program) and program[i] in rd.delim3:
                                    results.append(("tulip", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim3))
                                    i = skip(i, program)
                                    continue
                # TREE delim24
                elif i < len(program) and program[i] == 'r':
                    i += 1
                    tmp_wrd = "tr"
                    # TRUE
                    if i < len(program) and program[i] == 'u':
                        i += 1
                        tmp_wrd = "tru"
                        if i < len(program) and program[i] == 'e':
                            i += 1
                            tmp_wrd = "true"
                            if i < len(program) and program[i] in rd.delimb:
                                results.append(("true", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delimb))
                                i = skip(i, program)
                                continue
                    elif i < len(program) and program[i] == 'e':
                        i += 1
                        tmp_wrd = "tre"
                        if i < len(program) and program[i] == 'e':
                            i += 1
                            tmp_wrd = "tree"
                            if i < len(program) and program[i] in rd.delim24:
                                results.append(("tree", rw))
                                continue
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delim24))
                                i = skip(i, program)
                                continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # VIOLA delim4
            elif i < len(program) and program[i] == 'v':
                i += 1
                tmp_wrd = "v"
                if i < len(program) and program[i] == 'i':
                    i += 1
                    tmp_wrd = "vi"
                    if i < len(program) and program[i] == 'o':
                        i += 1
                        tmp_wrd = "vio"
                        if i < len(program) and program[i] == 'l':
                            i += 1
                            tmp_wrd = "viol"
                            if i < len(program) and program[i] == 'a':
                                i += 1
                                tmp_wrd = "viola"
                                if i < len(program) and program[i] in rd.delim4:
                                    results.append(("viola", rw))
                                    continue
                                else:
                                    # Finish whole word if error
                                    results.append(Errors.delim(
                                        i, tmp_wrd, program[i], rd.delim4))
                                    i = skip(i, program)
                                    continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # WILLOW
            elif i < len(program) and program[i] == 'w':
                i += 1
                tmp_wrd = "w"
                if i < len(program) and program[i] == 'i':
                    i += 1
                    tmp_wrd = "wi"
                    if i < len(program) and program[i] == 'l':
                        i += 1
                        tmp_wrd = "wil"
                        if i < len(program) and program[i] == 'l':
                            i += 1
                            tmp_wrd = "will"
                            if i < len(program) and program[i] == 'o':
                                i += 1
                                tmp_wrd = "willo"
                                if i < len(program) and program[i] == 'w':
                                    i += 1
                                    tmp_wrd = "willow"
                                    if i < len(program) and program[i] in rd.delim3:
                                        results.append(("willow", rw))
                                        continue
                                    else:
                                        # Finish whole word if error
                                        results.append(Errors.delim(
                                            i, tmp_wrd, program[i], rd.delim3))
                                        i = skip(i, program)
                                        continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # ---------------------- Reserved Symbol ---------------------- #

            # + delim5, += delim19
            elif i < len(program) and program[i] == '+':
                i += 1
                tmp_wrd = "+"
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("+", rs))
                    continue
                elif i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = "+="
                    if i < len(program) and program[i] in rd.delim19:
                        results.append(("+=", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim19))
                        i = skip(i, program)
                        continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim5))
                    i = skip(i, program)
                    continue

            # - delim19
            elif i < len(program) and program[i] == '-':
                i += 1
                tmp_wrd = "-"
                if i < len(program) and program[i] in rd.delim19:
                    results.append(("-", rs))
                    continue
                # -= delim19
                elif i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = "-="
                    if i < len(program) and program[i] in rd.delim19:
                        results.append(("-=", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim19))
                        i = skip(i, program)
                        continue
                # --> delim2
                elif i < len(program) and program[i] == '-':
                    i += 1
                    tmp_wrd = "--"
                    if i < len(program) and program[i] == '>':
                        i += 1
                        tmp_wrd = "-->"
                        if i < len(program) and program[i] in rd.delim2:
                            results.append(("-->", rs))
                            continue
                        else:
                            # Finish whole word if error
                            results.append(Errors.delim(
                                i, tmp_wrd, program[i], rd.delim2))
                            i = skip(i, program)
                            continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim19))
                    i = skip(i, program)
                    continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # * delim13, ** delim13, **= delim13, *= delim13
            elif i < len(program) and program[i] == '*':
                i += 1
                tmp_wrd = "*"
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("*", rs))
                    continue
                elif i < len(program) and program[i] == '#':
                    i += 1
                    tmp_wrd = "*#"
                    if i < len(program) and program[i] in rd.delim25:
                        results.append(("*#", rs))
                        tmp_wrd = ""
                        tmp_wrd = program[i]
                        i += 1
                        for x in range(50):
                            if program[i] == "\n":
                                results.append(Errors.delim(i, tmp_wrd, program[i], ["\""]))
                                i = skip(i, program)
                                break
                            if i < len(program) and program[i].isalnum():
                                tmp_wrd += program[i]
                                i += 1
                            if x == 49:
                                if program[i].isalnum():
                                    tmp_wrd += program[i]
                                    results.append(Errors.Id(i, tmp_wrd))
                                    i = skip(i, program)
                                    continue
                            if program[i] in rd.delimi:
                                results.append((tmp_wrd, Id))
                                break
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim25))
                        i = skip(i, program)
                        continue
                # ** delim13
                elif i < len(program) and program[i] == '*':
                    i += 1
                    tmp_wrd = "**"
                    if i < len(program) and program[i] in rd.delim13:
                        results.append(("**", rs))
                        continue
                    # **= delim13
                    elif i < len(program) and program[i] == '=':
                        i += 1
                        tmp_wrd = "**="
                        if i < len(program) and program[i] in rd.delim13:
                            results.append(("**=", rs))
                            continue
                        else:
                            # Finish whole word if error
                            results.append(Errors.delim(
                                i, tmp_wrd, program[i], rd.delim13))
                            i = skip(i, program)
                            continue
                    # **#
                    elif i < len(program) and program[i] == '#':
                        i += 1
                        tmp_wrd = "**#"
                        if i < len(program) and program[i] in rd.delim20:
                            results.append(("**#", rs))
                            tmp_wrd = ""
                            tmp_wrd = program[i]
                            i += 1
                            for x in range(50):
                                if i < len(program) and program[i].isalnum():
                                    tmp_wrd += program[i]
                                    i += 1
                                if x == 49:
                                    if program[i].isalnum():
                                        tmp_wrd += program[i]
                                        results.append(Errors.Id(i, tmp_wrd))
                                        i = skip(i, program)
                                        continue
                                if program[i] in rd.delim26:
                                    results.append((tmp_wrd, Id))
                                    break
                            continue
                        else:
                            # Finish whole word if error
                            results.append(Errors.delim(
                                i, tmp_wrd, program[i], rd.delim26))
                            i = skip(i, program)
                            continue
                # *= delim13
                elif i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = "*="
                    if i < len(program) and program[i] in rd.delim13:
                        results.append(("*=", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim13))
                        i = skip(i, program)
                        continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim13))
                    i = skip(i, program)
                    continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # /, //, //=, /= delim13
            elif i < len(program) and program[i] == '/':
                i += 1
                tmp_wrd = "/"
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("/", rs))
                    continue
                # // delim13
                elif i < len(program) and program[i] == '/':
                    i += 1
                    tmp_wrd = "//"
                    if i < len(program) and program[i] in rd.delim13:
                        results.append(("//", rs))
                        continue
                    # //= delim13
                    elif i < len(program) and program[i] == '=':
                        i += 1
                        tmp_wrd = "//="
                        if i < len(program) and program[i] in rd.delim13:
                            results.append(("//=", rs))
                            continue
                        else:
                            # Finish whole word if error
                            results.append(Errors.delim(
                                i, tmp_wrd, program[i], rd.delim13))
                            i = skip(i, program)
                            continue
                # /= delim13
                elif i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = "/="
                    if i < len(program) and program[i] in rd.delim13:
                        results.append(("/=", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim13))
                        i = skip(i, program)
                        continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim13))
                    i = skip(i, program)
                    continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # %, %= delim13
            elif i < len(program) and program[i] == '%':
                i += 1
                tmp_wrd = "%"
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("%", rs))
                    continue
                # %= delim13
                elif i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = "%="
                    if i < len(program) and program[i] in rd.delim13:
                        results.append(("%=", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim13))
                        i = skip(i, program)
                        continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim13))
                    i = skip(i, program)
                    continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # !=
            elif i < len(program) and program[i] == '!':
                i += 1
                tmp_wrd = "!"
                if i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = "!="
                    if i < len(program) and program[i] in rd.delim5:
                        results.append(("!=", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim5))
                        i = skip(i, program)
                        continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # >
            elif i < len(program) and program[i] == '>':
                i += 1
                tmp_wrd = ">"
                if i < len(program) and program[i] in rd.delim22:
                    results.append((">", rs))
                    continue

                # >=
                elif i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = ">="
                    if i < len(program) and program[i] in rd.delim13:
                        results.append((">=", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim13))
                        i = skip(i, program)
                        continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim22))
                    i = skip(i, program)
                    continue
                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # <
            elif i < len(program) and program[i] == '<':
                i += 1
                tmp_wrd = "<"
                if i < len(program) and program[i] in rd.delim22:
                    results.append(("<", rs))
                    continue

                # <=
                elif i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = "<="
                    if i < len(program) and program[i] in rd.delim22:
                        results.append(("<=", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim22))
                        i = skip(i, program)
                        continue

                # <--
                elif i < len(program) and program[i] == '-':
                    i += 1
                    tmp_wrd = "<-"
                    if i < len(program) and program[i] == '-':
                        i += 1
                        tmp_wrd = "<--"
                        if i < len(program) and program[i] in rd.delim14:
                            results.append(("<--", rs))
                            print("comment start")
                            isComment = True
                            continue
                        else:
                            # Finish whole word if error
                            results.append(Errors.delim(
                                i, tmp_wrd, program[i], rd.delim14))
                            i = skip(i, program)
                            continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # (
            elif i < len(program) and program[i] == '(':
                i += 1
                tmp_wrd = "("
                if i < len(program) and program[i] in rd.delim6:
                    results.append(("(", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim6))
                    i = skip(i, program)
                    continue

            # [
            elif i < len(program) and program[i] == '[':
                i += 1
                tmp_wrd = "["
                if i < len(program) and program[i] in rd.delim6:
                    results.append(("[", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim6))
                    i = skip(i, program)
                    continue

            # {
            elif i < len(program) and program[i] == '{':
                i += 1
                tmp_wrd = "{"
                if i < len(program) and program[i] in rd.delim23:
                    results.append(("{", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim23))
                    i = skip(i, program)
                    continue

            # ]
            elif i < len(program) and program[i] == ']':
                i += 1
                tmp_wrd = "]"
                if i < len(program) and program[i] in rd.delim12:
                    results.append(("]", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim12))
                    i = skip(i, program)
                    continue

            # }
            elif i < len(program) and program[i] == '}':
                i += 1
                tmp_wrd = "}"
                if i < len(program) and program[i] in rd.delim18:
                    results.append(("}", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim18))
                    i = skip(i, program)
                    continue

            # ) delim17
            elif i < len(program) and program[i] == ')':
                i += 1
                tmp_wrd = ")"
                if i < len(program) and program[i] in rd.delim17:
                    results.append((")", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim17))
                    i = skip(i, program)
                    continue

            # , delim7
            elif i < len(program) and program[i] == ',':
                i += 1
                tmp_wrd = ","
                if i < len(program) and program[i] in rd.delim7:
                    results.append((",", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim7))
                    i = skip(i, program)
                    continue

            # : delim15
            elif i < len(program) and program[i] == ':':
                i += 1
                tmp_wrd = ":"
                if i < len(program) and program[i] in rd.delim15:
                    results.append((": ", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim15))
                    i = skip(i, program)
                    continue

            # . delim8
            elif i < len(program) and program[i] == '.':
                i += 1
                tmp_wrd = "."
                if i < len(program) and program[i] in rd.delim28:
                    results.append((".", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim28))
                    i = skip(i, program)
                    continue

            # ; delim16
            elif i < len(program) and program[i] == ';':
                i += 1
                tmp_wrd = ";"
                if i < len(program) and program[i] in rd.delim16:
                    results.append((";", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim16))
                    i = skip(i, program)
                    continue

            # # delim20
            elif i < len(program) and program[i] == '#':
                i += 1
                tmp_wrd = "#"
                if i < len(program) and program[i] in rd.delim20:
                    results.append(("#", rs))
                    tmp_wrd = ""
                    tmp_wrd = program[i]
                    i += 1
                    for x in range(50):
                        if program[i] == "\n":
                            results.append(Errors.delim(i, tmp_wrd, program[i], ["\""]))
                            i = skip(i, program)
                            break
                        if i < len(program) and program[i].isalnum():
                            tmp_wrd += program[i]
                            i += 1
                        if x == 49:
                            if program[i].isalnum():
                                tmp_wrd += program[i]
                                results.append(Errors.Id(i, tmp_wrd))
                                i = skip(i, program)
                                continue
                        if program[i] in rd.delimi:
                            results.append((tmp_wrd, Id))
                            break
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim20))
                    i = skip(i, program)
                    continue

            # ? delim20
            elif i < len(program) and program[i] == '?':
                i += 1
                tmp_wrd = "?"
                if i < len(program) and program[i] in rd.delim20:
                    results.append(("?", rs))

                    comment = ''
                    single_symbols = [" ", "\n", "\t", ";", ",", "(", ")", "#"]
                    while i < len(program) and program[i] not in single_symbols:
                        comment += program[i]
                        i += 1

                    results.append((comment, cmnt))

                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim20))
                    i = skip(i, program)
                    continue

            # =, ==, =!, =&, =/ delim8
            elif i < len(program) and program[i] == '=':
                i += 1
                tmp_wrd = "="
                if i < len(program) and program[i] == '=':
                    i += 1
                    tmp_wrd = "=="
                    if i < len(program) and program[i] in rd.delim8:
                        results.append(("==", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim8))
                        i = skip(i, program)
                        continue
                elif i < len(program) and program[i] == '!':
                    i += 1
                    tmp_wrd = "=!"
                    if i < len(program) and program[i] in rd.delim8:
                        results.append(("=!", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim8))
                        i = skip(i, program)
                        continue
                elif i < len(program) and program[i] == '&':
                    i += 1
                    tmp_wrd = "=&"
                    if i < len(program) and program[i] in rd.delim8:
                        results.append(("=&", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim8))
                        i = skip(i, program)
                        continue
                elif i < len(program) and program[i] == '/':
                    i += 1
                    tmp_wrd = "=/"
                    if i < len(program) and program[i] in rd.delim8:
                        results.append(("=/", rs))
                        continue
                    else:
                        # Finish whole word if error
                        results.append(Errors.delim(
                            i, tmp_wrd, program[i], rd.delim8))
                        i = skip(i, program)
                        continue
                elif i < len(program) and program[i] in rd.delim8:
                    results.append(("=", rs))
                    continue
                else:
                    # Finish whole word if error
                    results.append(Errors.delim(
                        i, tmp_wrd, program[i], rd.delim8))
                    i = skip(i, program)
                    continue

                # Finish whole word if error
                i, tmp_wrd = skipV1(i, program, tmp_wrd)
                results.append(Errors.Id(i, tmp_wrd))
                continue

            # ---------------------- Literals ---------------------- #

            # Tint
            elif i < len(program) and program[i].isdigit():
                tmp_wrd = ""
                for x in range(6):
                    if i < len(program) and program[i].isdigit():
                        tmp_wrd += program[i]
                        i += 1

                    if x == 5:
                        if program[i].isdigit():
                            tmp_wrd += program[i]
                            results.append(Errors.Int(i, tmp_wrd))
                            i = skip(i, program)
                            continue
                        elif program[i] in rd.delimtf:
                            results.append((tmp_wrd, tint_lit))
                            continue
                        elif program[i] == ".":
                            tmp_wrd += program[i]
                            i += 1
                            break

                    continue

                if program[i - 1] == ".":
                    # Flora
                    for x in range(7):
                        if i < len(program) and program[i].isdigit():
                            tmp_wrd += program[i]
                            i += 1
                        if x == 5:
                            if program[i].isdigit():
                                tmp_wrd += program[i]
                                results.append(Errors.Float(i, tmp_wrd))
                                i = skip(i, program)
                                continue
                            elif program[i] in rd.delimtf:
                                results.append((tmp_wrd, flora_lit))
                                continue

                if program[i] not in rd.delimtf:
                    results.append(Errors.delim(i, tmp_wrd, program[i], rd.delimtf))
                    i = skip(i, program)
                    continue
                continue

            # String
            elif i < len(program) and program[i] == '"':
                tmp_wrd += program[i]
                i += 1
                if i < len(program) and program[i].isascii():
                    while True:
                        if program[i] == "\n":
                            results.append(Errors.delim(i, tmp_wrd, program[i], ["\""]))
                            i = skip(i, program)
                            break
                        if i < len(program) and program[i].isascii():
                            tmp_wrd += program[i]
                            i += 1

                        if i < len(program) and program[i] == '\\':
                            tmp_esc = "\\"
                            i += 1
                            if i < len(program) and program[i] == 'n':
                                tmp_esc = "\\n"
                                i += 1
                                results.append((tmp_esc, str_lit))
                            elif i < len(program) and program[i] == '\\':
                                tmp_esc = "\\\\"
                                i += 1
                                results.append((tmp_esc, str_lit))
                            elif i < len(program) and program[i] == '"':
                                tmp_esc = "\\\""
                                i += 1
                                results.append((tmp_esc, str_lit))
                            elif i < len(program) and program[i] == 't':
                                tmp_esc = "\\t"
                                i += 1
                                results.append((tmp_esc, str_lit))
                            elif i < len(program) and program[i] == '\'':
                                tmp_esc = "\\'"
                                i += 1
                                results.append((tmp_esc, str_lit))

                        if program[i] == '"':
                            tmp_wrd += program[i]
                            i += 1
                            if i < len(program) and program[i] in rd.delimtf:
                                results.append((tmp_wrd, str_lit))
                                break
                            else:
                                # Finish whole word if error
                                results.append(Errors.delim(
                                    i, tmp_wrd, program[i], rd.delimtf))
                                i = skip(i, program)
                                break
                    continue

            elif i < len(program) and program[i] == "'":
                tmp_wrd += program[i]
                i += 1
                if i < len(program) and program[i].isascii():
                    if program[i] == "\n":
                        results.append(Errors.delim(i, tmp_wrd, program[i], ["\""]))
                        i = skip(i, program)
                        continue
                    if i < len(program) and program[i].isascii():
                        tmp_wrd += program[i]
                        i += 1
                    if program[i] == "'":
                        tmp_wrd += program[i]
                        i += 1
                        if i < len(program) and program[i] in rd.delimtf:
                            results.append((tmp_wrd, ch_lit))
                            continue
                        else:
                            # Finish whole word if error
                            results.append(Errors.delim(
                                i, tmp_wrd, program[i], rd.delimtf))
                            i = skip(i, program)
                            continue
                    else:
                        results.append(Errors.delim(i, tmp_wrd, program[i], ["'"]))
                        i = skip(i, program)
                        continue

                if program[i] not in rd.delimtf:
                    results.append(Errors.delim(i, tmp_wrd, program[i], rd.delimtf))
                    i = skip(i, program)
                    continue
                continue

            if program[i] == ' ':
                results.append(("<space>", rs))
                i += 1
                continue

            if program[i] == "\t":
                i += 1
                continue

            # The letter is none existent
            single_symbols = [" ", "\n", "\t", ";", ",", "(", ")", "#"]
            while program[i] != ' ' and program[i] != '\n':
                if program[i] in single_symbols:
                    break
                tmp_wrd += program[i]
                i += 1
            results.append(Errors.Id(i, tmp_wrd))

    return results
