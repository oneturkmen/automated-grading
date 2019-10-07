import os
import glob
import zipfile

for directory in os.listdir('.'):
    zip_file = glob.glob(directory + '/*.zip')

    size_allowed = 1
    amount_of_zip_files = len(zip_file)

    if amount_of_zip_files > size_allowed:
        print("More than 1 element in the directory")
        for file in zip_file:
            print(file)
        break
    elif amount_of_zip_files < size_allowed:
        print("Nothing in the directory: " + directory)
    else:
        file = zip_file[0]
        print("Extracting from the following path: ", file)
        with zipfile.ZipFile(file, 'r') as zip:
            zip.extractall(directory)
        print("{0} Extracted into {1}".format(file, directory))
