# ------import 导入模块----
# import first_module
#
# stu = first_module.Student("张三", 20)
# print(stu.name, stu.age)
#
# print(first_module.g_num)

# ------from 模块名 import 功能代码----
# from first_module import Student
# from first_module import show
#
# stu = Student("李四", 20)
# print(stu.name, stu.age)
#
# show()

# -------from 模块名 import * 导入模块中所有的功能代码
# from first_module import *
# print(g_num)
# show()
# stu = Student("张三", 20)
#
# print(stu.name, stu.age)

# -------from 模块名 import * 使用__all__ 限定导入的功能代码
# from first_module import *
# print(g_num)
# show()

# Student("李四", 20)


# ------------import 模块名设置别名----
# import first_module as first  # as 设置模块的别名
# print(first.g_num)
#
# first.show()

# ----------from 模块名 import 功能代码 设置别名
from first_module import show as show_msg
from first_module import Student as Stu
s1 = Stu("李四", 20)
s1.show_msg()
show_msg()


