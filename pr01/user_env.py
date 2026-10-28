#!/usr/bin/env python3
import os, pwd, grp
uid, gid = os.getuid(), os.getgid()
print(f"Пользователь: {pwd.getpwuid(uid).pw_name} (UID: {uid})")
print(f"Группа: {grp.getgrgid(gid).gr_name} (GID: {gid})")
print(f"Домашняя папка: {pwd.getpwuid(uid).pw_dir}")
print(f"Рабочая директория: {os.getcwd()}")
