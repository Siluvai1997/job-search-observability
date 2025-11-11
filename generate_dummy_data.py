
import os
import random
import datetime
import yaml
from pathlib import Path

def main():
    base = Path("data/dummy_jobs")
    base.mkdir(parents=True, exist_ok=True)

    statuses = ["applied", "interview", "rejected", "offer"]
    companies = [f"Company{chr(65+i)}" for i in range(14)]  # A..N
    roles = ["DevOps Engineer", "Cloud Engineer", "SRE", "Platform Engineer"]

    today = datetime.date.today()
    start_month = 7 if today.month >= 7 else 1
    start = today.replace(month=start_month, day=1)

    rng = random.Random(42)

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
            "notes": f"Simulated record for {company} application."
        }
        with open(job_folder / "status.yaml", "w") as f:
            yaml.safe_dump(info, f, sort_keys=False)

    print(f"Generated dummy data under {base}")

if __name__ == "__main__":
    main()
