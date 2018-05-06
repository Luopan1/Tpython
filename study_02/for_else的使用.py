#coding=utf-8
nums=[11,22,33,44,55,66,77]

for temp in nums:
    print(temp)
    if temp==88:
        break
else:#执行完for循环之后执行者一句输出代码 如果for循环里面放一个break 就不会执行输出代码（跳出所有的循环）
    print("=============")