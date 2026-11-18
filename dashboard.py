
import getpass
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

st.set_page_config(
    page_title="ICU Research Dashboard",
    layout="wide"
)

st.title("ICU Data & Kidney Function Dashboard")
st.caption(
    "Synthetic research data — not for clinical use"
)

# Request password in the Streamlit interface
password = st.text_input(
    "PostgreSQL password",
    type="password"
)

if not password:
    st.info("Enter your PostgreSQL password to load data.")
    st.stop()

url = URL.create(
    "postgresql+psycopg",
    username="postgres",
    password=password,
    host="localhost",
    port=5432,
    database="icu-research"
)

query = text("""
    SELECT
        s.stay_id,
        l.measurement_time,
        l.test_value AS creatinine
    FROM icu_stays s
    JOIN lab_results l
      ON s.stay_id = l.stay_id
    WHERE l.test_name = 'Creatinine'
      AND l.unit = 'mg/dL'
    ORDER BY s.stay_id, l.measurement_time
""")

try:
    engine = create_engine(url)

    with engine.connect() as connection:
        df = pd.read_sql(query, connection)

    engine.dispose()

except Exception as error:
    st.error(f"Database connection failed: {error}")
    st.stop()

if df.empty:
    st.warning("No creatinine measurements found.")
    st.stop()

df["measurement_time"] = pd.to_datetime(
    df["measurement_time"]
)

df["baseline"] = df.groupby("stay_id")[
    "creatinine"
].transform("first")

df["change"] = df["creatinine"] - df["baseline"]

df["threshold_flag"] = df["change"] >= 0.3

# Dashboard metrics
col1, col2, col3 = st.columns(3)

col1.metric("ICU stays", df["stay_id"].nunique())
col2.metric("Lab observations", len(df))
col3.metric(
    "Flagged stays",
    df.loc[df["threshold_flag"], "stay_id"].nunique()
)

st.divider()

# Select a patient stay
selected_stay = st.selectbox(
    "Select ICU stay",
    sorted(df["stay_id"].unique())
)

patient_data = df[
    df["stay_id"] == selected_stay
].copy()

st.subheader(f"Creatinine Trend — Stay {selected_stay}")

st.line_chart(
    patient_data.set_index("measurement_time")[
        "creatinine"
    ],
    y_label="Creatinine (mg/dL)"
)

st.subheader("Laboratory Records")
st.dataframe(patient_data, hide_index=True)

st.caption(
    "Threshold flags are illustrative only. "
    "This is not a validated AKI diagnosis."
)
