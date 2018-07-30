# 装饰器：本质上就是一个函数，可以给原函数的功能上进行扩展，这样的好处是，不改变原函数的定义及调用的操作


# 装饰器-》 通过闭包完成装饰器
def decorator(new_func):
    print("装饰器的代码执行了")
    def inner():
        print("-" * 10)
        new_func()

    # 返回的函数是闭包
    return inner


# 提示: 在使用@decorator的时候装饰器的代码就会执行
@decorator  # show = decorator(show)
# 使用装饰器装饰下面的函数
def show():
    print("AAAA")


show()


# show = decorator(show)
#
# show()