"""
    @Time: 2021/5/12 22:18
    @Author: flying
    @Desc: 使用type()检查变量的类型
    @link: https://github.com/jackfrued/Python-100-Days/tree/master/Day01-15
"""
a = 100
b = 12.345
c = 1 + 5j
d = "hello world"
f = False
print("a = 100的类型：", type(a))
print("b = 12.345的类型：", type(b))
print("c = 1 + 5j的类型：", type(c))
print("d = hello world的类型", type(d))
print("f = False：", type(f))


x = 1000
y = 1000
print('x is y',x is y)
