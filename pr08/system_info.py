#!/usr/bin/env python3
import platform
import os
import sys

def get_system_report():
    print("=" * 55)
    print(" ПР-8: РАСШИРЕННЫЙ СБОР СИСТЕМНОЙ ИНФОРМАЦИИ ОС")
    print("=" * 55)
    print(f"Операционная система : {platform.system()}")
    print(f"Выпуск ядра (Release): {platform.release()}")
    print(f"Версия сборки (Ver)  : {platform.version()}")
    print(f"Имя хоста (Node name): {platform.node()}")
    print(f"Архитектура процессора: {platform.machine()}")
    print(f"Интерпретатор Python : {platform.python_version()}")
    print(f"Логических ядер CPU  : {os.cpu_count()}")
    print("=" * 55)

if __name__ == "__main__":
    get_system_report()
