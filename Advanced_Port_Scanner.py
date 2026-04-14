import socket
from concurrent.futures import ThreadPoolExecutor

target = input("Enter target IP or domain: ")
ports = range(1, 1025)

def scan_port(port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((target, port))
        
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"
        
        print(f"[OPEN] Port {port} | {banner}")
        s.close()
    except:
        pass

print(f"\nScanning {target}...\n")

with ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(scan_port, ports)