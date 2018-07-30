# 定义一个装饰器函数
def decorator(func):
    def inner(*args, **kwargs):
        print("计算结果如下:")
        # 这里需要对不定长参数进行拆包
        return func(*args, **kwargs)
    return inner


@decorator # => sum_num = decorator(sum_num)
def sum_num(num1, num2):
    result = num1 + num2
    return result

@decorator #=> sum_msg = decorator(sum_msg)
def sum_msg(num1, num2):
    print(num1, num2)

@decorator #=> show = decorator(show)
def show():
    print("我是一个无参数无返回值得函数")

show()
result = sum_num(1, 2)

print(result)