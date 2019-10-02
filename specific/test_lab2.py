import os
import glob
import subprocess

from subprocess import Popen, PIPE, STDOUT

# Open test_q1.in
test_q1_f = open("test_q1.in", "r")
test_q1 = str(test_q1_f.read())
test_q1_f.close()

# Open test_q2.in
test_q2_f = open("test_q2.in", "r")
test_q2 = str(test_q2_f.read())
test_q2_f.close()

# Open test_q7.in
test_q7_f = open("test_q7.in", "r")
test_q7 = [str(x[1]) for x in enumerate(test_q7_f)]
test_q7_f.close()

# Open test_q9.in
test_q9_f = open("test_q9.in", "r")
test_q9 = str(test_q9_f.read())
test_q9_f.close()


# Verify tests
print("Q1 = ", test_q1)
print("Q2 = ", test_q2)
print("Q7 = ", test_q7)
print("Q9 = ", test_q9)

# Compiling files

i = 1
for d in os.listdir():
    # Get all C files
    f = glob.glob(d + '/*.c')

    if d[-5:] != "file_":
        continue

    # Compile each C file with its own name
    for c_files in f:

        dir_of_exe = c_files[:-4]
        out_name = c_files[:-2] + ".out"

        # Debug info
        print("Student " + str(i) + " " + out_name)

        # Executable name
        program_name = out_name[-6:]
        test_num = program_name[1]

        if not test_num.isdigit():
            print("Are you trying to run some weird tests? Check test filenames")
            return

        test_num = int(test_num)

        print("Directory ", dir_of_exe)
        print("Out name ", out_name)

        # os.system("." + out_name + "< t_" + test_num + ".in > " + dir_of_exe + "q" + test_num + "_subm.txt")

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

    i += 1

