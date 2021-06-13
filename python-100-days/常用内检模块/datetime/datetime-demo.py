# @Time: 2021/6/6 14:56  
# @Author: flying
# @Desc: https://www.cnblogs.com/lhj588/archive/2012/04/23/2466653.html

# datetime类
#     datetime是date与time的结合体，包括date与time的所有信息。它的构造函数如下：datetime.datetime (year, month, day[ , hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )，各参数的含义与date、time的构造函数中的一样，要注意参数值的范围。
#     datetime类定义的类属性与方法：
#         datetime.min、datetime.max：datetime所能表示的最小值与最大值；
#         datetime.resolution：datetime最小单位；
#         datetime.today()：返回一个表示当前本地时间的datetime对象；
#         datetime.now([tz])：返回一个表示当前本地时间的datetime对象，如果提供了参数tz，则获取tz参数所指时区的本地时间；
#         datetime.utcnow()：返回一个当前utc时间的datetime对象；
#         datetime.fromtimestamp(timestamp[, tz])：根据时间戮创建一个datetime对象，参数tz指定时区信息；
#         datetime.utcfromtimestamp(timestamp)：根据时间戮创建一个datetime对象；
#         datetime.combine(date, time)：根据date和time，创建一个datetime对象；
#         datetime.strptime(date_string, format)：将格式字符串转换为datetime对象；
from datetime import *
import time

# print(datetime.max)
# print(datetime.min)
# print(datetime.resolution)
# print(datetime.today())
# print(datetime.now())
# print(datetime.utcnow())
# print(datetime.fromtimestamp(time.time()))
# print(datetime.utcfromtimestamp(time.time()))


# 格式字符串
#     datetime、date、time都提供了strftime()方法，该方法接收一个格式字符串，输出日期时间的字符串表示。下表是从python手册中拉过来的，我对些进行了简单的翻译（翻译的有点噢口~~）。
#
# 格式字符  意义
#
# %a 星期的简写。如 星期三为Web
# %A 星期的全写。如 星期三为Wednesday
# %b 月份的简写。如4月份为Apr
# %B月份的全写。如4月份为April
# %c:  日期时间的字符串表示。（如： 04/07/10 10:43:39）
# %d:  日在这个月中的天数（是这个月的第几天）
# %f:  微秒（范围[0,999999]）
# %H:  小时（24小时制，[0, 23]）
# %I:  小时（12小时制，[0, 11]）
# %j:  日在年中的天数 [001,366]（是当年的第几天）
# %m:  月份（[01,12]）
# %M:  分钟（[00,59]）
# %p:  AM或者PM
# %S:  秒（范围为[00,61]，为什么不是[00, 59]，参考python手册~_~）
# %U:  周在当年的周数当年的第几周），星期天作为周的第一天
# %w:  今天在这周的天数，范围为[0, 6]，6表示星期天
# %W:  周在当年的周数（是当年的第几周），星期一作为周的第一天
# %x:  日期字符串（如：04/07/10）
# %X:  时间字符串（如：10:43:39）
# %y:  2个数字表示的年份
# %Y:  4个数字表示的年份
# %z:  与utc时间的间隔 （如果是本地时间，返回空字符串）
# %Z:  时区名称（如果是本地时间，返回空字符串）
# %%:  %% => %

dt = datetime.now()
print(dt.strftime('%Y-%m-%d %H:%M:%S %f'))
print(dt.strftime('%y-%m-%d %I:%M:%S %p'))
print(dt.strftime("%a"))
print(dt.strftime("%A"))

print(dt.strftime("%b"))
print(dt.strftime("%B"))

print(dt.strftime('%c'))
print(dt.strftime('%x'))
print(dt.strftime('%X'))

print('今天是这周的第%s天' % dt.strftime('%w'))
print('今天是今年的第%s天' % dt.strftime('%j'))
print('今周是今年的第%s周' % dt.strftime('%U'))


#  获取当前日期和时间
now = datetime.now()
print(now)
print(type(now))

#  获取指定日期和时间
dt = datetime(2021, 6, 6, 14, 10)
print(dt)
#  datetime -> timestamp
print(dt.timestamp())

#  timestamp -> datetime
tt = 1622959800.0
df = datetime.fromtimestamp(tt)  # 本地时间
print(df)

tdf = datetime.utcfromtimestamp(tt)  # UTC时间 (本地时间 - 8)
print(tdf)

#  str ——> datetime
cday = datetime.strptime("2021-06-06 14:10:00", '%Y-%m-%d %H:%M:%S')
print(cday)


# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))

# datetime加减
now = datetime.now()
print(now)
datetime(2015, 5, 18, 16, 57, 3, 540997)
now + timedelta(hours=10)
print(now)


