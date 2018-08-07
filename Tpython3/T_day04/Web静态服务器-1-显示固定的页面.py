# coding=utf-8
import re
from multiprocessing import Process
from socket import *
import sys

WSGI_PYTHON_DIR = "./wsigipython"
HOME_PATH = "./html"


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
    requestHeaderLines = data.splitlines()
    requestHeaderLines = requestHeaderLines[0]
    requestPath = re.match(r"\w+ +(/[^ ]*) ", requestHeaderLines.decode("utf-8")).group(1)
    method = re.match(r"(\w+) +/[^ ]* ", requestHeaderLines.decode("utf-8")).group(1)

    if requestPath.endswith(".py"):
        global responceHeaderLine
        try:
            mTime = __import__(requestPath[1:-3])
        except:
            responceHeaderLine = "HTTP/1.1 404 NOT FOUND\r\n"
            responBody = "The file is not found!"
        else:
            env = {
                "PATH_INFO": requestPath,
                "METHOD": method
            }
            responBody = mTime.application(env, start_response)
        responce = responceHeaderLine + "\r\n" + responBody

    else:
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


def start_response(status, headers):
    responceHeader = "HTTP/1.1 " + status + "\r\n"
    global responceHeaderLine
    for header in headers:
        responceHeader += "%s: %s\r\n" % header
    responceHeaderLine = responceHeader


if __name__ == '__main__':
    sys.path.insert(1, WSGI_PYTHON_DIR)
    print(sys.path)
    main()
