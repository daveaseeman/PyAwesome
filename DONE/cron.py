#!/usr/bin/python3

from subprocess import Popen, PIPE
import os


def update_prices():
    with open("prices.csv","r") as f:
        data = f.read()

        data2 = data.split("\n")

        data2 = data2[1:] # get rid of top row with title

        num_products = len(data2)
        price = 0

        for d2 in data2:
             price += int(d2.split(",")[1].strip())
        print("\n----------Prince Changed. Updating Data--------------\n")
        print("Total products {}, total price {}, average price {} ".format(num_products, price, price/num_products))   


process = Popen(['md5sum prices.csv'], stdout=PIPE, stderr=PIPE, shell = True, universal_newlines=True)
stdout, stderr = process.communicate()
#print(stdout.split(" ")[0])

md5sum_current = stdout.split(" ")[0]

if os.path.exists("md5.txt"):
    with open("md5.txt", "r+") as f:
        md5_old = f.read()
        #print(md5_old)        
        f.seek(0)
        f.truncate()
        f.write(md5sum_current)
        if md5sum_current != md5_old:
            update_prices()

else:
    with open("md5.txt", "w+") as f:
        f.write(md5sum_current)
        update_prices()

print("At least the code is running!")  