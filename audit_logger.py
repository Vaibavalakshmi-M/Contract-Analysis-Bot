import json
from datetime import datetime

def save_audit(file_name, risk_score):
    log = {
        "file": file_name,
        "timestamp": str(datetime.now()),
        "risk": risk_score
    }

    with open("audit_logs/audit.json", "a") as f:
        f.write(json.dumps(log) + "\n")
