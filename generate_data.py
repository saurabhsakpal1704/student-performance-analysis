from pathlib import Path
import numpy as np
import pandas as pd

rng = np.random.default_rng(24)
n = 500
attendance = np.clip(rng.normal(82, 12, n), 35, 100)
study = np.clip(rng.gamma(2.5, 2.0, n), 0, 25)
assignments = np.clip(rng.normal(78, 18, n), 10, 100)
noise = rng.normal(0, 9, n)
score = np.clip(18 + 0.34*attendance + 0.75*study + 0.22*assignments + noise, 0, 100)
df = pd.DataFrame({
    "student_id": [f"DEMO-{i:04d}" for i in range(1, n+1)],
    "course": rng.choice(["Computer Science", "Data Science", "Business", "Engineering"], n),
    "cohort": rng.choice(["2024", "2025", "2026"], n),
    "attendance_pct": attendance.round(1),
    "study_hours_week": study.round(1),
    "assignments_completed_pct": assignments.round(1),
    "assessment_score": score.round(1)
})
out = Path("data/student_performance.csv")
out.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(out, index=False)
print(f"Created {n} synthetic demo records at {out}")
