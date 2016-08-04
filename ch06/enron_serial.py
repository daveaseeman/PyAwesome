#!/home/vagrant/miniconda3/bin/python

import os
import time

root_dir = "/enron/lay-k"

t0 = time.process_time()
word_count = 0
#http://python-notes.curiousefficiency.org/en/latest/python3/text_file_processing.html

def count_words(filename):
    with open(filename, "r", encoding = "latin-1") as f:
        data = f.read()

    return len(data.split(" "))

for directory, subdir, filenames in os.walk(root_dir):
    for filename in filenames:
        word_count += count_words(os.path.join(directory, filename))


t1 = time.process_time() - t0


print("Total words = ", word_count)    
print("Time difference serial = ", t1)
