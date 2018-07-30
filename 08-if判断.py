age = int(input("请输入您的年龄："))

# 在if语句外面的不受影响
# print("if语句开始判断了")
# if age >= 18:
#     # 条件成立if语句里面的代码才会执行
#     print("成年")
#
# print("if语句结束判断了")

# if - else 语句
# if age >= 18:
#
#     print("成年")
# else:
#     # 条件不成立会执行else语句
#     print("未成年")

# if - elif - else 语句，可以判断多个条件
if age >= 15 and age <= 17:
    print("少年")
elif age > 17 and age <= 40:
    print("中年")
elif age > 40 and age < 80:
    print("老年")
else:
    print("未知")

