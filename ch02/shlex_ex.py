#!/home/vagrant/miniconda3/bin/python

import shlex

my_string = ''' This is a string with "double quotes" and 'single quotes'. 

"It also has them 'embedded within each other' like so" '''

print(my_string)
print("\n With Python \n")
print(my_string.split())

print("\n With shlex\n")

print(shlex.split(my_string))

print("\n Loop over parts\n")
# Loop over the parts
for part in shlex.split(my_string):
    print(shlex.split(part))


print("\nBreak down even more\n")
# Go down even more
print(shlex.split(my_string)[8])

print(shlex.split(shlex.split(my_string)[8]))

# Extract parts in single inverted comma
print(shlex.split(shlex.split(my_string)[8])[4])
