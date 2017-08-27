# -*-coding:utf-8 -*-
import  time,uuid
from transwarp import  next_id
from transwarp import  Model,StringField,BooleanField,FloatField,TextField

class User(Model):
    __table__='users'
    id=StringField(primary_key=True,default=next_id,dd1='varchar(50)')
    email=StringField(updatable=False,dd1='varchar(50)')
    password=StringField(dd1='varchar(50)')
    admin=BooleanField()
    image=StringField(dd1='varchar(500)')
    name=StringField(dd1='varchar(50)')
    created_at=FloatField(updatable=False,default=time.time)

class Blog(Model):
    __table__='blogs'
    id=StringField(primary_key=True,default=next_id,dd1='varchar(50)')
    user_id=StringField(updatable=False,dd1='varchar(50)')
    user_name = StringField(dd1='varchar(50)')
    user_image = StringField(dd1='varchar(500)')
    name=StringField(dd1='varchar(50)')
    summary=StringField(dd1='varchar(50)')
    content=TextField()
    created_at=FloatField(updatable=False,default=time.time)

class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(updatable=False, ddl='varchar(50)')
    user_id = StringField(updatable=False, ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(updatable=False, default=time.time)









