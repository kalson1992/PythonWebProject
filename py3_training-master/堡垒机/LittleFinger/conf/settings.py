#-*- coding:utf-8 -*-
__author__ = 'Alex Li'
import os,sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DB_CONN ="mysql+pymysql://root:redhat123@192.168.242.129:3306/little_finger?charset=utf8"

'''
# Database
DATABASES = {
    'default': {
        'ENGINE': 'mysqldb',
        'NAME': 'LittleFinger',
        'HOST': '',
        'PORT':3306,
        'USER':'root',
        'PASSWORD': ''
    }
}
'''

