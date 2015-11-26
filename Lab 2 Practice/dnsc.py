import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = socket.gethostname()
port = 12346
s.bind((host, port))

print "Enter the cannonical address:"

canon = raw_input()

s.sendto(canon, (host, 12345))

IP = s.recvfrom(1024)

if IP == "":
	print "Not `found!"
else:
	print IP