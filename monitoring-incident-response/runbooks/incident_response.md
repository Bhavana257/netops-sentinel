# Simulated monitoring incident runbook
1. Start exporter, Prometheus, Grafana using README.
2. Verify `lab_service_up == 1` in Prometheus.
3. Create `app/simulate_fault.flag` on host; exporter detects it (Docker bind mount).
4. Verify `lab_service_up == 0`; wait ~15–30 seconds for `SimulatedServiceDown` to fire.
5. Remove the flag and verify recovery to 1 and alert resolution.
6. Complete postmortem, attach screenshots with timestamps, distinguish simulated signal from actual server failure.
7. Stop stack: `docker compose down`.
