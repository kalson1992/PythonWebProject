# -*-coding:utf-8 -*-
#author:kalson
from __future__ import print_function
user_status = False
def login(func):  # 把要执行的模块从这里传进来
    def inner(*args,**kwargs):  # 再定义一层函数
        _username = "alex"  # 假装这是DB里存的用户信息
        _password = "abc!23"  # 假装这是DB里存的用户信息
        global user_status
        if user_status == False:
            username = raw_input("user:")
            password = raw_input("pasword:")
            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")
        if user_status == True:
            func(*args,**kwargs)  # 看这里看这里，只要验证通过了，就调用相应功能
    return inner  # 用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数
@login
def home():
    print("---首页----")
def america():
    print("----欧美专区----")
def japan():
    print("----日韩专区----")
def henan():
    print("----河南专区----")
# home()
america()
print (user_status)
login(japan)()
henan()