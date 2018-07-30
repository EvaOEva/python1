
def get_decorator(char):
    # 定义装饰器函数
    def decorator1(func):
        def inner():
            print(char * 10)
            func()
        return inner
    return decorator1


# 把@后面的操作相当于执行了一个函数，返回了一个装饰器
@get_decorator("c")  # 有参数的装饰器
def show():
    print("1111")

show()