# 线程： 执行代码的分支，默认程序中只有一个线程
import time
import threading


def AA(count):
    for i in range(count):
        print("aa")
        time.sleep(0.2)


def BB(count):
    for i in range(count):
        print("bb")
        time.sleep(0.2)


if __name__ == '__main__':
    # 创建子线程执行对应的代码
    # target表示目标函数
    # args:表示以元组的方式给函数传参
    # kwargs:表示已字典的方式给函数传参
    # sub_thread = threading.Thread(target=AA, args=(3,))
    sub_thread = threading.Thread(target=AA, kwargs={"count": 3})
    three_thread = threading.Thread(target=BB, args=(3,))

    # 启动线程， 只有启动才会让线程执行对应函数里面的代码
    sub_thread.start()
    three_thread.start()

    # 主线程执行bb
    # BB()

    # 线程执行是无序的，有cpu调度决定的