#!/home/vagrant/miniconda3/bin/python
import numpy as np
import time
from numba import jit

@jit(cache=True, nopython=True)
def in_mandelbrot_set(c, iterations=400, threshold=2):
    z = 0
    for _ in range(iterations):
        z = z * z + c
    return abs(z) < threshold

t0 = time.process_time()
for y in np.linspace(1j, -1j, 40):
    print(*('#' if in_mandelbrot_set(x + y) else ' ' for x in np.linspace(-2, 0.5, 80)), sep='')

print("Time 2 diff = ",  time.process_time() -t0)    