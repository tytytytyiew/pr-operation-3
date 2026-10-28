#!/usr/bin/env python3
import os
import sys

def list_directory(path="."):
    print(f"Содержимое директории: {os.path.abspath(path)}")
    print("-" * 40)
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        item_type = "DIR " if os.path.isdir(item_path) else "FILE"
        print(f"[{item_type}] {item}")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "."
    list_directory(target)
