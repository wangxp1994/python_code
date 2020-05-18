
from socket import *
from threading import Thread

# host = "211.159.182.22"

host = "127.0.0.1"
port = 8888

def link(sock):
    while True:
        data = sock.recv(1024)
        if not data:
            break

        print (data)

clisock = socket(AF_INET, SOCK_STREAM)
clisock.connect((host, port))

t = Thread(target=link, args=(clisock,))
t.start()

while True:
    data = raw_input()
    if not data:
        break

    clisock.send(data)

clisock.close()
