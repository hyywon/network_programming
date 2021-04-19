from socket import *
import random

BUFF_SIZE = 1024
port = 5555
s_sock = socket(AF_INET,SOCK_DGRAM)
s_sock.bind(('',port))
print("Listening.. ")

while True:
    s_sock.settimeout(None)
    while True:
        data, addr = s_sock.recvfrom(BUFF_SIZE)
        if random.randint(1,10) <= 5:
            continue
        else :
            s_sock.sendto(b'ack',addr)
            print("<-", data.decode())
            break
        
    msg = input("->")
    reTx = 0     
    while reTx <= 3 :
        resp = str(reTx) + ' ' + msg
        s_sock.sendto(resp.encode(), addr)
        s_sock.settimeout(2)

        try: 
            data, addr = s_sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

s_sock.close()
