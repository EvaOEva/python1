# 生成器是一个特殊的迭代器，也就是说它可以通过next函数和for循环取值
# 迭代器和生成器的好处是： 根据需要每次生成一个值，不像列表把所有的数据都准备好，这样列表比较占用内存，而生成器和迭代器内存占用非常少

# 值只能往后面取不能往前面取值

# 1. 使用生成器的表达式
# result = [x for x in range(4)]
# print(result, type(result))

result = (x for x in range(4))
print(result)
# 测试： 使用next获取下一个值
# value = next(result)
# print(value)

# for value in result:
#     print(value)

# 2. 使用yield创建生成器
def show_num():
    for i in range(5):
        print("1111")
        # 代码遇到yield会暂停，然后把结果返回出去，下次启动生成器在暂停的位置继续往下执行
        # yield特点： 可以返回多次值，return只能返回一次只
        yield i
        print("2222")


g = show_num()
value = next(g)
print(value)
value = next(g)
print(value)

# for value in g:
#     print(value)