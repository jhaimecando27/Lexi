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


class Error(object):
    def delim(i, tmp_wrd, delim, delims):
        return (str(i + 1) + ": " + "\"" + tmp_wrd + esc(delim) + "\": Unknown Delimeter \"" + esc(delim) + "\": Available " + str(delims), "UNKNOWN DELIMITER")

    def id(i, tmp_wrd):
        return (str(i + 1) + ": " + "\"" + tmp_wrd + "\": Unknown Identifier missing \"#\" symbol", "UNKNOWN IDENTIFIER")
