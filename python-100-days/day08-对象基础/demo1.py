# @Time: 2021/5/12 22:18  
# @Author: flying
# @Desc:

class Student(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看岛国爱情大电影.' % self.name)


def main():
    # 创建学生对象并指定姓名和年龄
    stu1 = Student('骆昊', 38)
    # 给对象发study消息
    stu1.name = "flying"
    stu1.study('Python程序设计')
    # 给对象发watch_av消息
    stu1.watch_movie()

    stu2 = Student('王大锤', 15)
    stu2.study('思想品德')
    stu2.watch_movie()


if __name__ == '__main__':
    main()

'''
骆昊正在学习Python程序设计
骆昊正在观看岛国爱情大电影.
王大锤正在学习思想品德
王大锤只能观看《熊出没》.
'''
