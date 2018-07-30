# 魔法方法： 当前需要完成某个功能操作的时候会自动调用某个方法，比如: __init__，当前对象初始化的时候会调用改方法
# 魔法方法的表现形式: 以__，然后__结束的方法表示魔法方法
class Teacher(object):
    # init方法可以添加参数
    def __init__(self, name, age):
        # self： 表示当前对象
        # 给对象初始化，添加对象属性的
        print("对象初始化了")
        self.name = name
        self.age = age

    # 显示老师信息的方法
    def show_info(self):
        # self:当前对象, 哪个对象调用这个方法，这self就是谁(对象)
        print(self.name, self.age)

teacher = Teacher("李四", 20)
teacher.show_info()

teacher1 = Teacher("王五", 21)
teacher1.show_info()


# 作业： 把现实生活中看的事或者物抽象出来一个类， 类里面的属性和方法也要抽象出来