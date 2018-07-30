# 多态： 关注的是同一个方法，但是会出现不同的变形形式，提示： 在python里面不需要关心类型

class Text(object):
    def show(self):
        print("显示文字")


class Image(object):
    def show(self):
        print("显示图片")

class Video(object):
    def show(self):
        print("显示全屏的视频")


class Person(object):
    def show(self):
        print("我在跳舞")

# 实现显示数据的功能
def show_data(data):
    # 关心的是同一个方法，会出现不同的表现形式，那么这种操作叫做多态
    # 在python里面多态：只关心对象的方法，不关心对象的类型
    data.show()

image = Image()
video = Video()
person = Person()
show_data(person)
