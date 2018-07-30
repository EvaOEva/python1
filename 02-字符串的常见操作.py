# 字符串定义： 只要使用引号('xx', "xx", """jjj""", '''xxx''') 引起来的数据就叫做字符串

my_str = 'hello'

# 根据指定数据查找对应的下标(索引)
result = my_str.index("e")

print(result)

# 根据指定数据查找对应的下标(索引)
result = my_str.find("h")
print(result)

# find 和 index的区别, find如果没有找到数据那么返回的结果是-1， index如果没有找到指定数据那么程序崩溃
result = my_str.find("f")
print(result)

# result = my_str.index("x")
# print(result)

# 统计字符串长度(个数)
result = len(my_str)
print(result)


my_str = 'hello'
# 统计某个字符串出现的次数
result = my_str.count("l")
print(result)

# 替换指定数据
result = my_str.replace("l", 'x')
print(result)

my_str = "苹果,橘子,压力"
# 分割数据
result = my_str.split(',')
print(result)

my_url = "http://www.baidu.com"
# 判断是否以指定数据开头
result = my_url.startswith("http")

print(result)

result = my_url.endswith("xxx")
print(result)

# 需求： 把字符串以指定字符串分割数据成为三部分
my_str = "aaabbccc"
result = my_str.partition("bb")
print(result)

# join：根据指定字符串拼接数据，前提是最终的数据是字符串

# 指定字符串数据
flag_str = "-"

my_str = "abc"
result = flag_str.join(my_str)
print(result)

my_list = ('1', '2', '5')

result = flag_str.join(my_list)

print(result)

# 去除空格
my_str = ' hello '
result = my_str.strip()
print(result)

result = my_str.lstrip()
print(result)
result = my_str.rstrip()
print(result)

# 去除指定数据
my_str = 'ahelloa'
result = my_str.strip('a')
print(result)