
# Job Application Health Monitor

Monitor your job applications like a DevOps system monitors services.

This Streamlit app reads **privacy-safe dummy YAML records** and visualizes:
- KPIs (Total, Applied, Interview, Rejected, Offers)
- Status distribution (pie)
- Application table with filters
- **Applications per week timeline (Plotly)**
- **Weekly success-rate trend (Plotly)**

> Uses *dummy data* (Company A..N)

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

## Live Demo
Check out the live version of this dashboard on Streamlit Cloud:

### [Job Search Observability – Live Demo](https://job-search-observability-uvm4p3rhcdss5hox2mphbz.streamlit.app/)

This public demo runs directly from the GitHub repo and uses simulated data for privacy.
Feel free to explore:
  - Real-time metrics for job applications (total, interviews, rejections, offers)
  - Status distribution visualization
  - Weekly timeline of applications
  - Success-rate trend analysis
- Built with Python · Streamlit · Plotly · YAML
  Designed to demonstrate how DevOps observability concepts can be applied to everyday workflows like job hunting.

## Ideas to Extend
- Export CSV/PDF report
- Add SLA timers (e.g., auto-flag applications with no response for 14+ days)
- Integrate a Gmail API for private response tracking (keep data local)
- Publish to Streamlit Cloud for a live demo
