#!/usr/bin/env python3
import platform, os
print("=== Системная информация ===")
print("ОС:", platform.system(), platform.release())
print("Ядра CPU:", os.cpu_count())
