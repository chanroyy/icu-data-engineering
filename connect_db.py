
import getpass
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

print("Starting ICU database connection...")

# Ask for your PostgreSQL password
password = getpass.getpass("PostgreSQL password: ")

# Create connection
url = URL.create(
    "postgresql+psycopg",
    username="postgres",
    password=password,
    host="localhost",
    port=5432,
    database="icu-research"
)

engine = create_engine(url)

try:
    with engine.connect() as connection:
        print("\nConnected to PostgreSQL successfully!")

        query = text(
            "SELECT * FROM patients ORDER BY patient_id"
        )

        patients = pd.read_sql(query, connection)

        print("\nICU Patient Records:")
        print(patients.to_string(index=False))

except Exception as error:
    print("\nConnection failed:")
    print(error)

finally:
    engine.dispose()
