# # -*-coding:utf-8 -*-
# #author:kalson
# from  __future__ import  print_function
# import  threading,time,random
# def door():
#     door_open_time_counter=0
#     while True:
#         if door_swiping_event.is_set():
#             print("door opening")
#             door_open_time_counter+=1
#         else:
#             print("door closed,swipe to open")
#             door_open_time_counter=0
#             door_swiping_event.wait()
#         if door_open_time_counter>3:
#             door_swiping_event.clear()
#         time.sleep(0.5)
#
# def staff(n):
#     print ("staff [%s] is comming..."%n)
#     while True:
#         if door_swiping_event.is_set():
#             print ("door is opened ,passing")
#             break
#         else:
#             print ("staff [%s] sees door got closed,swipping the card..."%n)
#             print (door_swiping_event.set())
#             door_swiping_event.set()
#             print ("after set",door_swiping_event.set())
#         time.sleep(0.5)
# door_swiping_event=threading.Event()
# door_thread=threading.Thread(target=door)
# door_thread.start()
# for i in range(5):
#     p=threading.Thread(target=staff,args=(i,))
#     time.sleep(random.randrange(3))
#     p.start()

#
# import threading
# import time
#
#
# def sayhi(num):  # 定义每个线程要运行的函数
#
#     print("running on number:%s" % num)
#
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=sayhi, args=(1,))  # 生成一个线程实例
#     t2 = threading.Thread(target=sayhi, args=(2,))  # 生成另一个线程实例
#
#     t1.start()  # 启动线程
#     t2.start()  # 启动另一个线程
#
#     print(t1.getName())  # 获取线程名
#     print(t2.getName())


import time
import threading


def addNum():
    global num  # 在每个线程中都获取这个全局变量
    print('--get num:', num)
    time.sleep(5)
    num -= 1  # 对此公共变量进行-1操作


num = 100  # 设定一个共享变量
thread_list = []
for i in range(100):
    t = threading.Thread(target=addNum)
    t.start()
    thread_list.append(t)

for t in thread_list:  # 等待所有线程执行完毕
    t.join()

print('final num:', num)