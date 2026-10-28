#!/usr/bin/env python3
import platform
import os
import sys

def hardware_lab():
    print("=" * 60)
    print(" PR-8: LAB - HARDWARE RESOURCES & OS KERNEL MONITORING")
    print("=" * 60)
    
    print(f"OS System          : {platform.system()}")
    print(f"OS Release         : {platform.release()}")
    print(f"Kernel Version     : {platform.version()}")
    print(f"Machine Arch       : {platform.machine()}")
    print(f"Processor Name     : {platform.processor() or 'x86_64 CPU'}")
    print(f"Logical CPU Cores  : {os.cpu_count()}")
    
    # Чтение виртуальных файлов ядра Linux из /proc
    if platform.system().lower() == "linux":
        print("\n[Reading /proc/cpuinfo model name]:")
        try:
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if "model name" in line:
                        print("  ", line.strip())
                        break
        except Exception as e:
            print("  Could not read /proc/cpuinfo:", e)
            
        print("\n[Reading /proc/meminfo RAM stats]:")
        try:
            with open("/proc/meminfo", "r") as f:
                for i in range(3):
                    print("  ", f.readline().strip())
        except Exception as e:
            print("  Could not read /proc/meminfo:", e)
            
    print("=" * 60)

if __name__ == "__main__":
    hardware_lab()
