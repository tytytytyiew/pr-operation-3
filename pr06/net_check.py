#!/usr/bin/env python3
import subprocess
print("Проверка соединения с localhost:")
subprocess.run(["ping", "-c", "2", "127.0.0.1"])
