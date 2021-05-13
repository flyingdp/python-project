def add(a=0, b=0, c=0):
    return a + b + c


# 不传 则使用函数中定义的默认参数值
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(c=10, a=20, b=30))

'''
我们给上面两个函数的参数都设定了默认值，
这也就意味着如果在调用函数的时候如果没有传入对应参数的值时将使用该参数的默认值，
所以在上面的代码中我们可以用各种不同的方式去调用add函数，
这跟其他很多语言中函数重载的效果是一致的。
'''

'''
其实上面的add函数还有更好的实现方案，因为我们可能会对0个或多个参数进行加法运算，
而具体有多少个参数是由调用者来决定，我们作为函数的设计者对这一点是一无所知的，
因此在不确定参数个数的时候，我们可以使用可变参数，代码如下所示。
'''


def add(*agrs):
    total = 0
    for i in agrs:
        total += i
    return total


# 在调用add函数时可以传入0个或多个参数 http://login.sit.mayibank.net/login/loginhome.htm
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 2, 3, 4, 5, 6))
