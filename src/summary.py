import json
from collections import Counter
from pathlib import Path


def generate_summary(path="logs/network_health.jsonl"):
    """Summarize recorded network monitoring results."""
    log_path = Path(path)

    if not log_path.exists():
        return {"total_checks": 0, "severity_counts": {}}

    counts = Counter()
    total = 0

    with log_path.open(encoding="utf-8") as logfile:
        for line in logfile:
            if not line.strip():
                continue
            record = json.loads(line)
            severity = record.get("alert", {}).get("severity", "UNKNOWN")
            counts[severity] += 1
            total += 1

    return {
        "total_checks": total,
        "severity_counts": dict(counts),
    }


if __name__ == "__main__":
    print(json.dumps(generate_summary(), indent=2))
