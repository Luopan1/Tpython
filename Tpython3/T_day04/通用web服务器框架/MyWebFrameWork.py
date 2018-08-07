# coding=utf-8
import time

HTML_ROOT_DIR = "../html"


class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO", "/")
        if path.startswith("/static"):
            try:
                fileName = path[7:]
                f = open(HTML_ROOT_DIR + fileName, "rb")

                status = "200 ok"
                content = f.read()
                f.close()
                heades = []
                start_response(status, heades)
                return content.decode("utf-8")
            except:
                status = "404 Not Found"
                heades = []
                start_response(status, heades)
                return "Not Found"

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


urls = [
    ("/", showTime)
]
app = Application(urls)


def main():
    pass
    # urls = [
    #     ("/", showTime)
    # ]
    # app = Application(urls)
    # httpServer = HTTPServer(app)
    # httpServer.bind(7788)
    # httpServer.start()


if __name__ == '__main__':
    main()
