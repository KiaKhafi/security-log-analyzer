import json
from pathlib import Path


LOG_FILE = Path("sample.log")
REPORT_FILE = Path("report.json")
FAILED_LOGIN_THRESHOLD = 3


def analyze_log_file(file_path):
    success_count = 0
    failed_count = 0
    failed_by_ip = {}
    malformed_lines = 0

    with file_path.open("r", encoding="utf-8") as log_file:
        for line in log_file:
            if not line.strip():
                continue

            parts = line.strip().split("|")

            if len(parts) != 3:
                malformed_lines += 1
                continue

            ip_address = parts[1].strip()
            status = parts[2].strip()

            if not ip_address:
                malformed_lines += 1
                continue

            if status == "SUCCESS":
                success_count += 1
            elif status == "FAILED":
                failed_count += 1
                failed_by_ip[ip_address] = failed_by_ip.get(ip_address, 0) + 1
            else:
                malformed_lines += 1

    return {
        "successful_logins": success_count,
        "failed_logins": failed_count,
        "total_attempts": success_count + failed_count,
        "failed_attempts_by_ip": failed_by_ip,
        "malformed_lines": malformed_lines,
    }


def save_report(report, file_path):
    with file_path.open("w", encoding="utf-8") as report_file:
        json.dump(report, report_file, indent=4)


def main():
    print("Security Log Analyzer")
    print("Project initialized successfully.")

    try:
        report = analyze_log_file(LOG_FILE)
    except FileNotFoundError:
        print(f"\nError: Log file not found: {LOG_FILE}")
        return
    except OSError as error:
        print(f"\nError: Could not read log file: {error}")
        return

    print("\nAnalysis Report")
    print("-" * 30)
    print(f"Successful logins: {report['successful_logins']}")
    print(f"Failed logins: {report['failed_logins']}")
    print(f"Total login attempts: {report['total_attempts']}")
    print(f"Malformed lines skipped: {report['malformed_lines']}")

    print("\nFailed Attempts by IP")
    print("-" * 30)

    for ip_address, count in report["failed_attempts_by_ip"].items():
        print(f"{ip_address}: {count}")

        if count >= FAILED_LOGIN_THRESHOLD:
            print("  WARNING: Repeated failed logins detected.")

    try:
        save_report(report, REPORT_FILE)
    except OSError as error:
        print(f"\nError: Could not save report: {error}")
        return

    print(f"\nReport saved to {REPORT_FILE}")


if __name__ == "__main__":
    main()
