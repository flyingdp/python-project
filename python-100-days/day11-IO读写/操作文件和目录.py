# @Time: 2021/5/29 21:02  
# @Author: flying
# @Desc:
import os

print(os.name)  # nt->windows系统

print(os.environ)  # 环境变量

print(os.environ.get('ALLUSERSPROFILE'))  # 获取环境变量中某个属性值

# 查看当前目录的绝对路径:
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来(把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数):
path = os.path.join(os.path.abspath('.'), 'flying')
# 然后创建一个目录:
os.mkdir(path)
# 删除一个目录
# os.rmdir(path)

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split(path+"/dp.txt"))