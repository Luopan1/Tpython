# coding=utf-8
from socket import *

tcpSocket = socket(AF_INET, SOCK_STREAM)
addr = ("192.168.123.69", 8080)
tcpSocket.connect(addr)
sendData = input(">>")
tcpSocket.send(sendData.encode("gb2312"))
recvData = tcpSocket.recv(1024)
print(recvData.decode("gb2312"))
tcpSocket.close()
