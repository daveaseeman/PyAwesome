#!/home/vagrant/miniconda3/bin/python
from subprocess import Popen, PIPE


def update_values():
    with open("prices.csv", "r") as f:
        data = f.read()
        data = data.split("\n")

        data2 = data[1:]
        num_items = len(data2)

        total = 0

        for item in data2:
            price = int(item.split(",")[1])
            total += price

        average_price = total / num_items

        # This could be write to a database, or send an email, or anything
        print("----Data Updated----")
        print("Number of items = {}, Average price is {}".format(num_items, average_price))

process = Popen(['md5sum prices.csv'], stdout = PIPE, stderr = PIPE, shell = True, universal_newlines=True)

stdout, stderr = process.communicate()

md5sum = stdout.split(" ")[0]

with open("md5sum.txt", "r+") as f:
    md5sum_old = f.read()

    if md5sum != md5sum_old:
        f.seek(0)
        f.truncate()
        f.write(md5sum)
        print("Updating Md5 sum in file")
        update_values()

print("Running the cron.py file")        


