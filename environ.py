#!/usr/bin/python3

#vagrant@vagrant-ubuntu-trusty-64:/vagrant$ export DB_PASS=topsecret
#vagrant@vagrant-ubuntu-trusty-64:/vagrant$ echo $DB_PASS

import os
print(os.environ['HOME'])
print(os.environ['DB_PASS'])