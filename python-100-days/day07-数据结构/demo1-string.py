s1 = "hello"
s2 = "world"
print(s1, s2)
print(s1, s2, end='')

s1 = 'hello' * 3
print(s1)
s2 = 'world'
s1 += s2
print(s1)
print('ll' in s1)
print('good' not in s2)

# Python索引有两种方式，从左往右为从0开始逐一递增，从右往左为从-1开始逐一递减
# [) 左开右闭
str2 = 'abcd123456'
print(str2[2])  # c (下标从0开始)
print(str2[2:5])  # cd1
print(str2[2:])  # cd123456
print(str2[2::2])  # c135  步长为2
print(str2[::2])  # ac135
print(str2[::-1])  # 654321dcba
print(str2[-3:-1])  # 45
print('=================================================')

str1 = 'hello, world!'
# 通过内置函数len计算字符串的长度
print(len(str1))  # 13
# 获得字符串首字母大写的拷贝
print(str1.capitalize())  # Hello, world!
# 获得字符串每个单词首字母大写的拷贝
print(str1.title())  # Hello, World!
# 获得字符串变大写后的拷贝
print(str1.upper())  # HELLO, WORLD!
# 从字符串中查找子串所在位置
print(str1.find('or'))  # 8
print(str1.find('shit'))  # -1 没找到
# 与find类似但找不到子串时会引发异常
# print(str1.index('or'))
# print(str1.index('shit'))
# 检查字符串是否以指定的字符串开头
print(str1.startswith('He'))  # False
print(str1.startswith('hel'))  # True
# 检查字符串是否以指定的字符串结尾
print(str1.endswith('!'))  # True
# 将字符串以指定的宽度居中并在两侧填充指定的字符
print(str1.center(50, '*'))
# 将字符串以指定的宽度靠右放置左侧填充指定的字符
print(str1.rjust(50, ' '))
str2 = 'abc123456'
# 检查字符串是否由数字构成
print(str2.isdigit())  # False
# 检查字符串是否以字母构成
print(str2.isalpha())  # False
# 检查字符串是否以数字和字母构成
print(str2.isalnum())  # True

str3 = '  jackfrued@126.com '
print(str3)
# 获得字符串修剪左右两侧空格之后的拷贝
print(str3.strip())

print('=================================================')
a, b = 5, 10
print('%d * %d = %d' % (a, b, a * b))  # 等效于下边的
print('{0} * {1} = {2}'.format(a, b, a * b))
print(f'{a} * {b} = {a * b}')
