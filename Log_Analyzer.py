import re

log_file = input("Enter log file path: ")

failed_logins = 0
ips = {}

with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            failed_logins += 1
            
            ip_match = re.search(r'\d+\.\d+\.\d+\.\d+', line)
            if ip_match:
                ip = ip_match.group()
                ips[ip] = ips.get(ip, 0) + 1

print(f"\nFailed login attempts: {failed_logins}\n")

print("Suspicious IPs:")
for ip, count in ips.items():
    if count > 3:
        print(f"{ip} -> {count} attempts")