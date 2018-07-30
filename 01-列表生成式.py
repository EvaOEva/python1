# 列表生成式(列表推导式)：通俗理解使用for循环快速创建一个列表，最终要获取一个列表

my_list = []

for i in range(1, 6):
    print(i)
    my_list.append(i)

print(my_list)

# 列表推导式，目的快速创建一个列表
# 列表推导式的语法格式
my_list = [value for value in range(1, 6)]

print(my_list)

my_list = [value * 2 for value in range(1, 6)]

print(my_list)


result = [len(value) for value in ['abc', 'ab']]

print(result)

result = [value + "hello" for value in ['abc', 'ab']]

print(result)

my_list = [[x, y] for x in range(1, 3) for y in range(1, 3)]
print(my_list)

my_list = [value for value in range(1, 11) if value % 2 == 0]
print(my_list)