#!/home/vagrant/miniconda3/bin/python

import os
import time
import multiprocessing

NUM_PROCESSES  = 4

root_dir = "/enron/lay-k"

t0 = time.process_time()

def word_count_parallel(email_list, queue):

    word_count = 0
    for emails in email_list:
        with open(emails, "r", encoding = "latin-1") as f:
            data = f.read()

        word_count += len(data.split(" "))

    queue.put(word_count)

email_list=[]

for directory, subdir, filenames in os.walk(root_dir):
    for filename in filenames:
        email_list.append(os.path.join(directory, filename))

num_emails = len(email_list)

length = int(num_emails / NUM_PROCESSES)

emails1 = email_list[: length]

emails2 = email_list[length : 2 *length]

emails3 = email_list[2 * length : 3 *length]

emails4 = email_list[3 * length: ]


queue = multiprocessing.Queue()

p0 = multiprocessing.Process(target = word_count_parallel, args=(emails1, queue))
p1 = multiprocessing.Process(target = word_count_parallel, args=(emails2, queue))
p2 = multiprocessing.Process(target = word_count_parallel, args=(emails3, queue))
p3 = multiprocessing.Process(target = word_count_parallel, args=(emails4, queue))


p0.start()
p1.start()
p2.start()
p3.start()

p0.join()
p1.join()
p2.join()
p3.join()

word_count = 0

for q in range(NUM_PROCESSES):
    word_count += queue.get()

t1 = time.process_time() - t0


print("Total words = ", word_count)    
print("Time difference parallel = ", t1)
