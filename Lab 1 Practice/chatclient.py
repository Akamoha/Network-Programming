import socket
import thread
import time

s = socket.socket()
host = socket.gethostname()
port = 12345
s.connect((host, port))

def receiver(s):
	while True:
		msg = s.recv(1024)
		print msg
		
def sender(s):
	while True:
		msg = raw_input()
		s.send(msg)

thread.start_new_thread(sender, (s,))
thread.start_new_thread(receiver, (s,))

time.sleep(100000)