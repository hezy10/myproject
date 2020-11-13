import gevent
import time
from gevent import monkey

monkey.patch_all()



def func(name):
    for i in range(10):
        print(name,i)
        time.sleep(1)


gevent.joinall([
    gevent.spawn(func,'w1'),
    gevent.spawn(func,'w2'),
    gevent.spawn(func,'w3'),
])

# def func(num):
#     for i in range(num):
#         print(gevent.getcurrent(),i)
#         gevent.sleep(1)
#
#
# g1 = gevent.spawn(func,5)
# g2 = gevent.spawn(func,6)
# g3 = gevent.spawn(func,7)
#
# g1.join()
# g2.join()
# g3.join()
