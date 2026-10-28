#!/usr/bin/env python3
import sys
import io

def text_streams_lab():
    print("=" * 60)
    print(" PR-4: LAB - TEXT STREAMS, PIPES AND LOG FILTERING")
    print("=" * 60)
    
    # Имитируем системный поток логов /var/log/syslog
    mock_log_data = """
    Oct 28 10:00:01 server systemd[1]: Started Session 1 of user root.
    Oct 28 10:05:12 server kernel: [ 0.000000] Linux version 5.15.153
    Oct 28 10:12:44 server sshd[412]: Failed password for invalid user from 192.168.1.50
    Oct 28 10:15:00 server CRON[500]: (root) CMD (command -v debian-sa1)
    Oct 28 10:20:33 server kernel: Out of memory: Kill process 891 (python3)
    """
    
    print("Original Stream Content:")
    print(mock_log_data.strip())
    
    print("\nFiltering lines containing 'kernel' or 'Failed':")
    for line in mock_log_data.strip().split("\n"):
        if "kernel" in line or "Failed" in line:
            print("  MATCH ->", line.strip())
            
    print("=" * 60)

if __name__ == "__main__":
    text_streams_lab()
