import sys,unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'app'))
from exporter import metrics
class ExporterTests(unittest.TestCase):
 def test_healthy(self): self.assertIn('lab_service_up 1',metrics(False))
 def test_fault(self):
  self.assertIn('lab_service_up 0',metrics(True))
  self.assertIn('lab_simulated_incident 1',metrics(True))
