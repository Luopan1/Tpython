# coding=utf-8
import threading
import os.path
from queue import Queue


class CopyThread(threading.Thread):
    def __init__(self, fileName, queue):
        threading.Thread.__init__(self)
        self.fileName = fileName
        self.queue = queue

    def run(self):
        oldFile = open(oldFolder + "/" + self.fileName, "rb")
        newFile = open(newFolder + "/" + self.fileName, "wb")
        for temp in oldFile.readlines():
            newFile.write(temp)
        self.queue.put(oldFile)
        oldFile.close()
        newFile.close()


class CopyProgress(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue
        self.size = len(os.listdir(oldFolder))
        self.index = 0

    def run(self):
        if self.queue.qsize() > 0:
            self.queue.get()
            self.index += 1
            print("\r 当前的进度为%f", (self.index / self.size) * 100)


oldFolder = "C:\\Users\\19233\Desktop\Python\Python核心编程\python高级\html版\python高级-课件\Images"
newFolder = "C:\\Users\\19233\Desktop\Python\Python核心编程\python高级\html版\python高级-课件\Images-副本"
os.mkdir(newFolder)
queue = Queue()
index = 0
size = os.listdir(oldFolder)

for file in os.listdir(oldFolder):
    copyThread = CopyThread(file, queue)
    copyThread.start()

    queue.get()
    index += 1
    copyRate = index / len(size)
    print("\r copy的进度是%.2f%%" % (copyRate * 100), end="")
    if index == len(size):
        print("\n")
print("完成拷贝")
