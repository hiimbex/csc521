# csc521
My projects for Design and Organization of Programming Languages, including lexer, parser, and interpreter 

My implementations of the lexer, parser and interpretter can be found in the file python-quirk. 

Each is best ran individually given the requirements for the project indicate the lexer's output should contain each lexeme seperated by a new line in between, while as the parser takes a list as its input. Each takes input based on a variable at the top of the file which can easily be changed. The varibles are respectively `user_input`, `tokens`, and `tree`.

The lexer is based off my own implementation and does not use the class's base code. It's main feature is taking advantage of python's ability to split strings based on white space by originally adding spaces to the string before or after key words so as to seperate them from being ID'd as IDENTS later on by the lexer. There is one edge case surrounding the `RETURN` lexeme, caused by it being the only "word" token (var, print, return, function) that could have another token touching it (ie `function x(y){return y}` where the LBRACE touches return).

The parser is based off of the class's base code and further implements all of the fucntions. The parser is run beginning at `Program` and going down the tree from there. It's main features is its recrusive left decent nature by checking all possibilites. The functions each represent a level of the tree to be checked and are conveniently ordered by priority with `Program` and `Statement` at the top and `Number` and `Name` at the bottom.

The interpretter is also based off the class code and uses a scope stack to navigate the tree structure returned from the parser.
