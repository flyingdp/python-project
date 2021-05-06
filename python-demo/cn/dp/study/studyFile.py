# 文件操作
f = open("D:\data\dp.txt", "r", encoding="utf-8")
content = f.read()
print(content)
content1 = f.readline()
print(content1)