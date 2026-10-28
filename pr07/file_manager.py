#!/usr/bin/env python3
import os, sys
path = sys.argv[1] if len(sys.argv) > 1 else "."
print(f"=== Обход директории: {os.path.abspath(path)} ===")
for root, dirs, files in os.walk(path):
    print(f"Папка: {root}")
    for f in files:
        print(f"  [FILE] {f}")
