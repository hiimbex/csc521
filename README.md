# CSC521 Design and Organization of Programming Languages
My projects for CSC-521, including lexer, parser, and interpreter

My implementations of the lexer, parser and interpreter can be found in the file python-quirk.

Simply run all 3 files separately via `python lexer.py < example1.q` with the lexer.py being replaced by parser.py and interpreter.py as well as the file name to test different examples.

The lexer is based off my own implementation and does not use the class's base code. It's main feature is taking advantage of python's ability to split strings based on white space by originally adding spaces to the string before or after key words so as to separate them from being ID'd as IDENTS later on by the lexer. There is one edge case surrounding the `RETURN` lexeme, caused by it being the only "word" token (var, print, return, function) that could have another token touching it (ie `function x(y){return y}` where the LBRACE touches return).

The parser is based off of the class's base code and further implements all of the functions. The parser is run beginning at `Program` and going down the tree from there. It's main features is its recursive left decent nature by checking all possibilities. The functions each represent a level of the tree to be checked and are conveniently ordered by priority with `Program` and `Statement` at the top and `Number` and `Name` at the bottom.

The interpreter is also based off the class code and uses a scope stack to navigate the tree structure returned from the parser. It navigates the tree and stores data for variables from assignment and functions during their declaration in the scope. It decides where to travel based on the name found and calls `func_by_name` based off that.
