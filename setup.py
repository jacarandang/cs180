import sys
from os import path
from cx_Freeze import setup, Executable
import re
# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os", "pygame",  "getopt", "random", "time", "threading", "pickle", "classes"], "excludes": ["tkinter"], "include_files": ["actions", "res", "ai"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(  name = "Heart Attack",
        version = "0.1",
        description = "CS 140 Heart Attack",
        options = {"build_exe": build_exe_options},
        executables = [Executable("main.py", base=base)])