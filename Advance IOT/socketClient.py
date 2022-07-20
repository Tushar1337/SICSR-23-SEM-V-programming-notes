import socket
s=socket.socket()
host = socket.gethostname()
port = 9856
s.connect((host,port))
print(s.recv(1024).decode())
s.close
#this