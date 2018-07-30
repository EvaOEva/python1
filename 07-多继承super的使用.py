class A(object):
    def show_a(self):
        print("我是A类")


class B(object):
    def show_b(self):
        print("我是B类")


class C(A, B):
    def show(self):
        # 查看类继承顺序
        print(self.__class__.mro())
        # 指定类A要在self对象类继承顺序中找下一个类
        super(A, self).show_b()

C().show()