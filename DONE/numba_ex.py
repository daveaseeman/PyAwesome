#!/home/vagrant/miniconda3/bin/python
from numba import jit
import math

import time
@jit(cache=True, nopython = True)
def filter():
    coeffs = [0.1, 1.3, 5.6, 3.4, 9.8, 0.01, 2.2]

    sum = 0
    local_sum = 0
    for i in range(1000000):
        for j in range(len(coeffs)):
            local_sum += (i * math.sin(coeffs[j])) + (i * math.cos(coeffs[j]))
        sum += local_sum
        local_sum = 0
    print(sum)

t0 = time.process_time()

filter()    

print("Time 2 diff = ",  time.process_time() -t0)
