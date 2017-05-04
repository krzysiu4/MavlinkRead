import sys
import subprocess
args = ("./mavlink_control", "-d", "/dev/ttyACM0", "-b", "57600")
popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
print output
