# @Time: 2021/5/12 22:27  
# @Author: flying
# @Desc: https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/08.面向对象编程基础.md
class Test:
    def __init__(self, foo):
        self._foo = foo

    def bar(self):
        print(self._foo)


def main():
    test = Test('hello')
    test.bar()
    print(test._foo)


if __name__ == "__main__":
    main()