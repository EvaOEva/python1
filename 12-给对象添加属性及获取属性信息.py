class Teacher(object):
    def show(self):
        print("今天的天气很凉爽")


# 创建对象
teacher = Teacher()
# 动态添加对象属性
teacher.name = "李四"
teacher.age = 18


# 获取数据对应的属性
print(teacher.name, teacher.age)

# 修改属性
teacher.name = "王五"
print(teacher.name, teacher.age)

teacher.show()