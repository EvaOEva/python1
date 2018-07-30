# 在属性名和方法名前面加上'__'那么定义的属性和方法就是私有属性和私有方法
class Person(object):
    def __init__(self, name, age):
        # 公共属性
        self.name = name
        # 私有属性，只能在本类内部使用，在类外面不能使用
        # 注意点：私有属性指定在init方法里面添加
        self.__age = age

    def show(self):
        # 在类内部使用私有属性和私有方法是可以的
        print(self.name, self.__age)
        self.__money()

    def __money(self):
        print("100万")


person = Person("李四", 20)
print(person.name)
# 私有属性在外界访问不了
# print(person.__age)

# person.show()

# person.__money()

# 查看对象中的属性信息
# print(person.__dict__)
# # 本意是修改私有属性
# # 这里不是修改了私有属性，而是给对象添加了一个__age的对象属性
# # 提示：这里也不是添加的私有属性，只能在init方法里面添加
# person.__age = 22
# print(person.__age)
# print(person.__dict__)
# # 查看私有方法的
# print(Person.__dict__)

# 在python里面私有属性和私有方法没有做到绝对私有，只是把私有属性和私有方法进行了一个名字的伪装
# 非常规操作， 不建议大家以后这样使用
print(person.__dict__)
person._Person__age = 34
print(person._Person__age)
print(person.__dict__)


person._Person__money()
person.show()
