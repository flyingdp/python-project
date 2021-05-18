"""
 @Time: 2021/5/13 13:56
 @Author: flying
 @Desc:  之前我们讨论过Python中属性和方法访问权限的问题，
         虽然我们不建议将属性设置为私有的，但是如果直接将属性暴露给外界也是有问题的，
         比如我们没有办法检查赋给属性的值是否有效。
         我们之前的建议是将属性命名以单下划线开头，通过这种方式来暗示属性是受保护的，
         不建议外界直接访问，那么如果想访问属性可以通过属性的getter（访问器）和setter（修改器）方法进行对应的操作。
         如果要做到这点，就可以考虑使用@property包装器来包装getter和setter方法，使得对属性的访问既安全又方便
"""


class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Python内置的@property装饰器就是负责把一个方法变成属性调用的
    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 修改器 - setter方法
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩捉迷臧' % self._name)
        else:
            print('%s正在玩王者荣耀' % self._name)


def main():
    person = Person('flying', 26)
    person.play()

    person.name = '董朋'  # OK，实际转化为person.set_name('董朋')
    person.age = 12
    person.play()


if __name__ == '__main__':
    main()








