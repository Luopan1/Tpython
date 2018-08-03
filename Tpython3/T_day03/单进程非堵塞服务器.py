# coding=utf-8
from socket import *

serSocket = socket(AF_INET, SOCK_STREAM)
serSocket.bind(("", 7788))
serSocket.setblocking(False)
serSocket.listen(5)
clientLists = []
while True:
    try:
        clientSocket, addr = serSocket.accept()
        clientSocket.setblocking(False)
        clientLists.append((clientSocket, addr))
    except:
        pass
    else:
        print("来了一个新的连接%s" % str(addr))

    for clientSocket, addr in clientLists:
        try:
            content = clientSocket.recv(1024)
        except:
            pass
        else:
            if len(content) > 0:
                print("【%s:】%s" % (str(addr), content))
            else:
                print("%s已经断开连接" % str(addr))
                clientSocket.close()
                clientLists.remove((clientSocket, addr))
