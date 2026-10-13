# NetOps Sentinel

Automated Network Diagnostics and Incident Monitoring System.

## Overview
NetOps Sentinel is a Python-based monitoring application developed on Ubuntu Linux using WSL. It checks network connectivity, detects failures, generates alerts, and records incidents.

## Features
- DNS resolution and response-time monitoring
- TCP port connectivity checks
- Configurable monitoring targets and thresholds
- OK, WARNING, and CRITICAL alert classification
- Automated incident recording
- JSONL logging and monitoring summaries
- Continuous monitoring with configurable intervals
- Automated unit tests
- Simulated failure detection

## Technologies
Python 3, Linux, TCP/IP, DNS, JSON, unittest.

## Usage
Run these commands from the project root:

- Single monitoring cycle: `python3 -m src.runner`
- Continuous monitoring: `python3 -m src.scheduler --interval 60 --cycles 0`
- Summary report: `python3 -m src.summary`
- Automated tests: `python3 -m unittest discover -s tests -v`

Press Ctrl+C to stop continuous monitoring.

## Configuration
Edit `config/targets.json` to configure monitoring targets, TCP ports, and latency thresholds.

## Safety
Only monitor authorized systems. DNS and TCP checks do not guarantee full application health. Simulated failures are distinguished from actual observations.

## Project Purpose
Demonstrates Linux networking, Python automation, infrastructure monitoring, incident detection, and troubleshooting skills.
