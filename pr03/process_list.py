#!/usr/bin/env python3
import os
print(f"Текущий PID: {os.getpid()}, Родительский PPID: {os.getppid()}")
print("Активные процессы в системе:")
os.system("ps aux | head -n 6")
