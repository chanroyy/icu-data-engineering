
import getpass
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from validation import validate_lab_data

# Synthetic laboratory observations
data = [
    (7, 101, "Creatinine", 1.60, "mg/dL", "2026-01-12 09:00"),
    (8, 102, "Creatinine", 1.30, "mg/dL", "2026-01-13 10:00"),
    (9, 103, "Creatinine", 1.90, "mg/dL", "2026-01-14 08:00")
]

columns = [
    "lab_id", "stay_id", "test_name",
    "test_value", "unit", "measurement_time"
]

df = pd.DataFrame(data, columns=columns)

# Validate data before loading
validate_lab_data(df)

print("Data validation successful!")
print(df)

password = getpass.getpass("\nPostgreSQL password: ")

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
    with engine.begin() as connection:
        insert_query = text("""
            INSERT INTO lab_results (
                lab_id, stay_id, test_name,
                test_value, unit, measurement_time
            )
            VALUES (
                :lab_id, :stay_id, :test_name,
                :test_value, :unit, :measurement_time
            )
            ON CONFLICT (lab_id) DO NOTHING
        """)

        connection.execute(
            insert_query,
            df.to_dict(orient="records")
        )

        count = connection.execute(
            text("SELECT COUNT(*) FROM lab_results")
        ).scalar_one()

        print(f"\nTotal laboratory records: {count}")
        print("ETL pipeline completed successfully!")

except Exception as error:
    print("\nPipeline failed:")
    print(error)

finally:
    engine.dispose()
 