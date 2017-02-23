import re
user_input = "function SquareDistance(x1, y1, x2, y2) { return x1 ^ x2 + y1 ^ y2 } var distance = SquareDistance(2, 3, 5, 6)"
output = ""

base = ["=", "+", "-", "*", "/", "^", "(", ")", "{", "}", ",", ":"]

known = {"var": "VAR", "print": "PRINT", "=": "ASSIGN", "return": "RETURN",
        "function": "FUNCTION", "+": "ADD", "-": "SUB", "*": "MULT", "/": "DIV",
        "^": "EXP", "(": "LPAREN", ")": "RPAREN", "{": "LBRACE", "}": "RBRACE",
        ",": "COMMA", ":": "COLON"}

knownToIgnore = ["VAR", "PRINT","ASSIGN", "RETURN", "FUNCTION", "ADD", "SUB",
                 "MULT", "DIV", "EXP", "LPAREN", "RPAREN", "LBRACE", "RBRACE",
                 "COMMA", "COLON"]

NUMBER = re.compile("[+-]?((\d+(\.\d*)?)|(\.\d+))")
IDENT = re.compile("[a-zA-Z]+[a-zA-Z0-9_]*")

user_input = user_input.split()
#print user_input
output = ""
newoutput = ""

for word in user_input:
    #print word
    if word in known:
        output += known[word]
        output += " "
    else:
        for char in word:
            if char in known:
                output += " "
                output += known[char]
                output += " "
            else:
                output += char
        output += " "

newoutput = output.split()

finaloutput = ""

for term in newoutput:
    if term not in knownToIgnore:
        num = re.search(NUMBER, term)
        ident = re.search(IDENT, term)
        if ident:
            finaloutput += "IDENT: "
            finaloutput += term
            finaloutput += "\n"
        elif num:
            finaloutput += "NUMBER: "
            finaloutput += term
            finaloutput += "\n"
        else:
            print "WTF"
    else:
        finaloutput += term
        finaloutput += "\n"

print finaloutput
# for indexofChar in range(len(output)):
#     num = re.search(NUMBER, output[indexofChar])
#     ident = re.search(IDENT, output[indexofChar])
#     if output[indexofChar] in base:
#         newoutput += known[output[indexofChar]]
#         #newoutput += "\n"
#     elif num:
#         newoutput += "NUMBER "
#         newoutput += output[indexofChar]
#         #newoutput += "\n"
#     elif ident:
#         newoutput += " IDENT "
#         newoutput += output[indexofChar]
#         #newoutput += "\n"
#     else:
#         newoutput += output[indexofChar]
#         #newoutput += "\n"
#
# #print newoutput




#
# import sys
#
# #for the lexer
# lexemes = []
#
# unvariedLexemes = ["var", "function", "(", "(", "+"];
#
# def SplitSourceByWhitespace(source):
#     allSplits = []
#     for line in source:
#         thisSplit = line.split()
#         #for line.split():
#         allSplits += thisSplit
#     #print(allSplits)
#     return allSplits
#
#
# def SplitByUnvariedLexemes(source):
#     i=0
#     allSplits = []
#     while i< len(source):
#         line = source[i]
#         unvariedLexemeFound = False;
#         for lexeme in unvariedLexemes:
#
#             if(-1 != line.find(lexeme)):
#                 unvariedLexemeFound = True;
#                 split = line.split(lexeme)
#                 allSplits += split
#             if not unvariedLexemeFound:
#                 allSplits += line
#         i += 1
#     print(allSplits)
#     return allSplits
#
#
# def ReadInput():
#     lines = sys.stdin.readlines()
#     for line in lines:
#         print("echo: "+line)
#
#
#
# if __name__ == '__main__':
#     print ("starting __main__")
#     SplitByUnvariedLexemes(SplitSourceByWhitespace(sys.stdin.readlines()))