# Smart Campus Analytics: Student Success Platform

An analytics dashboard that integrates student data from 7 sources, calculates a
Student Success Score, flags at-risk students, and suggests actions for faculty
and administrators.

**Live demo:** https://your-app-name.streamlit.app

## What it does
- Integrates academic, attendance, LMS, engagement, placement, skills and feedback data
- Cleans the data (duplicates removed, missing values filled with department medians)
- Calculates a weighted Student Success Score (0-100)
- Flags academic risk and placement risk separately
- Explains each score (which indicators pull it up or down)
- Segments students and recommends an action for each group

## Tech stack
Python, pandas, NumPy, scikit-learn (KMeans), Streamlit, Plotly

## Project structure
- `generate_data.py`: creates synthetic student data (7 CSV files in `data/`)
- `pipeline.py`: cleaning, merging, scoring, risk flags, explainability, segmentation
- `app.py`: the Streamlit dashboard

## Run locally
pip install -r requirements.txt
python generate_data.py
streamlit run app.py

## Note
All data is synthetic, created to protect student privacy. The pipeline works
unchanged on real exports with the same columns.