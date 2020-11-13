# import os
# from multiprocessing import Process
# # 创建子进程
# # os.fork()
#
#
# # def sing():
# #     print(os.getpid())
# #     for i in range(5):
# #         print('唱歌')
# #
# #
# # def dancing():
# #     print(os.getpid())
# #     for i in range(5):
# #         print('跳舞')
# # if __name__ == '__main__':
# #     # 查看进程编号和父进程编号
# #     print(os.getpid(), os.getppid())
# #     sing()
# #     dancing()
#
#
# def child_process_pid(name):
#
#     print('我是子进程，进程编号{}，父进程编号{},名字是{}'.format(os.getpid(), os.getppid(), name))
#
#
# if __name__ == '__main__':
#     print(os.getpid())
#     # 创建子进程
#     cp = Process(target=child_process_pid, args=('紫禁城',))
#     # 调用
#     cp.start()
#     print(cp.name,cp.pid)
#     # cp.join()
#     print('end')
#     exit()
#     # GIL


# 多任务
# from multiprocessing import Process
#
#
# def func():
#     print('********')
#
#
# class MyProcess(Process):
#     def __init__(self,cname):
#          # 重写
#          # Process.__init__(self)
#          # super(MyProcess, self).__init__()
#         super().__init__()
#         self.cname = cname
#
#     # def run(self) -> None:
#     #     print('------------->')
#
# if __name__ == '__main__':
#     mp = MyProcess('123')
#     mp.start()                  # 调用run方法
#
#
#
# from multiprocessing import Pool
# import os
# import time
# 进程池
#
#
# def work(a):
#     print('这是第{}任务，进程编号是{}'.format(a, os.getpid()))
#     time.sleep(1)
#
# if __name__ == '__main__':
#     pool = Pool(3)
#     for i in range(10):
#         # pool.apply_async(work, args=(i,))
#         pool.apply(work, args=(i,))
#
#     pool.close()
#     pool.join()


# from multiprocessing import Queue
#
# que = Queue(5)
# que.put(1)
# que.put(2)
# que.put(3)
# que.put(4)
# que.put(5)
# # que.put(6)
# # que.put(6,False)
# # que.put(6,True,2)
#
# print(que.get())
# print(que.get())
# que.put(6)

# from multiprocessing import Pool
# from multiprocessing import Queue
# import os
# import time
# que = Queue(10)
#
#
# def put1(num):
#     que.put(num)
#
#
# def get1():
#     print('Queue取出的数字是{}，编号是{}'.format(que.get(),os.getpid()))
#     time.sleep(1)
#
#
# if __name__ == '__main__':
#     pool = Pool(2)
#     for i in range(10):
#         pool.apply_async(put1,args=(i,))
#         pool.apply_async(get1)
#
#     pool.close()
#     pool.join()


# from multiprocessing import Pool,Manager
# import time
# import os
#
#
# def read(q):
#     for i in range(10):
#         print('获取数据是{},id{}，父id{}'.format(q.get(),os.getpid(), os.getppid()))
#         time.sleep(1)
#
#
# def write(q):
#     for i in range(10):
#         q.put(i)
#
# if __name__ == '__main__':
#     print('id-->',os.getpid())
#     pool = Pool()
#     que = Manager().Queue()
#     pool.apply_async(write,args=(que,))
#     pool.apply_async(read,args=(que,))
#     pool.close()
#     pool.join()


