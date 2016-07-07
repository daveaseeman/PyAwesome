#!/home/vagrant/miniconda3/bin/python

import pexpect

p = pexpect.spawn("./get_tok.py")

print("Expecting Name:")
p.expect("Name:")
p.sendline("Shantnu")

print("Expecting Age:")

p.expect("Age:")
p.sendline("16")

print("Expecting token:")
p.expect("Your token is:")
print(p.readline())

p.expect(pexpect.EOF)