from src.scraper import BookScraper
from src.database import DatabaseManager
from src.transformer import DataTransformer

def main():
    print("Book Data Pipeline")

    
    scraper = BookScraper()
    db = DatabaseManager()
    transformer = DataTransformer()
    

    db.create_table()

    print("Scraping book data...")
    raw_books = scraper.scrape_all_books()

    print("Transforming book data...")
    clean_books = transformer.transform_books(raw_books)

    print("Inserting book data into the database...")
    db.insert_books(clean_books)

    print(f"Pipeline completed. Inserted {len(clean_books)} books into the database.")


if __name__ == "__main__":
    main()

    