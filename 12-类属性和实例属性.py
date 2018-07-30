# 类属性是在方法外和在类内部定义的属性叫做类属性
# 实例属性是在init方法里面定义的属性叫做实例属性
class Person(object):
    # 类属性，对象没有创建就想使用这个属性可以定义成类属性
    type = "黄种人"

    def __init__(self):
        # 实例(对象)属性
        self.name = "张三"
        self.age = 29

# --------------类属性的操作------------------------

# 查看类属性和方法
print(Person.__dict__)
# 使用类访问类属性
print(Person.type)
# 使用类不能访问对象属性
# print(Person.age)

# 修改类属性
Person.type = "白种人"
print(Person.type)
# 查看类属性和方法
print(Person.__dict__)

# ---------------对象属性的操作---------------------------
# 创建对象(实例)
xiao_ming = Person()
# 使用实例(对象)访问对象（实例）属性
print(xiao_ming.name)
# 对象可以访问类属性
print(xiao_ming.type)
# 对象不能修改类属性，其实是添加了一个对象属性
print("-------1-------")
# print(Person.__dict__)
# print(xiao_ming.__dict__)
# xiao_ming.type = "黑种人"
# print(xiao_ming.type)
#
# print(Person.__dict__)
# print(xiao_ming.__dict__)

print(xiao_ming.__dict__)
# 使用实例修改对象属性
xiao_ming.name = "李四"
print(xiao_ming.name)
print(xiao_ming.__dict__)

Person.type = "黄种人"
print(xiao_ming.type)

# 总结： 类属性的操作由类完成，对象的属性的操作使用对象完成，注意点： 对象可以访问类属性