import sqlite3

class DatabaseManager:
    
    def __init__(self):
        self.connection = sqlite3.connect('books.db')
        self.cursor = self.connection.cursor()
        
    
    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT,
                price REAL,
                availability BOOLEAN
            )
        ''')
        self.connection.commit()
    
    def insert_books(self, books):
        for book in books:
            self.cursor.execute('''
                INSERT INTO books (title, price, availability)
                VALUES (?, ?, ?)
            ''', (book['title'], book['price'], book['availability']))
        self.connection.commit()

    def get_books(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()