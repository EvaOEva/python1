# 函数定义的格式

# def 函数名(参数[可选]):
#     # 功能代码的实现

# 定义函数， 不会调用
def show():
    print("我叫Hello, 年龄: 18")

# 调用函数

# 函数名(参数)
show()


# 定义带有参数的函数
def show(name, age):
    # 判断数据是否是指定类型
    if isinstance(age, int):
        print("我叫%s, 年龄: %d" % (name, age))

# 调用带有参数的函数
show("test", '18')


