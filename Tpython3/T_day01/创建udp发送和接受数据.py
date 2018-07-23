# coding=utf-8
from socket import *

udpSocket = socket(AF_INET, SOCK_DGRAM)
addr = ("192.168.65.1", 8081)
sendData = input("请输入发送的数据\n")
udpSocket.bind(("", 7788))
udpSocket.sendto(sendData.encode("gb2312"), addr)
rcvData = udpSocket.recvfrom(1024)
content, destInfo = rcvData
print(content.decode("gb2312"))
print(destInfo)
udpSocket.close()
