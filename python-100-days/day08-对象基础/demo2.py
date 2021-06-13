# @Time: 2021/5/12 22:27  
# @Author: flying
# @Desc: https://github.com/jackfrued/Python-100-Days/blob/master/Day01-15/08.面向对象编程基础.md

# 在Python中，属性和方法的访问权限只有两种，也就是公开的和私有的，如果希望属性是私有的，在给属性命名时可以用两个下划线作为开头
class Test:


    def __init__(self, foo):
        self.__foo = foo


    def bar(self):
        print("foo值:%s" % self.__foo)

def main():
    test = Test('hello')
    test.bar()

    # test.__foo = 'world'
    # test.bar()
    #  无法从外部访问实例变量.__foo
    print(test.__foo)  # AttributeError: 'Test' object has no attribute '__foo' 因为foo变量是私有的

    # 仍然可以通过_Test__foo来访问__foo变量
    print(test._Test__foo)

if __name__ == "__main__":
    main()
