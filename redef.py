
# Regular Definitions:
zero = "0"
dig = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
let = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
       "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G",
       "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
       "S", "T", "U", "V", "W", "X", "Y", "Z"]
num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
newline = ["\n"]
diglet = dig + let
ht = ["#"]
space = [" "]
tab = "\t"
invalid = "`@$?"
ascii = [
    "\x00", "\x01", "\x02", "\x03", "\x04", "\x05", "\x06", "\x07",
    "\x08", "\t", "\n", "\x0b", "\x0c", "\r", "\x0e", "\x0f", "\x10",
    "\x11", "\x12", "\x13", "\x14", "\x15", "\x16", "\x17", "\x18",
    "\x19", "\x1a", "\x1b", "\x1c", "\x1d", "\x1e", "\x1f", " ", "!",
    "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".",
    "/", ":", ";", "<", "=", ">", "?", "@", "A", "B", "C", "D", "E", "F",
    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "[", "\\", "]", "^", "_", "`", "a", "b",
    "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p",
    "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "{", "|", "}", "~",
    "\x7f"
]


# Delimiters
delimi = space + ["=", ";"]
delimtf = space + ["+", "-", "*", "/", "%",
           ";", ")", "]", "}", "<", ">", "!", "=",]
delims = ["\"",]
delimc = ["'"]
delimb = space + ["=", "<", ">", "!", ";"]
delim1 = [";", " "]
delim2 = ["\n", ' ']
delim3 = [' ', "("]
delim4 = [" "]
delim5 = num + space + ht + ["(", "["]
delim6 = [
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d",
    "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
    "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F",
    "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
    "S", "T", "U", "V", "W", "X", "Y", "Z", ' ', "\"", "\n", "#", "(", "[",
    "{", ")"
]
delim7 = dig + space + ht + ["\""]
delim8 = num + ht + space + ["\""]
delim9 = space + newline
delim10 = [";", ' ',  "\n", ","]
delim11 = [";", "+", " ", ",", ")", "}", "]"]
delim12 = ["=", ";", ")", "}"]
delim13 = dig + space + ht + ["("]
delim14 = ascii
delim15 = space + dig + let + newline + ["\""]
delim16 = ["\n", " "]
delim17 = ["=", "-", "/", "*", "+", "]", ")", "}", ",", ";"]
delim18 = [";", ",", "]", "),", "}"]
delim19 = num + space, ht + ["("]
delim20 = let
delim21 = [":"]
delim22 = num + [" ", "(", "#"]
delim23 = space + newline + ["\""]
delim24 = ["("]
delim25 = space + [")", ","]
delim26 = space + [")"]
delim27 = space + num + ht + [",", "_", "["]
delim28 = let


# Reserved Words
SEED = "seed"  # Start
PLANT = "plant"  # End
# Data Types
TINT = "tint"
FLORA = "flora"
STRING = "string"
BLOOM = "bloom"
FLORIST = "florist"
TULIP = "tulip"
DIRT = "dirt"
STEM = "stem"
# Input and Output Statements
INPETAL = "inpetal"
MINT = "mint"
# Conditional Statements
LEAF = "leaf"
MOSS = "moss"
ELEAF = "eleaf"
TRUE = "true"
FALSE = "false"
BREAK = "break"
# Iterative Statements
Fern = "fern"
Willow = "willow"
# Others
TRANSPLANT = "transplant"
REGROW = "regrow"
LANTANA = "lantana"
CLEAR = "clear"
BARE = "bare"
FLORAL = "floral"
GARDEN = "garden"


# Reserved Symbols
Arithmetic_Operators = ["+", "-", "*", "/", "%", "**", "//"]
Assignment_Operators = ["=", "+=", "-=", "*=", "/=",
                        "%=", "//=", "**=", "&=", "|=", "^=", ">>=", "<<="]
Comparison_Operators = ["==", "!=", ">", "<", ">=", "<="]
Logical_Operators = ["=&", "=/", "=!"]
Bitwise_Operators = ["&", "|", "^", "~", "<<", ">>"]
Others = ["()", "[]", "{}", "“", ",", ":", ".", ";", "#", "<--", "-->"]
