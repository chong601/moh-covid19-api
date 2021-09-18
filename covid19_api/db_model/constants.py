from datetime import datetime
from hashlib import md5

# Ew.
# I just dislike the fact that convert date function HAS to live in constants module
# because 
def convert_date(date: str):
    # Double-conversion because strptime returns datetime, not date
    return datetime.date(datetime.strptime(date, '%Y-%m-%d'))


def hash_column_data(col_arr: list):
    col_arr.sort()
    return md5(bytes(''.join(col_arr), encoding='utf8')).hexdigest()


ROW_VERSION = {
    'cases_malaysia': {
        hash(frozenset(['date','cases_new'])): 1,
        hash(frozenset(['date','cases_new','cluster_import','cluster_religious','cluster_community','cluster_highRisk','cluster_education','cluster_detentionCentre','cluster_workplace'])): 2,
        hash(frozenset(['date','cases_new','cases_import','cases_recovered'])): 3,
        hash(frozenset(['date','cases_new','cases_import','cases_recovered','cluster_import','cluster_religious','cluster_community','cluster_highRisk','cluster_education','cluster_detentionCentre','cluster_workplace'])): 4,
    },

    'cases_state': {
        hash(frozenset(['date','state','cases_new'])): 1,
        hash(frozenset(['date','state','cases_import','cases_new','cases_recovered'])): 2,
        
    },

    'clusters': {
        hash(frozenset(['cluster','state','district','date_announced','date_last_onset','category','status','cases_new','cases_total','cases_active','tests','icu','deaths','recovered'])): 1
    },

    'deaths_malaysia': {
        hash(frozenset(['date','deaths_new'])): 1,
        hash(frozenset(['date','deaths_new','deaths_new_dod','deaths_bid','deaths_bid_dod'])): 2
    },

    'deaths_state': {
        hash(frozenset(['date','state','deaths_new'])): 1
    },

    'hospital': {
        hash(frozenset(['date','state','beds','beds_noncrit','admitted_pui','admitted_covid','admitted_total','discharged_pui','discharged_covid','discharged_total','hosp_covid','hosp_pui','hosp_noncovid'])): 1,
        hash(frozenset(['date','state','beds','beds_covid','beds_noncrit','admitted_pui','admitted_covid','admitted_total','discharged_pui','discharged_covid','discharged_total','hosp_covid','hosp_pui','hosp_noncovid'])): 2
    },

    'icu': {
        hash(frozenset(['date','state','bed_icu','bed_icu_rep','bed_icu_total','bed_icu_covid','vent','vent_port','icu_covid','icu_pui','icu_noncovid','vent_covid','vent_pui','vent_noncovid'])): 1,
        hash(frozenset(['date','state','beds_icu','beds_icu_rep','beds_icu_total','beds_icu_covid','vent','vent_port','icu_covid','icu_pui','icu_noncovid','vent_covid','vent_pui','vent_noncovid'])): 2
    },

    'pkrc': {
        hash(frozenset(['date','state','beds','admitted_pui','admitted_covid','admitted_total','discharge_pui','discharge_covid','discharge_total','pkrc_covid','pkrc_pui','pkrc_noncovid'])): 1
    },

    'tests_malaysia': {
        hash(frozenset(['date','rtk-ag','pcr'])): 1
    },

    'checkin_malaysia_time': {
        hash(frozenset(['date','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47'])): 1
    },

    'checkin_malaysia':{
        hash(frozenset(['date','checkins','unique_ind','unique_loc'])): 1
    },

    'checkin_state': {
        hash(frozenset(['date','state','checkins','unique_ind','unique_loc'])): 1
    },

    'trace_malaysia': {
        hash(frozenset(['date','casual_contacts'])): 1,
        hash(frozenset(['date','casual_contacts','hide_large','hide_small'])): 2
    },
    'population': {
        hash(frozenset(['state','idxs','pop','pop_18','pop_60'])): 1
    },
    'vaxreg_malaysia': {
        hash(frozenset(['date', 'state', 'total', 'phase2', 'mysj', 'call', 'web', 'children', 'elderly', 'comorb', 'oku'])): 1
    },
    'vaxreg_state': {
        hash(frozenset(['date', 'state', 'total', 'phase2', 'mysj', 'call', 'web', 'children', 'elderly', 'comorb', 'oku'])): 1
    },
    'vax_malaysia': {
        hash(frozenset(['date', 'dose1_daily', 'dose2_daily', 'total_daily', 'dose1_cumul', 'dose2_cumul', 'total_cumul'])): 1,
        hash(frozenset(['date', 'daily_partial', 'daily_full', 'daily', 'cumul_partial', 'cumul_full', 'cumul', 'pfizer1', 'pfizer2', 'sinovac1', 'sinovac2', 'astra1', 'astra2', 'pending'])): 2
    },
    'vax_state': {
        hash(frozenset(['date', 'state', 'dose1_daily', 'dose2_daily', 'total_daily', 'dose1_cumul', 'dose2_cumul', 'total_cumul'])): 1,
        hash(frozenset(['date', 'state', 'daily_partial', 'daily_full', 'daily', 'cumul_partial', 'cumul_full', 'cumul', 'pfizer1', 'pfizer2', 'sinovac1', 'sinovac2', 'astra1', 'astra2', 'pending'])): 2
    }
}

DATA_CONVERSION_DICT = {
    'cases_malaysia': {
        1: {'date': convert_date, 'cases_new': int},
        2: {'date': convert_date, 'cases_new': int, 'cluster_import': int, 'cluster_religious': int, 'cluster_community': int, 'cluster_highRisk': int, 'cluster_education': int, 'cluster_detentionCentre': int, 'cluster_workplace': int},
        3: {'date':  convert_date,'cases_new': int,'cases_import': int,'cases_recovered': int},
        4: {'date':  convert_date,'cases_new': int,'cases_import': int,'cases_recovered': int,'cluster_import': int,'cluster_religious': int,'cluster_community': int,'cluster_highRisk': int,'cluster_education': int,'cluster_detentionCentre': int,'cluster_workplace': int}
    },
    'cases_state': {
        1: {'date': convert_date, 'cases_new': int},
        2: {'date': convert_date, 'cases_import': int, 'cases_new': int, 'cases_recovered': int}
    },
    'clusters': {
        1: {'date_announced': convert_date,'date_last_onset': convert_date, 'cases_new':int,'cases_total':int, 'cases_active':int, 'tests':int, 'icu':int, 'deaths':int, 'recovered':int},
        2: {'date': convert_date, 'deaths_new': int, 'deaths_new_dod': int, 'deaths_bid': int, 'deaths_bid_dod': int}
    },
    'deaths_malaysia': {
        1: {'date': convert_date, 'deaths_new': int}
    },
    'deaths_state': {
        1: {'date': convert_date, 'deaths_new': int}
    },
    'hospital': {
        1: {'date': convert_date, 'beds': int, 'beds_noncrit': int, 'admitted_pui': int, 'admitted_covid': int, 'admitted_total': int, 'discharged_pui': int, 'discharged_covid': int, 'discharged_total': int, 'hosp_covid': int, 'hosp_pui': int, 'hosp_noncovid': int},
        2: {'date': convert_date, 'beds': int, 'beds_covid': int, 'beds_noncrit': int, 'admitted_pui': int, 'admitted_covid': int, 'admitted_total': int, 'discharged_pui': int, 'discharged_covid': int, 'discharged_total': int, 'hosp_covid': int, 'hosp_pui': int, 'hosp_noncovid': int}
    },
    'icu': {
        1: {'date': convert_date, 'bed_icu': int, 'bed_icu_rep': int, 'bed_icu_total': int, 'bed_icu_covid': int, 'vent': int, 'vent_port': int, 'icu_covid': int, 'icu_pui': int, 'icu_noncovid': int, 'vent_covid': int, 'vent_pui': int, 'vent_noncovid': int},
        2: {'date': convert_date, 'beds_icu': int, 'beds_icu_rep': int, 'beds_icu_total': int, 'beds_icu_covid': int, 'vent': int, 'vent_port': int, 'icu_covid': int, 'icu_pui': int, 'icu_noncovid': int, 'vent_covid': int, 'vent_pui': int, 'vent_noncovid': int}
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
    },
    'population': {
        1: {'idxs': int, 'pop': int, 'pop_18': int, 'pop_60': int}
    },
    'vaxreg_malaysia': {
        1: {'date': convert_date, 'total': int, 'phase2': int, 'mysj': int, 'call': int, 'web': int, 'children': int, 'elderly': int, 'comorb': int, 'oku': int}
    },
    'vaxreg_state': {
        1: {'date': convert_date, 'total': int, 'phase2': int, 'mysj': int, 'call': int, 'web': int, 'children': int, 'elderly': int, 'comorb': int, 'oku': int}
    },
    'vax_malaysia': {
        1: {'date': convert_date, 'dose1_daily': int, 'dose2_daily': int, 'total_daily': int, 'dose1_cumul': int, 'dose2_cumul': int, 'total_cumul': int},
        2: {'date': convert_date, 'daily_partial': int, 'daily_full': int, 'daily': int, 'cumul_partial': int, 'cumul_full': int, 'cumul': int, 'pfizer1': int, 'pfizer2': int, 'sinovac1': int, 'sinovac2': int, 'astra1': int, 'astra2': int, 'pending': int}
    },
    'vax_state': {
        1: {'date': convert_date, 'dose1_daily': int, 'dose2_daily': int, 'total_daily': int, 'dose1_cumul': int, 'dose2_cumul': int, 'total_cumul': int},
        2: {'date': convert_date, 'daily_partial': int, 'daily_full': int, 'daily': int, 'cumul_partial': int, 'cumul_full': int, 'cumul': int, 'pfizer1': int, 'pfizer2': int, 'sinovac1': int, 'sinovac2': int, 'astra1': int, 'astra2': int, 'pending': int}
    }
}

SUPPORTED_CSV_DATA = {
    'cases_malaysia': [
        hash_column_data(['date','cases_new']),
        hash_column_data(['date','cases_new', 'cases_import', 'cases_recovered','cluster_import','cluster_religious','cluster_community','cluster_highRisk','cluster_education','cluster_detentionCentre','cluster_workplace'])
    ],
    'cases_state': [
        hash_column_data(['date','state','cases_new']), hash_column_data(['date','state','cases_import','cases_new','cases_recovered'])
    ],

    'clusters': [
        hash_column_data(['cluster','state','district','date_announced','date_last_onset','category','status','cases_new','cases_total','cases_active','tests','icu','deaths','recovered'])
    ],

    'deaths_malaysia': [
        hash_column_data(['date','deaths_new']), hash_column_data(['date','deaths_new','deaths_new_dod','deaths_bid','deaths_bid_dod'])
    ],

    'deaths_state': [
        hash_column_data(['date','state','deaths_new'])
    ],

    'hospital': [
        hash_column_data(['date','state','beds','beds_noncrit','admitted_pui','admitted_covid','admitted_total','discharged_pui','discharged_covid','discharged_total','hosp_covid','hosp_pui','hosp_noncovid']),
        hash_column_data(['date','state','beds','beds_covid','beds_noncrit','admitted_pui','admitted_covid','admitted_total','discharged_pui','discharged_covid','discharged_total','hosp_covid','hosp_pui','hosp_noncovid'])
    ],

    'icu': [
        hash_column_data(['date','state','bed_icu','bed_icu_rep','bed_icu_total','bed_icu_covid','vent','vent_port','icu_covid','icu_pui','icu_noncovid','vent_covid','vent_pui','vent_noncovid']),
        hash_column_data(['date','state','beds_icu','beds_icu_rep','beds_icu_total','beds_icu_covid','vent','vent_port','icu_covid','icu_pui','icu_noncovid','vent_covid','vent_pui','vent_noncovid'])
    ],

    'pkrc': [
        hash_column_data(['date','state','beds','admitted_pui','admitted_covid','admitted_total','discharge_pui','discharge_covid','discharge_total','pkrc_covid','pkrc_pui','pkrc_noncovid'])
    ],

    'tests_malaysia': [
        hash_column_data(['date','rtk-ag','pcr'])
    ],

    'checkin_malaysia_time': [
        hash_column_data(['date','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47'])
    ],

    'checkin_malaysia':[
        hash_column_data(['date','checkins','unique_ind','unique_loc'])
    ],

    'checkin_state': [
        hash_column_data(['date','state','checkins','unique_ind','unique_loc'])
    ],

    'trace_malaysia': [
        hash_column_data(['date','casual_contacts']),
        hash_column_data(['date','casual_contacts','hide_large','hide_small'])
    ],
    'population': [
        hash_column_data(['state','idxs','pop','pop_18','pop_60'])
    ],
    'vaxreg_malaysia': [
        hash_column_data(['date', 'state', 'total', 'phase2', 'mysj', 'call', 'web', 'children', 'elderly', 'comorb', 'oku'])
    ],
    'vaxreg_state': [
        hash_column_data(['date', 'state', 'total', 'phase2', 'mysj', 'call', 'web', 'children', 'elderly', 'comorb', 'oku'])
    ],
    'vax_malaysia': [
        hash_column_data(['date', 'dose1_daily', 'dose2_daily', 'total_daily', 'dose1_cumul', 'dose2_cumul', 'total_cumul']),
        hash_column_data(['date', 'daily_partial', 'daily_full', 'daily', 'cumul_partial', 'cumul_full', 'cumul', 'pfizer1', 'pfizer2', 'sinovac1', 'sinovac2', 'astra1', 'astra2', 'pending'])
    ],
    'vax_state': [
        hash_column_data(['date', 'state', 'dose1_daily', 'dose2_daily', 'total_daily', 'dose1_cumul', 'dose2_cumul', 'total_cumul']),
        hash_column_data(['date', 'state', 'daily_partial', 'daily_full', 'daily', 'cumul_partial', 'cumul_full', 'cumul', 'pfizer1', 'pfizer2', 'sinovac1', 'sinovac2', 'astra1', 'astra2', 'pending'])
    ],
    'linelist_deaths': [
        hash_column_data(['date', 'date_positive', 'date_dose1', 'date_dose2', 'vaxtype', 'state', 'age', 'male', 'bid', 'malaysian', 'comorb'])
    ]
}

REMAP_DATA = {
    'tests_malaysia': {'rtk-ag': 'rtk_ag'},
    'checkin_malaysia_time': {
        '0': 'timeslot0', '1': 'timeslot1', '2': 'timeslot2', '3': 'timeslot3', '4': 'timeslot4', '5': 'timeslot5', '6': 'timeslot6', '7': 'timeslot7', '8': 'timeslot8', '9': 'timeslot9', '10': 'timeslot10', '11': 'timeslot11', '12': 'timeslot12', '13': 'timeslot13', '14': 'timeslot14', '15': 'timeslot15', '16': 'timeslot16', '17': 'timeslot17', '18': 'timeslot18', '19': 'timeslot19', '20': 'timeslot20', '21': 'timeslot21', '22': 'timeslot22', '23': 'timeslot23', '24': 'timeslot24', '25': 'timeslot25', '26': 'timeslot26', '27': 'timeslot27', '28': 'timeslot28', '29': 'timeslot29', '30': 'timeslot30', '31': 'timeslot31', '32': 'timeslot32', '33': 'timeslot33', '34': 'timeslot34', '35': 'timeslot35', '36': 'timeslot36', '37': 'timeslot37', '38': 'timeslot38', '39': 'timeslot39', '40': 'timeslot40', '41': 'timeslot41', '42': 'timeslot42', '43': 'timeslot43', '44': 'timeslot44', '45': 'timeslot45', '46': 'timeslot46', '47': 'timeslot47'
    }
}