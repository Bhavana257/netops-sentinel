import socket
import time


def check_dns(hostname):
    """Resolve a hostname and return diagnostic results."""
    start = time.monotonic()

    try:
        ip_address = socket.gethostbyname(hostname)
        return {
            "hostname": hostname,
            "status": "UP",
            "ip_address": ip_address,
            "response_ms": round(
                (time.monotonic() - start) * 1000, 2
            ),
        }
    except socket.gaierror as error:
        return {
            "hostname": hostname,
            "status": "DOWN",
            "ip_address": None,
            "error": str(error),
        }


def check_tcp(hostname, port, timeout=3):
    """Check TCP connectivity and measure connection latency."""
    start = time.monotonic()
    try:
        with socket.create_connection((hostname, port), timeout=timeout):
            return {
                "hostname": hostname,
                "port": port,
                "status": "UP",
                "response_ms": round((time.monotonic() - start) * 1000, 2),
            }
    except (OSError, ValueError) as error:
        return {
            "hostname": hostname,
            "port": port,
            "status": "DOWN",
            "error": str(error),
        }
