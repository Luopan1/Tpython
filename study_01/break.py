#coding=utf-8
i=1
while i<=5:
    if i==3:
        break #continue 退出本次循环  剩下的代码全部都不执行 直接跳转到判断i是否小于等于5 而i一直都等于3 从来都没有+1，成了死循环,
        # break 是退出所有的循环，下面的代码也不会执行
    print(i)
    i+=1