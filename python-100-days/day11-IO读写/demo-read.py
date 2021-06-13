# @Time: 2021/5/29 15:03  
# @Author: flying
# @Desc:
import time


def main():

    # 方法1
    # try:
    #     f = open("D:\data\dp.txt",'r')
    #     r = f.read()
    #     print(r)
    # finally:
    #     if f:
    #         f.close()

    # 方法2
    # with open("D:\data\dp.txt",'r',encoding='utf-8') as f:
    #     print(f.read())
    #
    # # 方法3 通过for-in循环逐行读取
    # with open("D:\data\dp.txt", 'r', encoding='utf-8') as f:
    #     for line in f:
    #         print(line, end='')
    #         time.sleep(1)

    # 方法3
    with open("D:\data\dp.txt", 'r',encoding='utf-8') as f:
        for line in f.readlines():
            print(line.strip())


    # # 方法4 读二进制文件
    # with open("D:\data\证件照.jpg", 'rb') as f:
    #     print(f.read())


if __name__ == '__main__':
    main()
