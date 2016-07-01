#!/home/vagrant/miniconda3/bin/python

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-s", "--servername", help = "The server name ", required = True)
parser.add_argument("-f", "--flag", help = "Flag to signal to store session", action ='store_true')
parser.add_argument("-p", "--ports", help = "The ports to ssh to", action='append')
args = parser.parse_args()
print(args)

cmd = "ssh_mine " + args.servername

if args.flag:
    cmd += " --save_session"

cmd += " -p " 
for port in args.ports:
    cmd +=  port + " "

print(cmd)

