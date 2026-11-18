
import pandas as pd
import pytest
from validation import validate_lab_data

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        "lab_id": [1, 2],
        "stay_id": [101, 101],
        "test_name": ["Creatinine", "Creatinine"],
        "test_value": [0.9, 1.4],
        "unit": ["mg/dL", "mg/dL"],
        "measurement_time": [
            "2026-01-10 09:00",
            "2026-01-11 09:00"
        ]
    })

def test_valid_data(sample_data):
    assert validate_lab_data(sample_data)

def test_duplicate_ids(sample_data):
    sample_data.loc[1, "lab_id"] = 1
    with pytest.raises(ValueError):
        validate_lab_data(sample_data)

def test_missing_value(sample_data):
    sample_data.loc[0, "test_value"] = None
    with pytest.raises(ValueError):
        validate_lab_data(sample_data)

def test_negative_value(sample_data):
    sample_data.loc[0, "test_value"] = -1
    with pytest.raises(ValueError):
        validate_lab_data(sample_data)

def test_invalid_timestamp(sample_data):
    sample_data.loc[0, "measurement_time"] = "invalid"
    with pytest.raises(ValueError):
        validate_lab_data(sample_data)
