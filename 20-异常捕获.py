# try:
#     num1 = input("请输入一个数字:")
#     num2 = input("请输入二个数字:")
#
#     result = int(num1) + int(num2)
#     print(result)
# except ValueError as e:
#     print(e, type(e))


# 提示： 多数异常类都是基础Exception
# try:
#     # 提示： 可能出现异常的代码放到try语句里面
#     num1 = input("请输入一个数字:")
#     num2 = input("请输入二个数字:")
#
#     result = int(num1) + int(num2)
#     print(result)
#
# except Exception as e: # e：表示异常对象
#     # 捕获到的异常会在except里面进行处理
#     print("请输入合法的数字")
#     print(e)


# 了解： 可以捕获多个异常类型

# try:
#     name = "zs"
#     del name
#
#     # 在try里面如果只选代码遇到了异常那么不会再执行try语句里面的代码， 会执行except
#     print(name)
#
#     result = 1 / 0
#     print(result)
# except (NameError, ZeroDivisionError) as e:
#     print(e, type(e))
#


# try:
#     # name = "zs"
#     # del name
#     #
#     # # 在try里面如果只选代码遇到了异常那么不会再执行try语句里面的代码， 会执行except
#     # print(name)
#
#     result = 1 / 0
#     print(result)
# except Exception as e:
#     print(e, type(e))


# try:
#     name = "zs"
#     del name
#
#     # 在try里面如果只选代码遇到了异常那么不会再执行try语句里面的代码， 会执行except
#     print(name)
#
#     result = 1 / 0
#     print(result)
# except NameError as e:
#     print(e, type(e))
#
# except ZeroDivisionError as e:
#     print(e, type(e))

try:
    # name = "zs"
    # del name
    #
    # # 在try里面如果只选代码遇到了异常那么不会再执行try语句里面的代码， 会执行except
    # print(name)

    result = 1 / 0
    print(result)
except Exception as e:
    print(e, type(e))
else:
    print("没有异常会执行else")
finally:
    print("有没有异常都会执行这个语句")