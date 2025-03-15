from .lexer import Lexer
from .token import Token 
from .errors import IllegalCharError

def run(file_name:str, text: str) -> tuple[list[Token], IllegalCharError|None]:
    lexer = Lexer(file_name, text)
    result, error = lexer.generate_tokens()

    return result, error