import json
import tempfile
import unittest
from pathlib import Path

from src.summary import generate_summary


class TestSummary(unittest.TestCase):

    def test_counts_alert_severities(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "health.jsonl"
            records = [
                {"alert": {"severity": "OK"}},
                {"alert": {"severity": "WARNING"}},
                {"alert": {"severity": "CRITICAL"}},
                {"alert": {"severity": "OK"}},
            ]
            path.write_text(
                "".join(json.dumps(r) + "\n" for r in records)
            )

            result = generate_summary(path)
            self.assertEqual(result["total_checks"], 4)
            self.assertEqual(result["severity_counts"]["OK"], 2)
            self.assertEqual(result["severity_counts"]["WARNING"], 1)
            self.assertEqual(result["severity_counts"]["CRITICAL"], 1)

    def test_missing_log_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "missing.jsonl"
            result = generate_summary(path)
            self.assertEqual(result["total_checks"], 0)
            self.assertEqual(result["severity_counts"], {})
