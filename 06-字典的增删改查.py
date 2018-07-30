# 定义空的字典
my_dict = {}

print(my_dict, type(my_dict))

# 添加键值对, key不在字典里面那么是添加
my_dict["name"] = "张三"
my_dict["age"] = 18
my_dict["sex"] = '男'
my_dict["address"] = '北京'
print(my_dict)

# 修改键值对, 可以存在就是修改键值对
my_dict["address"] = '上海'
print(my_dict)

# 删除键值对
del my_dict["age"]
print(my_dict)
# 字典是无序， 列表是有序
# 无序: 定义的数据顺序和输出数据数据不一致
# 有序：定义的数据顺序和输出数据一致
my_dict = {'name': '张三', 'sex': '男', 'address': '上海', 1:4}
# 随机删除键值对,返回key和value
# value = my_dict.popitem()

# 指定可以删除键值对，返回key对应value
value = my_dict.pop("sex")

print(value, my_dict)

# 判断key是否存在， 提示默认判断的key
result = "age" in my_dict
print(result)

result = "age" in my_dict.keys()
print(result)

# 获取字典中所有的value值
result = "张三" in my_dict.values()
print(result)