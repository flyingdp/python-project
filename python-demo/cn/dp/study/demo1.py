
# id 对象所存储的内存地址
# type 对象的数据类型

name = '董朋'
print(id(name))
print(type(name))
print(name)


print("我是董朋 开始学python")
print("I", "LOVE", "java")
print("100+100=", 100 + 100)
# name=input("请输入你的名字：\n")
# print("name="+name)
print("A的ASCII码是:", ord("A"))
print("65对应的字母是:", chr(65))
print("你好,%s" % "dp")
print("Hi,%s,my age is %d" % ("java", 23))
a = [1, 2, 3]
print(a)
print(len(a))
# if...else练习
age = 20
if age > 20:
    print("年龄大于20")
else:
    print("年龄小于20")
# for练习
print(list(range(11)))
sum = 0
for x in range(11):
    sum = sum + x
print(sum)
## while 练习
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)
## dict和set
map = {"name": "dongpeng", "work": "java+python"}
print(map)
print(map.get("name"))
print(map["work"])

t = input("input:")
print(type(t))
l = eval(t)
print(l)
