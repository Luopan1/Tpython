# coding=utf-8

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j += 1
        break #break在哪个while里面  就结束哪个循环
    print(" ")
    i += 1;
