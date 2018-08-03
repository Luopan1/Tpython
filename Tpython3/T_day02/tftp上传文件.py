# coding=utf-8
from socket import *
import struct


def main():
    code = "utf-8"
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(("", 8899))
    fileName = input("请输入你要上传的文件")
    uploadData = struct.pack("!H%dsb5sb" % len(fileName), 2, fileName.encode("utf-8"), 0, "octet".encode("utf-8"), 0)
    udpSocket.sendto(uploadData, ("192.168.1.179", 69))
    f = open(fileName, "rb")
    num = 0
    while True:
        recvData, serverInfo = udpSocket.recvfrom(1024)
        print(recvData)
        opNum = struct.unpack("!H", recvData[:2])

        packetNum = struct.unpack("!H", recvData[2:4])
        # print("opNum:%d    packNum:%d" % (opNum[0], packetNum[0]))
        if opNum[0] == 5:
            udpSocket.close()
            print("----- Illegal TFTP operation -----")
            break

        if opNum[0] == 4:
            if packetNum[0] == num:
                content = f.read()
                data = struct.pack("!HH", 3, packetNum[0]) + content
                udpSocket.sendto(data, serverInfo)
        if num != packetNum[0] or len(data) < 516:
            print("文件传输成功")
            udpSocket.close()
            f.close()
            break
        num += 1
        if num == 65515:
            num = 0


if __name__ == '__main__':
    main()
