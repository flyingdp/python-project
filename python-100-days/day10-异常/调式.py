"""
 @Time: 2021/5/17 17:20
 @Author: flying
 @Desc:
"""
import logging

logging.basicConfig(level=logging.INFO)


def loggingTest():
    s = '0'
    n = int(s)
    logging.info("n==%d" % n)
    print(10 / n)


def main():
    loggingTest()


if __name__ == '__main__':
    main()
