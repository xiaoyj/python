import socket
import time
i = 0
sock = socket.socket()
host = socket.gethostname()
sock.connect((host,8000))
while i < 20:
	print time.time(	)
	sock.send(str(time.time()))
	print sock.recv(1024)
	time.sleep(1) 
	i = i+1