import json
from datetime import datetime, timezone
from pathlib import Path

from src.monitor import check_dns, check_tcp
from src.alerts import evaluate_alert
from src.incidents import record_incident


def run_monitoring():
    config = json.loads(Path("config/targets.json").read_text())
    warning_ms = config["warning_latency_ms"]
    log_path = Path("logs/network_health.jsonl")
    log_path.parent.mkdir(parents=True, exist_ok=True)

    with log_path.open("a", encoding="utf-8") as logfile:
        for target in config["targets"]:
            hostname = target["hostname"]
            results = []

            if "DNS" in target["checks"]:
                results.append(check_dns(hostname))

            if "TCP" in target["checks"]:
                results.append(check_tcp(
                    hostname,
                    target["tcp_port"],
                    timeout=target.get("timeout_seconds", 3),
                ))

            for result in results:
                record = {
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "check_type": "TCP" if "port" in result else "DNS",
                    **result,
                }
                record["alert"] = evaluate_alert(result, warning_ms)
                record_incident(record)
                logfile.write(json.dumps(record) + "\n")
                print(json.dumps(record))


if __name__ == "__main__":
    run_monitoring()
