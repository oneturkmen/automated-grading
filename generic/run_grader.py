import os
import glob
import subprocess

from subprocess import Popen, PIPE, STDOUT

"""
>>>>>>>>>>>>>>>>> SET THE CONFIGURATION FLAGS <<<<<<<<<<<<<<<<

1. Put this file into the directory containing student submissions
    (i.e. folders named after them).
2. Create a directory "tests" in the current directory.
3. Put your tests into this "tests" directory. Make sure input test files end
    with ".in" and contain only 1 input.
4. Put the test names (with proper ".in" suffix) in the "test_names" list.
5. Configure this below (to run tests, set "debug" to False and "run" to True).

"""

debug = False
run = True
test_names = [
    "t_1.in", "t_2.in",
    "t_3.in", "t_4.in",
    "t_5.in", "t_6.in",
    "t_7.in", "t_8.in",
    "t_9.in", "t_10.in"
]

"""
>>>> Running tests ... DO NOT CHANGE UNLESS YOU KNOW WHAT YOU DO <<<<
"""

if len(test_names) <= 0:
    print("ERROR: No input test files defined!")
    os._exit(0)

if run and debug:
    print("ERROR: Debug is still on!")
    os._exit(0)


i = 1
for d in os.listdir():
    # Get all C files
    f = glob.glob(d + '/*.c')

    if not debug and d[-5:] != "file_":
        continue

    # Compile each C file with its own name
    for c_files in f:

        kernighan = c_files.split("/")
        dir_of_exe = kernighan[0] + "/"
        #dir_of_exe = c_files[:len(kernighan[-1]) + 2]

        c_files = kernighan[-1]
        out_name = c_files[:-2] + ".out"

        # Debug info
        print("Student " + str(i) + " " + out_name)
        i += 1

        if debug:
            print("C_files ", c_files)
            print("Kernighan ", kernighan)
            print("Directory ", dir_of_exe)
            print("Out name ", out_name)
            print()

        for test in test_names:

            if test[-2:] != "in":
                print("ERROR: Ill-defined test file. Please end it with .in")
                os._exit(0)
            if not os.path.exists("./tests/" + test):
                print("ERROR: Test {0} file not found".format(test))
                os._exit(0)

            if run:
                print("Running test {0} on {1}\n".format(test, dir_of_exe))
                os.system("./" + dir_of_exe + out_name
                        + "< " + "./tests/" + test
                        + " > " + dir_of_exe + test[:-3]
                    + "_subm.txt")
