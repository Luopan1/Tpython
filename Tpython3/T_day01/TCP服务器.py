# coding=utf-8
from socket import *
import time

tcpSocket = socket(AF_INET, SOCK_STREAM)
addr = (("", 7788))
tcpSocket.bind(addr)
tcpSocket.listen(5)
newSocket, chientAddr = tcpSocket.accept()
content = newSocket.recv(1024)

print(" %s" % (content))
newSocket.send("thank you".encode("gb2312"))
newSocket.close()
tcpSocket.close()
