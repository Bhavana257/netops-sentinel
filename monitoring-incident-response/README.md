# Data Center Monitoring & Incident Response (local simulation)

A dependency-free Python HTTP metrics exporter, Prometheus scrape configuration, alert rules, optional Docker Compose Grafana stack, and incident runbook. **Alerts are simulated** using a toggle file; no real server outage or hardware repair is claimed.

## Local quick start (Python only)
```bash
python3 -m unittest discover -s tests -v
python3 app/exporter.py --port 9109
# second terminal:
curl -fsS http://127.0.0.1:9109/metrics
```
Create `app/simulate_fault.flag` to trigger `lab_service_up 0`, then remove it to recover. Example: `touch app/simulate_fault.flag` and `rm app/simulate_fault.flag`.

## Optional Prometheus + Grafana (requires Docker Compose and images download)
```bash
docker compose up -d --build
# Prometheus http://localhost:9090 | Grafana http://localhost:3000
# Grafana default admin/admin; change password immediately; local lab only.
```
In Docker Compose, exporter is reachable at `exporter:9109`; Prometheus scrapes every 5s. Grafana provisioning points at Prometheus. Import `dashboards/lab-overview.json` manually if desired. Do not expose these ports publicly.

## Evidence
Capture baseline metric, fault state, alert firing (allow evaluation interval), recovery, and a completed `templates/postmortem.md`.
