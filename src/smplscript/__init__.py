from .lexer import Lexer
from .token import Token 
from .errors import IllegalCharError

def run(text: str) -> tuple[list[Token], IllegalCharError|None]:
    lexer = Lexer(text)
    result, error = lexer.generate_tokens()

    return result, error