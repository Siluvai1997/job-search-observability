import os
import random
import datetime
import yaml
import tempfile
from pathlib import Path

def main():
    # use /tmp so Streamlit Cloud can write
    base = Path(tempfile.gettempdir()) / "dummy_jobs"
    base.mkdir(parents=True, exist_ok=True)

    statuses = ["applied", "interview", "rejected", "offer"]
    companies = [f"Company{chr(65+i)}" for i in range(20)]
    roles = ["DevOps Engineer", "Cloud Engineer", "SRE", "Platform Engineer", "DevOps Analyst", "Infrastructure Engineer", "Kubernetes Engineer"]

    today = datetime.date.today()
    start = today.replace(month=max(1, today.month - 4), day=1)
    rng = random.Random()

    for company in companies:
        job_folder = base / company
        job_folder.mkdir(parents=True, exist_ok=True)
        delta_days = rng.randint(0, max(1, (today - start).days))
        date_applied = start + datetime.timedelta(days=delta_days)
        status = rng.choices(statuses, weights=[50, 20, 25, 5])[0]
        last_update = date_applied + datetime.timedelta(days=rng.randint(1, 21))
        info = {
            "job_title": rng.choice(roles),
            "status": status,
            "date_applied": str(date_applied),
            "last_update": str(min(last_update, today)),
            "notes": f"Simulated record for {company} application.",
        }
        with open(job_folder / "status.yaml", "w") as f:
            yaml.safe_dump(info, f)

    print(f" Dummy data created under {base}")
    return base

if __name__ == "__main__":
    main()
