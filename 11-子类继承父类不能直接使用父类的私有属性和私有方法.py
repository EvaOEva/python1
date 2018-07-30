class Person(object):
    def __init__(self):
        self.__age = 10

    def __show(self):
        print("我是一个私有方法")

    def test(self):
        print("测试")

class Student(Person):
    def show(self):
        # 访问父类的里面私有属性和私有方法
        # print(self.__age)
        # self.__show()
        self.test()


student = Student()
student.show()


# student = Student()
# # print(student.__age)
# student.__show()

# 总结： 子类继承父类，不能直接使用父类的私有属性和私有方法