import csv
import json


class BookExporter:

    def export_csv(self, books, file_path):
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            
            writer.writerow(["Title", "Price", "Availability"])

            
            for book in books:
                writer.writerow([
                    book["title"],
                    book["price"],
                    book["availability"]
                ])

    def export_json(self, books, file_path):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(books, file, indent=4)