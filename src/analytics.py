class DataAnalyzer:
    

    def __init__(self, book_data):
        self.book_data = book_data

    def average_price(self):
        if not self.book_data:
            return 0.0
        total_price = sum(book['price'] for book in self.book_data)
        return total_price / len(self.book_data)
    
    def availability_count(self):
        available_count = sum(1 for book in self.book_data if book['availability'])
        unavailable_count = len(self.book_data) - available_count
        return {
            'available': available_count,
            'unavailable': unavailable_count
        }
    
    def most_expensive_book(self):
        if not self.book_data:
            return None
        return max(self.book_data, key=lambda book: book['price'])
    
    def least_expensive_book(self):
        if not self.book_data:
            return None
        return min(self.book_data, key=lambda book: book['price'])
    
    