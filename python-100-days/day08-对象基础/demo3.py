"""
 @Time: 2021/5/13 10:58
 @Author: flying
 @Desc: Python并没有从语法上严格保证私有属性或方法的私密性，
        它只是给私有的属性和方法换了一个名字来妨碍对它们的访问，
        事实上如果你知道更换名字的规则仍然可以访问到它们，下面的代码就可以验证这一点
"""


class Test:
    def __init__(self, foo):
        self.__foo = foo


    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    test = Test('hello')
    test.__bar()



if __name__ == "__main__":
    main()