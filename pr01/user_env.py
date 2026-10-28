#!/usr/bin/env python3
import os
import pwd
import grp

def main():
    print("=" * 60)
    print(" PR-1: LAB - USERS AND SYSTEM ENVIRONMENT")
    print("=" * 60)
    uid = os.getuid()
    gid = os.getgid()
    user_pw = pwd.getpwuid(uid)
    group_gr = grp.getgrgid(gid)
    
    print(f"Login Username  : {user_pw.pw_name}")
    print(f"User ID (UID)   : {uid}")
    print(f"Group ID (GID)  : {gid}")
    print(f"Group Name      : {group_gr.gr_name}")
    print(f"Home Directory  : {user_pw.pw_dir}")
    print(f"Shell Program   : {user_pw.pw_shell}")
    print(f"Current Dir     : {os.getcwd()}")
    
    # Чтение системных файлов учетных записей ОС
    print("\n[Reading /etc/passwd first 3 lines]:")
    try:
        with open("/etc/passwd", "r") as f:
            for i in range(3):
                print("  ", f.readline().strip())
    except Exception as e:
        print("  Could not read /etc/passwd:", e)
    print("=" * 60)

if __name__ == "__main__":
    main()
