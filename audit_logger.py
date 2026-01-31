import json
import os
from datetime import datetime

def save_audit(file_name, risk_score):
    log_folder = "audit_logs"
    os.makedirs(log_folder, exist_ok=True)

    log = {
        "file": file_name,
        "timestamp": str(datetime.now()),
        "risk": risk_score
    }

    file_path = os.path.join(log_folder, "audit.json")

    with open(file_path, "a") as f:
        f.write(json.dumps(log) + "\n")
