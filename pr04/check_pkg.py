import subprocess

packages = ["htop", "curl", "git", "python3"]

print("=== Проверка установленных пакетов в системе ===")
for pkg in packages:
    result = subprocess.run(["dpkg", "-s", pkg], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    status = "Установлен" if result.returncode == 0 else "НЕ установлен"
    print(f"Пакет '{pkg}': {status}")
