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

        if program[i] == ' ':
            results.append(("<space>", rs))
            i += 1
            continue

        # The letter is none existent
        results.append((str(i) + ": " + program[i], un))
        while program[i] != ' ' and program[i] != '\n':
            i += 1

    return results
