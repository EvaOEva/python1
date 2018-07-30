import json  # 只能支持部分数据类型，不通用，比如: 列表，字典，int类型，自定义类型不可以需要额外指定

# my_list = [{"name": "张三", "age": 20}, {"name": "李四", "age": 22}]
#
# file = open("my_list.txt", "w", encoding="utf-8")
# # 序列化
# json.dump(my_list, file)
#
# file.close()

# file = open("my_list.txt", "r", encoding="utf-8")
#
# # 反序列化
# my_list = json.load(file)
#
# print(my_list)
# file.close()

class Student(object):
    def __init__(self):
        self.name = "李四"
        self.age = 10

file = open("stu.txt", "w", encoding="utf-8")
stu = Student()
# 序列化对象，本质上把对象的属性进行保存
# print(stu.__dict__)
json.dump(stu.__dict__, file)

file.close()

