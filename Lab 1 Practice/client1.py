import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))

myIP = socket.gethostbyname(socket.gethostname())

s.send(myIP)

datetime = s.recv(1024)

print datetime

s.close()