# -----import导入包里面的模块----
# import first_package.first  # *** 推荐导入方式1
# import first_package.second
#
# # 使用包模块里面的代码
# first_package.first.show()
# first_package.second.show_msg()

# # -----import导入包里面的模块设置别名----
# import first_package.first as one
# import first_package.second as two
#
# one.show()
#
# two.show_msg()


# ----from导入包名 import 模块名

# from first_package import first as one
# from first_package import second  # *** 推荐导入方式2
#
# one.show()
# second.show_msg()


# --- from 包名.模块名 import 功能代码
# from first_package.first import show  # 需要保证当前模块没有导入模块的功能代码
# from first_package.second import show_msg as show_info
#
# def show():
#     print("我是当前模块的函数")
#
# show()
# show_info()


# --- from 包名 import *, 默认不会导入包里面的所有模块，需要在init文件里面使用__all__ 去指定导入的模块
# from first_package import *
#
# first.show()

import first_package  # 直接导入包，不会导入对应的模块，需要在init文件中自己导入

first_package.first.show()
first_package.second.show_msg()


