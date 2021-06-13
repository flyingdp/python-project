# @Time: 2021/5/29 18:42  
# @Author: flying
# @Desc:    StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
#
# StringIO顾名思义就是在内存中读写str。
#
# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可

from io import StringIO


def main():
    # 写
    f = StringIO()
    f.write("Hello")
    f.write(" ")
    f.write("world!")
    print(f.getvalue())  # getvalue()方法用于获得写入后的str

    #  读
    rf = StringIO("I am Flying")
    while True:
        s = rf.readline()
        if s == '':
            break
        print(s.strip())



if __name__ == '__main__':
    main()
