import os
import glob
import subprocess

# Compiling files 
i = 1
for d in os.listdir('.'):
    # Get all C files
    f = glob.glob(d + '/*.c')

    # Compile each C file with its own name
    for c_files in f:
        print(c_files)
        subprocess.call(["gcc", c_files, "-o", c_files[:-2] + ".out"])
