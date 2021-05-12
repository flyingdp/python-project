"""
使用input()函数获取键盘输入(字符串)
使用int()函数将输入的字符串转换成整数
使用print()函数输出带占位符的字符串

Version: 0.1
Author: flying

说明：print函数中输出的字符串使用了占位符语法，
其中%d是整数的占位符，%f是小数的占位符，
%%表示百分号（因为百分号代表了占位符，所以带占位符的字符串中要表示百分号必须写成%%），
字符串之后的%后面跟的变量值会替换掉占位符然后输出到终端中，运行上面的程序，看看程序执行结果就明白啦。
"""
a = int(input('a = '))
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d - %d = %d' % (a, b, a - b))
print('%d * %d = %d' % (a, b, a * b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))  # 整除
print('%d %% %d = %d' % (a, b, a % b))  # 求余
print('%d ** %d = %d' % (a, b, a ** b))  # 指数

f = float(input("请输入华氏温度:"))
c = (f - 32) / 1.8
print('%.1f华氏度=%.1f摄氏度' % (f, c))

"""
输入年份 如果是闰年输出True 否则输出False

Version: 0.1
Author: flying
"""
year = int(input("请输入年份："))
is_leap = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
print("当前年份%d是否闰年:" % (year), is_leap);

