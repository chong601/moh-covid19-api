CASES_MALAYSIA_ROW_VERSION = {
    hash(frozenset(['date','cases_new'])): 1,
    hash(frozenset(['date','cases_new','cluster_import','cluster_religious','cluster_community','cluster_highRisk','cluster_education','cluster_detentionCentre','cluster_workplace'])): 2
}

CASES_STATE_ROW_VERSION = {
    hash(frozenset(['date','state','cases_new'])): 1
}

CLUSTERS_ROW_VERSION = {
    hash(frozenset(['cluster','state','district','date_announced','date_last_onset','category','status','cases_new','cases_total','cases_active','tests','icu','deaths','recovered'])): 1
}

DEATHS_MALAYSIA_ROW_VERSION = {
    hash(frozenset(['date','deaths_new'])): 1
}

DEATHS_STATE_ROW_VERSION = {
    hash(frozenset(['date','state','deaths_new'])): 1
}

HOSPITAL_ROW_VERSION = {
    hash(frozenset(['date','state','beds','beds_noncrit','admitted_pui','admitted_covid','admitted_total','discharged_pui','discharged_covid','discharged_total','hosp_covid','hosp_pui','hosp_noncovid'])): 1
}

ICU_ROW_VERSION = {
    hash(frozenset(['date','state','bed_icu','bed_icu_rep','bed_icu_total','bed_icu_covid','vent','vent_port','icu_covid','icu_pui','icu_noncovid','vent_covid','vent_pui','vent_noncovid'])): 1
}

PKRC_ROW_VERSION = {
    hash(frozenset(['date','state','beds','admitted_pui','admitted_covid','admitted_total','discharge_pui','discharge_covid','discharge_total','pkrc_covid','pkrc_pui','pkrc_noncovid'])): 1
}

TESTS_MALAYSIA_ROW_VERSION = {
    hash(frozenset(['date','rtk-ag','pcr'])): 1
}

CHECKIN_MALAYSIA_TIME_ROW_VERSION = {
    hash(frozenset(['date','0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47'])): 1
}

CHECKIN_MALAYSIA_ROW_VERSION = {
    hash(frozenset(['date','checkins','unique_ind','unique_loc'])): 1
}

CHECKIN_STATE_ROW_VERSION = {
    hash(frozenset(['date','state','checkins','unique_ind','unique_loc'])): 1
}

TRACE_MALAYSIA_ROW_VERSION = {
    hash(frozenset(['date','casual_contacts'])): 1,
    hash(frozenset(['date','casual_contacts','hide_large','hide_small'])): 2
}

POPULATION_ROW_VERSION = {
    hash(frozenset(['state','idxs','pop','pop_18','pop_60'])): 1
}
