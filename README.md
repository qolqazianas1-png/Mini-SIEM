# Mini-SIEM
Mini-SIEM (Security Information and Event Management): Python-based tool that analyzes Linux authentication logs, detects failed login attempts, identifies suspicious IP addresses, and generates basic security reports.

## Features

- Linux authentication log analysis
- Failed login detection
- Successful login tracking
- Suspicious IP identification
- Security report generation

## Project Structure

mini-siem/
├── collector/
├── sample_logs/
├── reports/

## Run

cd collector
python3 log_collector.py

## Example Output

=== SECURITY REPORT ===

Successful logins: 1
Failed logins: 5

Suspicious IPs:

ALERT: 192.168.1.10 -> 5 failed attempts
