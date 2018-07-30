# 格式化符号： %s, %d, %f, %x

# %s: 输出字符串
# %d: 输出int类型数字
# %f: 输出浮点数
# %x: 输出16进制数据

name = '张三丰'
print("我叫%s" % name)

score = 100
print("python考试分数:%d" % score)

pi = 3.1455926
# %f 默认小数保留6位
print("圆周率:%f" % pi)
# 保留两位小数
# %f会对进行四舍五入
print("圆周率:%.2f" % pi)

num = 16
print("%x" % num)