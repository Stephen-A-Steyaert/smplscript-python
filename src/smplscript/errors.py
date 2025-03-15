from .position import Position

# Error object is the base class for future errors
class Error:
    # Constructor
    # Initialize the object with an error name and details
    def __init__(self, error_name:str, pos_start:Position, pos_end:Position, details:str) -> None:
        self.error_name = error_name
        self.details = details
        self.pos_start = pos_start
        self.pos_end = pos_end
    
    # as_string() function:
    # Returns the error name and details as a string
    def as_string(self):
        error_str = f'{self.error_name}: {self.details}'
        error_str += f'\nFile {self.pos_start.file_name}, Line {self.pos_start.line + 1}'
        return error_str
    
class IllegalCharError(Error):
    # Constructor
    # Initialize the object with the "Illegal Character" error name and the inputted
    # details
    def __init__(self, pos_start:Position, pos_end:Position, details:str) -> None:
        super().__init__('Illegal Character', pos_start, pos_end, details)