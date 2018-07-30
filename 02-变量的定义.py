# 变量： 通俗理解就是存储程序数据的容器

# 变量定义的格式

# 变量名 = 数据

score = 100  # 定义了一个变量名字叫做score，存储的数据是100

print(score)

name = "张三"
print(name)

pi = 3.14
print(pi)

is_ok = True
print(is_ok)


# 提示： 在python里面不需要指定数据的类型，会根据数据自动推导出数据类型

# 通过type查看变量的类型
score_type = type(score)
print(score_type)

name_type = type(name)

print(name_type)

pi_type = type(pi)
print(pi_type)

print(type(is_ok))

# 总结： 常用的数据类型 int， str, float, bool, list, tuple, dict,set