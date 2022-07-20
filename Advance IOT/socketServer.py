import socket
s=socket.socket()
host=socket.gethostname()
port=9856
s.bind((host,port))
s.listen(5)
while True:
    c,addr=s.accept()
    print("Connected",addr)
    c.send("Thank you".encode())
    c.close()
