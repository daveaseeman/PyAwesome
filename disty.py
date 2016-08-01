#!/home/vagrant/miniconda3/bin/python
from distributed import Executor
import os
rootdir = "/enron/lay-k"

def word_count(inputfile):
    with open(inputfile, "r", encoding="latin-1") as f:
        data = f.read()

    words = len(data.split(" "))
    return words

def get_word_count():
    words = 0
    for directory, subdirectory, filenames in  os.walk(rootdir):
        for filename in filenames:
            words+= word_count(os.path.join(directory, filename))

    return words


executor = Executor('127.0.0.1:8786')

print("Yo Dude! Total words be : ", executor.submit(get_word_count).result())