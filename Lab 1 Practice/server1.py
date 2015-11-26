import socket
import time

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(10)

while True:
	c, addr = s.accept()

	localtime = time.asctime(time.localtime(time.time()))

	data = c.recv(1024)
	
	c.send(localtime)

	print "Client details:"
	print "IP address:", data
	
	c.close()

s.close()