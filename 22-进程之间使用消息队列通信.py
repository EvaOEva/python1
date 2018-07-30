import multiprocessing
import time


def add_data(queue):
    for i in range(3):
        print(i)
        queue.put(i)
        time.sleep(0.3)


def read_data(queue):
    while True:
        # 判断队列是否为空
        if queue.empty():
            break
        value = queue.get()
        print(value)

if __name__ == '__main__':
    # 默认是队列可以放入任意多个数据
    # 3：表示队列中最大有三个数据
    queue = multiprocessing.Queue(3)
    # 创建两个子进程
    add_proccess = multiprocessing.Process(target=add_data, args=(queue, ))
    read_procces = multiprocessing.Process(target=read_data, args=(queue, ))

    # 启动进程执行任务
    add_proccess.start()
    # 进程等待，主进程等待子进程执行完在让后面的代码执行
    add_proccess.join()
    read_procces.start()


# 多任务：使用线程和进程
# 从资源角度来说线程更加节省资源
# 进程销毁的资源比较多

# 从代码稳定性来说： 多进程要比多线程稳定性要强，因为一个进程挂掉不会影响其他进程