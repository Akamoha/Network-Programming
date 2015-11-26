import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(1)

c, addr = s.accept()

filename = c.recv(1024)

try:
	x = open(filename, 'r')
	filecontent = x.read()
	c.send(filecontent)
	c.close()
except:
	c.send("File not available.")
	c.close()