# 逻辑运算符: and, or, not

score = 90

# and 表示左右两边条件都成立才会执行if语句
if score >= 90 and score <= 100:
    print("优秀")


num1 = 1

# or 表示左右两边条件有一个条件成立就执行if语句
if num1 == 1 or num1 == 2:
    print("这个数字是我需要的")

# not: 对结果进行取反， not对False 取反就True，对True就是False
if not 1 == 2:
    print("条件成立执行")
