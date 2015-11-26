import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
serverport = 12345
s.bind((host, serverport))

count = 0

while True:
	try:
		s.sendto(str(count), (host, 12346))
		time.sleep(1)
		count += 1
	except:
		count = 0
		time.sleep(1)