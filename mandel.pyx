#!/home/vagrant/miniconda3/bin/python
from __future__ import print_function
import numpy as np
import time


def in_mandelbrot_set(complex c,  int iterations=400,  int threshold=2):
    cdef complex z = 0

    for _ in range(iterations):
        z = z * z + c
    return abs(z) < threshold



def mandel():
    cdef float x = 0
    cdef float y = 0
    for y in np.linspace(1j, -1j, 40):
        print(*('#' if in_mandelbrot_set(x + y) else ' ' for x in np.linspace(-2, 0.5, 80)), sep='')


mandel()    