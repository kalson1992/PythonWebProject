# -*-coding:utf-8 -*-
#author:kalson
from  __future__ import  print_function
import  threading,time,random
def door():
    door_open_time_counter=0
    while True:
        if door_swiping_event.is_set():
            print("door opening")
            door_open_time_counter+=1
        else:
            print("door closed,swipe to open")
            door_open_time_counter=0
            door_swiping_event.wait()
        if door_open_time_counter>3:
            door_swiping_event.clear()
        time.sleep(0.5)

def staff(n):
    print ("staff [%s] is comming..."%n)
    while True:
        if door_swiping_event.is_set():
            print ("door is opened ,passing")
            break
        else:
            print ("staff [%s] sees door got closed,swipping the card..."%n)
            print (door_swiping_event.set())
            door_swiping_event.set()
            print ("after set",door_swiping_event.set())
        time.sleep(0.5)
door_swiping_event=threading.Event()
door_thread=threading.Thread(target=door)
door_thread.start()
for i in range(5):
    p=threading.Thread(target=staff,args=(i,))
    time.sleep(random.randrange(3))
    p.start()
