
import getpass
import psycopg
from pathlib import Path

password = getpass.getpass("PostgreSQL password: ")

with psycopg.connect(
    host="localhost",
    port=5432,
    dbname="icu-research-test",
    user="postgres",
    password=password
) as conn:

    with conn.cursor() as cur:

        cur.execute("SELECT current_database()")
        print("Connected to:", cur.fetchone()[0])

        schema = Path("schema.sql").read_text(
            encoding="utf-8"
        )

        cur.execute(schema)

        for table in [
            "patients",
            "icu_stays",
            "lab_results",
            "vital_signs"
        ]:
            cur.execute(f"SELECT COUNT(*) FROM {table}")
            print(f"{table}: {cur.fetchone()[0]} records")

    conn.commit()

print("Database schema test successful!")
