
-- ICU Data Engineering Project
-- Synthetic data for educational and research practice

CREATE TABLE patients (
    patient_id INTEGER PRIMARY KEY,
    age INTEGER,
    sex VARCHAR(10)
);

CREATE TABLE icu_stays (
    stay_id INTEGER PRIMARY KEY,
    patient_id INTEGER REFERENCES patients(patient_id),
    admission_time TIMESTAMP,
    discharge_time TIMESTAMP
);

CREATE TABLE lab_results (
    lab_id INTEGER PRIMARY KEY,
    stay_id INTEGER REFERENCES icu_stays(stay_id),
    test_name VARCHAR(100),
    test_value NUMERIC(10,2),
    unit VARCHAR(30),
    measurement_time TIMESTAMP
);

CREATE TABLE vital_signs (
    vital_id INTEGER PRIMARY KEY,
    stay_id INTEGER REFERENCES icu_stays(stay_id),
    heart_rate INTEGER,
    systolic_bp INTEGER,
    measurement_time TIMESTAMP
);

CREATE INDEX idx_lab_stay_time
ON lab_results(stay_id, measurement_time);

-- Synthetic patient records

INSERT INTO patients VALUES
(1, 65, 'Male'),
(2, 54, 'Female'),
(3, 72, 'Male');

-- Synthetic ICU stays

INSERT INTO icu_stays VALUES
(101, 1, '2026-01-10 08:00', '2026-01-16 12:00'),
(102, 2, '2026-01-11 08:00', '2026-01-17 12:00'),
(103, 3, '2026-01-12 07:00', '2026-01-18 12:00');

-- Synthetic laboratory measurements

INSERT INTO lab_results VALUES
(1, 101, 'Creatinine', 0.90, 'mg/dL', '2026-01-10 09:00'),
(2, 101, 'Creatinine', 1.20, 'mg/dL', '2026-01-11 09:00'),
(3, 102, 'Creatinine', 1.10, 'mg/dL', '2026-01-11 10:00'),
(4, 102, 'Creatinine', 1.20, 'mg/dL', '2026-01-12 10:00'),
(5, 103, 'Creatinine', 0.80, 'mg/dL', '2026-01-12 08:00'),
(6, 103, 'Creatinine', 1.40, 'mg/dL', '2026-01-13 08:00');

-- Synthetic vital signs

INSERT INTO vital_signs VALUES
(1, 101, 95, 110, '2026-01-10 09:00'),
(2, 102, 82, 120, '2026-01-11 10:00'),
(3, 103, 110, 95, '2026-01-12 08:00');
