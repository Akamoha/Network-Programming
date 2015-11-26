import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
clientport = 12346
s.bind((host, clientport))

while True:
	data, addr = s.recvfrom(1024)
	print addr[1]