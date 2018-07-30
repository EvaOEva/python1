import random

# num = random.randint(1, 3)
# print(num)

from first_module import show  # 这种导入需要保证当前模块不要定义导入的功能代码
# 推荐导入模块的方式
import first_module
import sys
# import first_module, second_module # 不推荐这样导入


def show():
    print("哈哈哈")

show()
first_module.show()


# 模块导入的注意点：
# 1. 自定义的模块名不要和系统的模块名重名，
# 2. 导入的功能代码不要在当前模块定义否则使用不了导入模块的功能代码

# 查看模块搜索的顺序
print(sys.path)

