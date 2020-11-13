import threading
# import time
#
#
# # def info():
# #     print('0123456789')
# #     time.sleep(1)
# #
# # if __name__ == '__main__':
# #     t = threading.Thread(target=info)
# #     t.start()
#
#
# num = 0
#
# # 锁
# lock = threading.Lock()
#
#
# def func1(n):
#     global num
#     for i in range(n):
#         # 创建互斥锁
#         flag = lock.acquire()
#         if flag:
#             num += 1
#             # 释放互斥锁
#             lock.release()
#     print(num)
#
#
# def func2(n):
#     global num
#     for i in range(n):
#         flag = lock.acquire()
#         if flag:
#             num += 1
#             lock.release()
#     print(num)
#
# if __name__ == '__main__':
#     td = threading.Thread(target=func1,args=(1000000,))
#     td.start()
#     # time.sleep(1)
#     td1 = threading.Thread(target=func2,args=(1000000,))
#     td1.start()

# # 在多线程中，共享全局变量，局部变量不共享
# # import threading
# #
# #
# # class MyThread(threading.Thread):
# #     def __init__(self,num):
            # # 重写父类init
# #         threading.Thread.__init__(self)
# #         # super(MyThread, self).__init__()
# #         self.num = num
# #
# #     def run(self):
# #         self.num +=1
# #         print(self.num)
# #
# #
# # if __name__ == '__main__':
# #     t1 = MyThread(1)
# #     t2 = MyThread(3)
# #     t1.start()
# #     t2.start()


# 生产者消费者模式

import threading
from queue import Queue


class Producers(threading.Thread):
    def run(self):
        global que
        while True:
            if que.qsize() < 10:
                que.put('数据')


# class Consumers(threading.Thread):
#     def run(self):
#         global que
#         while True:
#             if que.qsize() > 0:
#                 print(self.name,que.get())
#
#
# if __name__ == '__main__':
#     que = Queue()
#     p = Producers()
#     p.start()
#     c = Consumers()
#     c.start()


# # 协同半自动
# import greenlet


# 协同全自动
import gevent
import time
from gevent import monkey

mo = monkey.patch_all()


def func(n):
    for i in range(10):
        print(n,i)
        time.sleep(1)


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(func,'w1'),
        gevent.spawn(func,'w2'),
        gevent.spawn(func,'w3')
    ])



