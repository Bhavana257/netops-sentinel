# NetOps Sentinel — Troubleshooting Runbook

## 1. Alert Triage
- OK: Check passed within the configured latency threshold.
- WARNING: Check passed but exceeded the latency threshold.
- CRITICAL: DNS resolution or TCP connection failed.

## 2. DNS Failure
1. Check hostname spelling and configuration.
2. Run `getent hosts google.com` for an authorized target.
3. Inspect `/etc/resolv.conf`.
4. Compare DNS results with another trusted resolver if permitted.
5. Record findings and retry the check.

## 3. TCP Connection Failure
1. Verify the target hostname and port.
2. Run `nc -vz -w 3 google.com 443` if netcat is installed.
3. Check service availability and firewall rules.
4. Review routing and connectivity.
5. Escalate unresolved service failures.

## 4. High Latency
1. Compare current and historical response times.
2. Repeat checks to rule out transient delays.
3. Check local network load and system resource usage.
4. Review DNS and TCP timings separately.

## 5. Incident Documentation
Record the affected target, detection time, severity, diagnostic evidence, actions taken, and resolution.

## 6. Safety
Monitor only authorized targets. Never disable firewalls or modify production network settings without approval. Distinguish simulated incidents from real outages.
