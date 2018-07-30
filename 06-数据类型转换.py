num1 = 10

my_str = "10"

# 把字符串转成 int 类型
num2 = int(my_str)

print(num2)
print(type(num2))

# 目前类型统一可以进行计算
result = num1 + num2

print(result)

my_float_str = "3.14"
num3 = float(my_float_str)
print(num3)
print(type(num3))

# int类和float类型计算会把int类型转成float类型
result = num1 + num3
print(result)


num4 = 4.55
# 注意点只取整数部分
num5 = int(num4)
print(num5)

result = str(num4)
print(result)
print(type(result))


# eval：获取字符串中原始数据
# my_str = "5.15"

my_str = '[1, 3, 5]'


value = eval(my_str)
print(value)
print(type(value))