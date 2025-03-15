# Error object is the base class for future errors
class Error:
    # Constructor
    # Initialize the object with an error name and details
    def __init__(self, error_name:str, details:str) -> None:
        self.error_name = error_name
        self.details = details
    
    # as_string() function:
    # Returns the error name and details as a string
    def as_string(self):
        return f'{self.error_name}: {self.details}'
    
class IllegalCharError(Error):
    # Constructor
    # Initialize the object with the "Illegal Character" error name and the inputted
    # details
    def __init__(self, details:str) -> None:
        super().__init__('Illegal Character', details)