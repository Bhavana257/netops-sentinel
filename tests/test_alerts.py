import unittest
from src.alerts import evaluate_alert


class TestAlertEngine(unittest.TestCase):

    def test_healthy_network(self):
        result = {"hostname": "localhost", "status": "UP", "response_ms": 50}
        self.assertEqual(evaluate_alert(result)["severity"], "OK")

    def test_high_latency(self):
        result = {"hostname": "localhost", "status": "UP", "response_ms": 350}
        self.assertEqual(evaluate_alert(result)["severity"], "WARNING")

    def test_connection_failure(self):
        result = {"hostname": "localhost", "status": "DOWN"}
        self.assertEqual(evaluate_alert(result)["severity"], "CRITICAL")

    def test_threshold_boundary(self):
        result = {"hostname": "localhost", "status": "UP", "response_ms": 200}
        self.assertEqual(evaluate_alert(result)["severity"], "OK")


if __name__ == "__main__":
    unittest.main()
