# escape char to string
def esc(s):
    if s == "\n":
        return "\\n"
    elif s == "\t":
        return "\\t"
    elif s == " ":
        return "<space>"
    else:
        return s


# skip remaining characters
def skip(i, program):
    single_symbols = [" ", "\n", "\t", ";", ",", "(", ")", "#"]
    while i < len(program) and program[i] not in single_symbols:
        i += 1
    return i


def skipV1(i, program, tmp_wrd):
    single_symbols = [" ", "\n", "\t", ";", ",", "(", ")", "#"]
    while i < len(program) and program[i] not in single_symbols:
        tmp_wrd += program[i]
        i += 1
    return i, tmp_wrd


class Errors():
    @staticmethod
    def delim(i, tmp_wrd, delim, delims):
        return (
                str(i + 1) + ": " + \
                "\"" + tmp_wrd + esc(delim) + \
                "\": Invalid token \"" + esc(delim) + \
                "\". Expecting Delimeter after \"" + \
                tmp_wrd + "\": Available " + \
                str(delims), "UNKNOWN DELIMITER"
                )

    @staticmethod
    def Id(i, tmp_wrd):
        return (
                str(i + 1) + ": " + \
                "\"" + tmp_wrd + \
                "\": Invalid token. Expecting \"#\" symbol after " + \
                tmp_wrd, "UNKNOWN IDENTIFIER"
                )

    @staticmethod
    def Int(i, tmp_wrd):
        return (
            str(i + 1) + ": " + \
            "\"" + tmp_wrd + \
            "\": Invalid range. "+ \
            "-999999 or 999999", "INVALID RANGE"
            )

    @staticmethod
    def Float(i, tmp_wrd):
        return (
            str(i + 1) + ": " + \
            "\"" + tmp_wrd + \
            "\": Invalid range. " + \
            "-999999.999999 or 999999.999999", "INVALID RANGE"
            )
