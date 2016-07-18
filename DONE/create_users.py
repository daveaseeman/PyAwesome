#!/usr/bin/python3
import pdb

'''
vagrant@vagrant-ubuntu-trusty-64:/vagrant$ sudo adduser user1
Adding user `user1' ...
Adding new group `user1' (1002) ...
Adding new user `user1' (1002) with group `user1' ...
Creating home directory `/home/user1' ...
Copying files from `/etc/skel' ...
Enter new UNIX password:
Retype new UNIX password:
passwd: password updated successfully
Changing the user information for user1
Enter the new value, or press ENTER for the default
        Full Name []:
        Room Number []:
        Work Phone []:
        Home Phone []:
        Other []:
Is the information correct? [Y/n] y



from subprocess import Popen, PIPE, STDOUT

p = Popen(['grep', 'f'], stdout=PIPE, stdin=PIPE, stderr=STDOUT,universal_newlines=True)

grep_stdout = p.communicate(input='one\ntwo\nthree\nfour\nfive\nsix\n')[0]
print(grep_stdout)

'''

from subprocess import Popen, PIPE, STDOUT
p = Popen(['sudo adduser user2'], stdout=PIPE, stdin=PIPE, stderr=STDOUT, universal_newlines=True, shell = True)
#pdb.set_trace()
print(p.stdout.read())
print(p.communicate('user2')[0].rstrip())

print(p.stdout.readline().rstrip())
print(p.communicate('user2')[0].rstrip())

print(p.stdout.readline().rstrip())
print(p.communicate('User 2 Of Course')[0].rstrip())

print(p.communicate('\n\n\n\n')[0].rstrip())

print(p.stdout.readline().rstrip())
print(p.communicate('y')[0].rstrip())