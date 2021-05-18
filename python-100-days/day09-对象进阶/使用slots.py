# @Time: 2021/5/16 20:33  
# @Author: flying
# @Desc:

from types import MethodType


class Student(object):
    pass


# 还可以尝试给实例绑定一个方法
def set_age(self, age):
    self.age = age


def main():
    s = Student()
    s.name = 'flying'
    print(s.name)
    s.set_age = MethodType(set_age, s)  # 给实例绑定一个方法
    s.set_age(25)  # 调用实例方法
    print(s.age)  # 测试结果

    # 但是，给一个实例绑定的方法，对另一个实例是不起作用的：
    s2 = Student()  # 创建新的实例
    # s2.set_age(25)  # AttributeError: 'Student' object has no attribute 'set_age'


if __name__ == '__main__':
    main()


# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class ClassInfo(object):
    __slots__ = ('name','age')

def main():
    classInfo = ClassInfo()
    classInfo.name = 'dongpeng'
    classInfo.age = 23
    print('classInfo.name = ', classInfo.name)
    print('classInfo.age = ', classInfo.age)
    # 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误
    # classInfo.score = 99 AttributeError: 'ClassInfo' object has no attribute 'score'


if __name__ == '__main__':
    main()