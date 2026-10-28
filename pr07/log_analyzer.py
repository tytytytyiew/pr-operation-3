#!/usr/bin/env python3
import sys
import os
import glob

def analyze_logs(log_dir):
    if not os.path.exists(log_dir):
        print(f"Ошибка: Директория {log_dir} не найдена.")
        return

    log_files = glob.glob(os.path.join(log_dir, "*.log"))
    print(f"Найдено лог-файлов для анализа: {len(log_files)}")
    
    error_count = 0
    warn_count = 0

    for file_path in log_files:
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if "ERROR" in line:
                    error_count += 1
                elif "WARN" in line:
                    warn_count += 1

    print("==========================================")
    print("         ОТЧЕТ АНАЛИЗА ЛОГОВ              ")
    print("==========================================")
    print(f"Всего ошибок (ERROR) : {error_count}")
    print(f"Всего предупреждений : {warn_count}")
    print("==========================================")

if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "data"
    analyze_logs(target)
