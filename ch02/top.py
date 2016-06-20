#!/home/vagrant/miniconda3/bin/python

from subprocess import Popen, PIPE

process = Popen(['top -b -n 1'], stdout = PIPE, stderr = PIPE, shell = True, universal_newlines=True)

stdout, stderr = process.communicate()

print(stdout)