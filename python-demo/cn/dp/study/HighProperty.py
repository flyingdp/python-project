from collections.abc import Iterable

L = ['aa', 'bb', 'cc', 'dd']
# L[0:3]表示,从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素
print(L[0:3])  # ['aa', 'bb', 'cc']
# 如果第一个索引是0 可以省略
print(L[:3])
print(L[:7])  # ['aa', 'bb', 'cc', 'dd']
# 支持-1 取倒数第一个元素
print(L[-2: -1])  # cc
print(L[-2:])  # cc dd

L = list(range(100))
print(L)

# 取出某一段数列 比如前10个数
print(L[:10])
# 取后10个数
print(L[-10:])
# 取前11-20个数
print(L[10:20])
# 前10个数，每两个取一个
print(L[:10:2])
# 所有数 每5个取一个
print(L[::5])
# 只写[:]就可以原样复制一个list
print(L[:])

print((0, 1, 2, 3, 4, 5)[:3])

print('ABCDEFG'[:3])

print('ABCDEFG'[::2])

d = {'a': 1, 'b': 2, 'c': 3}
print("#########key###########")
for key in d:
    print(key)
print("#########value###########")
for value in d.values():
    print(value)
print("######### 遍历key value ###########")
for k, v in d.items():
    print("key:", k + " value:", v)

print("######### 遍历字符串 ###########")
for ch in 'ABC':
    print(ch)

#  如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断
isTrue = isinstance('abcd', Iterable)  # str是否可以迭代
print("str是否可以迭代:", isTrue)
print("list是否可以迭代:", isinstance([1, 2, 3], Iterable))
print("整数是否可以迭代:", isinstance(123, Iterable))

#  最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)
print()

for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

L = list(range(1, 11))
print(L)

# 生成[1x1, 2x2, 3x3, ..., 10x10]
L = []
for x in range(1, 11):
    L.append(x * x)

print(L)

# 等同于下面的写法
L = [x * x for x in range(1, 11)]
print(L)

# for语句加if条件
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

L = [m + n for m in 'ABC' for n in 'XYZ']
print(L)

L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# if.......else............for
L = [x if x % 2 == 0 else -x for x in range(1, 11)]
print(L)

g = (x*x for x in range(10))
for n in g:
    print(n)

