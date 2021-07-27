import csv
from .constants import *
from .sqlalchemy_models import *


def parse_cases_malaysia(filename):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        count = 1
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = CASES_MALAYSIA_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = CasesMalaysia(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)
            count += 1


def parse_cases_state(filename):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = CASES_STATE_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = CasesState(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)


def parse_clusters(filename):
    # WARNING: This may require lengthy per-row checks to update data
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = CLUSTERS_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = Clusters(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)


def parse_deaths_malaysia(filename):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = DEATHS_MALAYSIA_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = DeathsMalaysia(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)


def parse_deaths_state(filename):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = DEATHS_STATE_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = DeathsState(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)


def parse_hospital_by_state(filename):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = HOSPITAL_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = HospitalByState(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)


def parse_icu_by_state(filename):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = ICU_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = ICUByState(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)


def parse_pkrc_by_state(filename):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = PKRC_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = PKRCByState(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)


def parse_tests_malaysia(filename):
    with open(filename, newline='', encoding='utf8') as file:
        csv_data = csv.DictReader(file)
        for csv_row in csv_data:
            row_with_data = [x.strip() for x, y in csv_row.items() if y.strip()]
            version_number = TESTS_MALAYSIA_ROW_VERSION.get(hash(frozenset(row_with_data)))
            temp_row = {k.strip(): v.strip() for k, v in csv_row.items() if k.strip() in row_with_data}
            temp_row['row_version'] = version_number
            db_obj = TestsMalaysia(**temp_row)
            # TODO: complete persisting DB data
            print(db_obj)
