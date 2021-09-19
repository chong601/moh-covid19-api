import csv
from .constants import *


def check_csv_file_support(filename: str, repository_name: str):
    with open(filename, newline='', encoding='utf8') as file:
        csv_dialect = csv.Sniffer().sniff(file.read(1048576))
        file.seek(0)
        csv_reader = csv.DictReader(file, dialect=csv_dialect)
        # This is so cursed I don't know where to start.
        if repository_name in SUPPORTED_CSV_DATA:
            return hash_column_data(csv_reader.fieldnames) in SUPPORTED_CSV_DATA[repository_name]
        return None


def parse_csv(filename: str):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for index, csv_row in enumerate(csv_data, 1):
            yield (index, csv_row)
