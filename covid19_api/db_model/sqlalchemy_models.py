from sqlalchemy import Text, Integer, Column, Date as SQLDate, Index
from uuid import uuid4
from dataclasses import dataclass
from datetime import date as PyDate
from ..api import db


@dataclass
class CasesMalaysia(db.Model, object):
    __tablename__ = 'cases_malaysia'

    cases_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Cases UUID')
    row_version: int = Column(Integer, comment="Row version")
    date: PyDate = Column(SQLDate, comment='Case date')
    cases_new: int = Column(Integer, comment='New cases')
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


Index('cases_malaysia_csv_pkey', )
@dataclass
class CasesState(db.Model, object):
    __tablename__ = 'cases_state'

    cases_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Cases UUID')
    row_version: int = Column(Integer, comment="Row version")
    date: PyDate = Column(SQLDate, comment='Case date')
    state: str = Column(Text, comment='State name')
    cases_new: int = Column(Integer, comment='New cases')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class Clusters(db.Model, object):
    __tablename__ = 'clusters'

    cluster_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Cluster UUID')
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

    death_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    deaths_new: int = Column(Integer, comment='New deaths for the reported date')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class DeathsState(db.Model, object):
    __tablename__ = 'deaths_state'

    death_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    deaths_new: int = Column(Integer, comment='New deaths for the reported date')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class HospitalByState(db.Model, object):
    __tablename__ = 'hospital_by_state'

    hospital_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    beds: int = Column(Integer, comment='Total available hospital beds')
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

    icu_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    state: str = Column(Text, comment='State name')
    bed_icu: int = Column(Integer, comment='Gazetted ICU beds')
    bed_icu_rep: int = Column(Integer, comment='Total ICU beds for Anaesthesiology & Critical Care departments')
    bed_icu_total: int = Column(Integer, comment='Total ICU beds')
    bed_icu_covid: int = Column(Integer, comment='Total ICU beds dedicated for COVID-19')
    vent: int = Column(Integer, comment='Total available ventilators')
    vent_port: int = Column(Integer, comment='Total available portable ventilators')
    icu_covid: int = Column(Integer, comment='Total number of COVID individuals under ICU care')
    icu_pui: int = Column(Integer, comment='Total number of PUI individuals under ICU care')
    icu_noncovid: int = Column(Integer, comment='Total number of non-COVID individuals under ICU care')
    vent_covid: int = Column(Integer, comment='Total number of COVID individuals that require ventilator')
    vent_pui: int = Column(Integer, comment='Total number of PUI individuals that require ventilator')
    vent_noncovid: int = Column(Integer, comment='Total number of non-COVID individuals that require ventilator')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class PKRCByState(db.Model, object):
    __tablename__ = 'pkrc_by_state'

    pkrc_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
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

    tests_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    rtk_ag: int = Column(Integer, comment='New deaths for the reported date')
    pcr: int = Column(Integer, comment='New deaths for the reported date')

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
    checkin_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Check-in UUID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
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

    # Don't ask me why I did this, the data structure for checkin_malaysia_time tied my hands.
    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class CheckinMalaysia(db.Model, object):
    __tablename__ = 'checkin_malaysia'

    checkin_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Checkin UUID')
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

    tests_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
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

    tests_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
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

    tests_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
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