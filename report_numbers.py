from pipeline import build, load_and_merge

df = build()
_, report = load_and_merge()

print("=== CLEANING ===")
for k, v in report.items():
    print(f"{k}: {v}")

print("\n=== OVERVIEW ===")
print("Students:", len(df))
print("Average Success Score:", round(df["success_score"].mean(), 1))
print(df["risk_level"].value_counts().to_string())
print("Academic risk:", int(df["academic_risk"].sum()))
print("Placement risk:", int(df["placement_risk"].sum()))

print("\n=== INSIGHTS ===")
hidden = df[(df["risk_level"] == "Low") & df["placement_risk"]]
print("Hidden placement risk (overall score looks Low risk):", len(hidden))

strong = df[df["cgpa"] > 7.5]
print(f"CGPA > 7.5 with placement risk: "
      f"{strong['placement_risk'].mean() * 100:.0f}% of {len(strong)} students")

low = df[df["attendance_pct"] < 65]
ok = df[df["attendance_pct"] >= 65]
if len(low) > 0:
    gap = ok["success_score"].mean() - low["success_score"].mean()
    print(f"Attendance < 65%: {len(low)} students, score {gap:.1f} points lower")

lms = df.groupby("department")["lms"].mean().round(0)
print("Lowest LMS department:", lms.idxmin(), int(lms.min()))

print("\nAverage score by department:")
print(df.groupby("department")["success_score"].mean().round(1).to_string())

print("\nStudents per segment:")
print(df["segment"].value_counts().to_string())