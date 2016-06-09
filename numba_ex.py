#!/home/vagrant/miniconda3/bin/python
from numba import jit

import time
@jit(cache=True, nopython = True)
def mult(inputs, filters, coeff):
    out = 0
    for f in filters:
        for i in inputs:
            out += i * f + coeff

    return out

filters = [2, 5, 7, 9, 17]
coeff = 2
inputs = list(range(10000))

t0 = time.process_time()

print(mult(inputs, filters, coeff))

print("Time 2 diff = ",  time.process_time() -t0)
