
''' 数值型：
int float complex(复数) bool
'''

import math
# 向上取整ceil
print(math.ceil(2.0005))
print(math.ceil(-1.5))

# 向下取整floor或//
print(math.floor(3.1))
print(math.floor(-1.5))

# 四舍六入，五取偶round
print(round(2.50))
print(round(3.50))
print(round(-4.5))
print(round(-3.5))

# int取整数部分
print(int(1.5))
print(int(-1.5))

# 最大值
print(max(2,3))

# 最小值
print(min(1,2))

# 进制函数 bin--2 oct--8 hex--16
print(bin(3))  # 返回的是字符串
print(oct(15))
print(hex(22))

# 查看数据类型type
print(type(0.1))    # 返回的是类型

# 类型判断isinstance
print(isinstance(0.6,float))

print(type(1+True))  # True等价于1，false等价于0
print(1+True)
print(1+True+3.2)   # 存在隐式转换
