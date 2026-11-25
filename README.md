\# ICU Data Engineering and Creatinine Analysis

## Technical Report

[Read the full technical report (PDF)](report/ICU_Technical_Report.pdf)

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



\## Installation and Setup



\### Prerequisites



\- Python 3

\- PostgreSQL

\- pgAdmin 4 (optional)

\- Git



\### 1. Clone the Repository



```bash

git clone https://github.com/chanroyy/icu-data-engineering.git

cd -icu-data-engineering

```



\### 2. Install Dependencies



```bash

python -m pip install -r requirements.txt

```



\### 3. Initialize the Database



\- Open PostgreSQL or pgAdmin 4.

\- Create a new database named `icu-research`.

\- Execute `schema.sql` in the new database.

\- The schema creates four relational tables, an index,

&#x20; and synthetic sample records.



The Python scripts use localhost, port 5432,

and the PostgreSQL user postgres.



Passwords are entered at runtime and are not

stored in the source code.



\### 4. Test Database Connectivity



```bash

python connect\_db.py

```



\### 5. Run the ETL Pipeline



```bash

python load\_icu\_data.py

```



\### 6. Run Automated Tests



```bash

python -m pytest -v

```



Expected result: five passing tests.



\### 7. Run Creatinine Analysis



```bash

python analyze\_icu.py

```



\### 8. Launch the Interactive Dashboard



```bash

python -m streamlit run dashboard.py

```



Open http://localhost:8501 in your browser.



\## Project Architecture



PostgreSQL Database

&#x20;   -> Python ETL Pipeline

&#x20;   -> Automated Data Validation

&#x20;   -> Exploratory Creatinine Analysis

&#x20;   -> Interactive Streamlit Dashboard



\## Database Administration



The project includes practical exercises in:



\- Database backup and restoration

\- Relational database design

\- Composite indexing

\- SQL query execution plan analysis

\- Duplicate-safe data loading



\## Limitations and Future Improvements



\- The dataset is synthetic and deliberately small.

\- Threshold-based flags are not clinical diagnoses.

\- Future extensions could include larger datasets,

&#x20; machine learning models, and additional validation rules.



