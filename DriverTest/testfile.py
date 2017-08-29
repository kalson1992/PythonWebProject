#-*-coding:utf-8 -*-
#author:kalson
s=set([3,4,'sd',53])
t=set(['hello',53])
print t|s
print t&s
print t-s
print t^s

f=open('DriverTest.py',mode='r',buffering=1024)
print f.readlines()
f.close()
def methodA(*args,**kwargs):
    print args
    print  kwargs
methodA(*(12,23),**{'key':"value"})
methodA(12,23,key="value")

name = "Alex"
def change_name():
    name = "Alex2"
    def change_name2():
        name = "Alex3"
        print "第3层打印"+name

    change_name2()  # 调用内层函数
    print "第2层打印%s"%name
change_name()
print("最外层打印", name)
g=(x*x for x in range(10))
print g
# for i in range(10):
#     print next(g)
for i in g:
    print i



