
#多线程
# import threading
# import time
#
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
# def fun_timer():
#     print('hello world')
#     global timer
#     timer = threading.Timer(3,fun_timer)
#     timer.start()
#
# timer = threading.Timer(2,fun_timer)
# timer.start()
#
# time.sleep(10)
# timer.cancel()

#定时器（装饰器+time.sleep)
import time

def myDecorator(func):
    def wrapper():
        time.sleep(2)
        func()
    return wrapper

@myDecorator
def greet():
    for s in range(100):
        time.sleep(2)
        print(s)

Greet = myDecorator(greet)

for i in range(10):
    Greet()


