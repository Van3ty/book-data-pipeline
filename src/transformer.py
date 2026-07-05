import re

class DataTransformer:

    def transform_books(self, data):
        clean_books = []
        for book in data:
            clean_book = {}
            clean_book['price'] = float(re.sub(r'[^\d.]', '', book['price']))
            clean_book['availability'] = "In stock" in book['availability']
            clean_books.append(clean_book)
        return clean_books