# coding=utf-8
import time

from Tpython3.T_day04.通用web服务器框架.MyWebServerceFrameWork import HTTPServer


class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        for urls, handler in self.urls:
            if path == urls:
                return handler(env, start_response)
        status = "404 Not Found"
        heades = []
        start_response(status, heades)
        return "Not Found"


def showTime(env, start_responce):
    status = "200 ok"
    heades = [
        ("Content-Type", "text/plain")
    ]
    start_responce(status, heades)
    return time.ctime()


def main():
    urls = [
        ("/", showTime)
    ]
    app = Application(urls)
    httpServer = HTTPServer(app)
    httpServer.bind(7788)
    httpServer.start()


if __name__ == '__main__':
    main()
