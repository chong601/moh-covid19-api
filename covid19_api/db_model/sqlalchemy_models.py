from sqlalchemy import Text, Integer, Column, Date as SQLDate, Index
from uuid import uuid4
from dataclasses import dataclass
from datetime import datetime, date as PyDate
from sqlalchemy.sql.sqltypes import DateTime
from ..api import db


@dataclass
class CasesMalaysia(db.Model, object):
    __tablename__ = 'cases_malaysia'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Case ID')
    row_version: int = Column(Integer, comment="Row version")
    date: PyDate = Column(SQLDate, comment='Case date')
    cases_new: int = Column(Integer, comment='New local cases')
    cases_import: int = Column(Integer, comment='New import cases')
    cases_recovered: int = Column(Integer, comment='Recovered cases')
    cluster_import: int = Column(Integer, default=None, comment='Import new cases')
    cluster_religious: int = Column(Integer, default=None, comment='Religious new cases')
    cluster_community: int = Column(Integer, default=None, comment='Community new cases')
    cluster_highRisk: int = Column(Integer, default=None, comment='High-risk new cases')
    cluster_education: int = Column(Integer, default=None, comment='Education-related new cases')
    cluster_detentionCentre: int = Column(Integer, default=None, comment='Detention centre new cases')
    cluster_workplace: int = Column(Integer, default=None, comment='Workplace new cases')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class CasesState(db.Model, object):
    __tablename__ = 'cases_state'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Case ID')
    row_version: int = Column(Integer, comment="Row version")
    date: PyDate = Column(SQLDate, comment='Case date')
    state: str = Column(Text, comment='State name')
    cases_import: int = Column(Integer, comment='New import cases')
    cases_new: int = Column(Integer, comment='New local cases')
    cases_recovered: int = Column(Integer, comment='Recovered cases')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class Clusters(db.Model, object):
    __tablename__ = 'clusters'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Cluster ID')
    row_version: int = Column(Integer, comment='Row version')
    cluster: str = Column(Text, comment='Cluster name')
    state: str = Column(Text, comment='State name')
    district: str = Column(Text, comment='District name')
    date_announced: PyDate = Column(SQLDate, comment='Date cluster is announced')
    date_last_onset: PyDate = Column(SQLDate, comment='Most recent date for individuals with symptoms')
    category: str = Column(Text, comment='Cluster category')
    status: str = Column(Text, comment='Cluster status')
    cases_new: int = Column(Integer, comment='New cases reported within 24 hours since last report')
    cases_total: int = Column(Integer, comment='Cluster total number of cases')
    cases_active: int = Column(Integer, comment='Cluster active cases')
    tests: int = Column(Integer, comment='Number of tests performed for the cluster')
    icu: int = Column(Integer, comment='Number of individuals under ICU care for the cluster')
    deaths: int = Column(Integer, comment='Number of deaths for the cluster')
    recovered: int = Column(Integer, comment='Number of recovered individuals for the cluster')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class DeathsMalaysia(db.Model, object):
    __tablename__ = 'deaths_malaysia'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Deaths ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    # FIXME: Change comment when the government _eventually_ update the CSV file details
    # Guessing what these data means are annoying.
    deaths_new: int = Column(Integer, comment='New deaths for the reported date')
    deaths_new_dod: int = Column(Integer, comment='New deaths for the reported date')
    deaths_bid: int = Column(Integer, comment='New deaths for the reported date')
    deaths_new_dod: int = Column(Integer, comment='New deaths for the reported date')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class DeathsState(db.Model, object):
    __tablename__ = 'deaths_state'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Deaths ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    # FIXME: Change comment when the government _eventually_ update the CSV file details
    # Guessing what these data means are annoying.
    deaths_new: int = Column(Integer, comment='New deaths for the reported date')
    deaths_new_dod: int = Column(Integer, comment='New deaths for the reported date')
    deaths_bid: int = Column(Integer, comment='New deaths for the reported date')
    deaths_new_dod: int = Column(Integer, comment='New deaths for the reported date')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class HospitalByState(db.Model, object):
    __tablename__ = 'hospital_by_state'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Hospital ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    beds: int = Column(Integer, comment='Total available hospital beds')
    beds_covid: int = Column(Integer, comment='Total available hospital beds dedicated for COVID-19')
    beds_noncrit: int = Column(Integer, comment='Total available hospital beds for non-critical care')
    admitted_pui: int = Column(Integer, comment='Total admitted persons under investigation')
    admitted_covid: int = Column(Integer, comment='Total admitted persons with COVID-19')
    admitted_total: int = Column(Integer, comment='Total admissions')
    discharged_pui: int = Column(Integer, comment='Total discharged persons under investigation')
    discharged_covid: int = Column(Integer, comment='Total discharged persons with COVID-19')
    discharged_total: int = Column(Integer, comment='Total discharges')
    hosp_pui: int = Column(Integer, comment='Total hospitalised persons under investigation')
    hosp_covid: int = Column(Integer, comment='Total hospitalised COVID-19 patients')
    hosp_noncovid: int = Column(Integer, comment='Total non-COVID patients')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class ICUByState(db.Model, object):
    __tablename__ = 'icu_by_state'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='ICU ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    beds_icu: int = Column(Integer, comment='Gazetted ICU beds')
    beds_icu_rep: int = Column(Integer, comment='Total ICU beds for Anaesthesiology & Critical Care departments')
    beds_icu_total: int = Column(Integer, comment='Total ICU beds')
    beds_icu_covid: int = Column(Integer, comment='Total ICU beds dedicated for COVID-19')
    vent: int = Column(Integer, comment='Total available ventilators')
    vent_port: int = Column(Integer, comment='Total available portable ventilators')
    icu_covid: int = Column(Integer, comment='Total number of COVID individuals under ICU care')
    icu_pui: int = Column(Integer, comment='Total number of PUI individuals under ICU care')
    icu_noncovid: int = Column(Integer, comment='Total number of non-COVID individuals under ICU care')
    vent_covid: int = Column(Integer, comment='Total number of COVID individuals that require ventilator')
    vent_pui: int = Column(Integer, comment='Total number of PUI individuals that require ventilator')
    vent_noncovid: int = Column(Integer, comment='Total number of non-COVID individuals that require ventilator')
    vent_used: int = Column(Integer, comment='Total ventilators in use')
    vent_port_used: int = Column(Integer, comment='Total portable ventilator in use')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class PKRCByState(db.Model, object):
    __tablename__ = 'pkrc_by_state'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='PKRC ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    beds: int = Column(Integer, comment='Total available PKRC beds')
    admitted_pui: int = Column(Integer, comment='Total admitted persons under investigation')
    admitted_covid: int = Column(Integer, comment='Total admitted persons with COVID-19')
    admitted_total: int = Column(Integer, comment='Total admissions')
    discharge_pui: int = Column(Integer, comment='Total discharged persons under investigation')
    discharge_covid: int = Column(Integer, comment='Total discharged persons with COVID-19')
    discharge_total: int = Column(Integer, comment='Total discharges')
    pkrc_pui: int = Column(Integer, comment='Total hospitalised persons under investigation')
    pkrc_covid: int = Column(Integer, comment='Total hospitalised COVID-19 patients')
    pkrc_noncovid: int = Column(Integer, comment='Total non-COVID patients')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class TestsMalaysia(db.Model, object):
    __tablename__ = 'tests_malaysia'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Tests UUID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    rtk_ag: int = Column(Integer, comment='Total RTK-Ag tests performed')
    pcr: int = Column(Integer, comment='Total RT-PCR tests performed')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            if k == 'rtk-ag':
                setattr(self, 'rtk_ag', v)
                continue
            setattr(self, k, v)


@dataclass
class CheckinMalaysiaTime(db.Model, object):
    __tablename__ = 'checkin_malaysia_time'

    # This column definition is just cursed.
    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Check-in ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    # Uhhhhh...
    # This timeslot part should be in JSON, but I'm QUITE worried about DB support...
    # I THINK this can be converted into text that will be casted into JSON during query,
    # but that would mean relegating most of the work on Python which is less than nice IMO.
    # Also that data conversion is kinda an ass to deal with as well, but we'll see.
    timeslot0: int = Column(Integer, comment='Time-slot')
    timeslot1: int = Column(Integer, comment='Time-slot')
    timeslot2: int = Column(Integer, comment='Time-slot')
    timeslot3: int = Column(Integer, comment='Time-slot')
    timeslot4: int = Column(Integer, comment='Time-slot')
    timeslot5: int = Column(Integer, comment='Time-slot')
    timeslot6: int = Column(Integer, comment='Time-slot')
    timeslot7: int = Column(Integer, comment='Time-slot')
    timeslot8: int = Column(Integer, comment='Time-slot')
    timeslot9: int = Column(Integer, comment='Time-slot')
    timeslot10: int = Column(Integer, comment='Time-slot')
    timeslot11: int = Column(Integer, comment='Time-slot')
    timeslot12: int = Column(Integer, comment='Time-slot')
    timeslot13: int = Column(Integer, comment='Time-slot')
    timeslot14: int = Column(Integer, comment='Time-slot')
    timeslot15: int = Column(Integer, comment='Time-slot')
    timeslot16: int = Column(Integer, comment='Time-slot')
    timeslot17: int = Column(Integer, comment='Time-slot')
    timeslot18: int = Column(Integer, comment='Time-slot')
    timeslot19: int = Column(Integer, comment='Time-slot')
    timeslot20: int = Column(Integer, comment='Time-slot')
    timeslot21: int = Column(Integer, comment='Time-slot')
    timeslot22: int = Column(Integer, comment='Time-slot')
    timeslot23: int = Column(Integer, comment='Time-slot')
    timeslot24: int = Column(Integer, comment='Time-slot')
    timeslot25: int = Column(Integer, comment='Time-slot')
    timeslot26: int = Column(Integer, comment='Time-slot')
    timeslot27: int = Column(Integer, comment='Time-slot')
    timeslot28: int = Column(Integer, comment='Time-slot')
    timeslot29: int = Column(Integer, comment='Time-slot')
    timeslot30: int = Column(Integer, comment='Time-slot')
    timeslot31: int = Column(Integer, comment='Time-slot')
    timeslot32: int = Column(Integer, comment='Time-slot')
    timeslot33: int = Column(Integer, comment='Time-slot')
    timeslot34: int = Column(Integer, comment='Time-slot')
    timeslot35: int = Column(Integer, comment='Time-slot')
    timeslot36: int = Column(Integer, comment='Time-slot')
    timeslot37: int = Column(Integer, comment='Time-slot')
    timeslot38: int = Column(Integer, comment='Time-slot')
    timeslot39: int = Column(Integer, comment='Time-slot')
    timeslot40: int = Column(Integer, comment='Time-slot')
    timeslot41: int = Column(Integer, comment='Time-slot')
    timeslot42: int = Column(Integer, comment='Time-slot')
    timeslot43: int = Column(Integer, comment='Time-slot')
    timeslot44: int = Column(Integer, comment='Time-slot')
    timeslot45: int = Column(Integer, comment='Time-slot')
    timeslot46: int = Column(Integer, comment='Time-slot')
    timeslot47: int = Column(Integer, comment='Time-slot')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class CheckinMalaysia(db.Model, object):
    __tablename__ = 'checkin_malaysia'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Checkin ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    checkins: int = Column(Integer, comment='Number of checkins')
    unique_ind: int = Column(Integer, comment='Number of unique individuals checking in')
    unique_loc: int = Column(Integer, comment='Number of unique premises checked in')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class CheckinState(db.Model, object):
    __tablename__ = 'checkin_state'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Checkin ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    checkins: int = Column(Integer, comment='Number of checkins')
    unique_ind: int = Column(Integer, comment='Number of unique individuals checking in')
    unique_loc: int = Column(Integer, comment='Number of unique premises checked in')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class TraceMalaysia(db.Model, object):
    __tablename__ = 'trace_malaysia'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Trace ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    casual_contacts: int = Column(Integer, comment='Casual contact count')
    hide_large: int = Column(Integer, comment='Large hotspot count identified by CPRC HIDE system')
    hide_small: int = Column(Integer, comment='Small hotspot count identified by CPRC HIDE system')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class Population(db.Model, object):
    __tablename__ = 'population'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Population ID')
    row_version: int = Column(Integer, comment='Row version')
    """'state','idxs','pop','pop_18','pop_60'"""
    state: str = Column(Text, comment='State name')
    idxs: int = Column(Integer, comment='Population index (possibly MOH internal)')
    pop: int = Column(Integer, comment='Total state population')
    pop_18: int = Column(Integer, comment='Total state population ages >= 18')
    pop_60: int = Column(Integer, comment='Total state population ages >= 60')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class RepositoryUpdateStatus(db.Model, object):
    __tablename__ = 'repository_update_status'

    repository_id: str = Column(Text, primary_key=True, default=uuid4, comment='Repository UUID')
    repository_name: str = Column(Text, nullable=False, comment='Repository name')
    repository_category: str = Column(Text, nullable=False, comment='Repository category')
    last_update: datetime = Column(DateTime, nullable=False, comment='Last successful update date and time')
    repository_hash: str = Column(Text, nullable=False, comment='SHA-256 of the last successful hash')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class VaxRegMalaysia(db.Model, object):
    __tablename__ = 'vaxreg_malaysia'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Row ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Date')
    state: str = Column(Text, comment='State name')
    total: int = Column(Integer, comment='Number of unique registrants')
    phase2: int = Column(Integer, comment='Number of unique individuals eligible for Phase 2')
    mysj: int = Column(Integer, comment='Number of individuals registered via MySejahtera')
    call: int = Column(Integer, comment='Number of individuals registered via the call centre')
    web: int = Column(Integer, comment='Number of individuals registered via the website')
    children: int = Column(Integer, comment='Number of individuals below 18')
    elderly: int = Column(Integer, comment='Number of individuals aged 60 and above')
    comorb: int = Column(Integer, comment='Number of individuals self-declaring at least 1 comorbidity')
    oku: int = Column(Integer, comment='Number of individuals self-declaring as OKU')
    

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class VaxRegState(db.Model, object):
    __tablename__ = 'vaxreg_state'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Row ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Date')
    state: str = Column(Text, comment='State name')
    total: int = Column(Integer, comment='Number of unique registrants')
    phase2: int = Column(Integer, comment='Number of unique individuals eligible for Phase 2')
    mysj: int = Column(Integer, comment='Number of individuals registered via MySejahtera')
    call: int = Column(Integer, comment='Number of individuals registered via the call centre')
    web: int = Column(Integer, comment='Number of individuals registered via the website')
    children: int = Column(Integer, comment='Number of individuals below 18')
    elderly: int = Column(Integer, comment='Number of individuals aged 60 and above')
    comorb: int = Column(Integer, comment='Number of individuals self-declaring at least 1 comorbidity')
    oku: int = Column(Integer, comment='Number of individuals self-declaring as OKU')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class VaxMalaysia(db.Model, object):
    __tablename__ = 'vax_malaysia'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Row ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    daily_partial: int = Column(Integer, comment='1st doses (for double-dose vaccines) delivered between 0000 and 2359 on date')
    daily_full: int = Column(Integer, comment='2nd doses (for single-dose vaccines) and 1-dose vaccines (e.g. Cansino) delivered between 0000 and 2359 on date.')
    daily: int = Column(Integer, comment='Total daily delivered between 0000 and 2359 on date')
    cumul_partial: int = Column(Integer, comment='Sum of cumulative partial doses delivered until row date')
    cumul_full: int = Column(Integer, comment='Sum of cumulative full doses delivered until row date')
    cumul: int = Column(Integer, comment='Total cumulative doses delivered until row date')
    pfizer1: int = Column(Integer, comment='1st dose of PFizer vaccine delivered between 0000 and 2359 on date')
    pfizer2: int = Column(Integer, comment='2nd dose of PFizer vaccine delivered between 0000 and 2359 on date')
    sinovac1: int = Column(Integer, comment='1st dose of SinoVac vaccine delivered between 0000 and 2359 on date')
    sinovac2: int = Column(Integer, comment='2nd dose of SinoVac vaccine delivered between 0000 and 2359 on date')
    astra1: int = Column(Integer, comment='1st dose of AstraZeneca vaccine delivered between 0000 and 2359 on date')
    astra2: int = Column(Integer, comment='2nd dose of AstraZeneca vaccine delivered between 0000 and 2359 on date')
    cansino: int = Column(Integer, comment='Single-dose CanSino vaccine delivered between 0000 and 2359 on date')
    pending: int = Column(Integer, comment='Doses delivered that are quarantined in VMS (Vaccine Management System)')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class VaxState(db.Model, object):
    __tablename__ = 'vax_state'

    row_id: int = Column(Integer, primary_key=True, autoincrement=False, comment='Row ID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    daily_partial: int = Column(Integer, comment='1st doses (for double-dose vaccines) delivered between 0000 and 2359 on date')
    daily_full: int = Column(Integer, comment='2nd doses (for single-dose vaccines) and 1-dose vaccines (e.g. Cansino) delivered between 0000 and 2359 on date.')
    daily: int = Column(Integer, comment='Total daily delivered between 0000 and 2359 on date')
    cumul_partial: int = Column(Integer, comment='Sum of cumulative partial doses delivered until row date')
    cumul_full: int = Column(Integer, comment='Sum of cumulative full doses delivered until row date')
    cumul: int = Column(Integer, comment='Total cumulative doses delivered until row date')
    pfizer1: int = Column(Integer, comment='1st dose of PFizer vaccine delivered between 0000 and 2359 on date')
    pfizer2: int = Column(Integer, comment='2nd dose of PFizer vaccine delivered between 0000 and 2359 on date')
    sinovac1: int = Column(Integer, comment='1st dose of SinoVac vaccine delivered between 0000 and 2359 on date')
    sinovac2: int = Column(Integer, comment='2nd dose of SinoVac vaccine delivered between 0000 and 2359 on date')
    astra1: int = Column(Integer, comment='1st dose of AstraZeneca vaccine delivered between 0000 and 2359 on date')
    astra2: int = Column(Integer, comment='2nd dose of AstraZeneca vaccine delivered between 0000 and 2359 on date')
    cansino: int = Column(Integer, comment='Single-dose CanSino vaccine delivered between 0000 and 2359 on date')
    pending: int = Column(Integer, comment='Doses delivered that are quarantined in VMS (Vaccine Management System)')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


# Column index definition
Index('cases_malaysia_csv_pkey', CasesMalaysia.date)
Index('cases_state_csv_pkey', CasesState.date, CasesState.state)
Index('clusters_csv_pkey', Clusters.cluster, Clusters.date_announced)
Index('deaths_malaysia_csv_pkey', DeathsMalaysia.date)
Index('deaths_state_csv_pkey', DeathsState.date, DeathsState.state)
Index('hospital_csv_pkey', HospitalByState.date, HospitalByState.state)
Index('icu_csv_pkey', ICUByState.date, ICUByState.state)
Index('pkrc_csv_pkey', PKRCByState.date, PKRCByState.state)
Index('tests_malaysia_csv_pkey', TestsMalaysia.date)
Index('checkin_malaysia_time_csv_pkey', CheckinMalaysiaTime.date)
Index('checkin_malaysia_csv_pkey', CheckinMalaysia.date)
Index('checkin_state_csv_pkey', CheckinState.date, CheckinState.state)
Index('trace_malaysia_csv_pkey', TraceMalaysia.date)
Index('population_state_idx', Population.state)
Index('population_csv_pkey', Population.idxs)
Index('repository_update_status_search_idx', RepositoryUpdateStatus.repository_name, RepositoryUpdateStatus.repository_category)
Index('vaxreg_malaysia_csv_pkey', VaxRegMalaysia.date)
Index('vaxreg_state_csv_pkey', VaxRegState.date, VaxRegState.state)
Index('vax_malaysia_csv_pkey', VaxMalaysia.date)
Index('vax_state_csv_pkey', VaxState.date, VaxState.state)
