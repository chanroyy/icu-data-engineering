
import pandas as pd

def validate_lab_data(df):
    required = [
        "lab_id", "stay_id", "test_name",
        "test_value", "unit", "measurement_time"
    ]

    if not set(required).issubset(df.columns):
        raise ValueError("Missing required columns")

    if df.empty:
        raise ValueError("Dataset is empty")

    if df["lab_id"].isna().any():
        raise ValueError("Missing lab IDs")

    if df["lab_id"].duplicated().any():
        raise ValueError("Duplicate lab IDs")

    if df["stay_id"].isna().any():
        raise ValueError("Missing ICU stay IDs")

    values = pd.to_numeric(
        df["test_value"], errors="coerce"
    )

    if values.isna().any() or (values <= 0).any():
        raise ValueError("Invalid laboratory values")

    if df["unit"].isna().any():
        raise ValueError("Missing units")

   timestamps = pd.to_datetime(
    df["measurement_time"],
    format="ISO8601",
    errors="coerce"
)

    if timestamps.isna().any():
        raise ValueError("Invalid timestamps")

    return True
