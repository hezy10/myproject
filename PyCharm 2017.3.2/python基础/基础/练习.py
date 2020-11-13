# 三个数排序输出
num = []
for i in range(3):
    num.append(input('>>>>'))

order = None
if num[0] > num[1]:
    if num[1] > num[2]:
        order = [2,1,0]
    else:
        if num[0] > num[2]:
            order = [1,2,0]
        else:
            order = [1,0,2]
else:
    if num[1] < num[2]:
        order = [0,1,2]
    else:
        if 1:
            pass