# work with files and folders

# read environment variables

# run system commands

# get system information

import os

import platform

print(os.name)

# nt   # Windows
# posix  # Linux / Mac


# current working directory

print(os.getcwd())

# C:\Users\HP\OneDrive\Desktop\AI\clones\python1\os_module

print(os.cpu_count()) #computer can run 12 parallel CPU tasks at the same time.

print(os.getlogin()) # HP

print(platform.system()) # Windows
print(platform.release()) # 10