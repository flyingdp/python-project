from random import randint

# 随机生成整数：[a-b]区间的整数（包含两端）
print(randint(1, 6))


# 若不传参数 默认使用2
def roll_dice(n=2):
    total = 0
    for _ in range(n):
        random = randint(1, 6)
        total += random
    return total


print(roll_dice())
print(roll_dice(3))
