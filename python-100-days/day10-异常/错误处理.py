"""
 @Time: 2021/5/17 14:38
 @Author: flying
 @Desc:
"""


# 当我们认为某些代码可能会出错时，就可以用try来运行这段代码，
# 如果执行出错，则后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完except后，
# 如果有finally语句块，则执行finally语句块，至此，执行完毕。
import logging


def main():
    try:
        print('try........')
        # r = 10 / int('a')
        r = 10 / 0
        print('result=', r)
    except ValueError as e:
        logging.exception(e)
        # print('ValueError', e)
    except ZeroDivisionError as e:
        logging.exception(e)
        print("ZeroDivisionError:", e)
    # 此外，如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句：
    else:
        print('no error')
    finally:
        print('finally')


if __name__ == '__main__':
    main()
