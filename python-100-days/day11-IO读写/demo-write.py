# @Time: 2021/5/29 18:30  
# @Author: flying
# @Desc:

def main():
    # 方法1
    try:
        f = open("D:\data\dp.txt",'w')
        r = f.write('dongpeng')

        # ff = open("D:\data\dp.txt",'r')
        # print(ff.read())
    finally:
        if f:
            f.close()

    #方法2
    with open('D:\data\dp.txt', 'w') as f:
        f.write('Hello, world!')

    # 细心的童鞋会发现，以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。

if __name__ == '__main__':
    main()