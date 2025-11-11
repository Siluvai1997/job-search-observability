# Job Search Observability

> A Streamlit + Plotly dashboard that visualizes your job-application health using dummy data for privacy. Demonstrates data automation, observability concepts, and dashboard design — DevOps applied to everyday life.

---

## Live Demo
**[Open in Streamlit](https://job-search-observability-uvm4p3rhcdss5hox2mphbz.streamlit.app/)**

This interactive dashboard visualizes your job applications as if they were production services, applying **DevOps observability** principles to your career tracking.

---

## Overview

**Job Search Observability** is a Python + Streamlit dashboard that tracks and analyzes your job applications with the same approach DevOps teams use to monitor system health.

It helps visualize:

- Total applications, interviews, offers, and rejections  
- Status distribution  
- Applications per week  
- Weekly success-rate trends  
- Filterable data table for analysis

---

## Tech Stack

| Component | Technology |
|------------|-------------|
| UI / Dashboard | Streamlit |
| Data Handling | Pandas |
| Visualization | Plotly |
| Data Format | YAML (for demo dataset) |
| Language | Python 3.10+ |

---

## Repository Structure

```
job-search-observability/
├── app.py                        # Streamlit app
├── generate_dummy_data.py        # Optional data generator
├── data/
│   └── dummy_jobs/               # Pre-generated demo YAML files
├── requirements.txt
├── README.md
└── docs/
    └── architecture_diagram.txt
```

---

## Demo Data

This dashboard uses **pre-generated dummy YAML files** stored under  
`data/dummy_jobs/` to simulate real job-application data.

Each record represents a different company and contains:

```yaml
job_title: Cloud Engineer
status: interview
date_applied: 2025-09-14
last_update: 2025-09-25
notes: "Demo record for visualization."
```

The data is intentionally fictional and safe to publish.  
You can view or edit these files directly to adjust the dashboard visuals.

---

## Generate New Dummy Data (Optional)

The included `generate_dummy_data.py` script can be used to generate new demo data locally:

```bash
python generate_dummy_data.py
```

It creates about **20–30 randomized YAML files** under `data/dummy_jobs/`, each simulating a unique company and application status.

Commit and push these new files to update your public dashboard.

---

## How to Run Locally

```bash
# 1. Clone the repo
git clone https://github.com/Siluvai1997/job-search-observability.git
cd job-search-observability

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run Streamlit app
streamlit run app.py
```

Then open your browser at **http://localhost:8501**

---

## Concept Inspiration

> "If we monitor systems to ensure uptime, why not monitor our job search the same way?"

This project applies the **DevOps mindset** to personal career management — tracking outcomes, metrics, and performance indicators like a production-grade system.

---

## Future Enhancements

- Add email or LinkedIn API integration for auto-tracking responses  
- Introduce analytics for “response rate per job board”  
- Export dashboards as PDF reports  
- Integrate persistent storage for long-term history  

---

⭐ If you like this project, consider giving it a star on GitHub — it helps more people discover it!
