import socket

#HOST = '127.0.0.1'
HOST = '192.168.50.235' # Symbolic name meaning all available interfaces
PORT = 9999            # Arbitrary non-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print ('Connected by', addr)


#connection setup done and client connected.
conn.close()
