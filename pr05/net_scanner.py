#!/usr/bin/env python3
import socket
import subprocess
import sys
import os

def check_host(host):
    """Проверяет доступность узла через системную команду ping."""
    param = '-c' if sys.platform != 'win32' else '-n'
    command = ['ping', param, '1', host]
    try:
        output = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=3)
        return output.returncode == 0
    except subprocess.TimeoutExpired:
        return False

def get_network_info():
    """Собирает информацию об имени хоста и IP-адресах."""
    hostname = socket.gethostname()
    try:
        ip_addr = socket.gethostbyname(hostname)
    except socket.gaierror:
        ip_addr = "127.0.0.1"
    return hostname, ip_addr

def main():
    print("==================================================")
    print("     СЕТЕВОЙ АНАЛИЗАТОР СИСТЕМЫ (Вариант B)     ")
    print("==================================================")
    
    hostname, ip_addr = get_network_info()
    print(f"Имя хоста  : {hostname}")
    print(f"Локальный IP: {ip_addr}")
    print("--------------------------------------------------")
    
    hosts_to_check = ["127.0.0.1", "8.8.8.8", "google.com", "yandex.ru"]
    print("Проверка базовых узлов:")
    for host in hosts_to_check:
        status = "ДОСТУПЕН" if check_host(host) else "НЕДОСТУПЕН"
        print(f"  [+] {host:<15} ---> {status}")

if __name__ == "__main__":
    main()
