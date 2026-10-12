import os
import numpy as np
import pandas as pd

# ---------- Section A: Setup ----------
np.random.seed(42)
N = 300
os.makedirs("data", exist_ok=True)

ids = [f"S{i:04d}" for i in range(1, N + 1)]
clip = lambda x, lo, hi: np.clip(x, lo, hi)
effort = np.random.normal(0, 1, N)   # hidden "hard-working level" of each student

# ---------- Section B: Academic office ----------
academic = pd.DataFrame({
    "student_id": ids,
    "name": [f"Student {i}" for i in range(1, N + 1)],
    "department": np.random.choice(["CSE", "ECE", "MECH", "CIVIL"], N),
    "cgpa": clip(7.0 + 0.8 * effort + np.random.normal(0, 0.6, N), 3, 10).round(2),
    "backlogs": np.random.poisson(np.clip(0.8 - 0.4 * effort, 0.05, None)),
})

# ---------- Section C: Attendance register ----------
attendance = pd.DataFrame({
    "student_id": ids,
    "attendance_pct": clip(78 + 8 * effort + np.random.normal(0, 7, N), 30, 100).round(1),
})

# ---------- Section D: LMS (online learning portal) ----------
lms = pd.DataFrame({
    "student_id": ids,
    "logins_per_week": np.random.poisson(np.clip(6 + 2 * effort, 1, None)),
    "assignment_completion_pct": clip(75 + 12 * effort + np.random.normal(0, 10, N), 0, 100).round(1),
})

# ---------- Section E: Engagement (clubs, events) ----------
engagement = pd.DataFrame({
    "student_id": ids,
    "events": np.random.poisson(3, N),
    "clubs": np.random.randint(0, 4, N),
    "hackathons": np.random.poisson(1, N),
    "certifications": np.random.poisson(np.clip(1.5 + 0.5 * effort, 0.1, None)),
})

# ---------- Section F: Placement cell ----------
placement = pd.DataFrame({
    "student_id": ids,
    "aptitude": clip(60 + 6 * effort + np.random.normal(0, 12, N), 0, 100).round(0),
    "coding": clip(55 + 8 * effort + np.random.normal(0, 16, N), 0, 100).round(0),
    "mock_interview": clip(55 + 6 * effort + np.random.normal(0, 14, N), 0, 100).round(0),
})

# ---------- Section G: Skills assessment ----------
skills = pd.DataFrame({
    "student_id": ids,
    "technical": clip(60 + 6 * effort + np.random.normal(0, 12, N), 0, 100).round(0),
    "softskill": clip(62 + 4 * effort + np.random.normal(0, 12, N), 0, 100).round(0),
})

# ---------- Section H: Feedback ----------
feedback = pd.DataFrame({
    "student_id": ids,
    "satisfaction": np.random.randint(1, 6, N),
})

# ---------- Section I: Insert Ravi (S0001) ----------
academic.loc[0, ["name", "department", "cgpa", "backlogs"]] = ["Ravi", "CSE", 8.2, 0]
attendance.loc[0, "attendance_pct"] = 82.0
lms.loc[0, ["logins_per_week", "assignment_completion_pct"]] = [5, 70.0]
engagement.loc[0, ["events", "clubs", "hackathons", "certifications"]] = [2, 1, 0, 1]
placement.loc[0, ["aptitude", "coding", "mock_interview"]] = [55, 28, 40]
skills.loc[0, ["technical", "softskill"]] = [50, 60]
feedback.loc[0, "satisfaction"] = 4

# ---------- Section J: Make the data messy (like real life) ----------
attendance.loc[np.random.choice(range(1, N), 12, replace=False), "attendance_pct"] = np.nan
placement.loc[np.random.choice(range(1, N), 10, replace=False), "coding"] = np.nan
lms = pd.concat([lms, lms.sample(5, random_state=1)])

# ---------- Section K: Save each as a CSV ----------
tables = {"academic": academic, "attendance": attendance, "lms": lms,
          "engagement": engagement, "placement": placement,
          "skills": skills, "feedback": feedback}

for name, df in tables.items():
    df.to_csv(f"data/{name}.csv", index=False)
    print(f"Saved data/{name}.csv  ({len(df)} rows)")