# Python数据类型一数字和字符串 https://www.jianshu.com/p/0424d49f325d

a = 10
# 1:使用id()和type()可以查看变量的值在内存中的ID号和数据类型
print(id(a))
print(type(a))

b = "123"
print(id(b))
print(type(b))

# 使用input()数据的输入 (无论输入的是什么格式,最终都会是字符串的格式)
# c = input("input:")
# print(c)
# print(type(c))
#
# # 将str类型转换为list类型，可以使用eval()
# d = input("input:")
# print(d)
# print(type(d))
# e = eval(d)
# print(e)
# print(type(e))

# 变量赋值
f = g = h = i = 10
print(f, g, h, i)

x = 1
y = 2
x, y = y, x
print(x, y)

# 格式化输出(使用%s 和%d 可以表示字符串和数字,在格式化输出的时候可以带入)
print("this is python %d" % 3)
print("my name is %s age is %d" % ("flying", 24))

# 数字
a = 10  # 系统自动添加了类型相当于 a=int(10)
print("a=", a, "type", type(a))
b = 10.99  # 系统自动添加了类型相当于 a=float(10.99)
print("b=", b, "type", type(b))
c = 1 - 2  # 负数
print("c=", c, "type", type(c))

# 字符串处理
a = 'abcdef'
print(a[0], a[1], a[-1])
b = '  abcd ef '
print(b.strip())  # strip() 去除首末的空格

c = "###12##3###"
print(c.strip("#"))

d = '###***abc***&&&'
print(d.strip("*"))
print(d.strip("#*&"))
print(d.lstrip("#"))
print(d.rstrip("*&"))

name = 'root:x:0:0:root:/root:/bin/bash'
print(name.split(":"))
print(name.split(":")[4])
print(name.split(":", 1))  # 指定切分的次数

name = 'welcome    to  new     home'
print(name)
print(name.split())

# replace() 字符替换,第一个字符表示要替换的字符，第二个表示新的字符，第三个数字表示替换的个数
a = 'Hello world'
aa = a.replace('o', 'O', 2)
print(aa)

c = '{} {} {}'.format('a', 'b', 2)
c = '{0} {1} {0}'.format('a', 'b', 3)
# print(c)
print('{name} {sex} {age}'.format(name='a', sex='b', age=45))

# isdigit() 判断输入的字符串是否是数字:
num = '123'
print(num.isdigit())

# find()和 rfind() 查找字符所在的索引位置,找不到时返回-1，rfind()表示从右向左查找
a = 'hello world'
print(a.find('3'))
print(a.find('o'))
print(a.find('o', 4, 8))
print(a.find('o', 5, 8))
print(a.rfind('o', 4, 8))

# index()和rindex() 显示字符所在的下标索引，数字表示指定的索引范围，字符不存在会报错，rindex()表示从右向左查找
print("index开始练习")
print(a.index('o'))
print(a.index('o', 4, 8))  # todo
print(a.index('o', 5, 8))
print(a.rindex('o', 4, 8))

# join() 表示拼接字符串
print("join开始练习")
name = ['welcome', 'to', 'new', 'home']
print(name)
print(" ".join(name))
print(":".join(name))

# center(),ljust(),rjust(),zfull() 字符填充
a = 'hello'
print(a.center(30, "*"))
'************hello*************'
print(a.rjust(30, '*'))
'*************************hello'
print(a.ljust(30, '*'))
'hello*************************'
print(a.ljust(30))
'hello                         '
print(a.zfill(30))
'0000000000000000000000000hello'

# 字母大小写转换
name = 'hello world'
print(name.upper())  # 全部大写
'HELLO WORLD'
print(name.capitalize())  # 第一个单词首字母大写
'Hello world'
print(name.swapcase())  # 大小写反转
'HELLO WORLD'
print(name.title())  # 每个单词首字母大写
'Hello World'
name = 'HELLO'
print(name.lower())  # 全部小写
'hello'
