from covid19_api.db_model.sqlalchemy_models import *
from covid19_api.db_model.utils import parse_csv
import os
from covid19_api.api import db
from hashlib import sha256

FILE_LIST = {
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
current_dir = os.path.join('covid19-public-main', 'new')
for category_name, category_file_list in FILE_LIST.items():
    for entry_dict in category_file_list:

        filename: str = entry_dict['filename']
        real_file_path = os.path.join(current_dir, category_name, filename)
        repository_name = filename.rsplit('.')[0]
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

        data_array = parse_csv(real_file_path, repository_name)
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
print('Import complete.')