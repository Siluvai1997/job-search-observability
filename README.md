
# Job Application Health Monitor

Monitor your job applications like a DevOps system monitors services.

This Streamlit app reads **privacy-safe dummy YAML records** and visualizes:
- KPIs (Total, Applied, Interview, Rejected, Offers)
- Status distribution (pie)
- Application table with filters
- **Applications per week timeline (Plotly)**
- **Weekly success-rate trend (Plotly)**

> Uses *dummy data* (Company A..N) so you can publish this repo safely.

## Tech Stack
- Python 3.10+
- Streamlit
- Pandas
- PyYAML
- Plotly

## Run Locally
```bash
pip install -r requirements.txt
python generate_dummy_data.py   # creates data/dummy_jobs/* with YAML files
streamlit run app.py
```

## Project Layout
```
job-application-health-monitor/
├── app.py
├── generate_dummy_data.py
├── data/
│   └── dummy_jobs/     # created by generate_dummy_data.py
├── requirements.txt
├── README.md
└── docs/
    └── architecture_diagram.txt
```

## Privacy Note
All records are simulated; no real company names or job details are included.  
For private usage, point the app to your real folder structure *without committing data* to Git.

## Ideas to Extend
- Export CSV/PDF report
- Add SLA timers (e.g., auto-flag applications with no response for 14+ days)
- Integrate a Gmail API for private response tracking (keep data local)
- Publish to Streamlit Cloud for a live demo
