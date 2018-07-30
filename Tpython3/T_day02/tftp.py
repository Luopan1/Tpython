# coding=utf-8
import struct
from socket import *
import os
import time


def main():
    fileName = input("请输入要下载的文件的名字")
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    requestFileData = struct.pack("!H%dsb5sb" % len(fileName), 1, fileName.encode("utf-8"), 0, "octet".encode("utf-8"),0)
    udpSocket.sendto(requestFileData, ("192.168.1.179", 69))
    f = open(fileName, "w")
    num = 0
    while True:
        responseData = udpSocket.recvfrom(1024)
        print(responseData)
        recvData, serverInfo = responseData
        print("recvData:%s" % recvData)

        """opNum是操作码 3 表示有数据的文件 5 表示文件不存在  返回的是一个元祖 需要根据下标去取值"""

        opNum = struct.unpack("!H", recvData[:2])
        print("opNum:%s" % opNum)
        if opNum[0] == 5:
            print("******FILE NOT FOUND******")
            break
        """ packetNum返回的是块序号"""
        packetNum = struct.unpack("!H", recvData[2:4])
        print(packetNum)
        if opNum[0] == 3:
            num = num + 1
            if num == 65536:
                num = 0
            if num == packetNum[0]:
                f.write(recvData[4:].decode("utf-8"))
                num = packetNum[0]  # 这句代码没必要写 为了程序代码的安全，建议写上
        # 整理ACK的数据包
        ackData = struct.pack("!HH", 4, packetNum[0])  # 返回当前收到的块序号 让服务器接着发送下一块数据
        udpSocket.sendto(ackData, serverInfo)
        if len(recvData) < 516:
            udpSocket.close()
            break


if __name__ == "__main__":
    main()
