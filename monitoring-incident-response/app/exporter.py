#!/usr/bin/env python3
import argparse
from http.server import BaseHTTPRequestHandler,ThreadingHTTPServer
from pathlib import Path
FLAG=Path(__file__).with_name('simulate_fault.flag')

def metrics(fault=False):
    return ('# HELP lab_service_up Simulated service availability\n'
            '# TYPE lab_service_up gauge\n'
            f'lab_service_up {0 if fault else 1}\n'
            '# HELP lab_simulated_incident Lab simulated incident state\n'
            '# TYPE lab_simulated_incident gauge\n'
            f'lab_simulated_incident {1 if fault else 0}\n')
class Handler(BaseHTTPRequestHandler):
 def do_GET(self):
  if self.path!='/metrics':
   self.send_error(404); return
  payload=metrics(FLAG.exists()).encode()
  self.send_response(200); self.send_header('Content-Type','text/plain; version=0.0.4'); self.send_header('Content-Length',str(len(payload))); self.end_headers(); self.wfile.write(payload)
if __name__=='__main__':
 p=argparse.ArgumentParser(); p.add_argument('--port',type=int,default=9109); a=p.parse_args()
 print('Metrics listening on',a.port,flush=True)
 ThreadingHTTPServer(('0.0.0.0',a.port),Handler).serve_forever()
