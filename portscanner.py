import socket
import sys
from datetime import datetime

target ="45.33.32.156"

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("[-] Hostname could not be resolved.")
    sys.exit()

print(f"\n[+] Starting scan on: {target_ip}")
start_time = datetime.now()

for port in range(1, 101):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(0.5)

    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"[+] Port {port} is OPEN")
    s.close()

end_time = datetime.now()
total_time = end_time - start_time
print(f"\n[+] Scan completed in: {total_time}")
