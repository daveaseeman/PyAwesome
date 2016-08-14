#!/home/vagrant/miniconda3/bin/python
def mul(a,b):
    c = 0
    d = 0.0
    for i in range(1000):
        for j in range(50):
            c+= a * b

            d += a/b

    return c,d

print(mul(7, 2))