import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr) 
msg = sock.recv(1024) 
print(msg.decode())

name = "Hwang yewon"
sock.send(name.encode())
print(name)

num = sock.recv(1024)
num = num.decode()
num = socket.ntohl(int(num))
print(num)

sock.close()
