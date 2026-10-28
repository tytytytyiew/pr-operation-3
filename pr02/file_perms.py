#!/usr/bin/env python3
import os
import sys
import stat

def examine_inode(target_path):
    print("=" * 60)
    print(f" PR-2: LAB - INODE AND FILE PERMISSIONS FOR: {target_path}")
    print("=" * 60)
    
    if not os.path.exists(target_path):
        print(f"Error: Path '{target_path}' does not exist.")
        return
        
    st = os.stat(target_path)
    
    print(f"Inode Number    : {st.st_ino}")
    print(f"File Size       : {st.st_size} bytes")
    print(f"Owner UID / GID : {st.st_uid} / {st.st_gid}")
    print(f"Octal Mode      : {oct(st.st_mode)[-3:]}")
    print(f"Is Directory    : {os.path.isdir(target_path)}")
    
    # Детальная проверка разрешений POSIX
    print("\nPOSIX Access Flags:")
    print(f"  Owner Read     : {bool(st.st_mode & stat.S_IRUSR)}")
    print(f"  Owner Write    : {bool(st.st_mode & stat.S_IWUSR)}")
    print(f"  Owner Execute  : {bool(st.st_mode & stat.S_IXUSR)}")
    print(f"  Group Read     : {bool(st.st_mode & stat.S_IRGRP)}")
    print(f"  Others Read    : {bool(st.st_mode & stat.S_IROTH)}")
    print("=" * 60)

if __name__ == "__main__":
    path_arg = sys.argv[1] if len(sys.argv) > 1 else "."
    examine_inode(path_arg)
