def decorator1(func):
    def inner():# 其实就是你封装传入函数的代码
        print("-" * 30)
        func()
    return inner


def decorator2(func):
    def inner():# 其实就是你封装传入函数的代码
        print("*" * 30)
        func()
    return inner


@decorator1 # show => decorator1(decorator2.inner) => decorator1.inner
@decorator2 #  => show = decorator2(show)  ->  decorator2.inner
def show():
    print("AAAA")

show()

