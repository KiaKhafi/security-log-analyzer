Security Log Analyzer

A Python command-line tool that analyzes authentication logs, summarizes login activity, identifies repeated failed login attempts by IP address, and exports a JSON report.

Features

Counts successful and failed login attempts.

Calculates the total number of valid login attempts.

Groups failed login attempts by IP address.

Warns when an IP address has three or more failed login attempts.

Detects and counts malformed log entries.

Exports analysis results to a JSON report.

Handles missing log files and file access errors.

Requirements

Python 3.10 or later

No external Python packages are required.

Project Structure

security-log-analyzer/
├── main.py
├── sample.log
├── README.md
├── .gitignore
└── report.json  # Generated when the program runs

Log Format

The input file uses pipe-separated fields in the following format:

timestamp | IP address | status

Supported status values are SUCCESS and FAILED.

Example:

2026-10-28 09:15:00 | 192.168.1.10 | SUCCESS
2026-10-28 09:16:00 | 192.168.1.20 | FAILED
2026-10-28 09:17:00 | 192.168.1.20 | FAILED
2026-10-28 09:18:00 | 192.168.1.20 | FAILED

How to Run

Run the following command from the project directory:

python main.py

The program reads sample.log, displays an analysis summary, and writes the results to report.json.

Example Output

Security Log Analyzer
Project initialized successfully.

Analysis Report
------------------------------
Successful logins: 1
Failed logins: 3
Total login attempts: 4
Malformed lines skipped: 0

Failed Attempts by IP
------------------------------
192.168.1.20: 3
  WARNING: Repeated failed logins detected.

Report saved to report.json

JSON Report

The generated JSON report contains the following fields:

successful_logins: Number of successful login attempts.

failed_logins: Number of failed login attempts.

total_attempts: Total number of valid login attempts.

failed_attempts_by_ip: Failed login counts grouped by IP address.

malformed_lines: Number of invalid log entries skipped during analysis.

Current Limitations

The input and output file paths are configured in the source code.

The tool analyzes log files locally and does not monitor live network traffic.

Repeated failed logins are flagged using a fixed threshold of three attempts per IP address.

Future Improvements

Support command-line arguments for input and output paths.

Add unit tests and automated test coverage.

Improve log validation and reporting.

Support configurable detection thresholds.

Add timestamps and severity levels to security alerts.

Disclaimer

This tool is intended for educational purposes and defensive security log analysis. It does not perform network monitoring, intrusion prevention, or automatic IP blocking.