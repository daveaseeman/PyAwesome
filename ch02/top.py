#!/home/vagrant/miniconda3/bin/python

from subprocess import Popen, PIPE

process = Popen(['top -b -n 1'], stdout = PIPE, stderr = PIPE, shell = True, universal_newlines=True)

stdout, stderr = process.communicate()

print(stdout.split("\n")[7])

top_cpu_line = stdout.split("\n")[7]

print(top_cpu_line.split())

print("CPU is: {}%".format(top_cpu_line.split()[8]))

cpu = top_cpu_line.split()[8]

program = top_cpu_line.split()[11]

user = top_cpu_line.split()[1]

if float(cpu) > 90:
    cmd = "killall " + program

    process = Popen([cmd], stdout = PIPE, stderr = PIPE, shell = True, universal_newlines=True)

    stdout, stderr = process.communicate()

    print(stdout)

    print("Killing program {} from user {} because CPU too high: {}%".format(program, user, cpu))





