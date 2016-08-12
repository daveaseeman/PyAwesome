#!/home/vagrant/miniconda3/bin/python
import math

cdef extern from "math.h":
    float sinf(float theta)
    float cosf(float theta)

def filter():
    coeffs = [0.1, 1.3, 5.6, 3.4, 9.8, 0.01, 2.2]

    cdef float sum = 0
    cdef float local_sum = 0
    for i in range(1000000):
        for j in range(len(coeffs)):
            local_sum += (i * sinf(coeffs[j])) + (i * cosf(coeffs[j]))
        sum += local_sum
        local_sum = 0
    print(sum)


if __name__ == '__main__':
        filter()