import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM	)
host = socket.gethostname()
port = 12346
s.bind((host, port))

while True:
	try:
		s.sendto("Update", (host, 12345))
		data, addr = s.recvfrom(1024)
		print data,
		time.sleep(1)
		print ""
	except:
		time.sleep(1)