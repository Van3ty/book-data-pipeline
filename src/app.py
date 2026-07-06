from src.scraper import BookScraper
from src.database import DatabaseManager
from src.transformer import DataTransformer
from src.analytics import DataAnalyzer

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

    # Run analysis on the cleaned data
    analyzer = DataAnalyzer(clean_books)

    print("\n--- Book Data Analysis ---")
    print(f"Average price: £{analyzer.average_price():.2f}")

    availability = analyzer.availability_count()
    print(f"Available: {availability['available']}, Unavailable: {availability['unavailable']}")

    most_expensive = analyzer.most_expensive_book()
    print(f"Most expensive: {most_expensive['title']} (£{most_expensive['price']:.2f})")

    least_expensive = analyzer.least_expensive_book()
    print(f"Least expensive: {least_expensive['title']} (£{least_expensive['price']:.2f})")


if __name__ == "__main__":
    main()