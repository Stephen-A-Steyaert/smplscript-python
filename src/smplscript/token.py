""""
" Token object, will be used in the Lexer to represent pieces of the code, and will
" be used in the Parser to represent the abrstract syntax tree.
"""

class Token:
    # Constructor
    # Initialize the object with a type and a value (if any)
    def __init__(self, type:str, value=str|float|int|None) -> None:
        self.type = type
        self.value = value
    
    # __repr__ function:
    # Return the type and value (if any) of the token
    def __repr__(self) -> str:
        return f'{self.type}:{self.value}' if self.value else f'{self.type}'