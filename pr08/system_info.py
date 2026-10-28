#!/usr/bin/env python3
import platform, os
print("=== Системная информация ОС ===")
print("ОС:", platform.system(), platform.release())
print("Хост:", platform.node())
print("Ядра CPU:", os.cpu_count())
