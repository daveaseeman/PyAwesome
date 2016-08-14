#!/home/vagrant/miniconda3/bin/python
import math
#from Cython.Compiler.Options import directive_defaults
cdef extern from "math.h":
    float cosf(float theta)
    float sinf(float theta)
    float acosf(float theta)

def filter():
    coeffs = [0.1, 1.3, 5.6, 3.4, 9.8, 0.01, 2.2]

    sum = 0
    local_sum = 0
    for i in range(1000000):
        for j in range(len(coeffs)):
            local_sum += (i * sinf(coeffs[j])) + (i * cosf(coeffs[j]))
        sum += local_sum
        local_sum = 0
    print(sum)


if __name__ == '__main__':
        filter()    