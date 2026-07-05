improt sqlite3

class DatabaseManager:
    
    def __init__(self):
        self.connection = None
        self.cursor = None