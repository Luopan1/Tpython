# coding=utf-8
from socket import *
from time import ctime
from threading import Thread

udpSocket = None
addr = None


def sendData():
    while True:
        sendData = input("<<")
        if sendData == "q":
            udpSocket.close()
            break
        udpSocket.sendto(sendData.encode("gb2312"), addr)


def receData():
    while True:
        content, desInfp = udpSocket.recvfrom(1024)
        print('【%s】%s:%s' % (ctime(), desInfp, content.decode("gb2312")))


if __name__ == '__main__':
    udpSocket = socket(AF_INET, SOCK_DGRAM)
    addr = ("192.168.65.1", 8081)
    udpSocket.bind(("", 7799))
    sendThread = Thread(target=sendData)
    receThrad = Thread(target=receData)
    sendThread.start()
    receThrad.start()

    receThrad.join()
    sendThread.join()
