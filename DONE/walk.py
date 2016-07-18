#!/usr/bin/python3

import os
import shutil
import pdb


file_list = []

for directory, subdirectory, filenames in  os.walk("./temp"):
    print(directory, subdirectory, filenames)
    for filename in filenames:
        name, extension = os.path.splitext(filename)
        print(name, extension)
        if extension == ".jpg":
            os.remove(os.path.join(directory, filename))
            print("Deleting ", os.path.join(directory, filename))

        if extension == ".txt":
            if filename in file_list:
                os.remove(os.path.join(directory, filename))
                print("Deleting ", os.path.join(directory, filename))
        
        file_list.append(filename)

    path1, dir1 = os.path.split(directory)
    if dir1 == "del":
        shutil.rmtree(directory)
        print("Deleting ", directory)

for directory, subdirectory, filenames in  os.walk("./temp"):
    if (not subdirectory) and (len(filenames) == 0):
        print(directory, "Empty!")
        os.rmdir(directory)