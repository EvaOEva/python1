import functools
# 偏函数： 通俗理解指明函数的参数偏爱某个值这样的函数就叫做偏函数

def show(num1, num2, num3=1):
    result = num1 + num2 + num3
    return result


result = show(1, 2)

print(result)

# 定义一个偏函数
def show2(num1, num2, num3=2):
    result = show(num1, num2, num3)
    return result

result = show2(1, 2)

print(result)


# 指明函数的参数设置为某个值
new_func = functools.partial(show2, num2=2)  # 返回的函数就是偏函数
result = new_func(1)

print(result)

# 指明内置函数的参数偏爱某个值，生成一个偏函数
result = int("123")

# 这里就用到了偏函数
new_func = functools.partial(int, base=2)
result = new_func('11')
print(result)

