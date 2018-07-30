# 元组：以小括号表现形式的数据集合， 比如: (1, 4, 'abc')
# 元组也可以存放任意数据
# 元组指定根据下标获取数据，不能对元组进行数据的修改
my_tuple = (1, 4, 'abc', True, 1.2)
print(my_tuple)

value = my_tuple[-1]

print(value)


value = my_tuple[0]

print(value)

# 元组不能根据下标删除数据
# del my_tuple[2]
# 不支持数据的修改
# my_tuple[0] = 2
# print(my_tuple)


my_tuple = (1,[3, 5])
# 直接根据下标修改元组中的数据，不支持
# my_tuple[1] = [2, 4]

# 获取列表
my_list = my_tuple[1]
# 根据列表修改数据
my_list[0] = 2
del my_list[1]

print(my_tuple)

# 注意点: 如果元组中只有一个元素，那么需要加上一个逗号
my_tuple = (5,)

print(my_tuple, type(my_tuple))


# 判断数据是否存在
my_tuple = (5, 10, 10, 10)

result = 5 in my_tuple

print(result)

result = 5 not in my_tuple

print(result)

index = my_tuple.index(5)

print(index)

result = my_tuple.count(10)

print(result)










