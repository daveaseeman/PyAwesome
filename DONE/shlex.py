#!/usr/bin/python3
import shlex

#Change this use my own example:

#anothr string this is "a test"
string = '''This string has embedded "double quotes" and 'single quotes' in it,
and even "a 'nested example'".'''


print(string.split())


print(shlex.split(string))