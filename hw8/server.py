from socket import *
from collections import deque

BUFF_SIZE = 1024
port = 5555
mbox = {}
s_sock = socket(AF_INET,SOCK_DGRAM)
s_sock.bind(('',port))
print("Listening.. ")

while True:
    data, addr = s_sock.recvfrom(BUFF_SIZE)
    req = data.decode()
    msg = list(req.split())
    print(msg[0])

    if msg[0] == "send":
        message = " ".join(msg[2:])
        
        if msg[1] in mbox :
            mbox[msg[1]].append(message)
        else :
            mbox[msg[1]] = deque([message])

        s_sock.sendto(b'OK',addr)

    elif msg[0] == "receive":
        
        if msg[1] in mbox:
            if mbox[msg[1]]:
                message = mbox[msg[1]].popleft()
                s_sock.sendto(message.encode(),addr)
                print(mbox[msg[1]])
            else:
                print(mbox[msg[1]])
                s_sock.sendto(b'No messages',addr)
        else:
            s_sock.sendto(b'No messages',addr)

    elif msg[0] == "quit":
        break

s_sock.close()
