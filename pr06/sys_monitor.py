#!/usr/bin/env python3
import os
import sys
import time
import datetime

def get_cpu_load():
    """Считывает загрузку процессора из /proc/loadavg."""
    try:
        with open("/proc/loadavg", "r") as f:
            load = f.read().split()[:3]
        return f"Load Average (1m, 5m, 15m): {load[0]}, {load[1]}, {load[2]}"
    except Exception as e:
        return f"Ошибка чтения CPU: {e}"

def get_memory_info():
    """Считывает использование памяти из /proc/meminfo."""
    mem_info = {}
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                parts = line.split(':')
                if len(parts) == 2:
                    key = parts[0].strip()
                    val = parts[1].strip().split()[0] # в килобайтах
                    mem_info[key] = int(val)
        
        total_kb = mem_info.get("MemTotal", 1)
        free_kb = mem_info.get("MemAvailable", mem_info.get("MemFree", 0))
        used_kb = total_kb - free_kb
        
        percent = (used_kb / total_kb) * 100
        return f"Память: всего {total_kb // 1024} МБ, занято {used_kb // 1024} МБ ({percent:.1f}%)."
    except Exception as e:
        return f"Ошибка чтения памяти: {e}"

def get_disk_info():
    """Проверяет свободное место на корневом диске."""
    try:
        st = os.statvfs("/")
        total = (st.f_blocks * st.f_frsize) / (1024 * 1024 * 1024)
        free = (st.f_bavail * st.f_frsize) / (1024 * 1024 * 1024)
        used = total - free
        percent = (used / total) * 100
        return f"Диск '/': всего {total:.1f} ГБ, свободно {free:.1f} ГБ (использовано {percent:.1f}%)."
    except Exception as e:
        return f"Ошибка диска: {e}"

def main():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("=" * 60)
    print(f"  СИСТЕМНЫЙ МОНИТОР (Вариант B) | {now}")
    print("=" * 60)
    print(f"[+] {get_cpu_load()}")
    print(f"[+] {get_memory_info()}")
    print(f"[+] {get_disk_info()}")
    print("-" * 60)

if __name__ == "__main__":
    main()
