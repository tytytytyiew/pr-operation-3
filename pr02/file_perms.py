#!/usr/bin/env python3
import os, sys
path = sys.argv[1] if len(sys.argv) > 1 else "."
st = os.stat(path)
print(f"Путь: {path}")
print(f"Права доступа (octal): {oct(st.st_mode)[-3:]}")
print(f"Размер: {st.st_size} байт")
