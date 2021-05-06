import math


def print_s():
    print('*' * 15)
    print('hello'.center(15, '*'))
    print('*' * 15)


print_s()


def newuser(name, age, sex='male'):
    print(name, age, sex)


newuser('dp', 13)
newuser("aa", 20, 'female')


def foo(x, y, *args):
    print(x)
    print(y)
    print(args)


print("foo方法-----按照位置定义的实参溢出的情况使用* 输出的内容为变量值和元组")
foo(1, 2, 3, 4, 5)


def foo(x, y, **kwargs):
    print(x)
    print(y)
    print(kwargs)


print('foo方法-----按照关键字定义的实参溢出的情况使用** 输出的内容为变量值和列表')
foo(x=1, y=2, a=3, b=4, c=5)


def foo(name, age, *, sex):  # * 后面的sex为命名关键字参数，对其传值需要指明关键字，否则会报错。
    print(name)
    print(age)
    print(sex)


foo('andy', 22, sex='male')  # sex必须以关键字形式传值


# 函数的定义类似与变量的定义，可以当作对象来赋值:
def foo():
    print("from foo")


f = foo  # 函数名其实就是指向一个函数对象的引用，完全可以把函数名赋给一个变量，相当于给这个函数起了一个“别名”：
f()  # 执行 f()


def foo():
    print('from foo2')


def wrapper(func):
    print(func())


# wrapper(foo)


# 定义函数
# def show_args(arg, *args, **kwargs):  # 第一个参数是单个参数；第二个参数是不定长参数；第三个是不定长字典。
#     print(arg)
#     for item in args:
#         print(item)
#     for key, value in kwargs.items():
#         print(key, value)
# args = [1, 5, 3, 4]
# kwargs = dict(name='testing', age=24, year=2014)
# print (show_args("hey", *args, **kwargs))

# 结果是：
# hey
# 1
# 5
# 3
# 4
# name testing
# age 24

# pass空函数 如果想定义一个什么事也不做的空函数，可以用pass语句
# pass语句什么都不做，那有什么用？实际上pass可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来
def nop():
    # print("我是nop方法")
    pass


a = nop
a()


def move(x, y, step, angle=0):
    nx = x + step * angle
    ny = y - step * angle
    return nx, ny


x, y = move(1, 2, 3, 4)
print("x=", x, "y=", y)
z = move(1, 2, 3, 4)
print("z=", z)

########################可变参数###########################
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum
sum = calc(1, 2, 3)
print("sum==", sum)
sum2 = calc()
# print(sum2) #0
nums = [1, 2, 3]
nums = (4, 5, 6)
# *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
print(calc(*nums))

##########################关键字参数#############################
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
#函数person除了必选参数name和age外，还接受关键字参数kw。在调用该函数时，可以只传入必选参数
person("MIKE",30)
person("Boy",35,city = 'BeiJing')
person('Adam', 45, gender='M', job='Engineer')

# 和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去
extra = {'city':'beijing','job':'engineer'}
person('Jack',24,city = extra['city'],job = extra['job'])

# 当然,上面复杂的调用可以用简化的写法：
# **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
person("John",34,**extra)


##########################命名关键字参数#############################
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)
# 但是调用者仍可以传入不受限制的关键字参数：
person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)

# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下
def person(name,age,*,city,job):
    print(name,age,city,job)
person('Jack', 24, city='Beijing', job='Engineer') #city和job必传

