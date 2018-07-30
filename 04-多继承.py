# 多继承：相当于继承多个父类

class A(object):
    # def show(self):
    #     print("我是A类")
    pass


class B(object):
    def show_info(self):
        print("我是B类")

    # def show(self):
    #     print("我是B类")


class C(A, B):
    pass


c = C()
c.show()
c.show_info()
# 在python里面方法的调用会遵循mro，类继承顺序, 决定了方法调用时候的查找顺序
print(C.mro())