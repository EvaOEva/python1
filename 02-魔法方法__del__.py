# __del__: 当对象释放的时候会自动调用__del__方法
# 1. 程序退出，程序中所使用的对象全部销毁
# 2. 当前对象的内存地址没有变量使用的时候，那么对象会销毁
import time


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 当对象的引用计数为0的时候回调用__del__
    def __del__(self):
        print("对象释放了:", self)


# 创建对象
xiao_ming = Person("小明", 20)
print(xiao_ming)

xiao_lan = xiao_ming

# 删除变量
del xiao_ming
del xiao_lan

# 引用计数: 内存地址被变量使用的次数，当前引用计数为0表示对象销毁

time.sleep(3)
print("程序退出了")
