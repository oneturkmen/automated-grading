import os
import tarfile
import glob


# Untarring tar files
i = 1
for d in os.listdir('.'):
    # Get all paths that end with .tar (all matching files' paths)
    f = glob.glob(d + '/*.tar')

    # If more than 1 tar in the directory, something is weird
    if len(f) > 1:
        print("More than 1 element in the directory: ")
        print(f)
        print()
        break
    if len(f) <= 0:
        continue
    # Ignore this script file
    if f[0][-3:] != 'tar':
        print(d)
        print(f)
        continue
    # If there is nothing, then student did not submit anything
    if len(f) <= 0:
        print()
        print("Nothing in the directory: ")
        print(d)
        print()
        continue
    
    # Open and extract tar file
    print("Extracting from the following path: ", f)
    tf = tarfile.open(f[0])
    tf.extractall(path=d)
    tf.close()

    # Process info
    print("{0} Extracted into {1}".format(i, d))
    i += 1


