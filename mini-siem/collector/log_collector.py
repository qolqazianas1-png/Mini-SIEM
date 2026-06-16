failed_count = 0
success_count = 0
suspicious_ips = {}

with open("../sample_logs/auth.log", "r") as file:
    logs = file.readlines()

for log in logs:
    log = log.strip()

    if "Failed password" in log:
        failed_count += 1

        ip = log.split()[-1]

        if ip not in suspicious_ips:
            suspicious_ips[ip] = 0

        suspicious_ips[ip] += 1

    elif "Accepted password" in log:
        success_count += 1

report = f"""
=== SECURITY REPORT ===

Successful logins: {success_count}
Failed logins: {failed_count}

Suspicious IPs:
"""

for ip, attempts in suspicious_ips.items():
    if attempts >= 3:
        report += f"\nALERT: {ip} -> {attempts} failed attempts"

print(report)

with open("report.txt", "w") as file:
    file.write(report)
