from socket import *
import random

BUFF_SIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
addr = ('localhost', port)

while True:
    msg = input("->")
    reTx = 0 
    while reTx <= 3 :
        resp = str(reTx) + ' ' + msg
        c_sock.sendto(resp.encode(), addr)
        c_sock.settimeout(2)

        try: 
            data, addr = c_sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break

    c_sock.settimeout(None)      
    while True:
        data, addr = c_sock.recvfrom(BUFF_SIZE)
        if random.randint(1,10) <= 5:
            continue
        else :
            c_sock.sendto(b'ack',addr)
            print("<-", data.decode())
            break


c_sock.close()