# 定义一个装饰器函数
def decorator(func):
    def inner(num1, num2):
        print("计算结果如下:")
        return func(num1, num2)
    return inner


@decorator # => sum_num = decorator(sum_num)
def sum_num(num1, num2):
    result = num1 + num2
    return result

@decorator #=> sum_msg = decorator(sum_msg)
def sum_msg(num1, num2):
    print(num1, num2)



# result = sum_num(1, 2)
#
# print(result)
# 提示： sum_msg执行这个函数相当于装饰器里面inner函数
result = sum_msg(1, 4)
print(result)