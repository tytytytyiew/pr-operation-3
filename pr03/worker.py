import time
import os

print(f"Запущен рабочий процесс. PID: {os.getpid()}")
while True:
    time.sleep(5)
