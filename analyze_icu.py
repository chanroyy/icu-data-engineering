
import getpass
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

password = getpass.getpass("PostgreSQL password: ")

url = URL.create(
    "postgresql+psycopg",
    username="postgres",
    password=password,
    host="localhost",
    port=5432,
    database="icu-research"
)

engine = create_engine(url)

query = text("""
    SELECT
        p.patient_id,
        s.stay_id,
        l.measurement_time,
        l.test_value AS creatinine
    FROM patients p
    JOIN icu_stays s
        ON p.patient_id = s.patient_id
    JOIN lab_results l
        ON s.stay_id = l.stay_id
    WHERE l.test_name = 'Creatinine'
      AND l.unit = 'mg/dL'
    ORDER BY s.stay_id, l.measurement_time
""")

try:
    with engine.connect() as connection:
        df = pd.read_sql(query, connection)

    if df.empty:
        raise ValueError("No creatinine records found.")

    df["measurement_time"] = pd.to_datetime(
        df["measurement_time"]
    )

    # Calculate changes relative to the first observation
    df["baseline"] = df.groupby("stay_id")[
        "creatinine"
    ].transform("first")

    df["change"] = df["creatinine"] - df["baseline"]

    # Illustrative threshold only, not an AKI diagnosis
    df["increase_0_3"] = df["change"] >= 0.3

    print("\nICU Creatinine Analysis:")
    print(df.to_string(index=False))

    summary = df.groupby("stay_id").agg(
        first_creatinine=("baseline", "first"),
        latest_creatinine=("creatinine", "last"),
        max_increase=("change", "max"),
        threshold_flag=("increase_0_3", "any")
    )

    print("\nSummary by ICU stay:")
    print(summary.to_string())

except Exception as error:
    print("\nAnalysis failed:")
    print(error)

finally:
    engine.dispose()
