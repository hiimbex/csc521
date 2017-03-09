import re

user_input = "function SquareDistance(x1, y1, x2, y2){return x1^x2 + y1 ^ y2 } var distance = SquareDistance(2, 3, 5, 6) result = oldsum - value / 100 print result"

base = ["=", "+", "-", "*", "/", "^", "(", ")", "{", "}", ",", ":"]

known = {"var": "VAR", "print": "PRINT", "=": "ASSIGN", "return": "RETURN",
         "function": "FUNCTION", "+": "ADD", "-": "SUB", "*": "MULT", "/":
         "DIV", "^": "EXP", "(": "LPAREN", ")": "RPAREN", "{": "LBRACE", "}":
         "RBRACE", ",": "COMMA", ":": "COLON"}

knownToIgnore = ["VAR", "PRINT", "ASSIGN", "RETURN", "FUNCTION", "ADD", "SUB",
                 "MULT", "DIV", "EXP", "LPAREN", "RPAREN", "LBRACE", "RBRACE",
                 "COMMA", "COLON"]

NUMBER = re.compile("[+-]?((\d+(\.\d*)?)|(\.\d+))")
IDENT = re.compile("[a-zA-Z]+[a-zA-Z0-9_]*")

user_input = user_input.split()
output = ""

'''
    Checks if every word is a key word, if it is replace it with the
    knownToIgnore version. If a word is not a key word,
    it checks every chacter, searching for values in the base list,
    changing it to the knownToIgnore version as well.
'''
for word in user_input:
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

output = output.split()

finaloutput = ""

'''
    Now that we know every (almost!) key word will be in knownToIgnore,
    we can go through and check for idents and numbers.
'''

for term in output:
    # return has an edge case, so this is a final check
    if term == "return":
        finaloutput += "RETURN"
        finaloutput += "\n"
    elif term not in knownToIgnore:
        num = re.search(NUMBER, term)
        ident = re.search(IDENT, term)
        if ident:
            finaloutput += "IDENT:"
            finaloutput += term
            finaloutput += "\n"
        elif num:
            finaloutput += "NUMBER:"
            finaloutput += term
            finaloutput += "\n"
    else:
        finaloutput += term
        finaloutput += "\n"

print finaloutput
