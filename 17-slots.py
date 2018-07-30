# 指明创建对象的时候不能再添加其他属性，只能是指定的属性
class Student(object):
    # 这样操作可以让对象的属性固定
    __slots__ = ("name", "age")

    def __init__(self, name, age):

        self.name = name
        self.age = age

stu = Student("xx", 20)
# stu.sex = "男"
print(stu.name, stu.age)
stu.name = "王五"


print(stu.name, stu.age)