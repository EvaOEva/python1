# _*_ coding: utf-8 _*_

# 新式类的定义方式，建议大家使用新式类的方式
class Teacher(object):
    # 类属性
    country = "中国"

    # 方法
    def show(self):
        print("哈哈，我是大家的授课老师")


print(Teacher.__bases__)
t1 = Teacher()
t1.show()

t2 = Teacher()
t2.show()