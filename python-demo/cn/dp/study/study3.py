# 字典 https://www.jianshu.com/p/0b5625ec1ee8
# 字典用于存多个值，使用key-value存取，取值速度快。
# key必须是不可变类型（也称作可hash类型），value可以是任意类型,字典中key是无序的。
# 不可变类型的数据可以当作字典的key(数字，字符串，元组)

# 存值
dir = {'a': 1, 'b': 2, 'c': 3}
print(dir)
dir['D'] = 4
print(dir)

# 删除字典的值
dir.pop('a')
print(dir)
print(dir.pop("aa", "None"))
print(dir)

# get() 取值,当值不存在时,可以指定返回值
print(dir.get('b'))
print(dir.get('a', "not is key"))

# 取出所有的key和value
dir = {'a': 1, 'b': 2, 'c': 3}
print("dir的keys:", dir.keys())
print("dir的values:", dir.values())
print("dir的items:", dir.items())
for key, value in dir.items():
    print(key, value)

# 复制字典
dir = {'a': 1, 'b': 2, 'c': 3}
c = dir.copy();
print(c)

# fromkeys()创建字符串
dir = dict.fromkeys(['a', 'b', 'c'], "123321")
print(dir)

# update()更新字典
dir = {'a': 1, 'b': 2, 'c': 3}
a = {'name': 'xxx', 'age': 23, 'a': 8888}
dir.update(a)
print(dir)


