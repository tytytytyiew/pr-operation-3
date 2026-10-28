#!/usr/bin/env python3
logs = "[INFO] System OK\n[ERROR] Disk full\n[WARNING] Low memory\n[ERROR] Port bind failed"
print("Все логи:\n", logs)
print("\nОтфильтрованные ошибки ([ERROR]):")
for line in logs.split("\n"):
    if "[ERROR]" in line:
        print(" ->", line)
