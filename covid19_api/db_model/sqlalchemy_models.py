from sqlalchemy import Text, Integer, Column, Date as SQLDate
from uuid import uuid4
from dataclasses import dataclass
from datetime import date as PyDate


@dataclass
class CasesMalaysia(object):
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


@dataclass
class CasesState(object):
    __tablename__ = 'cases_state'

    cases_uuid: str = Column(Text, primary_key=True, comment='Cases UUID')
    row_version: int = Column(Integer, comment="Row version")
    date: PyDate = Column(SQLDate, comment='Case date')
    state: str = Column(Text, comment='State name')
    cases_new: int = Column(Integer, comment='New cases')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class Clusters(object):
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
class DeathsMalaysia(object):
    __tablename__ = 'deaths_malaysia'

    death_uuid: str = Column(Text, primary_key=True, default=uuid4, comment='Deaths UUID')
    row_version: int = Column(Integer, comment='Row version')
    date: PyDate = Column(SQLDate, comment='Reported date')
    deaths_new: int = Column(Integer, comment='New deaths for the reported date')

    def __init__(self, **kwargs) -> None:
        for k, v in kwargs.items():
            setattr(self, k, v)


@dataclass
class DeathsState(object):
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
class HospitalByState(object):
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
class ICUByState(object):
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
class PKRCByState(object):
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
class TestsMalaysia(object):
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
