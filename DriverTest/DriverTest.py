#!/bin/python
# -*- coding:UTF-8 -*-
from __future__ import print_function
import ctypes
from _ctypes import pointer
import time
import threading
from time import sleep
from lib2to3.pgen2 import driver
import logging


class func():
    __mdfunc = ctypes.cdll.LoadLibrary("/usr/lib/libmdfunction.so")
    __a = ctypes.c_int32()

    def mdOpen(self):
        # open function
        openRet = func.__mdfunc.mdOpen(151, -1, pointer(func.__a))
#         print("open result", openRet)
        logging.info("open result:%d"%openRet)

    # mdSendEx function
    def mdSendEx(self, netno, stationNo, devtype, devNo, size01):
        size = ctypes.c_int32()
        size.value = size01
        array = (ctypes.c_int32 * size.value)()
        #         print (array)
        for i in range(0, size.value):
            array[i] = ctypes.c_int(i % 256)
        t1 = time.time()
        sendRet = func.__mdfunc.mdSendEx(func.__a.value, netno, stationNo, devtype, devNo, pointer(size), array)
        t2 = time.time()
        # print (str(t2-t1))
#         print(stationNo, "-send result:", sendRet, "send using time", str(t2 - t1))
        logging.info("stationNo:%d send result:%d send time:%d"%(stationNo,sendRet,t2-t1))
    #         print ()
    #         for i in range(0,size.value):
    #             print (array[i],end=' ')

    def mdReceive(self, netno, stationNo, devtype, devNo, size01):
        # mdRecive function
        size = ctypes.c_int32()
        size.value = size01
        parray = (ctypes.c_int32 * size.value)()
        #         print (parray)
        t3 = time.time()
        receiveRet = func.__mdfunc.mdReceiveEx(func.__a.value, netno, stationNo, devtype, devNo, pointer(size), parray)
        t4 = time.time()
        print(stationNo, "-receive result", receiveRet, "receive using time", str(t4 - t3))
        logging.info("stationNo:%d receive result:%d receive time:%d"%(stationNo,receiveRet,t4-t3))
    #         print ()
    #         for i in range(0,size.value):
    #             print (parray[i],end=' ')
    #         print ()
    #mdRandWEx function
    def mdRandWEx(self,netno,stationNo,dev,buf,bufsize):
        if not len(dev)%3==1:
            print ("please input the right number!")
            return
        cdev=(ctypes.c_int32*len(dev))()
        for i in range(0,len(dev)):
            cdev[i]=ctypes.c_int32(dev[i])
        cbuf=(ctypes.c_int16*len(buf))()
        for i in range(0,len(buf)):
            cbuf[i]=ctypes.c_int16(buf[i])

        randWExret=func.__mdfunc.mdRandWEx(func.__a.value,netno,stationNo,cdev,cbuf,bufsize)
#         print ("randWExret:",randWExret)
        logging.info("randWExret:%d"%randWExret)
    #mdRandREx function
    def mdRandREx(self,netno,stationNo,dev,buf,bufsize):
        if not len(dev)%3==1:
            print ("please input the right number!")
            return
        cdev=(ctypes.c_int32*len(dev))()
        for i in range(0,len(dev)):
            cdev[i]=ctypes.c_int32(dev[i])
        cbuf=(ctypes.c_int16*len(buf))()
        for i in range(0,len(buf)):
            cbuf[i]=ctypes.c_int16(buf[i])
        randRExret=func.__mdfunc.mdRandREx(func.__a.value,netno,stationNo,cdev,cbuf,bufsize)
#         print  ("randRExret:",randRExret)
        logging.info("randRExret:%d"%randRExret)
        outputarr=[]
        for i in cbuf:
#             print (i,end=" ")
            outputarr.append(i)
        logging.info(str(outputarr))
    # close?function
    def mdClose(self):
        closeRet = func.__mdfunc.mdClose(func.__a.value)
#         print("close result:", closeRet)
        logging.info("close result:%d"%closeRet)
    def multiSend(self, count, netno, stationNo, devtype, devNo, size01):
        for i in range(count):
            self.mdSendEx(netno, stationNo, devtype, devNo, size01)
            sleep(0.1)

    def multiReceive(self, count, netno, stationNo, devtype, devNo, size01):
        for i in range(count):
            self.mdReceive(netno, stationNo, devtype, devNo, size01)
            sleep(0.1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    driverfun = func()
    driverfun.mdOpen()
  
    threads = []
    count = 10
    #     t1=threading.Thread(target=driverfun.mdSendEx,args=(1,255,23,0,4096))
    #     t2=threading.Thread(target=driverfun.mdReceive,args=(1,255,23,0,4096))
    #     t3=threading.Thread(target=driverfun.mdSendEx,args=(1,255,24,0,262144))
    #     t4=threading.Thread(target=driverfun.mdReceive,args=(1,255,24,0,262144))
    #     t5=threading.Thread(target=driverfun.mdSendEx,args=(1,2,220,0,65536))
    #     t6=threading.Thread(target=driverfun.mdReceive,args=(1,2,220,0,65536))
    #     t1=threading.Thread(target=driverfun.multiSend,args=(count,1,255,23,0,4096))
    #     t2=threading.Thread(target=driverfun.multiReceive,args=(count,1,255,23,0,4096))
    # t3 = threading.Thread(target=driverfun.multiSend, args=(count, 1, 255, 24, 0, 262144))
    # t4 = threading.Thread(target=driverfun.multiReceive, args=(count, 1, 255, 24, 0, 262144))
    # t5 = threading.Thread(target=driverfun.multiSend, args=(count, 1, 2, 220, 0, 2))
    # t6 = threading.Thread(target=driverfun.multiReceive, args=(count, 1, 2, 220, 32768, 2))
    #     threads.append(t1)
    #     threads.append(t2)
    # threads.append(t3)
    # threads.append(t4)
    # threads.append(t5)
    # threads.append(t6)

    # for t in threads:
    #     t.setDaemon(True)
    #     t.start()
    for i in range(10):
        driverfun.mdRandWEx(1,255,(4,5,0,8,23,0,8,24,0,8,14,0,2),(255,1,1000,29932,123,3434,23323,61111,65535,65536,24312,20000),12)
        driverfun.mdRandREx(1,255,(4,5,0,8,23,0,8,24,0,8,14,0,2),(0,0,0,0,0,0,0,0,0,0,0,0),12)


    driverfun.mdClose()
