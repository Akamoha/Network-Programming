import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))

seconds = 0

while True:
	data, addr = s.recvfrom(1024)
	s.sendto(str(seconds), (host, 12346))
	seconds += 1