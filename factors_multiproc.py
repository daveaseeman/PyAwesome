#!/usr/bin/python3

from multiprocessing import Process, Queue
import math

num_cores = 4

def find_factors(num, start =2):
    factors = []
    for i in range(start, num):
        if num % i == 0:
            factors.append(i)
            
    return factors

number = 1234567890
num_per_core = math.ceil(number / num_cores)

for i in range(0, number, num_per_core):
    print(a[i:i+num_per_core])

print(find_factors())