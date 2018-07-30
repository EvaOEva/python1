# 文件访问模式:
# 1. r：只读， 文件不存在会崩溃
# 2. w: 只写
# 3. a: 追加写入
# 4. rb: 以二进制方式读取文件数据
# 5. wb: 以二进制方式写入文件数据
# 6. ab: 以二进制方式追加写入文件数据
# 7. r+, w+, a+, 支持读写， 但是要看前面的主模式
# 8. rb+, wb+, ab+ 支持二进制方式读写操作

# -------------r模式-----------------

# # 打开文件使用open函数
# file = open("1.txt", "r", encoding="utf-8")  # 默认是r模式，r表示只读
# # 读取文件中的数据
# content = file.read() # 读取文件中的所有数据
# print(content)
# # 关闭文件
# file.close()

# -------------w模式-----------------
# 提示： w模式：如果文件不存在，那么会创建一个文件并打开，然后写入数据
# 提示： w模式: 如果文件存在，那么会把文件中原有数据先清空，然后在写入
# 打开文件
# 注意点： 如果使用w模式每次打开文件会先清空文件，然后在写入
# 提示： 如果在windows开发python，那么需要指定编码格式
# 在mac和linux上编码格式默认是utf-8
# file = open("1.txt", "w", encoding="utf-8")
# # 查看编码格式
# print(file.encoding)
# # 写入数据
# file.write("A")
# # 打开文件后多次写入数据不会覆盖前面的数据
# file.write("B")
# file.write("哈哈")
# # 关闭文件
# file.close()

# -------------------a模式追加写入数据-----------------
# file = open("1.txt", "a", encoding="utf-8")
# file.write("abc")
# file.close()

# 在python2里面不支持文件中有中文，需要指定编码格式
# _*_ coding:utf-8 _*_
# 在python3里面默认是支持中文的，使用utf-8编码的

# --------------------rb模式以二进制方式读取数据-----------------------------
# 提示：binary mode doesn't take an encoding argument，表示如果是二进制模式不需要指定编码格式
# file = open("1.txt", "rb")
# file_data = file.read()
# # 对二进制数据进行utf-8解码操作, 二进制到字符串叫解码
# content = file_data.decode("utf-8")
# print(content)
# # 不支持写入操作
# # file.write("呵呵呵".encode("utf-8"))
# file.close()

# --------------------wb模式以二进制方式写入数据---------
# file = open("1.txt", "wb")
#
# content = "hello 哈哈"
# # 字符串到二进制叫做编码
# # 对字符串进行utf-8编码得到二进制数据
# file_data = content.encode("utf-8")
# file.write(file_data)
#
# # 不能读取数据
# # file.read()
#
# file.close()

# --------------------ab模式追加写入数据-------------------------
# file = open("1.txt", "ab")
#
# content = "hello 哈哈"
# # 字符串到二进制叫做编码
# # 对字符串进行utf-8编码得到二进制数据
# file_data = content.encode("utf-8")
# file.write(file_data)
# 不能读取数据
# file.read()
#
# file.close()


# -----------------r+ 读写--------------------------
# 为了兼容不同操作系统，只要没有看到b模式可以使用encoding指定编码格式
file = open("1.txt", "r+", encoding="utf-8")

# 提示：写入数据时候不会先清空数据，把指定数据中的数据替换成写入的数据，文件中其他的数据还保留
file.write("abc")

result = file.read()
print(result)

file.close()
