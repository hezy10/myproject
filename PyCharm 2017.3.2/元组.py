
# ########################元组的元素不可以被修改########################
# tuple(元组)
tup = (1,2,3,4,5,6,'admin',1,1,1)

print(tup.count(1))
print(tup.index(1))

###################当元组的元素只有一个时后面要加上','类型才会是元组######################
tup1 = (2,)
print(type(tup1))
