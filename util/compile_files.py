import os
import glob
import subprocess

# Compiling files 
i = 1
for d in os.listdir('.'):

    #rename folders to replace spaces by underscores
    if "." not in d and " " in d:
        new_d = d.replace(" ","_")
        os.rename(d,new_d)
        d = new_d
    # Get all C files
    f = glob.glob(d + '/*.c')

    # Compile each C file with its own name
    for c_files in f:
        print(c_files)
        subprocess.call(["gcc", c_files, "-o", c_files[:-2] + ".out"])