# @Time: 2021/5/12 21:53  
# @Author: flying
# @Desc: Set操作：Python中的集合跟数学上的集合是一致的，不允许有重复元素，而且可以进行交集、并集、差集等运算。

# 创建集合的字面量语法
set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length =', len(set1))
# 创建集合的构造器语法(面向对象部分会进行详细讲解)
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 创建集合的推导式语法(推导式也可以用于推导集合)
set4 = {num for num in range(1, 10) if num % 3 == 0 or num % 5 == 0}
print(set4)  # {9, 3, 5, 6}

set1.add(4)
set1.add(5)
print(set1)  # {1, 2, 3, 4, 5}
set2.update([11, 12])
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set2)

print(set3.pop())
print(set3)

print('========================集合的成员、交集、并集、差集等运算==========================')
set1 = {1, 2, 3, 4, 2, 4}
set2 = {3, 4, 6, 7, 8, 9, 1}
# 集合的交集、并集、差集、对称差运算
print(set1 & set2)
# print(set1.intersection(set2))
print(set1 | set2)
# print(set1.union(set2))
print(set1 - set2)
# print(set1.difference(set2))
print(set1 ^ set2)
# print(set1.symmetric_difference(set2))
# 判断子集和超集
print(set2 <= set1)
# print(set2.issubset(set1))
print(set3 <= set1)
# print(set3.issubset(set1))
print(set1 >= set2)
# print(set1.issuperset(set2))
print(set1 >= set3)
# print(set1.issuperset(set3))

'''
说明： 
Python中允许通过一些特殊的方法来为某种类型或数据结构自定义运算符（后面的章节中会讲到），
上面的代码中我们对集合进行运算的时候可以调用集合对象的方法，也可以直接使用对应的运算符，
例如&运算符跟intersection方法的作用就是一样的，但是使用运算符让代码更加直观。
'''