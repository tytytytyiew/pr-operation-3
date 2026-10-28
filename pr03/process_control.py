#!/usr/bin/env python3
import os
import time
import subprocess

def process_lab():
    print("=" * 60)
    print(" PR-3: LAB - PROCESS MANAGEMENT & SIGNALS")
    print("=" * 60)
    
    my_pid = os.getpid()
    parent_pid = os.getppid()
    
    print(f"Current Process PID   : {my_pid}")
    print(f"Parent Process PPID   : {parent_pid}")
    print(f"Process Group ID      : {os.getpgrp()}")
    
    # Демонстрация порождения дочернего процесса (fork имитация через subprocess)
    print("\nSpawning a child process (sleep 1)...")
    child = subprocess.Popen(["sleep", "1"])
    print(f"Spawned child PID     : {child.pid}")
    
    child.wait()
    print("Child process finished successfully.")
    
    print("\nListing current python process using 'ps':")
    subprocess.run(["ps", "-fp", str(my_pid)])
    print("=" * 60)

if __name__ == "__main__":
    process_lab()
