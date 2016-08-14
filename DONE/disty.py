#!/home/vagrant/miniconda3/bin/python

import os
from distributed import Executor
import time

def count_words(filename):
    with open(filename, "r", encoding = "latin-1") as f:
        data = f.read()

    return len(data.split(" "))

def remote_word_count():
    root_dir = "/enron/lay-k/family"
    word_count = 0
    for directory, subdir, filenames in os.walk(root_dir):
        for filename in filenames:
            print(filename)
            word_count += count_words(os.path.join(directory, filename))


    return word_count


executor = Executor("127.0.0.1:8786")

run = executor.submit(remote_word_count)
time.sleep(5)
print("Total words on remote machine = ", run.result())
