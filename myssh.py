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

stdin, stdout, stderr =  ssh.exec_command("lscpu")

std1 = stdout.read()

ssh.close()

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('192.168.0.8', username='pi', password = "pi")

stdin, stdout, stderr =  ssh.exec_command("lscpu")

std2 = stdout.read()

ssh.close()


print("For 1st:", re.findall(b"Architecture:[ ]* ([ \w]*)", std1))

print("For 2nd:", re.findall(b"Architecture:[ ]* ([ \w]*)", std2))

