#!/usr/bin/python3
import math
cimport numpy as np
import numpy as np
from Cython.Compiler.Options import directive_defaults
cdef extern from "math.h":
    float cosf(float theta)
    float sinf(float theta)
    float acosf(float theta)
import pstats, cProfile

directive_defaults['linetrace'] = True
directive_defaults['binding'] = True

def filter():
    cdef np.ndarray[np.double_t, ndim=1] coeffs = np.array([0.1, 1.3, 5.6, 3.4, 9.8, 0.01, 2.2])

    cdef float sum = 0
    cdef float local_sum = 0
    cdef int length = len(coeffs)
    #for i in range(1000000):
    for i from 0 <= i < 1000000: # no effect
        #for j in range(len(coeffs)):
        for j from 0 <= j < length:
            local_sum += (i * sinf(coeffs[j])) + (i * cosf(coeffs[j]))
        sum += local_sum
        local_sum = 0
    print(sum)


def profile():
    cProfile.runctx("filter()", globals(), locals(), "Profile.prof")

    s = pstats.Stats("Profile.prof")
    s.strip_dirs().sort_stats("time").print_stats()




if __name__ == '__main__':
        filter()    