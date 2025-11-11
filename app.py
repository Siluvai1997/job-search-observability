
import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path
import yaml

st.set_page_config(page_title="Job Application Health Monitor", page_icon="📊", layout="wide")

st.title("Job Application Health Monitor")
st.write("Treat your job search like a DevOps system — visualize application health, status distribution, and trends over time.")

# Load YAML records
jobs = []
root = Path("data/dummy_jobs")
# Auto-generate demo data if folder is empty (for Streamlit Cloud)
if not root.exists() or not any(root.iterdir()):
    import subprocess, sys
    subprocess.run([sys.executable, "generate_dummy_data.py"], check=False)
if not root.exists():
    st.error("No data found. Run: `python generate_dummy_data.py`")
    st.stop()

for company_dir in sorted(root.iterdir()):
    status_file = company_dir / "status.yaml"
    if status_file.exists():
        with open(status_file) as f:
            info = yaml.safe_load(f)
            info["company"] = company_dir.name
            jobs.append(info)

if not jobs:
    st.warning("No job YAML files found. Run: `python generate_dummy_data.py`")
    st.stop()

df = pd.DataFrame(jobs)
# Parse dates
df["date_applied"] = pd.to_datetime(df["date_applied"], errors="coerce")
df["last_update"] = pd.to_datetime(df["last_update"], errors="coerce")

# KPI metrics
total = len(df)
applied = (df["status"] == "applied").sum()
interview = (df["status"] == "interview").sum()
rejected = (df["status"] == "rejected").sum()
offer = (df["status"] == "offer").sum()
success_rate = round(((interview + offer) / total) * 100, 2) if total else 0.0

c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total", total)
c2.metric("Applied", applied)
c3.metric("Interview", interview)
c4.metric("Rejected", rejected)
c5.metric("Offers", offer)

st.progress(success_rate/100.0, text=f"Success Rate: {success_rate}%")

# Status distribution pie (Plotly)
st.subheader("Status Distribution")
status_counts = df["status"].value_counts().reset_index()
status_counts.columns = ["status", "count"]
fig_pie = px.pie(status_counts, names="status", values="count", hole=0.35)
st.plotly_chart(fig_pie, use_container_width=True)

# Table view with filters
st.subheader("Application Summary")
left, right = st.columns([2, 1])
with right:
    status_filter = st.multiselect("Filter by status", options=sorted(df["status"].unique()), default=list(df["status"].unique()))
    role_filter = st.multiselect("Filter by role", options=sorted(df["job_title"].unique()), default=list(df["job_title"].unique()))
    sort_col = st.selectbox("Sort by", options=["date_applied", "last_update", "status", "job_title", "company"], index=0)
with left:
    filtered = df[df["status"].isin(status_filter) & df["job_title"].isin(role_filter)].copy()
    filtered = filtered.sort_values(by=sort_col, ascending=True)
    st.dataframe(filtered[["company", "job_title", "status", "date_applied", "last_update", "notes"]], use_container_width=True)

# --- New: Timeline - Applications per Week
st.subheader("Applications per Week")
weekly = df.set_index("date_applied").sort_index()
weekly_counts = weekly.resample("W-MON").size().reset_index(name="applications")
weekly_counts.rename(columns={"date_applied": "week"}, inplace=True)
fig_line_apps = px.line(weekly_counts, x="week", y="applications", markers=True)
fig_line_apps.update_layout(xaxis_title="Week (starting Monday)", yaxis_title="Applications")
st.plotly_chart(fig_line_apps, use_container_width=True)

# --- New: Weekly Success Rate Trend
st.subheader("Weekly Success Rate (Interview + Offer)")
weekly_status = weekly.resample("W-MON")["status"].value_counts().unstack(fill_value=0).reset_index()
weekly_status.rename(columns={"date_applied": "week"}, inplace=True)

def success_rate_row(row):
    success = row.get("interview", 0) + row.get("offer", 0)
    total = sum([row.get(s, 0) for s in ["applied", "interview", "rejected", "offer"]])
    return (success / total) * 100 if total else 0

weekly_status["success_rate_pct"] = weekly_status.apply(success_rate_row, axis=1)
fig_line_sr = px.line(weekly_status, x="week", y="success_rate_pct", markers=True)
fig_line_sr.update_layout(xaxis_title="Week (starting Monday)", yaxis_title="Success Rate (%)")
st.plotly_chart(fig_line_sr, use_container_width=True)
