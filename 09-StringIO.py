# 把字符串数据写入到内存
import io

# StringIO的操作和文件写入和读取的操作很类似
str_io = io.StringIO()

# 向内存写入字符串数据
str_io.write("hello")
str_io.write("world")
# str_io.write("哈哈".encode("utf-8"))

# 获取数据
# content = str_io.getvalue()
# print(content)

# 设置文件指针的位置到文件开头
str_io.seek(0)
# 默认全部读取出来
# read(2): 读取指定长度
result = str_io.read()
print(result)