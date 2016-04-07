#!/usr/bin/python3
import configparser
import pdb

config = configparser.ConfigParser()

configFilePath = 'config.cfg'

config.read(configFilePath)
server = config.get('main_config', 'server')
flag = config.get('main_config', 'flag')
ports = config.get('main_config', 'ports')

port_split = ports.split(",")

print(server, flag, ports)


cmd = "ssh_mine " + server

if flag == 'True': # explain why. bool(string) is always true!!!
    cmd += " --save_session "

for port in port_split:
    cmd += " --port " + port + " "

print("The final command that will be run is: ")    
print(cmd)
