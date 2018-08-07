# coding=utf-8
import socket
from multiprocessing import Process
import re, sys


WSGI_PYTHON_DIR = "../html"


class HTTPServer(object):
    def __init__(self, application):
        self.application = application
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    def bind(self, port):
        self.server_socket.bind(("", port))

    def start(self):
        self.server_socket.listen(5)
        while True:
            newClient, addr = self.server_socket.accept()
            handClientProcess = Process(target=self.handlerClient, args=(newClient,))
            handClientProcess.start()
            newClient.close()

    def handlerClient(self, newClicent):
        content = newClicent.recv(2048)
        request_line = content.splitlines()
        fileName = re.match(r"\w+ +(/[^ ]*) ", request_line[0].decode("utf-8")).group(1)
        method = re.match(r"(\w+) +/[^ ]* ", request_line[0].decode("utf-8")).group(1)
        env = {
            "PATH_INFO": fileName,
            "METHOD": method
        }
        print(fileName)
        responseBody = self.application(env, self.start_responce)
        responce = self.headerLines + "\r\n" + responseBody
        newClicent.send(responce.encode("utf-8"))
        newClicent.close()

    def start_responce(self, status, heads):
        headerLines = "HTTP/1.1" + status + "\r\n"
        for head in heads:
            headerLines += "%s:%s\r\n" % head
        self.headerLines = headerLines

def main():
    if len(sys.argv) < 2:
        sys.exit("python MyWebServer.py Module:app")
    sys.path.insert(1, WSGI_PYTHON_DIR)
    print(sys.argv)
    module, appName = sys.argv[1].split(":")
    m = __import__(module)
    app = getattr(m, appName)
    httpServer = HTTPServer(app)
    httpServer.bind(7788)
    httpServer.start()


if __name__ == '__main__':
    main()
