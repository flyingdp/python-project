# @Time: 2021/6/6 16:15  
# @Author: flying
# @Desc:

from collections import *

cnt = Counter()

wordList = ['a', 'b', 'c', 'c', 'a', 'a']
for word in wordList:
    cnt[word] += 1
print(cnt)

c = Counter()
c = Counter('gallahad')  # 从可迭代的字符串初始化counter

