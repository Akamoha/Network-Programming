import socket
import thread
import time

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(1)

c, addr = s.accept()

def receiver(c):
	while True:
		msg = c.recv(1024)
		print msg
		
def sender(c):
	while True:
		msg = raw_input()
		c.send(msg)

thread.start_new_thread(sender, (c,))
thread.start_new_thread(receiver, (c,))

time.sleep(100000)