from covid19_api.db_model.sqlalchemy_models import *
from covid19_api.db_model.utils import parse_csv
import os
from covid19_api.api import db
from hashlib import sha1

FILE_LIST = {
    'epidemic': [
        # {'filename': 'cases_malaysia.csv', 'model': CasesMalaysia, 'primary_key': ['date']},
        # {'filename': 'cases_state.csv', 'model': CasesState, 'primary_key': ['date', 'state']},
        {'filename': 'clusters.csv', 'model': Clusters, 'primary_key': ['cluster']},
        # {'filename': 'deaths_malaysia.csv', 'model': DeathsMalaysia, 'primary_key': ['date']},
        # {'filename': 'deaths_state.csv', 'model': DeathsState, 'primary_key': ['date', 'state']},
        # {'filename': 'hospital.csv', 'model': HospitalByState, 'primary_key': ['date', 'state']},
        # {'filename': 'icu.csv', 'model': ICUByState, 'primary_key': ['date', 'state']},
        # {'filename': 'pkrc.csv', 'model': PKRCByState, 'primary_key': ['date', 'state']},
        # {'filename': 'tests_malaysia.csv', 'model': TestsMalaysia, 'primary_key': ['date']},
    ],
    # 'mysejahtera': [
    #     {'filename': 'checkin_malaysia_time.csv', 'model': CheckinMalaysiaTime, 'primary_key': ['date']},
    #     {'filename': 'checkin_malaysia.csv', 'model': CheckinMalaysia, 'primary_key': ['date']},
    #     {'filename': 'checkin_state.csv', 'model': CheckinState, 'primary_key': ['date', 'state']},
    #     {'filename': 'trace_malaysia.csv', 'model': TraceMalaysia, 'primary_key': ['date']},
    # ],
    # 'static': [
    #     {'filename': 'population.csv', 'model': Population, 'primary_key': ['idx']},
    # ]
}

current_dir = os.path.join('covid19-public-main', 'new')
for category_name, category_file_list in FILE_LIST.items():
    for entry_dict in category_file_list:
        filename: str = entry_dict['filename']

        print(f'Start parsing {category_name} from CSV file {filename}')
        real_file_path = os.path.join(current_dir, category_name, filename)
        
        data_array = parse_csv(real_file_path, filename.rsplit('.')[0])
        if db.session.query(entry_dict['model']).count() == 0:
            print(f'{filename.rsplit(".", 1)[0]} is a fresh import. Using bulk saving method...')
            data_array = [entry_dict['model'](**dict_data) for dict_data in data_array]
            db.session.bulk_save_objects(data_array)
            print('Bulk save completed.')
            print('Committing...')
            db.session.commit()
            print('Database commit finished.')
        else:
            to_update = []
            for data in data_array:
                data: dict
                filter_column = [getattr(entry_dict['model'],primary_key) for primary_key in entry_dict['primary_key']]
                filter_data = {primary_key: data[primary_key] for primary_key in entry_dict['primary_key']}
                row_data = db.session.query(entry_dict['model']).filter_by(**filter_data).count()
                if row_data == 1: 
                    obj = db.session.query(entry_dict['model']).filter_by(**filter_data).one()
                    data_keys = list(data.keys())
                    data_hash = sha1(b''.join([str(data[x]).encode('utf-8') for x in data_keys])).hexdigest()
                    obj_hash = sha1(b''.join([str(getattr(obj, x)).encode('utf-8') for x in data_keys])).hexdigest()
                    if data_hash == obj_hash:
                        # print(f'Data hash {data_hash} matches object data hash {obj_hash}')
                        continue
                    print(f'Data hash {data_hash} != object hash {obj_hash}. Updating...')
                    for k, v in data.items():
                        if getattr(obj, k) != v:
                            print(f'Setting key {k} with value {v}')
                            setattr(obj, k, v)
                    db.session.commit()
                    print('Update complete.')
                elif row_data > 1:
                    db.session.query(entry_dict['model']).filter_by(**filter_data).delete()
                    new_obj = entry_dict['model'](**data)
                    to_update.append(new_obj)
                elif row_data == 0:
                    print('Row not found. Creating new row...')
                    new_obj = entry_dict['model'](**data)
                    print(f'Created new row instance {new_obj}')
                    to_update.append(new_obj)
                    print('Row data queued.')
            if len(to_update) > 1:
                print('Committing...')
                db.session.bulk_save_objects(to_update)
                db.session.commit()
                print('Commit success.')
            else:
                print('No data to update. Skipping commit phase.')
        print(f'Finish parsing {category_name} from CSV file {entry_dict["filename"]}')