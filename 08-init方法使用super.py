class A(object):
    def __init__(self, name):
        print("A")
        self.name = name

class B(A):
    # 提示： 如果子类提供了调用的方法，那么不会主动调用父类的方法
    def __init__(self, subject):
        # 调用父类的init方法
        # self.__init__("zhangsan")
        # 使用类名调用父类的init方法
        # AA.__init__(self, "李四")
        # print("B")
        
        # super调用父类里面的init
        # super(B, self).__init__("王五")
        # 如果子类提供了init方法想要使用父类的init方法需要自己调用
        # 简写 super()-> super(B, self)
        super().__init__("冯琦")

        self.subject = subject

    def show(self):
        print("我是B类")

b = B("python")
print(b.subject)
print(b.name)
b.show()