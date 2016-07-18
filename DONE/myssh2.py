#!/usr/bin/python3

# lscpu ifconfig  df

# in book, explain: ok for simple cases. for complicated, ansible, fabrix etc

import re
import paramiko
ssh = paramiko.SSHClient()
k = paramiko.RSAKey.from_private_key_file("/home/vagrant/.ssh/id_rsa")
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect('127.0.0.1', username='vagrant', password='vagrant')
ssh.connect('192.168.33.10', username='vagrant', pkey=k)

stdin, stdout, stderr =  ssh.exec_command("sudo dmesg")

print(stdout.read())

ssh.close()
ssh = paramiko.SSHClient()
