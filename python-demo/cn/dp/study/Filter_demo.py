def is_odd(n):
    return n % 2 == 1


L = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(L)


def not_empty(s):
    return s and s.strip()


L = list(filter(not_empty, ['A', '', 'B', '', None, 'C']))
print(L)

#  排序操作 sorted 默认 从小到大 排序
S = sorted([36, 5, -12, 9, -21])
print(S)

# 此外，sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序
S = sorted([36, 5, -12, 9, -21], key=abs)
print(S)

# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面
S = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(S)

# 忽略 大小写(忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写）再比较)
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 要进行反向排序，不必改动key函数，可以传入第三个参数reverse=True
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# 请用sorted()对上述列表分别按名字排序
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)
