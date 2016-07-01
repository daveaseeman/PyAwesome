#!/home/vagrant/miniconda3/bin/python
import pdb
import pexpect
child = pexpect.spawn('./a.py')
child.expect('Name: ')
child.sendline('Jackson')

child.expect('Age: ')
child.sendline('33')


child.expect('Your token is: ')
print(child.read())
child.expect(pexpect.EOF)

