import time
from greenlet import greenlet


def A():
    while True:
        print("----A---")
        gr2.switch()
        time.sleep(0.5)


def B():
    while True:
        print("----B---")
        gr1.switch()
        time.sleep(0.5)


if __name__ == '__main__':
    gr1 = greenlet(A)
    gr2 = greenlet(B)
    gr1.switch()
