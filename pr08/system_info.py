#!/usr/bin/env python3
import platform, os
print("=== Системная информация ОС ===")
print("ОС:", platform.system(), platform.release())
print("Хост:", platform.node())
print("Архитектура:", platform.machine())
print("Ядра процессора:", os.cpu_count())
