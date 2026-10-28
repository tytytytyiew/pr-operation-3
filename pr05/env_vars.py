#!/usr/bin/env python3
import os
os.environ["CUSTOM_OS_VAR"] = "Running_OK"
print("USER:", os.environ.get("USER"))
print("HOME:", os.environ.get("HOME"))
print("CUSTOM_OS_VAR:", os.environ.get("CUSTOM_OS_VAR"))
