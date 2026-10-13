def evaluate_alert(result, warning_ms=200):
    """Classify a monitoring result by severity."""
    if result["status"] != "UP":
        severity = "CRITICAL"
        message = "Network diagnostic check failed"
    elif result.get("response_ms", 0) > warning_ms:
        severity = "WARNING"
        message = "Network response exceeded latency threshold"
    else:
        severity = "OK"
        message = "Network diagnostic check passed"

    return {
        "hostname": result["hostname"],
        "check_type": "TCP" if "port" in result else "DNS",
        "severity": severity,
        "message": message,
    }
