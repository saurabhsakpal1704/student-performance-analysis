from pathlib import Path
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Student Performance Analytics", page_icon="📊", layout="wide")
st.title("📊 Student Performance Analysis")
st.caption("Synthetic demonstration dataset. No real student records are included.")
path = Path("data/student_performance.csv")
if not path.exists():
    st.warning("Run `python generate_data.py` first.")
    st.stop()
df = pd.read_csv(path)
with st.sidebar:
    st.header("Filters")
    courses = st.multiselect("Course", sorted(df.course.unique()), default=sorted(df.course.unique()))
    cohorts = st.multiselect("Cohort", sorted(df.cohort.unique()), default=sorted(df.cohort.unique()))
    threshold = st.slider("Pass threshold", 0, 100, 40)
filtered = df[df.course.isin(courses) & df.cohort.isin(cohorts)].copy()
if filtered.empty:
    st.info("No rows match these filters.")
    st.stop()
a,b,c = st.columns(3)
a.metric("Learners in view", len(filtered))
b.metric("Average assessment", f"{filtered.assessment_score.mean():.1f}/100")
c.metric("Pass rate", f"{(filtered.assessment_score >= threshold).mean():.1%}")
left,right = st.columns(2)
left.plotly_chart(px.histogram(filtered, x="assessment_score", nbins=20, title="Assessment score distribution"), use_container_width=True)
right.plotly_chart(px.scatter(filtered, x="attendance_pct", y="assessment_score", color="course", title="Attendance vs assessment score"), use_container_width=True)
st.plotly_chart(px.box(filtered, x="cohort", y="assessment_score", color="course", title="Scores by cohort and course"), use_container_width=True)
st.download_button("Download filtered data", filtered.to_csv(index=False).encode(), "filtered_student_performance.csv", "text/csv")
with st.expander("View data"):
    st.dataframe(filtered, use_container_width=True)
