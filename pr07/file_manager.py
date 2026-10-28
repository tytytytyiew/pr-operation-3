#!/usr/bin/env python3
import os
import sys

def explore_directory(target_path="."):
    print("=" * 50)
    abs_path = os.path.abspath(target_path)
    print(f" ПР-7: СКАНИРОВАНИЕ ДИРЕКТОРИИ -> {abs_path}")
    print("=" * 50)
    
    if not os.path.exists(target_path):
        print(f"Путь '{target_path}' не найден.")
        return

    dir_count = 0
    file_count = 0

    try:
        for root, dirs, files in os.walk(target_path):
            level = root.replace(target_path, '').count(os.sep)
            indent = ' ' * 4 * level
            print(f"{indent}[DIR] {os.path.basename(root) or root}")
            dir_count += len(dirs)
            
            sub_indent = ' ' * 4 * (level + 1)
            for f in files:
                file_path = os.path.join(root, f)
                try:
                    f_size = os.path.getsize(file_path)
                    print(f"{sub_indent}[FILE] {f} ({f_size} байт)")
                except OSError:
                    print(f"{sub_indent}[FILE] {f} (ошибка доступа)")
                file_count += 1
                
        print("-" * 50)
        print(f"Итог: директорий — {dir_count}, файлов — {file_count}")
        print("=" * 50)
        
    except PermissionError:
        print("Ошибка: недостаточно прав для сканирования каталога.")

if __name__ == "__main__":
    path_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    explore_directory(path_arg)
