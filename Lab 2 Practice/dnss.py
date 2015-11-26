import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))


while True:
	canon, addr = s.recvfrom(1024)
	f = open("DNS.txt", 'r')
	answer = ""
	while True:
		try:
			line = f.next().split()
			if line[0] == canon:
				answer = line[1]
				break
		except:
			break
	s.sendto(answer, (host, 12346))
	
s.close()