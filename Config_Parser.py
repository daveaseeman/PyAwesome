#!/usr/bin/python3
import configparser
config = configparser.ConfigParser()

configFilePath = r'config.cfg'
print(config.read(configFilePath))