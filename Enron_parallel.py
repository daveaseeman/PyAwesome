#!/home/vagrant/miniconda3/bin/python
import pdb
import os
import multiprocessing
import time

rootdir = "/enron/lay-k"

emails = []
t0 = time.process_time()

def word_count_parallel(elist, queue):
    words = 0
    for inputfile in elist:
        with open(inputfile, "r", encoding="latin-1") as f:
            data = f.read()

            words += len(data.split(" "))
            #print(words)
    queue.put(words)


for directory, subdirectory, filenames in  os.walk(rootdir):
    for filename in filenames:
        emails.append(os.path.join(directory, filename))

emails = set(emails)
emails = list(emails)


length = int(len(emails) / 4)

email1 = emails[0:length]
email2 = emails[length : 2 * length]

email3 = emails[2 *length : 3 * length]
email4 = emails[3 *length :]

words1 = words2 = words3 = words4 = 0

queue = multiprocessing.Queue()

p1 = multiprocessing.Process(target=word_count_parallel, args=(email1, queue))
p2 = multiprocessing.Process(target=word_count_parallel, args=(email2, queue))
p3 = multiprocessing.Process(target=word_count_parallel, args=(email3, queue))
p4 = multiprocessing.Process(target=word_count_parallel, args=(email4, queue))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

total  = 0

for i in range(4):
    total += queue.get()

print("Total parallel", total)

print("Time 2 diff = ",  time.process_time() -t0)