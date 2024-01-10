# Lexical Analyser Logic
import redef as rd


def lexical_analysis(program):
    rw = "RESERVED WORD"
    rs = "RESERVED SYMBOL"
    un = "unknown"
    i = 0
    results = []

    while i < len(program) and program[i] != '\n':
        if i < len(program) and program[i] == 'b':
            i += 1
            # BARE
            if i < len(program) and program[i] == 'a':
                i += 1
                if i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        if i < len(program) and program[i] in rd.delim1:
                            results.append(("bare", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue
            # BLOOM
            elif i < len(program) and program[i] == 'l':
                i += 1
                if i < len(program) and program[i] == 'o':
                    i += 1
                    if i < len(program) and program[i] == 'o':
                        i += 1
                        if i < len(program) and program[i] == 'm':
                            i += 1
                            if i < len(program) and program[i] in rd.delim4:
                                results.append(("bloom", rw))
                                results.append((program[i], rs))
                                continue
            # BREAK
            elif i < len(program) and program[i] == 'r':
                i += 1
                if i < len(program) and program[i] == 'e':
                    i += 1
                    if i < len(program) and program[i] == 'a':
                        i += 1
                        if i < len(program) and program[i] == 'k':
                            i += 1
                            if i < len(program) and program[i] in rd.delim1:
                                results.append(("break", rw))
                                results.append((program[i], rs))
                                i += 1
                                continue

            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # CLEAR
        elif i < len(program) and program[i] == 'c':
            i += 1
            if i < len(program) and program[i] == 'l':
                i += 1
                if i < len(program) and program[i] == 'e':
                    i += 1
                    if i < len(program) and program[i] == 'a':
                        i += 1
                        if i < len(program) and program[i] == 'r':
                            i += 1
                            if i < len(program) and program[i] in rd.delim1:
                                results.append(("clear", rw))
                                results.append((program[i], rs))
                                i += 1
                                continue

            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # DIRT
        elif i < len(program) and program[i] == 'd':
            i += 1
            if i < len(program) and program[i] == 'i':
                i += 1
                if i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 't':
                        i += 1
                        if i < len(program) and program[i] in rd.delim4:
                            results.append(("dirt", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue

            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # ELEAF
        elif i < len(program) and program[i] == 'e':
            i += 1
            if i < len(program) and program[i] == 'l':
                i += 1
                if i < len(program) and program[i] == 'e':
                    i += 1
                    if i < len(program) and program[i] == 'a':
                        i += 1
                        if i < len(program) and program[i] == 'f':
                            i += 1
                            if i < len(program) and program[i] in rd.delim3:
                                results.append(("eleaf", rw))
                                results.append((program[i], rs))
                                i += 1
                                continue

            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # FALSE
        elif i < len(program) and program[i] == 'f':
            i += 1
            if i < len(program) and program[i] == 'a':
                i += 1
                if i < len(program) and program[i] == 'l':
                    i += 1
                    if i < len(program) and program[i] == 's':
                        i += 1
                        if i < len(program) and program[i] == 'e':
                            i += 1
                            if i < len(program) and program[i] in rd.delim1:
                                results.append(("false", rw))
                                results.append((program[i], rs))
                                i += 1
                                continue
            # FERN
            if i < len(program) and program[i] == 'e':
                i += 1
                if i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 'n':
                        i += 1
                        if i < len(program) and program[i] in rd.delim3:
                            results.append(("fern", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue

            # FLORA
            if i < len(program) and program[i] == 'l':
                i += 1
                if i < len(program) and program[i] == 'o':
                    i += 1
                    if i < len(program) and program[i] == 'r':
                        i += 1
                        if i < len(program) and program[i] == 'a':
                            i += 1
                            if i < len(program) and program[i] in rd.delim4:
                                results.append(("flora", rw))
                                results.append((program[i], rs))
                                i += 1
                                continue

                            # FLORAL
                            elif i < len(program) and program[i] == 'l':
                                i += 1
                                if i < len(program) and program[i] in rd.delim4:
                                    results.append(("floral", rw))
                                    results.append((program[i], rs))
                                    i += 1
                                    continue

                        # FLORIST
                        elif i < len(program) and program[i] == 'i':
                            i += 1
                            if i < len(program) and program[i] == 's':
                                i += 1
                                if i < len(program) and program[i] == 't':
                                    i += 1
                                    if i < len(program) and program[i] in rd.delim4:
                                        results.append(("florist", rw))
                                        results.append((program[i], rs))
                                        i += 1
                                        continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # GARDEN
        elif i < len(program) and program[i] == 'g':
            i += 1
            if i < len(program) and program[i] == 'a':
                i += 1
                if i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 'd':
                        i += 1
                        if i < len(program) and program[i] == 'e':
                            i += 1
                            if i < len(program) and program[i] == 'n':
                                i += 1
                                if i < len(program) and program[i] in rd.delim4:
                                    results.append(("garden", rw))
                                    results.append((program[i], rs))
                                    i += 1
                                    continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # INPETAL
        elif i < len(program) and program[i] == 'i':
            i += 1
            if i < len(program) and program[i] == 'n':
                i += 1
                if i < len(program) and program[i] == 'p':
                    i += 1
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        if i < len(program) and program[i] == 't':
                            i += 1
                            if i < len(program) and program[i] == 'a':
                                i += 1
                                if i < len(program) and program[i] == 'l':
                                    i += 1
                                    if i < len(program) and program[i] in rd.delim3:
                                        results.append(("inpetal", rw))
                                        results.append((program[i], rs))
                                        i += 1
                                        continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # LANTENA
        elif i < len(program) and program[i] == 'l':
            i += 1
            if i < len(program) and program[i] == 'a':
                i += 1
                if i < len(program) and program[i] == 'n':
                    i += 1
                    if i < len(program) and program[i] == 't':
                        i += 1
                        if i < len(program) and program[i] == 'e':
                            i += 1
                            if i < len(program) and program[i] == 'n':
                                i += 1
                                if i < len(program) and program[i] == 'a':
                                    i += 1
                                    if i < len(program) and program[i] in rd.delim3:
                                        results.append(("lantena", rw))
                                        results.append((program[i], rs))
                                        i += 1
                                        continue
            # LEAF
            elif i < len(program) and program[i] == 'e':
                i += 1
                if i < len(program) and program[i] == 'a':
                    i += 1
                    if i < len(program) and program[i] == 'f':
                        i += 1
                        if i < len(program) and program[i] in rd.delim3:
                            results.append(("leaf", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # MINT
        elif i < len(program) and program[i] == 'm':
            i += 1
            if i < len(program) and program[i] == 'i':
                i += 1
                if i < len(program) and program[i] == 'n':
                    i += 1
                    if i < len(program) and program[i] == 't':
                        i += 1
                        if i < len(program) and program[i] in rd.delim3:
                            results.append(("mint", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # REGROW
        elif i < len(program) and program[i] == 'r':
            i += 1
            if i < len(program) and program[i] == 'e':
                i += 1
                if i < len(program) and program[i] == 'g':
                    i += 1
                    if i < len(program) and program[i] == 'r':
                        i += 1
                        if i < len(program) and program[i] == 'o':
                            i += 1
                            if i < len(program) and program[i] == 'w':
                                i += 1
                                if i < len(program) and program[i] in rd.delim9:
                                    results.append(("regrow", rw))
                                    results.append((program[i], rs))
                                    i += 1
                                    continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # SEED
        elif i < len(program) and program[i] == 's':
            i += 1
            if i < len(program) and program[i] == 'e':
                i += 1
                if i < len(program) and program[i] == 'e':
                    i += 1
                    if i < len(program) and program[i] == 'd':
                        i += 1
                        if i < len(program) and program[i] in rd.delim16:
                            results.append(("seed", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue
            # STEM
            elif i < len(program) and program[i] == 't':
                i += 1
                if i < len(program) and program[i] == 'e':
                    i += 1
                    if i < len(program) and program[i] == 'm':
                        i += 1
                        if i < len(program) and program[i] in rd.delim4:
                            results.append(("stem", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue
                # STRING
                elif i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 'i':
                        i += 1
                        if i < len(program) and program[i] == 'n':
                            i += 1
                            if i < len(program) and program[i] == 'g':
                                i += 1
                                if i < len(program) and program[i] in rd.delim4:
                                    results.append(("string", rw))
                                    results.append((program[i], rs))
                                    i += 1
                                    continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # TINT
        elif i < len(program) and program[i] == 't':
            i += 1
            if i < len(program) and program[i] == 'i':
                i += 1
                if i < len(program) and program[i] == 'n':
                    i += 1
                    if i < len(program) and program[i] == 't':
                        i += 1
                        if i < len(program) and program[i] in rd.delim3:
                            results.append(("tint", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue
            # TRANSPLANT
            elif i < len(program) and program[i] == 'r':
                i += 1
                if i < len(program) and program[i] == 'a':
                    i += 1
                    if i < len(program) and program[i] == 'n':
                        i += 1
                        if i < len(program) and program[i] == 's':
                            i += 1
                            if i < len(program) and program[i] == 'p':
                                i += 1
                                if i < len(program) and program[i] == 'l':
                                    i += 1
                                    if i < len(program) and program[i] == 'a':
                                        i += 1
                                        if i < len(program) and program[i] == 'n':
                                            i += 1
                                            if i < len(program) and program[i] == 't':
                                                i += 1
                                                if i < len(program) and program[i] in rd.delim4:
                                                    results.append(
                                                        ("transplant", rw))
                                                    results.append(
                                                        (program[i], rs))
                                                    i += 1
                                                    continue
                # TRUE
                if i < len(program) and program[i] == 'u':
                    i += 1
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        if i < len(program) and program[i] in rd.delim1:
                            results.append(("true", rw))
                            results.append((program[i], rs))
                            i += 1
                            continue
                # TULIP
                elif i < len(program) and program[i] == 'u':
                    i += 1
                    if i < len(program) and program[i] == 'l':
                        i += 1
                        if i < len(program) and program[i] == 'i':
                            i += 1
                            if i < len(program) and program[i] == 'p':
                                i += 1
                                if i < len(program) and program[i] in rd.delim3:
                                    results.append(("tulip", rw))
                                    results.append((program[i], rs))
                                    i += 1
                                    continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        # WILLOW
        elif i < len(program) and program[i] == 'w':
            i += 1
            if i < len(program) and program[i] == 'i':
                i += 1
                if i < len(program) and program[i] == 'l':
                    i += 1
                    if i < len(program) and program[i] == 'l':
                        i += 1
                        if i < len(program) and program[i] == 'o':
                            i += 1
                            if i < len(program) and program[i] == 'w':
                                i += 1
                                if i < len(program) and program[i] in rd.delim4:
                                    results.append(("willow", rw))
                                    results.append((program[i], rs))
                                    i += 1
                                    continue
            # Finish whole word if error
            results.append((str(i) + ": " + program[i], un))
            while program[i] != ' ' and program[i] != '\n':
                i += 1
            continue

        if program[i] == ' ':
            results.append(("<space>", rs))
            i += 1
            continue

        # The letter is none existent
        results.append((str(i) + ": " + program[i], un))
        while program[i] != ' ' and program[i] != '\n':
            i += 1

    return results
