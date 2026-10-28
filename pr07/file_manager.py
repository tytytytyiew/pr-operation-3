#!/usr/bin/env python3
import os
import sys

def fs_lab(target_dir="."):
    print("=" * 60)
    print(f" PR-7: LAB - FILE SYSTEM TRAVERSAL & DESCRIPTORS: {os.path.abspath(target_dir)}")
    print("=" * 60)
    
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} does not exist.")
        return
        
    file_count = 0
    dir_count = 0
    
    # Демонстрация низкоуровневого открытия файла (системный вызов open/read)
    sample_file = __file__
    print(f"Demonstrating low-level file descriptor read on: {sample_file}")
    fd = os.open(sample_file, os.O_RDONLY)
    content_bytes = os.read(fd, 100)
    os.close(fd)
    print(f"  First 100 bytes via File Descriptor (fd): {content_bytes[:50]}...\n")
    
    print("Walking directory tree:")
    for root, dirs, files in os.walk(target_dir):
        dir_count += len(dirs)
        file_count += len(files)
        level = root.replace(target_dir, "").count(os.sep)
        indent = "  " * level
        print(f"{indent}[DIR]  {os.path.basename(root) or root}")
        for f in files[:3]: # ограничиваем вывод для читаемости
            print(f"{indent}  [FILE] {f}")
            
    print("-" * 60)
    print(f"Total Subdirectories : {dir_count}")
    print(f"Total Files          : {file_count}")
    print("=" * 60)

if __name__ == "__main__":
    path_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    fs_lab(path_arg)
