import csv
from datetime import datetime
from .constants import *
from .sqlalchemy_models import *

def convert_date(date: str):
    # Double-conversion because strptime returns datetime, not date
    return datetime.date(datetime.strptime(date, '%Y-%m-%d'))

DATA_CONVERSION_DICT = {
    'cases_malaysia': {
        1: {'date': convert_date, 'cases_new': int},
        2: {'date': convert_date, 'cases_new': int, 'cluster_import': int, 'cluster_religious': int, 'cluster_community': int, 'cluster_highRisk': int, 'cluster_education': int, 'cluster_detentionCentre': int, 'cluster_workplace': int}
    },
    'cases_state': {
        1: {'date': convert_date, 'cases_new': int}
    },
    'clusters': {
        1: {'date_announced': convert_date,'date_last_onset': convert_date, 'cases_new':int,'cases_total':int, 'cases_active':int, 'tests':int, 'icu':int, 'deaths':int, 'recovered':int}
    },
    'deaths_malaysia': {
        1: {'date': convert_date, 'deaths_new': int}
    },
    'deaths_state': {
        1: {'date': convert_date, 'deaths_new': int}
    },
    'hospital': {
        1: {'date': convert_date, 'beds': int, 'beds_noncrit': int, 'admitted_pui': int, 'admitted_covid': int, 'admitted_total': int, 'discharged_pui': int, 'discharged_covid': int, 'discharged_total': int, 'hosp_covid': int, 'hosp_pui': int, 'hosp_noncovid': int}
    },
    'icu': {
        1: {'date': convert_date, 'bed_icu': int, 'bed_icu_rep': int, 'bed_icu_total': int, 'bed_icu_covid': int, 'vent': int, 'vent_port': int, 'icu_covid': int, 'icu_pui': int, 'icu_noncovid': int, 'vent_covid': int, 'vent_pui': int, 'vent_noncovid': int}
    },
    'pkrc': {
        1: {'date': convert_date, 'beds': int, 'admitted_pui': int, 'admitted_covid': int,'admitted_total': int, 'discharge_pui': int, 'discharge_covid': int, 'discharge_total': int,'pkrc_covid': int, 'pkrc_pui': int, 'pkrc_noncovid': int}
    },
    'tests_malaysia': {
        1: {'date': convert_date, 'rtk-ag': int, 'pcr': int}
    },
    'checkin_malaysia_time': {
        1: {'date': convert_date, '0': int, '1': int, '2': int, '3': int, '4': int, '5': int, '6': int, '7': int, '8': int, '9': int, '10': int, '11': int, '12': int, '13': int, '14': int, '15': int, '16': int, '17': int, '18': int, '19': int, '20': int, '21': int, '22': int, '23': int, '24': int, '25': int, '26': int, '27': int, '28': int, '29': int, '30': int, '31': int, '32': int, '33': int, '34': int, '35': int, '36': int, '37': int, '38': int, '39': int, '40': int, '41': int, '42': int, '43': int, '44': int, '45': int, '46': int, '47': int}
    },
    'checkin_malaysia': {
        1: {'date': convert_date, 'checkins': int, 'unique_ind': int, 'unique_loc': int}
    },
    'checkin_state': {
        1: {'date': convert_date, 'checkins': int, 'unique_ind': int, 'unique_loc': int}
    },
    'trace_malaysia': {
        1: {'date': convert_date, 'casual_contacts': int},
        2: {'date': convert_date, 'casual_contacts': int, 'hide_large': int, 'hide_small': int}
    }
}


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
