# 📚 Book Data Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline built with Python.

The application scrapes book data from a public website, transforms and validates the collected data, stores it in a SQLite database, performs analytics, and exports the processed dataset to CSV and JSON formats.

---

## Features

- 🌐 Scrapes 1000+ books from BooksToScrape.com
- 🧹 Cleans and transforms scraped data
- 🗄️ Stores processed data in SQLite
- 📊 Performs basic analytics on the dataset
- 📁 Exports data to CSV and JSON
- 🧱 Modular architecture following OOP principles

---

## Technologies

- Python 3
- Requests
- BeautifulSoup4
- SQLite3
- JSON
- CSV
- Regular Expressions (re)

---

## Project Structure

```
book-data-pipeline/
│
├── app.py                 # Runs the complete ETL pipeline
│
├── src/
│   ├── scraper.py         # Extract stage
│   ├── transformer.py     # Transform stage
│   ├── database.py        # Load stage
│   ├── analytics.py       # Data analysis
│   └── exporter.py        # CSV / JSON export
│
├── exports/
│   ├── books.csv
│   └── books.json
│
├── books.db
├── requirements.txt
└── README.md
```

---

## ETL Pipeline

```
Website
   │
   ▼
BookScraper
   │
   ▼
Raw Book Data
   │
   ▼
DataTransformer
   │
   ▼
Clean Book Data
   │
   ▼
DatabaseManager
   │
   ▼
SQLite Database
   │
   ├────────► BookAnalytics
   │
   └────────► BookExporter
                    │
                    ▼
             CSV / JSON Files
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/Van3ty/book-data-pipeline.git
cd book-data-pipeline
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

Run the ETL pipeline

```bash
python app.py
```

Run analytics

```bash
python analytics.py
```

Export data

```bash
python exporter.py
```

---

## Example Output

```
=== Book Data Pipeline ===

Scraping book data...
✓ 1000 books scraped

Transforming data...
✓ Data cleaned

Saving to SQLite...
✓ 1000 books inserted

Running analytics...
✓ Complete

Exporting data...
✓ books.csv created
✓ books.json created

Pipeline completed successfully.
```

---

## What I Learned

During this project I practiced:

- Object-Oriented Programming
- Software Architecture
- ETL Pipeline Design
- Web Scraping
- SQLite Databases
- SQL
- Data Cleaning
- Python Modules
- Exception Handling
- Git & GitHub
- Working with JSON and CSV files

---

## Future Improvements

- Logging
- Unit tests
- Configuration file
- PostgreSQL support
- Docker support
- Scheduled pipeline execution
- REST API integration

---

## Author

Ivan Iliev Gochev

GitHub:
https://github.com/Van3ty