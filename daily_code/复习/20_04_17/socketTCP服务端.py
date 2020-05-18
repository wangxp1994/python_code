from socket import *

sockfd = socket(AF_INET, SOCK_STREAM)

sockfd.bind(("localhost", 8888))

sockfd.listen(10)

conn, addr = sockfd.accept()
print("接收的地址是{}".format(addr))

data = conn.recv(1024)
print(data.decode())

conn.close()
sockfd.close()
