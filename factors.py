#!/usr/bin/python3

def find_factors(num, start =2):
    factors = []
    for i in range(start, num):
        if num % i == 0:
            factors.append(i)
            
    return factors

print(find_factors(1234567890))