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


def parse_csv(filename: str, data_type: str):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        csv_list = []
        for index, csv_row in enumerate(csv_data, 1):
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = ROW_VERSION[data_type][hash(frozenset(row_with_data))]
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_id'] = index
            temp_row['row_version'] = version_number
            conv_func: dict = DATA_CONVERSION_DICT[data_type][temp_row['row_version']]
            for k, v in conv_func.items():
                temp_row[k] = v(temp_row[k])
            if REMAP_DATA.get(data_type, None) is not None:
                for k, v in REMAP_DATA[data_type].items():
                    temp_data = temp_row[k]
                    del temp_row[k]
                    temp_row[v] = temp_data
            csv_list.append(temp_row)
        return csv_list
