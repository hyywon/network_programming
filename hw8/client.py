from socket import *

BUFF_SIZE = 1024
port = 5555

c_sock = socket(AF_INET, SOCK_DGRAM)
addr = ('localhost', port)
while True :
    msg = input("Enter the message(\"send mboxId message\" or \"receive mboxId\"):")

    c_sock.sendto(msg.encode(), addr)
    if msg == "quit":
        break
    else:
        data, ad = c_sock.recvfrom(BUFF_SIZE)
        print(data.decode())
        pass

c_sock.close()