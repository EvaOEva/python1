# 集合(set): 以大括号表现形式的数据集合，集合里面不能有重复数据，集合也是无序

# 集合根据下标获取数据和修改数据，可以添加和删除

my_set = {1, 4, 'abc', 'hello'}

my_set.remove("abc")
my_set.add("bcd")


print(my_set)

# 添加数据
my_set.add(5)
print(my_set, type(my_set))

# my_set.remove('abc')

my_set.discard("abcd")

# 总结: remove删除数据，数据必须存在，否则会崩溃， discard: 删除指定数据，数据存在会忽略，不会崩溃
print(my_set)

# 测试
# my_set[0] = 3
# value = my_set[0]
# print(value)

for value in my_set:
    print(value)

# 定义空的集合的时候不能直接使用{}

my_set = set()
my_set.add(1)
my_set.add(1)
print(my_set, type(my_set))


# 集合可以对容器类型数据去重
my_list = [1, 1, 3, 5, 3]
# 把列表转成集合，会把数据去重
my_set = set(my_list)

print(my_set)

# 列表，元组， 集合 三者之间可以相互转换
my_tuple = (5, 3)
print(my_tuple, type(my_tuple))

# tuple(xxx)





