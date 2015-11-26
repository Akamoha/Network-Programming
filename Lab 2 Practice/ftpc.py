import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

s.send("T5.jpg")

filecontent = s.recv(1499658)

f = open("newfile.jpg", 'w')

f.write(filecontent)

s.close()