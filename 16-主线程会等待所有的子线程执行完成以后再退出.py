import time
import threading


def AA():
    print("AA：", threading.current_thread())
    print("这个代码是在子线程中执行的")
    while True:
        print("AA")
        time.sleep(0.2)


if __name__ == '__main__':
    print("main：", threading.current_thread())
    # target指定的目标函数是在子线程中执行的
    t1 = threading.Thread(target=AA, daemon=True)
    # 设置守护线程, 主线程退出子线程直接销毁不在执行对应的代码
    # t1.setDaemon(True)
    t1.start()

    time.sleep(1)
    print("over")

    # 总结： 主线程会等到子线程执行完成以后程序再退出