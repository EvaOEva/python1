# read, readline, readlines, 读取文件的操作
# file = open("1.txt", "r", encoding="utf-8")
# # 读取指定长度数据, 提示：如果是r模式读取的是指定数据的长度
# content = file.read(1)
# print(content)
# file.close()

# file = open("1.txt", "rb")
# # 读取指定长度数据, 提示：如果是rb模式读取的是字节数
# content = file.read(4)
# # 注意点： 在utf-8编码格式下一个汉字占用三个字节，一个字母和数字占用1个字节
# file_data = content.decode("utf-8")
# print(file_data)
# file.close()

# 根据指定的文件指针读取数据
# file = open("1.txt", "rb")
# # 查看文件指针的位置
# result = file.tell()
# print(result)
# # 设置文件指针的位置
# file.seek(7)
# result = file.tell()
# print(result)
#
# file_data = file.read()
# content = file_data.decode("utf-8")
# print(content)
#
# file.close()

# file = open("2.txt", "rb")
# # 读取一行数据, 当读取数据的时候遇到'\n'表示读取数据结束
# file_data = file.readline()
# print(file_data.decode("utf-8"))
#
# file.close()

file = open("2.txt", "rb")
# 文件中的数据按照每行去读取，把每行的数据放到一个列表里面
file_data = file.readlines()
for data in file_data:
    print(data.decode("utf-8"))

file.close()