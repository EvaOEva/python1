# 迭代器： 在类里面有__iter__和__next__的方法创建的对象就是迭代器，作用：根据数据的位置获取下一个位置的值
from collections import Iterator


class MyIterator(object):
    def __init__(self):
        self.my_list = [4, 5, 19]
        self.current_index = 0

    def __iter__(self):
        # 返回一个迭代器对象
        return self

    def __next__(self):
        if self.current_index < len(self.my_list):
            # 获取迭代器中的下一个值
            result = self.my_list[self.current_index]
            self.current_index += 1
            return result
        else:
            # 抛出停止迭代异常
            raise StopIteration()


# 创建迭代器
my_iterator = MyIterator()
result = isinstance(my_iterator, Iterator)

print(result)
# 使用next函数获取迭代器中的下一个值
# result = next(my_iterator)
# print(result)
#
# result = next(my_iterator)
# print(result)
#
# result = next(my_iterator)
# print(result)
#
# result = next(my_iterator)
# print(result)

# for循环内部会自动处理停止迭代异常
for value in my_iterator:
    print(value)