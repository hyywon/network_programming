from socket import *
import threading

def handler(sock) :
    while True:
        msg= sock.recv(1024)
        print(msg.decode())

addr = ('localhost', 5555)
sock = socket(AF_INET, SOCK_STREAM)
sock.connect(addr)


my_id = input('ID�� �Է��ϼ��� ') 
sock.send(('['+my_id+']').encode())

th = threading.Thread(target=handler, args=(sock,)) 
th.daemon = True
th.start()


while True:
    msg = '[' + my_id + '] ' + input()
    sock.send(msg.encode())