
# Position object to keep track of the current position in the source code.
class Position:
    # Constructor
    # Initialize the object with index, column, and line number.
    def __init__(self, index:int, line:int, col:int, file_name:str, file_contents:str) -> None:
        self.index = index
        self.col = col
        self.line = line
        self.file_name = file_name
        self.file_contents = file_contents
    
    # advance function
    # Adds 1 to the index and column. May move to the next line if current_char is a newline.
    def advance(self, current_char:str) -> 'Position':
        self.index += 1
        self.col += 1

        if current_char == '\n':
            self.col = 0
            self.line += 1
        
        return self
    
    # copy function
    # Returns a new Position object with the same index, column, and line number.
    def copy(self) -> 'Position':
        return Position(self.index, self.col, self.line, self.file_name, self.file_contents)