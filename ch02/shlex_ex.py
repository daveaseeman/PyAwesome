#!/home/vagrant/miniconda3/bin/python

import shlex

my_string = ''' This is a string with "double qoutes" and 'single qoutes'. 

"It also has them 'embedded within each other' like so" '''

print(my_string)
print("\n\n")
print(my_string.split())

print("\n\n")

print(shlex.split(my_string))
