# Lexical Analyser Logic
import redef as rd


def lexical_analysis(program):
    i = 0
    results = []
    while i < len(program):
        if i < len(program) and program[i] == 'b':
            i += 1
            if i < len(program) and program[i] == 'a':
                i += 1
                if i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        if i < len(program) and program[i] in rd.delim1:
                            results.append(("bare", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue

            elif i < len(program) and program[i] == 'l':
                i += 1
                if i < len(program) and program[i] == 'o':
                    i += 1
                    if i < len(program) and program[i] == 'o':
                        i += 1
                        if i < len(program) and program[i] == 'm':
                            i += 1
                            if i < len(program) and program[i] in rd.delim4:
                                results.append(("bloom", "Reserved Word"))
                                i += 1
                                if i == len(program):
                                    return results
                                continue

            elif i < len(program) and program[i] == 'r':
                i += 1
                if i < len(program) and program[i] == 'e':
                    i += 1
                    if i < len(program) and program[i] == 'a':
                        i += 1
                        if i < len(program) and program[i] == 'k':
                            i += 1
                            if i < len(program) and program[i] in rd.delim1:
                                results.append(("break", "Reserved Word"))
                                if i == len(program):
                                    return results
                                continue

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
                                results.append(("clear", "Reserved Word"))
                                i += 1
                                if i == len(program):
                                    return results
                                continue

        elif i < len(program) and program[i] == 'd':
            i += 1
            if i < len(program) and program[i] == 'i':
                i += 1
                if i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 't':
                        i += 1
                        if i < len(program) and program[i] in rd.delim4:
                            results.append(("dirt", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue

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
                                results.append(("eleaf", "Reserved Word"))
                                i += 1
                                if i == len(program):
                                    return results
                                continue

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
                                results.append(("false", "Reserved Word"))
                                i += 1
                                if i == len(program):
                                    return results
                                continue

            elif i < len(program) and program[i] == 'e':
                i += 1
                if i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 'n':
                        i += 1
                        if i < len(program) and program[i] in rd.delim3:
                            results.append(("fern", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue

            elif i < len(program) and program[i] == 'l':
                i += 1
                if i < len(program) and program[i] == 'o':
                    i += 1
                    if i < len(program) and program[i] == 'r':
                        i += 1
                        if i < len(program) and program[i] == 'a':
                            i += 1
                            if i < len(program) and program[i] in rd.delim4:
                                results.append(("flora", "Reserved Word"))
                                i += 1
                                if i == len(program):
                                    return results
                                continue
                            elif i < len(program) and program[i] == 'l':
                                i += 1
                                if i < len(program) and program[i] in rd.delim4:
                                    results.append(("floral", "Reserved Word"))
                                    i += 1
                                    if i == len(program):
                                        return results
                                    continue
                        elif i < len(program) and program[i] == 'i':
                            i += 1
                            if i < len(program) and program[i] == 's':
                                i += 1
                                if i < len(program) and program[i] == 't':
                                    i += 1
                                    if i < len(program) and program[i] in rd.delim4:
                                        results.append(
                                            ("florist", "Reserved Word"))
                                        i += 1
                                        if i == len(program):
                                            return results
                                        continue

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
                                if i < len(program) and program[i] in rd.delim3:
                                    results.append(("garden", "Reserved Word"))
                                    i += 1
                                    if i == len(program):
                                        return results
                                    continue
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
                                        results.append(
                                            ("inpetal", "Reserved Word"))
                                        i += 1
                                        if i == len(program):
                                            return results
                                        continue
        elif i < len(program) and program[i] == 'l':
            i += 1
            if i < len(program) and program[i] == 'a':
                i += 1
                if i < len(program) and program[i] == 'n':
                    i += 1
                    if i < len(program) and program[i] == 't':
                        i += 1
                        if i < len(program) and program[i] == 'a':
                            i += 1
                            if i < len(program) and program[i] == 'n':
                                i += 1
                                if i < len(program) and program[i] == 'a':
                                    i += 1
                                    if i < len(program) and program[i] in rd.delim3:
                                        results.append(
                                            ("lantana", "Reserved Word"))
                                        i += 1
                                        if i == len(program):
                                            return results
                                        continue
            elif i < len(program) and program[i] == 'e':
                i += 1
                if i < len(program) and program[i] == 'a':
                    i += 1
                    if i < len(program) and program[i] == 'f':
                        i += 1
                        if i < len(program) and program[i] in rd.delim3:
                            results.append(("leaf", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue
        elif i < len(program) and program[i] == 'm':
            i += 1
            if i < len(program) and program[i] == 'i':
                i += 1
                if i < len(program) and program[i] == 'n':
                    i += 1
                    if i < len(program) and program[i] == 't':
                        i += 1
                        if i < len(program) and program[i] in rd.delim3:
                            results.append(("mint", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue
            elif i < len(program) and program[i] == 'o':
                i += 1
                if i < len(program) and program[i] == 's':
                    i += 1
                    if i < len(program) and program[i] == 's':
                        i += 1
                        if i < len(program) and program[i] in rd.delim4:
                            results.append(("moss", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue
        elif i < len(program) and program[i] == 'p':
            i += 1
            if i < len(program) and program[i] == 'l':
                i += 1
                if i < len(program) and program[i] == 'a':
                    i += 1
                    if i < len(program) and program[i] == 'n':
                        i += 1
                        if i < len(program) and program[i] == 't':
                            i += 1
                            if i < len(program) and program[i] in rd.delim16:
                                results.append(("plant", "Reserved Word"))
                                i += 1
                                if i == len(program):
                                    return results
                                continue
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
                                    results.append(("regrow", "Reserved Word"))
                                    i += 1
                                    if i == len(program):
                                        return results
                                    continue
        elif i < len(program) and program[i] == 's':
            i += 1
            if i < len(program) and program[i] == 'e':
                i += 1
                if i < len(program) and program[i] == 'e':
                    i += 1
                    if i < len(program) and program[i] == 'd':
                        i += 1
                        if i < len(program) and program[i] in rd.delim16:
                            results.append(("seed", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue
            elif i < len(program) and program[i] == 't':
                i += 1
                if i < len(program) and program[i] == 'e':
                    i += 1
                    if i < len(program) and program[i] == 'm':
                        i += 1
                        if i < len(program) and program[i] in rd.delim4:
                            results.append(("stem", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue
                elif i < len(program) and program[i] == 'r':
                    i += 1
                    if i < len(program) and program[i] == 'i':
                        i += 1
                        if i < len(program) and program[i] == 'n':
                            i += 1
                            if i < len(program) and program[i] == 'g':
                                i += 1
                                if i < len(program) and program[i] in rd.delim4:
                                    results.append(("string", "Reserved Word"))
                                    i += 1
                                    if i == len(program):
                                        return results
                                    continue
        elif i < len(program) and program[i] == 't':
            i += 1
            if i < len(program) and program[i] == 'i':
                i += 1
                if i < len(program) and program[i] == 'n':
                    i += 1
                    if i < len(program) and program[i] == 't':
                        i += 1
                        if i < len(program) and program[i] in rd.delim4:
                            results.append(("tint", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue
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
                                                        ("transplant", "Reserved Word"))
                                                    i += 1
                                                    if i == len(program):
                                                        return results
                                                    continue
                elif i < len(program) and program[i] == 'u':
                    i += 1
                    if i < len(program) and program[i] == 'e':
                        i += 1
                        if i < len(program) and program[i] in rd.delim1:
                            results.append(("true", "Reserved Word"))
                            i += 1
                            if i == len(program):
                                return results
                            continue
            elif i < len(program) and program[i] == 'u':
                i += 1
                if i < len(program) and program[i] == 'l':
                    i += 1
                    if i < len(program) and program[i] == 'i':
                        i += 1
                        if i < len(program) and program[i] == 'p':
                            i += 1
                            if i < len(program) and program[i] in rd.delim4:
                                results.append(("tulip", "Reserved Word"))
                                i += 1
                                if i == len(program):
                                    return results
                                continue
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
                                if i < len(program) and program[i] in rd.delim3:
                                    results.append(("willow", "Reserved Word"))
                                    i += 1
                                    if i == len(program):
                                        return results
                                    continue
        elif i < len(program) and program[i] == '+':
            i += 1
            if i < len(program) and program[i] in rd.delim19:
                results.append(("+", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("+=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '-':
            i += 1
            if i < len(program) and program[i] in rd.delim5:
                results.append(("-", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("-=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
            elif i < len(program) and program[i] == '-':
                i += 1
                if i < len(program) and program[i] == '>':
                    i += 1
                    if i < len(program) and program[i] in rd.delim2:
                        results.append(("-->", "Reserved Symbol"))
                        i += 1
                        if i == len(program):
                            return results
                        continue
        elif i < len(program) and program[i] == '*':
            i += 1
            if i < len(program) and program[i] in rd.delim13:
                results.append(("*", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '*':
                i += 1
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("**", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("**=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("*=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '/':
            i += 1
            if i < len(program) and program[i] in rd.delim13:
                results.append(("/", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '/':
                i += 1
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("//", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
                elif i < len(program) and program[i] == '=':
                    i += 1
                    if i < len(program) and program[i] in rd.delim13:
                        results.append(("//=", "Reserved Symbol"))
                        i += 1
                        if i == len(program):
                            return results
                        continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("/=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '%':
            i += 1
            if i < len(program) and program[i] in rd.delim13:
                results.append(("%", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim13:
                    results.append(("%=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '&':
            i += 1
            if i < len(program) and program[i] in rd.delim5:
                results.append(("&", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("&=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '|':
            i += 1
            if i < len(program) and program[i] in rd.delim5:
                results.append(("|", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("|=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '>':
            i += 1
            if i < len(program) and program[i] in rd.delim5:
                results.append((">", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '>':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append((">>", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
                elif i < len(program) and program[i] == '=':
                    i += 1
                    if i < len(program) and program[i] in rd.delim5:
                        results.append((">>=", "Reserved Symbol"))
                        i += 1
                        if i == len(program):
                            return results
                        continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append((">=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '<':
            i += 1
            if i < len(program) and program[i] in rd.delim5:
                results.append(("<", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '<':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("<<", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
                elif i < len(program) and program[i] == '=':
                    i += 1
                    if i < len(program) and program[i] in rd.delim5:
                        results.append(("<<=", "Reserved Symbol"))
                        i += 1
                        if i == len(program):
                            return results
                        continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("<=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
            elif i < len(program) and program[i] == '-':
                i += 1
                if i < len(program) and program[i] == '-':
                    i += 1
                    if i < len(program) and program[i] in rd.delim14:
                        results.append(("<--", "Reserved Symbol"))
                        i += 1
                        if i == len(program):
                            return results
                        continue
        elif i < len(program) and program[i] == '^':
            i += 1
            if i < len(program) and program[i] in rd.delim5:
                results.append(("^", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("^=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '~':
            i += 1
            if i < len(program) and program[i] in rd.delim5:
                results.append(("~", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == '!':
            i += 1
            if i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim5:
                    results.append(("!=", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        elif i < len(program) and program[i] == '(':
            i += 1
            if i < len(program) and program[i] in rd.delim6:
                results.append(("(", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == '[':
            i += 1
            if i < len(program) and program[i] in rd.delim6:
                results.append(("[", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == '{':
            i += 1
            if i < len(program) and program[i] in rd.delim6:
                results.append(("{", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == ']':
            i += 1
            if i < len(program) and program[i] in rd.delim12:
                results.append(("]", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == '}':
            i += 1
            if i < len(program) and program[i] in rd.delim18:
                results.append(("}", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == ')':
            i += 1
            if i < len(program) and program[i] in rd.delim17:
                results.append((")", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == ',':
            i += 1
            if i < len(program) and program[i] in rd.delim7:
                results.append((",", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == ':':
            i += 1
            if i < len(program) and program[i] in rd.delim15:
                results.append((":", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == '.':
            i += 1
            if i < len(program) and program[i] in rd.delim8:
                results.append((".", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == ';':
            i += 1
            if i < len(program) and program[i] in rd.delim16:
                results.append((";", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
        elif i < len(program) and program[i] == '=':
            i += 1
            if i < len(program) and program[i] in rd.delim8:
                results.append(("=", "Reserved Symbol"))
                i += 1
                if i == len(program):
                    return results
                continue
            elif i < len(program) and program[i] == '=':
                i += 1
                if i < len(program) and program[i] in rd.delim8:
                    results.append(("==", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
            elif i < len(program) and program[i] == '!':
                i += 1
                if i < len(program) and program[i] in rd.delim8:
                    results.append(("=!", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
            elif i < len(program) and program[i] == '&':
                i += 1
                if i < len(program) and program[i] in rd.delim8:
                    results.append(("=&", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
            elif i < len(program) and program[i] == '/':
                i += 1
                if i < len(program) and program[i] in rd.delim8:
                    results.append(("=/", "Reserved Symbol"))
                    i += 1
                    if i == len(program):
                        return results
                    continue
        # Negative whole tint or flora
        elif i < len(program) and program[i] == '-':
            i += 1
            if i < len(program) and program[i] in [str(num) for num in range(1, 10)]:
                i += 1
                if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                    i += 1
                    if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                        i += 1
                        if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                            i += 1
                            if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                i += 1
                                if i < len(program) and program[i] == '.':
                                    i += 1
                                    if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                        i += 1
                                        if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                            i += 1
                                            if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                                i += 1
                                                if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                                    i += 1
                                                    if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                                        i += 1
                                                        if i < len(program) and program[i] in rd.delimtf:
                                                            results.append(
                                                                (program[:-i], "{type}lit"))
                                                            i += 1
                                                            if i == len(program):
                                                                return results
                                                            continue
                                                    elif i < len(program) and program[i] in rd.delimtf:
                                                        results.append(
                                                            program[:i])
                                                        i += 1
                                                        continue
                                                elif i < len(program) and program[i] in rd.delimtf:
                                                    results.append(program[:i])
                                                    i += 1
                                                    continue
                                            elif i < len(program) and program[i] in rd.delimtf:
                                                results.append(program[:i])
                                                i += 1
                                                continue
                                        elif i < len(program) and program[i] in rd.delimtf:
                                            results.append(program[:i])
                                            i += 1
                                            continue
                                elif i < len(program) and program[i] in rd.delimtf:
                                    results.append(program[:i])
                                    i += 1
                                    continue
                            elif i < len(program) and program[i] in rd.delimtf:
                                results.append(program[:i])
                                i += 1
                                continue
                        elif i < len(program) and program[i] in rd.delimtf:
                            results.append(program[:i])
                            i += 1
                            continue
                    elif i < len(program) and program[i] in rd.delimtf:
                        results.append(program[:i])
                        i += 1
                        continue
                elif i < len(program) and program[i] in rd.delimtf:
                    results.append(program[:i])
                    i += 1
                    continue
        # For tint and flora that has 0 as the whole number
        elif i < len(program) and program[i] == '0':
            i += 1
            if i < len(program) and program[i] == '.':
                i += 1
                if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                    i += 1
                    if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                        i += 1
                        if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                            i += 1
                            if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                i += 1
                                if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                    i += 1
                                    if i < len(program) and program[i] in rd.delimtf:
                                        results.append(program[:i])
                                        i += 1
                                        continue
                                elif i < len(program) and program[i] in rd.delimtf:
                                    results.append(program[:i])
                                    i += 1
                                    continue
                            elif i < len(program) and program[i] in rd.delimtf:
                                results.append(program[:i])
                                i += 1
                                continue
                        elif i < len(program) and program[i] in rd.delimtf:
                            results.append(program[:i])
                            i += 1
                            continue
                    elif i < len(program) and program[i] in rd.delimtf:
                        results.append(program[:i])
                        i += 1
                        continue
            elif i < len(program) and program[i] in rd.delimtf:
                results.append(program[:i])
                i += 1
                continue
        # Positive tint and flora
        elif i < len(program) and program[i] in [str(num) for num in range(1, 10)]:
            i += 1
            if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                i += 1
                if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                    i += 1
                    if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                        i += 1
                        if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                            i += 1
                            if i < len(program) and program[i] == '.':
                                i += 1
                                if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                    i += 1
                                    if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                        i += 1
                                        if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                            i += 1
                                            if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                                i += 1
                                                if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                                    i += 1
                                                    if i < len(program) and program[i] in rd.delimtf:
                                                        results.append(
                                                            program[:i])
                                                        i += 1
                                                        continue
                                                elif i < len(program) and program[i] in rd.delimtf:
                                                    results.append(program[:i])
                                                    i += 1
                                                    continue
                                            elif i < len(program) and program[i] in rd.delimtf:
                                                results.append(program[:i])
                                                i += 1
                                                continue
                                        elif i < len(program) and program[i] in rd.delimtf:
                                            results.append(program[:i])
                                            i += 1
                                            continue
                                    elif i < len(program) and program[i] in rd.delimtf:
                                        results.append(program[:i])
                                        i += 1
                                        continue
                            elif i < len(program) and program[i] in rd.delimtf:
                                results.append(program[:i])
                                i += 1
                                continue
                        elif i < len(program) and program[i] in rd.delimtf:
                            results.append(program[:i])
                            i += 1
                            continue
                    elif i < len(program) and program[i] in rd.delimtf:
                        results.append(program[:i])
                        i += 1
                        continue
                elif i < len(program) and program[i] in rd.delimtf:
                    results.append(program[:i])
                    i += 1
                    continue
            elif i < len(program) and program[i] in rd.delimtf:
                results.append(program[:i])
                i += 1
                continue
        # Negative tint and flora that has 0 as the whole number
        elif i < len(program) and program[i] == '-':
            i += 1
            if i < len(program) and program[i] == '0':
                i += 1
                if i < len(program) and program[i] == '.':
                    i += 1
                    if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                        i += 1
                        if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                            i += 1
                            if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                i += 1
                                if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                    i += 1
                                    if i < len(program) and program[i] in [str(num) for num in range(0, 10)]:
                                        i += 1
                                        if i < len(program) and program[i] in rd.delimtf:
                                            results.append(program[:i])
                                            i += 1
                                            continue
                                    elif i < len(program) and program[i] in rd.delimtf:
                                        results.append(program[:i])
                                        i += 1
                                        continue
                                elif i < len(program) and program[i] in rd.delimtf:
                                    results.append(program[:i])
                                    i += 1
                                    continue
                            elif i < len(program) and program[i] in rd.delimtf:
                                results.append(program[:i])
                                i += 1
                                continue
                        elif i < len(program) and program[i] in rd.delimtf:
                            results.append(program[:i])
                            i += 1
                            continue
                elif i < len(program) and program[i] in rd.delimtf:
                    results.append(program[:i])
                    i += 1
                    continue
        elif i < len(program) and program[i] == '#':
            i += 1
            if i < len(program) and program[i] in [chr(asc) for asc in range(65, 91)] + [chr(asc) for asc in range(97, 123)]:
                i += 1
                if i < len(program) and program[i] in [chr(asc) for asc in range(48, 58)] + [chr(asc) for asc in range(65, 91)] + [chr(asc) for asc in range(97, 123)]:
                    i += 1
                    if i < len(program) and program[i] in [chr(asc) for asc in range(48, 58)] + [chr(asc) for asc in range(65, 91)] + [chr(asc) for asc in range(97, 123)]:
                        i += 1
                        if i < len(program) and program[i] in [chr(asc) for asc in range(48, 58)] + [chr(asc) for asc in range(65, 91)] + [chr(asc) for asc in range(97, 123)]:
                            i += 1
                            if i < len(program) and program[i] in [chr(asc) for asc in range(48, 58)] + [chr(asc) for asc in range(65, 91)] + [chr(asc) for asc in range(97, 123)]:
                                i += 1
                                if i < len(program) and program[i] in [chr(asc) for asc in range(48, 58)] + [chr(asc) for asc in range(65, 91)] + [chr(asc) for asc in range(97, 123)]:
                                    i += 1
                                    if i < len(program) and program[i] in [chr(asc) for asc in range(48, 58)] + [chr(asc) for asc in range(65, 91)] + [chr(asc) for asc in range(97, 123)]:
                                        i += 1
                                        if i < len(program) and program[i] in rd.delimi:
                                            results.append(program[:i])
                                            i += 1
                                            continue
                                    elif i < len(program) and program[i] in rd.delimi:
                                        results.append(program[:i])
                                        i += 1
                                        continue
                                elif i < len(program) and program[i] in rd.delimi:
                                    results.append(program[:i])
                                    i += 1
                                    continue
                            elif i < len(program) and program[i] in rd.delimi:
                                results.append(program[:i])
                                i += 1
                                continue
                        elif i < len(program) and program[i] in rd.delimi:
                            results.append(program[:i])
                            i += 1
                            continue
                    elif i < len(program) and program[i] in rd.delimi:
                        results.append(program[:i])
                        i += 1
                        continue
                elif i < len(program) and program[i] in rd.delimi:
                    results.append(program[:i])
                    i += 1
                    continue
        elif i < len(program) and program[i] == '"':
            i += 1
            if i < len(program) and program[i] in list(map(chr, range(128))):
                i += 1
                while i < len(program):
                    if i < len(program) and program[i] in list(map(chr, range(128))):
                        i += 1
                        if i < len(program) and program[i] in rd.delims:
                            results.append(program[:i])
                            i += 1
                            continue
                    elif i < len(program) and program[i] in rd.delims:
                        results.append(program[:i])
                        i += 1
                        continue
    return results


def ignore_comment(program):
    cleaned_text = remove_pattern(program, '<--', '-->')

    return cleaned_text


def remove_pattern(text, start_pattern, end_pattern):
    while True:
        start_index = text.find(start_pattern)
        end_index = text.find(end_pattern, start_index + len(start_pattern))

        if start_index != -1 and end_index != -1:
            text = text[:start_index] + text[end_index + len(end_pattern):]
        else:
            break

    return text


def error_check(prog):
    pass
