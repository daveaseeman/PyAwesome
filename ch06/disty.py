#!/home/vagrant/miniconda3/bin/python

import os
from distributed import Executor

def count_words(filename):
    with open(filename, "r", encoding = "latin-1") as f:
        data = f.read()

    return len(data.split(" "))


def remote_word_count():
    root_dir = "/enron/lay-k"

    word_count = 0
    for directory, subdir, filenames in os.walk(root_dir):
        for filename in filenames:
            word_count += count_words(os.path.join(directory, filename))

    return word_count


executor = Executor("127.0.0.1:8786")

words = executor.submit(remote_word_count)

print("\n\n Word Count on remote machine is: ", words.result())

