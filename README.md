

\# ICU Data Engineering and Creatinine Analysis



\## Project Overview



A Python and PostgreSQL project demonstrating data engineering,

data validation, exploratory analysis, and visualization using

synthetic intensive care unit (ICU) data.



This project was developed as a technical portfolio exercise.



\## Technologies



\- Python

\- PostgreSQL

\- SQLAlchemy

\- pandas

\- pytest

\- Streamlit

\- Git



\## Project Features



\### 1. Relational Database

PostgreSQL database containing:

\- Patients

\- ICU stays

\- Laboratory results

\- Vital signs



\### 2. ETL Pipeline

Python pipeline for validating and loading synthetic laboratory

measurements into PostgreSQL.



Duplicate laboratory IDs are handled to support repeatable loading.



\### 3. Automated Testing

Five pytest tests covering:

\- Valid laboratory data

\- Duplicate IDs

\- Missing values

\- Negative laboratory values

\- Invalid timestamps



\### 4. Creatinine Analysis

Exploratory analysis of creatinine measurements across ICU stays.



A simple increase threshold of 0.3 mg/dL is used to flag

observations for further review.



These flags are not clinical diagnoses of acute kidney injury.



\### 5. Interactive Dashboard

Streamlit dashboard displaying:

\- ICU stay counts

\- Laboratory observation counts

\- Flagged ICU stays

\- Creatinine trends

\- Raw laboratory data



\### 6. Database Administration

\- PostgreSQL backup and restoration

\- Index creation and inspection

\- Query performance analysis using EXPLAIN ANALYZE



\## Project Files



\- connect\_db.py - PostgreSQL connectivity

\- load\_icu\_data.py - ETL pipeline

\- validation.py - Data validation

\- test\_validation.py - Automated tests

\- analyze\_icu.py - Creatinine analysis

\- dashboard.py - Streamlit dashboard



\## Data Disclaimer



All patient and laboratory data are synthetic.



This project is for educational and portfolio purposes only.

It is not intended for clinical decision-making.



