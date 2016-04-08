#!/usr/bin/python3

# bash way
# https://github.com/stephenturner/oneliners
# find . -name "*.txt" | sed "s/\.txt$//" | xargs -i echo mv {}.txt {}.bak | sh


# also mention this http://www.compciv.org/topics/bash/variables-and-substitution/
# regards dangers of space or * in file names in bash
# maybe have example?? Bash vs Python

import os

os.chdir("temp")
print(os.listdir("."))

for f in os.listdir("."):
    filename, extension = os.path.splitext(f)
    print(filename, extension)
    if extension == ".bak":
        new_name = filename + ".txt"
        os.rename(f, new_name)
        print("Renaming {} to {}".format(f, new_name))
