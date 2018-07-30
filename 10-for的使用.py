# 获取容器类型（字符串，列表，元组， 字典， set）中的每一个数据使用for循环是最简单

# my_str = 'abc'
# for value in my_str:
#     print(value)
#
my_list = ['苹果', '鸭梨']
for value in my_list:
    print(value)

# 循环遍历时候下标和数据都需要可以使用enumerate

# my_list = enumerate(['苹果', '鸭梨'])
# for value in my_list:
#     print(value[0], value[1], type(value))

print("-------------")

# index， value获取的是元组中的每一个值，就是拆包
for index, value in enumerate(['苹果', '鸭梨']):
    print(index, value)

print("-------------")
for value in enumerate((1, 5)):
    print(value)

# 遍历数据的时候需要下标可以通过enumerate

# 默认是遍历是key
my_dict = {"name": "张三", "age": 18}
# for key in my_dict:
#     print(key, my_dict[key])
#
# for value in {"name": "张三", "age": 18}.values():
#     print(value)
# 其实遍历的是每一项字典中的键值对
for key, value in my_dict.items():
    print(key, value)

my_set = {1, 5, 7}
for value in my_set:
    print(value)