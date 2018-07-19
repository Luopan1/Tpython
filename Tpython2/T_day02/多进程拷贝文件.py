# coding = utf-8
from multiprocessing import Pool, Manager
import os


def copyFileTask(name, oldFolderName, newFolderName, queue):
    fr = open(oldFolderName + "/" + name)
    fw = open(newFolderName + "/" + name, "w")
    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()
    queue.put(name)


def main():
    oldFolderName = "/home/lozzow/PycharmProjects/Python/Day_05"
    newFolderName = oldFolderName + "-复件"
    os.mkdir(newFolderName)
    # 获取旧文件夹所有的文件名字
    fileNames = os.listdir(oldFolderName)  # 使用多进程的方式拷贝文件
    pool = Pool(5)
    queue = Manager().Queue()
    for name in fileNames:
        pool.apply_async(copyFileTask, args=(name, oldFolderName, newFolderName, queue,))

    pool.close()
    pool.join()

    num = 0
    allNum = len(fileNames)
    while True:
        queue.get()
        num += 1
        copyRate = num / allNum
        print("\r copy的进度是%.2f%%" % (copyRate * 100), end="")
        if num == allNum:
            break
    print("完成拷贝")


if __name__ == "__main__":
    main()
