# 列表： 以中括号表现形式的数据集合， 比如: [1, 4]
# 提示：列表里面可以放入任意类型数据

my_list = [1, 1.22, "abc", True]
print(my_list, type(my_list))

# 获取列表中的可以根据下标获取
value = my_list[0]

print(value)

# python中的下标： 下标其实就是一个编号，可以根据编号找到某个数据，在python里面下标可以有正数下标和负数下标
# 正数下标:默认是从0开始，0：表示第一个元素， 负数下标: 提示 -1表示倒数第一个元素

result = my_list[-1]
print(result)

result = my_list[-4]
print(result)

result = my_list[3]
print(result)

# 列表的增删改查
my_list = []  # 空的列表

# 向列表中追加一个指定数据
my_list.append(1)
print(my_list)
my_list.append("大家好")
print(my_list)

# 插入指定数据
my_list.insert(1, 'abc')

print(my_list)

my_list1 = ["西瓜", '草莓', "芒果"]

# my_list.append(my_list1)
# print(my_list)

# extend
my_list.extend(my_list1)
print(my_list)

my_list = [1, 'abc', '大家好', '西瓜', '草莓', '芒果']
# 修改数据
my_list[0] = '葡萄'
print(my_list)

# my_list[5] = '桃子'
my_list[-1] = '桃子'
print(my_list)

# 删除数据

# remove删除指定数据
my_list.remove("abc")
print(my_list)

# 根据下标删除指定数据
del my_list[0]
print(my_list)

# 注意点： 下标要合法
# del my_list[5]
# print(my_list)

# 根据下标删除数据并返回删除的数据
my_list = ['大家好', '西瓜', '草莓', '桃子']
# pop不指定下标默认删除倒数第一个数据
result = my_list.pop()
print(result, my_list)

result = my_list.pop(0)

print(result, my_list)

# 判断指定数据是否在列表里面
my_list = ['大家好', '西瓜', '草莓', '桃子']

result = '西瓜' in my_list
print(result)

result = '西瓜' not in my_list
print(result)

# 根据数据在列表中查找指定的下标
index = my_list.index("草莓")

print(index)

# 根据指定数据获取数据在列表中的个数
count = my_list.count("芒果")

print(count)





