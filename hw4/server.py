import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('localhost', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print("Connection from ", addr)
    client.send(b'Hello '+ addr[0].encode()) 

    name = client.recv(1024)
    print(name.decode())
    
    num = 20181526
    num = socket.htonl(num)
    num = str(num) + ' '
    client.send(num.encode())
    client.close()