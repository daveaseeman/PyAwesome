# Usage:
# $ pip install configparser
# $ python config_parser.py

import configparser

config = configparser.ConfigParser()

config.read('config.cfg')

server = config.get('main_config', 'server')
ports = config.get('main_config', 'ports')
flag = config.get('main_config', 'flag')

print(server)

ports = ports.replace(" ","").split(",")
for port in ports:
    print(port)

print(flag)
