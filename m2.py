#!/home/vagrant/miniconda3/bin/python
import math
import numpy as np
from numba import jit

@jit
def mandelbrot(z , c , n=400):
    
    for i in range(n):
        z = z * z + c
    if abs(z) > 1000:
        return float("nan")
    else:
        return z 

print("\n".join(["".join(["#" if not math.isnan(mandelbrot(0, x + 1j * y).real) else " "
                 for x in [a * 0.02 for a in range(-80, 30)]]) 
                 for y in [a * 0.05 for a in range(-20, 20)]])
     )
 