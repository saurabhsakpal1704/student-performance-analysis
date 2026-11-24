# Student Performance Analysis

A Python analytics project that explores attendance, study time, assignment completion and assessment scores, with a Streamlit dashboard.

> **Demo-data note:** the generator creates synthetic student-like records. It is not real student data.

## Setup
```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
pip install -r requirements.txt
python generate_data.py
streamlit run app.py
```

## What it includes
- Synthetic CSV generator with a fixed random seed
- Summary statistics and pass-rate calculations
- Score distributions and attendance relationship plots
- Filters for course and cohort
- Downloadable filtered CSV from the dashboard

## Replace with your own data
Create `data/student_performance.csv` with columns: `student_id`, `course`, `cohort`, `attendance_pct`, `study_hours_week`, `assignments_completed_pct`, `assessment_score`. Only use data you are authorized to process, and remove direct identifiers before analysis.
