# 拆包: 通俗理解把容器类型（字符串，列表，元组，字典，集合）中每一个数据使用不同变量进行保存

my_str = 'abc'
# 注意点: 变量个数要和容器的个数一致
a, b, c = my_str
print(a, b, c)

my_list = [1, 5]
num1, num2 = my_list
print(num1, num2)

my_list = (1, 5)
num1, num2 = my_list
print(num1, num2)

my_dict = {"name": "李四", "age": 18}.values()
key1, key2 = my_dict
print(key1, key2)

my_set = {3, 5}
num1, num2 = my_set
print(num1, num2)
