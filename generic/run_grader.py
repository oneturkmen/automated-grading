import os
import glob
import subprocess

from subprocess import Popen, PIPE, STDOUT

# Open test_q1.in
# test_q1_f = open("test_q1.in", "r")
# test_q1 = str(test_q1_f.read())
# test_q1_f.close()

"""
>>>>>>>>>>>>>>>>> SET THE CONFIGURATION FLAGS <<<<<<<<<<<<<<<<

1. Put this file into the directory containing student submissions
    (i.e. folders named after them).
2. Create a directory "tests" in the current directory.
3. Put your tests into this "tests" directory. Make sure input test files end with
    ".in" and contain only 1 input.
4. Put the test names (with proper ".in" suffix) in the "test_names" list.
5. Configure this below (to run tests, set debug to False and run to True).

"""
debug = True
run = False
test_names = [
    "t_1.in", "t_2.in", 
    "t_3.in", "t_4.in", 
    "t_4.in", "t_5.in",
    "t_6.in"
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
        dir_of_exe = c_files[:len(kernighan[-1]) + 2]

        c_files = kernighan[-1]
        out_name = c_files[:-2] + ".out"

        # Debug info
        print("Student " + str(i) + " " + out_name)

        if debug:
            print("C_files ", c_files)
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

            os.system("./" + dir_of_exe + out_name + "< " + "./tests/" + test + " > " + dir_of_exe + test[:-3] + "_subm.txt")

        # # Piecewise test runner
        # if program_name == "q1.out":
        #     print("... Testing Q1")
        #     os.system("./" + out_name + "< test_q1.in > " + dir_of_exe + "q1_result.txt")
        # elif program_name == "q2.out":
        #     print("... Testing Q2")
        #     os.system("./" + out_name + "< test_q2.in > " + dir_of_exe + "q2_result.txt")
        # elif program_name == "q7.out":
        #     print("... Testing Q7")
        #     index_q7 = 1
        #     for index_q7 in range(5):
        #         os.system("./" + out_name + "< test_q7_" + str(index_q7)
        #                 + ".in > " + dir_of_exe
        #                 + "q7_result_" + str(index_q7) +  ".txt")
        #         index_q7 += 1
        # elif program_name == "q9.out":
        #     print("... Testing Q9")
        #     os.system("./" + out_name + "< test_q9.in > " + dir_of_exe + "q9_result.txt")


