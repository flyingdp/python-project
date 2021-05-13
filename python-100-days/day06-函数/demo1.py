
"""求阶乘"""
def fac(num):
    result = 1
    for n in range(1,num+1):
        result*=n
    return result

m = int(input("请输入阶乘的数字:"))
print("%d的阶乘是：" %(m),fac(m))

