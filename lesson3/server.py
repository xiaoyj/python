import socket
import time
s=socket.socket()
host = socket.gethostname()
s.bind((host,8000))
s.listen(10)
connection,adress = s.accept()
while True:
	mes = connection.recv(1024)
	print time.time(	)
	hi = time.time() - float(mes)
	connection.send(str(hi))