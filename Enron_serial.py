#!/home/vagrant/miniconda3/bin/python
import pdb
import os
import multiprocessing
import time

rootdir = "/enron/lay-k"

emails = []
words = 0
t0 = time.process_time()
def word_count(inputfile):
    with open(inputfile, "r", encoding="latin-1") as f:
        data = f.read()

    words = len(data.split(" "))
    return words

for directory, subdirectory, filenames in  os.walk(rootdir):
    for filename in filenames:
        words+= word_count(os.path.join(directory, filename))
print("total words ", words)        
print("Time 1 diff = ",  time.process_time() -t0)
