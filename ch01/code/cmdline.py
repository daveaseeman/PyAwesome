# Usage:
# $ python cmdline.py arg arg arg ...

import argparse

parser=argparse.ArgumentParser(description='Do Stuff')

parser.add_argument('-n', '--name', help='Enter the name', required = True, type=str)

args=parser.parse_args()

print(args)
