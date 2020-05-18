from socket import *

sockfd = socket(AF_INET, SOCK_STREAM)

sockfd.connect(("127.0.0.1", 8888))

sockfd.send("我爱你".encode())

sockfd.close()