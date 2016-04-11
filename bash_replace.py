#!/usr/bin/python3

from subprocess import Popen, PIPE
import pdb

process = Popen(['top -b -n 1'], stdout=PIPE, stderr=PIPE, shell = True, universal_newlines=True)
stdout, stderr = process.communicate()
#print(stdout)
#pdb.set_trace()
cpu_line = stdout.split("\n")[7]
print(cpu_line)
cpu = cpu_line.split()[8]
user = cpu_line.split()[1]

print("Top cpu loading is: ",cpu)

if float(cpu) > 90:
    process = Popen(['sudo killall yes'], stdout=PIPE, stderr=PIPE, shell = True)
    stdout, stderr = process.communicate()
    print(stdout)

    # add logging

