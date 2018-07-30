from io import BytesIO

byte_io = BytesIO()

# 向内存写入二进制数据
byte_io.write("哈哈".encode("utf-8"))
# 读取数据, 获取写入到内存中的全部数据
data = byte_io.getvalue()
print(data)

content = data.decode("utf-8")
print(content)