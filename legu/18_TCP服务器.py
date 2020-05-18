
from socket import *
from threading import Thread

host = ""
port = 8888

socklst = {}


def link(sock, addr):
    print (addr, "已经连接")

    sock.send("please input your name")
    name = sock.recv(1024)
    socklst[name] = sock
    print (socklst)

    while True:
        try:
            data = sock.recv(1024)
        except:
            break

        if not data:
            break

        txt = ">>>" + name + ":" + data
        sendAll(name, txt)

    socklst.pop(sock)
    sock.close()


def sendAll(name, txt):
    for p in socklst:
        if name == p:
            continue
        socklst[p].send(txt)



# 开启套接字
sersock = socket(AF_INET, SOCK_STREAM)
# 绑定服务端口
sersock.bind((host, port))
# 开始监听
sersock.listen(5)
print ("开始监听")

while True:
    # 等待客户端连接
    clisock, addr = sersock.accept()

    t = Thread(target=link, args=(clisock, addr,))
    t.start()


sersock.close()



