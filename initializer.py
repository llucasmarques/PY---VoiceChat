import subprocess
import socket

HOST = '192.168.50.156'    # The remote host
PORT = 13000       # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = s.connect_ex((HOST,PORT))


if result == 0:
   print ("Port on another computer is open. Running Client Program.")
   subprocess.call(['python','client.py'])
else:
   print ("Port on another computer is not open. Running Server Program.")
   subprocess.call(['python','server.py'])
