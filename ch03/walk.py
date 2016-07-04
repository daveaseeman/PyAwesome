#!/home/vagrant/miniconda3/bin/python

import os
import shutil

files_found = []

for directories, subdirs, files in  os.walk("./temp"):
    print(directories, subdirs, files)

    for filename in files:
        filename2, ext = os.path.splitext(filename)
        if ext == ".jpg":
            
            file_to_delete = os.path.join(directories, filename)
            print("Deleting jpg file: ", file_to_delete)
            os.remove(file_to_delete)

        elif filename in files_found:
            file_to_delete = os.path.join(directories, filename)
            print("Deleting duplicate file ", file_to_delete)
            os.remove(file_to_delete)

        files_found.append(filename)


    head, tail = os.path.split(directories)
    if tail == "del":
        print("Directory to delete: ", tail)
        shutil.rmtree(directories)

