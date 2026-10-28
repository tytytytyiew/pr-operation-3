#!/usr/bin/env python3
import os
import sys
import shutil
import datetime

def make_backup(src_dir, dest_dir):
    if not os.path.exists(src_dir):
        print(f"Ошибка: Исходная директория '{src_dir}' не найдена!")
        sys.exit(1)
        
    os.makedirs(dest_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.basename(os.path.normpath(src_dir))
    archive_name = os.path.join(dest_dir, f"{base_name}_backup_{timestamp}")
    
    try:
        archive_path = shutil.make_archive(archive_name, 'zip', src_dir)
        print(f"[УСПЕХ] Бэкап успешно создан: {archive_path}")
    except Exception as e:
        print(f"[ОШИБКА] Не удалось создать архив: {e}")

if __name__ == "__main__":
    source = sys.argv[1] if len(sys.argv) > 1 else "pr02"
    destination = sys.argv[2] if len(sys.argv) > 2 else "backups"
    
    print(f"Запуск архивации папки '{source}' в '{destination}'...")
    make_backup(source, destination)
