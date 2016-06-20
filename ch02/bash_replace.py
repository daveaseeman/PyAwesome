#!/home/vagrant/miniconda3/bin/python

import os

os.chdir("temp")
print(os.listdir())

for f in os.listdir():
    filename, extension = os.path.splitext(f)
    print("filename = {}, extension = {}".format(filename, extension))

    if extension == ".txt":
        new_file = filename + ".bak"
        os.rename(f, new_file)

print(os.listdir())        