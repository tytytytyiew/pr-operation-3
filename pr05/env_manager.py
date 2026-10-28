#!/usr/bin/env python3
import os

def env_lab():
    print("=" * 60)
    print(" PR-5: LAB - OPERATING SYSTEM ENVIRONMENT VARIABLES")
    print("=" * 60)
    
    # Установка и изменение переменных окружения процесса
    os.environ["OS_COURSE_VAR"] = "Active_Execution_Test"
    os.environ["USER_CUSTOM_PATH"] = "/opt/os_course/bin"
    
    print(f"USER       : {os.environ.get('USER', 'Not Set')}")
    print(f"HOME       : {os.environ.get('HOME', 'Not Set')}")
    print(f"SHELL      : {os.environ.get('SHELL', 'Not Set')}")
    print(f"LANG       : {os.environ.get('LANG', 'Not Set')}")
    
    print(f"\nCustom Environment Variable OS_COURSE_VAR:")
    print(f"  Value = {os.environ.get('OS_COURSE_VAR')}")
    
    print("\nFirst 3 entries of os.environ:")
    count = 0
    for k, v in os.environ.items():
        if count < 3:
            print(f"  {k} = {v}")
            count += 1
    print("=" * 60)

if __name__ == "__main__":
    env_lab()
