print("hello")

for i in range(5,-1,-1):
    print(i)

#Using Socket to get hostname
import socket
hostname=socket.gethostname();
print(hostname)
#using os to get environment details
import os
homedir = os.environ['HOME']
print(homedir)
#expand user way
import os.path
homed = os.path.expanduser("~")
print (homed)

#to know the python installation location.
#/Library/Frameworks/Python.framework/Versions/2.7/bin -- This is the location where pip exists
import sys
print(sys.executable)
import cx_Oracle


