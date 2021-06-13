# @Time: 2021/6/6 14:39  
# @Author: flying
# @Desc:

# Time类
#     time类表示时间，由时、分、秒以及微秒组成。（我不是从火星来的~~）time类的构造函数如下：
#     class datetime.time(hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ) ：各参数的意义不作解释，这里留意一下参数tzinfo，它表示时区信息。注意一下各参数的取值范围：hour的范围为[0, 24)，minute的范围为[0, 60)，second的范围为[0, 60)，microsecond的范围为[0, 1000000)。
#
# time类定义的类属性：
# time.min、time.max：time类所能表示的最小、最大时间。其中，time.min = time(0, 0, 0, 0)， time.max = time(23, 59, 59, 999999)；
# time.resolution：时间的最小单位，这里是1微秒；
# time类提供的实例方法和属性：
# time.hour、time.minute、time.second、time.microsecond：时、分、秒、微秒；
# time.tzinfo：时区信息；
# time.replace([ hour[ , minute[ , second[ , microsecond[ , tzinfo] ] ] ] ] )：创建一个新的时间对象，用参数指定的时、分、秒、微秒代替原有对象中的属性（原有对象仍保持不变）；
# time.isoformat()：返回型如"HH:MM:SS"格式的字符串表示；
# time.strftime(fmt)：返回自定义格式化字符串。在下面详细介绍；

from datetime import *

tm = time(23, 30, 30)
print(tm)
print('hour: %d, minute: %d, second: %d, microsecond: %d' % (tm.hour, tm.minute, tm.second, tm.microsecond))

tm1 = tm.replace(hour=20)
print(tm1)
print(tm.isoformat())

