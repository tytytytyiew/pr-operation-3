#!/usr/bin/env python3
import os, sys
path = sys.argv[1] if len(sys.argv) > 1 else "."
print(f"Содержимое: {os.path.abspath(path)}")
for i in os.listdir(path):
    print("DIR " if os.path.isdir(os.path.join(path, i)) else "FILE", i)
