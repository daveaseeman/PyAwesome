#!/home/vagrant/miniconda3/bin/python

import configparser

config = configparser.ConfigParser()

config.read("config.cfg")

server = config.get("main_config", "server")
ports =  config.get("main_config", "ports")
flag =  config.get("main_config", "flag")

ports = ports.split(",")

print(server)

for port in ports:
    print(port)

print(flag)    