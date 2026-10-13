import json
from datetime import datetime, timezone
from pathlib import Path


def record_incident(result, path="reports/incidents.jsonl"):
    """Save actionable alerts as structured incident records."""
    alert = result.get("alert", {})
    severity = alert.get("severity")

    if severity not in ("WARNING", "CRITICAL"):
        return None

    incident = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "hostname": result["hostname"],
        "check_type": result["check_type"],
        "severity": severity,
        "message": alert["message"],
        "simulated": result.get("simulated", False),
    }

    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)

    with destination.open("a", encoding="utf-8") as file:
        file.write(json.dumps(incident) + "\n")

    return incident
