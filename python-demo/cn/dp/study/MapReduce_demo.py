from functools import reduce


def f(x):
    return x * x


# map()传入的第一个参数是f，即函数对象本身。
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
r = map(f, [1, 2, 3, 4])
print(list(r))

print(list(map(str, [11, 12, 13])))


def fn(x, y):
    return x + y


# 再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
r = reduce(fn, [1, 3, 5, 7, 9])
print(r)
