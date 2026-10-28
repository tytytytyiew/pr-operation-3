import sys
import os

# Проверяем аргумент командной строки или берем файл по умолчанию
log_file = sys.argv[1] if len(sys.argv) > 1 else "data/01.log"

if os.path.exists(log_file):
    size = os.path.getsize(log_file)
    print(f"Файл найден: {log_file} (размер: {size} байт)")
else:
    print(f"Внимание: файл {log_file} не существует.")
