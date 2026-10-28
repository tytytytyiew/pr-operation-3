#!/usr/bin/env python3
import socket
import subprocess
import platform

def network_lab():
    print("=" * 60)
    print(" PR-6: LAB - NETWORK INTERFACES AND SOCKET DIAGNOSTICS")
    print("=" * 60)
    
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print(f"Local Hostname  : {hostname}")
    print(f"Resolved IP     : {local_ip}")
    
    # Проверка сетевого соединения через loopback
    target = "127.0.0.1"
    flag = "-n" if platform.system().lower() == "windows" else "-c"
    
    print(f"\nPinging loopback ({target})...")
    try:
        res = subprocess.run(["ping", flag, "2", target], capture_output=True, text=True, timeout=5)
        print(res.stdout if res.stdout else res.stderr)
    except Exception as e:
        print("Ping execution failed:", e)
    print("=" * 60)

if __name__ == "__main__":
    network_lab()
