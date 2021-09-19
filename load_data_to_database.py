from covid19_api.db_model.utils import parse_csv, check_csv_file_support
import os
from covid19_api.api import db
from covid19_api.db_model.sqlalchemy_models import *
from hashlib import sha256
from covid19_api.db_model.constants import *

COVID19_FILE_LIST = {
    'epidemic': [
        {'filename': 'cases_malaysia.csv', 'model': CasesMalaysia, 'primary_key': ['date']},
        {'filename': 'cases_state.csv', 'model': CasesState, 'primary_key': ['date', 'state']},
        {'filename': 'clusters.csv', 'model': Clusters, 'primary_key': ['cluster', 'date_announced']},
        {'filename': 'deaths_malaysia.csv', 'model': DeathsMalaysia, 'primary_key': ['date']},
        {'filename': 'deaths_state.csv', 'model': DeathsState, 'primary_key': ['date', 'state']},
        {'filename': 'hospital.csv', 'model': HospitalByState, 'primary_key': ['date', 'state']},
        {'filename': 'icu.csv', 'model': ICUByState, 'primary_key': ['date', 'state']},
        {'filename': 'pkrc.csv', 'model': PKRCByState, 'primary_key': ['date', 'state']},
        {'filename': 'tests_malaysia.csv', 'model': TestsMalaysia, 'primary_key': ['date']},
    ],
    'mysejahtera': [
        {'filename': 'checkin_malaysia_time.csv', 'model': CheckinMalaysiaTime, 'primary_key': ['date']},
        {'filename': 'checkin_malaysia.csv', 'model': CheckinMalaysia, 'primary_key': ['date']},
        {'filename': 'checkin_state.csv', 'model': CheckinState, 'primary_key': ['date', 'state']},
        {'filename': 'trace_malaysia.csv', 'model': TraceMalaysia, 'primary_key': ['date']},
    ],
    'static': [
        {'filename': 'population.csv', 'model': Population, 'primary_key': ['idxs']},
    ]
}

VACCINATION_FILE_LIST = {
    'registration': [
        {'filename': 'vaxreg_malaysia.csv', 'model': VaxRegMalaysia, 'primary_key': ['date']},
        {'filename': 'vaxreg_state.csv', 'model': VaxRegState, 'primary_key': ['date', 'state']}]
    ,
    'vaccination': [
        {'filename': 'vax_malaysia.csv', 'model': VaxMalaysia, 'primary_key': ['date']},
        {'filename': 'vax_state.csv', 'model': VaxState, 'primary_key': ['date', 'state']}]
    
}

AVAILABLE_MODULES = {
    'covid19': {
        'filelist': COVID19_FILE_LIST,
        'path': os.path.join('covid19-public'),
        'name': 'COVID-19 data'
    },
    'vaccination': {
        'filelist': VACCINATION_FILE_LIST,
        'path': os.path.join('citf-public'),
        'name': 'vaccination data'
    }
}

BUF_SIZE = 131072  # bytes
def hash_file(filename):
    with open(filename, 'rb') as file:
        hash_function = sha256()
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                # Break out of the loop when data is finished
                break
            hash_function.update(data)
    return hash_function.hexdigest()


print('Start importing.')
for module_name, module_details in AVAILABLE_MODULES.items():
    print(f"Start processing {module_details['name']}")
    current_dir = module_details['path']
    file_list: dict = module_details['filelist'].items()
    for category_name, category_file_list in file_list:
        
        for entry_dict in category_file_list:
            filename: str = entry_dict['filename']
            real_file_path = os.path.join(current_dir, category_name, filename)
            # Accommodate repository name extraction with file paths
            # It does it this way (assuming file name is 'epidemic/linelist/linelist_deaths.csv):
            # 1) Split it based on path separator reported by Python 
            #    ['epidemic', 'linelist', 'linelist_deaths.csv']
            # 2) Get the last element
            # 3) Split based on file separator
            #    ['linelist_deaths', 'csv']
            # 4) Get the first element
            repository_name = filename.rsplit(os.path.sep)[-1].rsplit('.')[0]
            csv_file_support = check_csv_file_support(real_file_path, repository_name)
            if csv_file_support is None:
                print(f'CSV file {real_file_path} is not recognized. Please file a bug report')
                continue
            elif not csv_file_support:
                print(f'CSV file {real_file_path} has a different column structure than expected. Please file a bug report')
                continue 

            file_hash = hash_file(real_file_path)
            update_dict = {
                'repository_name': repository_name,
                'repository_category': category_name
            }

            db_file_hash = db.session.query(RepositoryUpdateStatus.repository_hash).filter_by(**update_dict).one_or_none()

            if db_file_hash is None:
                pass
            elif db_file_hash[0] == file_hash:
                print(f'{category_name}/{repository_name} up to date. Skipping...')
                continue

            print(f'Start parsing {category_name} from CSV file {filename}')

            csv_row_data: dict = parse_csv(real_file_path, repository_name)
            data_array = []
            for index, data in csv_row_data:
                row_with_data = [x.strip() for x, y in data.items() if y.strip()]
                version_number = ROW_VERSION[repository_name][hash(frozenset(row_with_data))]
                temp_row = {k.strip(): v.strip() for k, v in data.items() if k.strip() in row_with_data}
                temp_row['row_id'] = index
                temp_row['row_version'] = version_number
                conv_func: dict = DATA_CONVERSION_DICT[repository_name][temp_row['row_version']]
                row = list(temp_row.keys())
                for key in row:
                    if key in conv_func:
                        temp_row[key] = conv_func.get(key)(temp_row[key])
                if REMAP_DATA.get(repository_name, None) is not None:
                    for key in row:
                        if key in REMAP_DATA[repository_name]:
                            temp_data = temp_row[key]
                            del temp_row[key]
                            temp_row[REMAP_DATA[repository_name][key]] = temp_data
                data_array.append(temp_row)

            if db.session.query(entry_dict['model']).count() == 0:
                print(f'{filename.rsplit(".", 1)[0]} is a fresh import. Using bulk saving method...')
            else:
                print(f'{filename.rsplit(".", 1)[0]} is a new data update. Purging existing data...')
                db.session.query(entry_dict['model']).delete()
                print('Purge completed. Flushing changes into database...')
                db.session.flush()
                print('Flush complete. Start importing new data using bulk saving method.')

            data_array = [entry_dict['model'](**dict_data) for dict_data in data_array]
            db.session.bulk_save_objects(data_array)
            db.session.flush()
            print('Bulk save completed')

            updated_data = {
                'last_update': datetime.now(),
                'repository_hash': file_hash
            }
            if db.session.query(RepositoryUpdateStatus.repository_name, RepositoryUpdateStatus.repository_category).filter_by(**update_dict).count():
                print(f'Updating {repository_name} repository status...')
                obj = db.session.query(RepositoryUpdateStatus).filter_by(**update_dict).update(updated_data)
                print('Update complete')
            else:
                update_dict.update(updated_data)
                print(f'Saving {repository_name} entry details...')
                db.session.add(RepositoryUpdateStatus(**update_dict))
                print('Save completed.')
            print('Committing changes to database...')
            db.session.commit()
            print('Commit to database success.')
            print(f'Finish parsing {category_name} from CSV file {entry_dict["filename"]}')
    print(f"Finish processing {module_details['name']}")
print('Import complete.')