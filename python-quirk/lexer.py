import re, sys, os, pickle

user_input = "function SquareDistance(x1, y1, x2, y2){return x1^x2 + y1 ^ y2, 86 }  var distance = SquareDistance(2, 3, 5, 6):1 print oldsum/hello+8"

user_input = "print 1 + 4 - 3"
user_input = "var x = (5 * 2) / 5 print x"
user_input = "function foo_func(){ return 2 ^ 8 } print foo_func()"
user_input = "function baz_func(a,b){ var y = a - + b var z = a - - b return y,z } var v,w = baz_func(-5, +2) print v print w"
user_input = "function cloud_func(a){ return a, a^2, a^3 } print cloud_func(2):1"
user_input = "print (5*9)"

#user_input = "var y = 7 print 8-y"

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
        finaloutput += " "
    elif term not in knownToIgnore:
        num = re.search(NUMBER, term)
        ident = re.search(IDENT, term)
        if ident:
            finaloutput += "IDENT:"
            finaloutput += term
            finaloutput += " "
        elif num:
            finaloutput += "NUMBER:"
            finaloutput += term
            finaloutput += " "
    else:
        finaloutput += term
        finaloutput += " "

print finaloutput

os.system("python parser.py {0}".format(finaloutput))
