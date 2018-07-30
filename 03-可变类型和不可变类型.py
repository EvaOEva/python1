# 可变类型：可以在原有数据的基础上对数据进行修改(添加或者删除或者修改数据)，修改后内存地址不变
# 不可变类型: 不能在原有数据的基础上对数据进行修改，当然直接赋值一个新值，那么内存地址会发生改变

# 可变类型: 列表，集合，字典，对数据进行修改后内存地址不变
# 不可变类型: 字符串，数字，元组，不能再原有数据的基础上对数据进行修改

my_list = [1, 5, 6]
# 查看内存地址
print(my_list, id(my_list))
my_list[0] = 2
my_list.append(7)
del my_list[1]
print(my_list, id(my_list))

my_dict = {"name": "李四", "age": 10}

print(my_dict, id(my_dict))

my_dict["name"] = "王五"

my_dict["sex"] = "男"

del my_dict["age"]
print(my_dict, id(my_dict))

my_set = {5, 10}
print(my_set, id(my_set))
my_set.add("666")
my_set.remove(5)

print(my_set, id(my_set))
# 可变类型： 允许在原有数据的基础上修改的数据，修改后内存地址不变

# ------------不可变类型的操作------------------

my_str = "hello"
print(id(my_str))
# my_str[0] = 'a'

my_str = "world"

print(id(my_str))

my_num = 5
print(id(my_num))
# my_num[0] = 1

my_num = 6

print(id(my_num))

my_tuple = (1, 5)
print(id(my_tuple))

# my_tuple[0] = 2
my_tuple = (4, 6)

print(id(my_tuple))

# 不可变类型：修改数据内存地址会发生变化， 其实修改的是变量存储的内存地址
