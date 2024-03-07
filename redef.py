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
id = let + num + ["_", "-"]
ht = ["#"]
space = [" "]
tab = "\t"
invalid = "`@$?"
ascii = [chr(i) for i in range(128)]


# Delimiters
delimi = space + ["=", ";", ")", "(", ","]
delimtf = newline + space + ["+", "-", "*", "/", "%",
                   ";", ")", "]", "}", "<", ">", "!", "=", ",", ":"]
delims = ["\"",]
delimc = ["'"]
delimb = space + ["=", "<", ">", "!", ";", "]", ")"]
delim1 = [";", " "]
delim2 = ["\n", ' ']
delim3 = [' ', "("]
delim4 = [" "]
delim5 = num + space + ht + ["(", "["]
delim6 = let + num + space + newline + ht + \
    ["(", "[", "{", "\"", "\'", ")", "]"]
delim7 = newline + dig + space + ht + ["\"", "\'", "(", "[", "{"]
delim8 = let + num + ht + space + ["\"", "["]
delim9 = space + newline
delim10 = [";", ' ',  "\n", ","]
delim11 = [";", "+", " ", ",", ")", "}", "]"]
delim12 = space + ["=", ";", ")", "}"]
delim13 = dig + space + ["("]
delim14 = ascii
delim15 = space + dig + let + newline + ["\"", ")", "]"]
delim16 = let + ht + ["\n", " ", ")"]
delim17 = newline + space + ["=", "-", "/", "*", "+", "]",
                             ")", "}", ",", ";", "\'", "(", "."]
delim18 = [";", ",", "]", "),", "}", "."]
delim19 = num + space + ht + ["("]
delim20 = let
delim21 = space + [":", "("]
delim22 = num + [" ", "(", "#"]
delim23 = space + newline + ["\"", "}", "("] + dig
delim24 = space + ["("]
delim25 = newline + space + [")", ","]
delim26 = newline + space + [")"]
delim27 = space + num + ht + [",", "_", "[", ")", ":"]
delim28 = let + ht


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
