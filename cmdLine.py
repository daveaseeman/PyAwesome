#!/usr/bin/python3

import argparse
parser = argparse.ArgumentParser()

flag = False

parser.add_argument("-s", "--server", help="The server to connect to", required = True)
parser.add_argument("-f", "--flag", help="Flag to signal if session should be saved", action = "store_true")
parser.add_argument("-p", "--ports", help="Ports to connect to", action = "append")

args = parser.parse_args()
print(args)

cmd = "ssh_mine " + args.server
if args.flag:
    cmd += " --save_session "

for port in args.ports:
    cmd += " --port " + port + " "

print("The final command that will be run is: ")    
print(cmd)

