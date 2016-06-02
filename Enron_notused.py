#!/usr/bin/python3
import pdb
import os
from deco import *

rootdir = "/enron/lay-k"

@concurrent
def email_analyse(inputfile):
    with open(inputfile, "r", encoding="latin-1") as f:
        data = f.read()

    words = len(data.split(" "))
    return words


@synchronized
def read_files():
    words = []
#pdb.set_trace()
    for directory, subdirectory, filenames in  os.walk(rootdir):
        for filename in filenames:
            #print(directory, subdirectory)
            words.append((filename, email_analyse(os.path.join(directory, filename))))

            #print(filename, " words =  ", words)
            return words



print(read_files().get())