# coding=utf-8
from multiprocessing import Process
from socket import *


def main():
    tcpScoket = socket(AF_INET, SOCK_STREAM)
    tcpScoket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcpScoket.bind(("", 7788))
    tcpScoket.listen(5)
    while True:
        clientSocket, addr = tcpScoket.accept()
        p = Process(target=handclient, args=(clientSocket,))
        p.start()
        clientSocket.close()


def handclient(cli_socket):
    data = cli_socket.recv(2048)
    HOME_PATH = "./html"
    requestHeaderLines = data.splitlines()
    try:
     requestPath = requestHeaderLines[0].decode("utf-8").split(" ")[1]
    except:
        pass
    print(requestPath)
    if "/" == requestPath:
        requestPath = "/index.html"
        print("-------------")

    try:
        print(HOME_PATH + requestPath)
        f = open(HOME_PATH + requestPath, "rb")
        content = f.read()
    except:
        responceHeaderLine = "HTTP/1.1 404 NOT FOUND\r\n"
        responBody = "The file is not found!"
    else:
        responceHeaderLine = "HTTP/1.1 200 OK\r\n"
        responceHeaderLine += "\r\n"
        responBody = content.decode("utf-8")
    responce = responceHeaderLine + responBody
    cli_socket.send(bytes(responce, "utf-8"))
    cli_socket.close()


if __name__ == '__main__':
    main()
