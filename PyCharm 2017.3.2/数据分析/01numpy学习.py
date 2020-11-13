import numpy as np


# newlis = [1, 2, 3]
# print(newlis)
# arr1 = np.array(newlis)
# print(arr1)

# rand不指定参数返回的是一个浮点数，指定参数，就是数组大小
# arr1 = np.random.rand(2, 3)

# arr1 = np.random.randint(20, size=4)

# 不指定参数，默认数据区间0-1，返回的是浮点数
# arr1 = np.random.uniform(2, 6, size=(3, 4))
# arr1 = np.zeros((3, 3),dtype=int)
# arr1 = np.ones((2, 2), dtype=int)

# 维度转换
# arr2 = np.arange(1, 17)
# arr1 = arr2.reshape((4, 4))
# print(arr1)
# print('维度个数', arr1.ndim)
# print('维度大小', arr1.shape)
# print('数据类型', arr1.dtype)

arr1 = np.arange(1, 11).reshape(5, 2)
arr2 = np.arange(1, 11).reshape(2, 5)
arr4 = np.arange(1, 11).reshape(2, 5)
arr3 = np.arange(5)
arr5 = np.arange(5)
print(arr3 + arr2)
print(arr4 + arr2)
print(arr5 + arr3)
print(arr3+3)
print(arr1*3)
arr6 = np.arange(0, 10, 2)
arr7 = arr6.astype(np.float64)
print(arr7.dtype)