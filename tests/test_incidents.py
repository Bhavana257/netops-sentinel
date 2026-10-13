import json
import tempfile
import unittest
from pathlib import Path

from src.alerts import evaluate_alert
from src.incidents import record_incident


class TestIncidentRecording(unittest.TestCase):

    def test_critical_incident_saved(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "incidents.jsonl"
            result = {
                "hostname": "test.local",
                "check_type": "TCP",
                "status": "DOWN",
                "simulated": True,
            }
            result["alert"] = evaluate_alert(result)

            incident = record_incident(result, path)

            self.assertEqual(incident["severity"], "CRITICAL")
            self.assertTrue(incident["simulated"])
            self.assertEqual(
                json.loads(path.read_text())["severity"],
                "CRITICAL",
            )

    def test_healthy_result_not_recorded(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "incidents.jsonl"
            result = {
                "hostname": "test.local",
                "check_type": "DNS",
                "status": "UP",
                "response_ms": 50,
            }
            result["alert"] = evaluate_alert(result)

            self.assertIsNone(record_incident(result, path))
            self.assertFalse(path.exists())
