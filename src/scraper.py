import requests
from bs4 import BeautifulSoup


class BookScraper:
    

    def __init__(self):
        self.base_url = "https://books.toscrape.com/" 
        self.all_books = []

    def fetch_page(self, url=None):
        if url is None:
            url = self.base_url

        response = requests.get(url)
        if response.status_code == 200:
            return response
        
        raise Exception(f"Failed to fetch page: {response.status_code}")

    def parse_page(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        books = []
        for article in soup.select('.product_pod'):
            title = article.h3.a['title']
            price = article.select_one('.price_color').text
            availability = article.select_one('.availability').text.strip()
            books.append({
                'title': title,
                'price': price,
                'availability': availability
            })
        return books
    

    def scrape_all_books(self):
        for page in range(1, 51): 
            url = f"{self.base_url}catalogue/page-{page}.html"
            response = self.fetch_page(url)
            books = self.parse_page(response)
            self.all_books.extend(books)
        return self.all_books
        
    

