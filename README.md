# moh-covid19-api

Because speedrunning code writing is fun™. ~~And it took longer than what I thought it would take to finish it. Oops.~~

Jokes aside, this project provides [Ministry of Health Malaysia COVID-19 statistics](https://github.com/MoH-Malaysia/covid19-public) and [COVID-19 Immunisation Task Force (CITF) public vaccination](https://github.com/CITF-Malaysia/citf-public) data in API form.

API specification will be defined soon™.
# Things to work on
- [phase 2 in-progress] Better database model (the source data makes it difficult to build one)
- [in progress] Complete the initial REST API implementation
- [x] Make CSV data import less cancerous (it's pretty cancerific)
- Code cleanups
- Make PR to [official Ministry of Health Malaysia COVID-19 repository](https://github.com/MoH-Malaysia/covid19-public) to promote this project!

# Available APIs
### Epidemic data
| Name | Description | URL endpoint | Status |
| - | - | - | - |
| cases_malaysia | Country-wide new cases data | /epidemic/cases_malaysia<br>/epidemic/cases_malaysia/{date} | Done |
| cases_state | Per-state new cases data | /epidemic/cases_state<br>/epidemic/cases_state/{state}<br>/epidemic/cases_state/{state}/{date} | Done |
| clusters | All cluster data | TBD | In progress |
| deaths_malaysia | Country-wide new deaths data | /epidemic/deaths_malaysia<br>/epidemic/deaths_malaysia/{date} | Done |
| deaths_state | Per-state new deaths data | /epidemic/deaths_state<br>/epidemic/deaths_state/{state}<br>/epidemic/deaths_state/{state}/{date} | Done |
| hospital | Per-state hospital data | /epidemic/hospital<br>/epidemic/hospital/{state}<br>/epidemic/hospital/{state}/{date} | Done |
| icu | Per-state ICU data | /epidemic/icu<br>/epidemic/icu/{state}<br>/epidemic/icu/{state}/{date} | Done |
| pkrc | Per-state PKRC data | /epidemic/pkrc<br>/epidemic/pkrc/{state}<br>/epidemic/pkrc/{state}/{date} | Done |
| tests_malaysia | Country-wide COVID-19 testing data | /epidemic/tests_malaysia<br>/epidemic/tests_malaysia/{date} | Done |

### MySejahtera data
| Name | Description | URL endpoint | Status |
| - | - | - | - |
| checkin_malaysia_time | MySejahtera check-in by time data | /mysejahtera/checkin_malaysia_time<br>/mysejahtera/checkin_malaysia_time/{date} | Done |
| checkin_malaysia | Country-wide MySejahtera check-in data | /mysejahtera/checkin_malaysia<br>/mysejahtera/checkin_malaysia{date} | Done |
| checkin_state | Per-state MySejahtera check-in data | /mysejahtera/checkin_state<br>/mysejahtera/checkin_state/{state}<br>/mysejahtera/checkin_state/{state}/{date} | Done |
| trace_malaysia | Contact tracing and HIDE system data | /mysejahtera/trace_malaysia<br>/mysejahtera/trace_malaysia/{date}| In progress |

### Static data
| Name | Description | URL endpoint | Status |
| - | - | - | - |
| population | Population data | /static/population<br>/static/population/{state} | Done |

### Vaccination registration data
| Name | Description | URL endpoint | Status |
| - | - | - | - |
| vaxreg_malaysia | Country-wide vaccination registration data | TBD | In progress |
| vaxreg_state | Per-state vaccination registration data | TBD | In progress |

### Vaccination data
| Name | Description | URL endpoint | Status |
| - | - | - | - |
| vax_malaysia | Country-wide vaccination data | URL endpoint | In progress |
| vax_state | Per-state vaccination data | URL endpoint | In progress |

# Features
- [x] Pandemic data
  - [x] Country-wide case count
  - [x] Per-state case count
  - [x] Cluster details
  - [x] Country-wide deaths
  - [x] Per-state deaths
  - [x] Per-state hospital statistics
  - [x] Per-state ICU statistics
  - [x] Per-state PKRC statistics
  - [x] COVID-19 testing
- [x] MySejahtera data
  - [x] Check-ins by time
  - [x] Country-wide check-ins
  - [x] Per-state check-ins
  - [x] Contact tracing and HIDE hotspot
- [x] Population data
- [ ] [NEW] Vaccination data
  - [ ] [NEW] Country-wide vaccine registration statistics
  - [ ] [NEW] Per-state vaccine registration statistics
  - [ ] [NEW] Country-wide vaccination statistics
  - [ ] [NEW] Per-state vaccination statistics
