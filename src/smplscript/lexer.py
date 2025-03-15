from . import constants
from .errors import IllegalCharError
from .position import Position
from .token import Token

# Lexer object will be use to tokenize input code.
class Lexer:
    # Constructor
    # Initializes the text field to the input text, sents the current positiion to 
    # -1, advances to the next character in the text
    def __init__(self, file_name:str, text: str) -> None:
        self.text = text
        self.pos = Position(-1, -1, 0, file_name, text)
        self.current_char = None
        self.advance()
    
    # advance() function:
    # Increments the current position, checks if the current position is less than the 
    # length of the text, if it is, sets the current character to the character at the 
    # current position in the text
    def advance(self) -> None:
        self.pos.advance()
        self.current_char = self.text[self.pos.index] if self.pos.index < len(self.text) else None
    
    # make_number() function:
    # Creates a number from the current character in the text, advances to the next 
    # character, repeats until the current character is not a digit or a period, then 
    # returns the Token with the corresponding type and value
    def make_number(self) -> Token:
        num_str = ''
        dot_count = 0

        while self.current_char is not None and self.current_char \
            in constants.DIGITS + '.':
                if self.current_char == '.':
                    if dot_count == 1: break
                    dot_count+=1
                    num_str += '.'
                else:
                    num_str += self.current_char
                self.advance()
        if dot_count:
            return Token(constants.TT_FLOAT, float(num_str))
        return Token(constants.TT_INT, int(num_str))

    # generate_tokens() function:
    # Generates tokens from the text, returns a vector of tokens or an error if an 
    # illegal character is found
    def generate_tokens(self) -> tuple[list[Token], IllegalCharError|None]:
        tokens:list[Token] = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char in constants.DIGITS:
                self.make_number()
            elif self.current_char == '+':
                tokens.append(Token(constants.TT_PLUS))
                self.advance()
            elif self.current_char == '-':
                tokens.append(Token(constants.TT_MINUS))
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(constants.TT_MUL))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(constants.TT_DIV))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(constants.TT_LPAREN))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(constants.TT_RPAREN))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, f"'{char}'")

        return tokens, None