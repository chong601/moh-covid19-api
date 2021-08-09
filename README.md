# moh-covid19-api

Because speedrunning code writing is fun™. ~~And it took longer than what I thought it would take to finish it. Oops.~~

Jokes aside, this project provides [Ministry of Health Malaysia COVID-19 statistics](https://github.com/MoH-Malaysia/covid19-public) and [COVID-19 Immunisation Task Force (CITF) public vaccination](https://github.com/CITF-Malaysia/citf-public) data in API form.

API specification will be defined soon™.
# Things to work on
- [phase 2 in-progress] Better database model (the source data makes it difficult to build one)
- [in progress] Complete the initial REST API implementation
- [done] Make CSV data import less cancerous (it's pretty cancerific)
- Code cleanups
- Make PR to [official Ministry of Health Malaysia COVID-19 repository](https://github.com/MoH-Malaysia/covid19-public) to promote this project!

# Features
- [done] Pandemic data
  - [done] Country-wide case count
  - [done] Per-state case count
  - [done] Cluster details
  - [done] Country-wide deaths
  - [done] Per-state deaths
  - [done] Per-state hospital statistics
  - [done] Per-state ICU statistics
  - [done] Per-state PKRC statistics
  - [done] COVID-19 testing
- [done] MySejahtera data
  - [done] Check-ins by time
  - [done] Country-wide check-ins
  - [done] Per-state check-ins
  - [done] Contact tracing and HIDE hotspot
- [done] Population data
- [in-progress] [NEW] Vaccination data
  - [in-progress] [NEW] Country-wide vaccine registration statistics
  - [in-progress] [NEW] Per-state vaccine registration statistics
  - [in-progress] [NEW] Country-wide vaccination statistics
  - [in-progress] [NEW] Per-state vaccination statistics
