#!/usr/bin/python3

from subprocess import Popen, PIPE

process = Popen(['md5sum prices.csv'], stdout=PIPE, stderr=PIPE, shell = True, universal_newlines=True)
stdout, stderr = process.communicate()
print(stdout.split(" ")[0])

md5sum = stdout.split(" ")[0]

# @TODO: How to create file 1st time round, read it later on
with open("md5.txt", "r+") as f:
    md5 = f.read()
    print(md5)
    f.write(md5sum)

with open("prices.csv","r") as f:
    data = f.read()

data2 = data.split("\n")

data2 = data2[1:] # get rid of top row with title

num_products = len(data2)
price = 0

for d2 in data2:
     price += int(d2.split(",")[1].strip())

print("Total products {}, total price {}, average price {} ".format(num_products, price, price/num_products))     