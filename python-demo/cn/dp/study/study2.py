# https://www.jianshu.com/p/3628bd29b260
list1 = ['a', 'b', 'c', 1, 2, 3, 4]
print(type(list1))
print(list1[0], list1[3])
print(list1[2:4])
# 追加新的元素
list1.append("add")
print(list1)
# 插入指定元素到指定位置
a = ['1', '2', '4']
a.insert(2, "3")
print(a)
# 删除元素,默认会弹出最后一个元素
a_list = ['a', 'b', 'c', 1, 2, 3, 'add']
a_list.pop()
print(a_list)
# 删除指定下标的元素
a_list.pop(0)
print(a_list)

# 删除指定的元素
a_list.remove('c')
print(a_list)

# 统计元素个数
print("元素的个数:", a_list.__len__())

# 是否包含元素
print('b' in a_list)

# 清除列表内容
# print(a.clear())

# 拷贝列表内容
copy = a_list.copy()
print(copy)

# 列表元素反转
b = ['c', 'c', 'b', 'a']
b.reverse()
print(b)

# 排序
a = [1, 2, 4, 1, 9, 6, -1]
print("排序前:", a)
a.sort()
print("排序后:", a)

# 循环赋值
a = [1, 2, 4]
n1, n2, n3 = a
print("n1=", n1)
print("n2=", n2)
print("n3=", n3)

a = '321'
n1, n2, n3 = a
print("n1=", n1)
print("n2=", n2)
print("n3=", n3)

# 元组
# 元组的作用主要是用来存多个值,对比列表来说，主要是用来读。是一个不可变的列表，其值不可变，其他属性和列表类似
a = (1, 2, 3, 4, 5)
print(a[2])
print(a[1:3])
print(len(a))
