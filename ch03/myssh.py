#!/home/vagrant/miniconda3/bin/python

import paramiko
import re

ssh = paramiko.SSHClient()

mykey = paramiko.RSAKey.from_private_key_file('/home/vagrant/.ssh/id_rsa')

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect("192.168.33.10", username="vagrant", pkey=mykey)


stdin, stdout, stderr = ssh.exec_command("lscpu")

arch1 = stdout.read()

ssh.close()



ssh.connect("192.168.0.13", username="pi", pkey=mykey)


stdin, stdout, stderr = ssh.exec_command("lscpu")

arch2 = stdout.read()

ssh.close()


print("Architecture 1 = ", re.findall(b"Architecture:[ ]* ([\w]*)", arch1))

print("Architecture 2 RPI = ", re.findall(b"Architecture:[ ]* ([)"\w]*, arch2))