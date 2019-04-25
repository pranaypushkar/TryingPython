#Working code for Server-Client
import socket
sd = socket.socket()
addr = socket.gethostname()
port = 15001
sd.bind((addr,port))
sd.listen(5)
while True:
	AccSock, ClntAddr = sd.accept()
	AccSock.send(b"Thanks for calling")
	AccSock.close() 