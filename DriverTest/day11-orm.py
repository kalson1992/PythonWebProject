# -*-coding:utf-8 -*-
#author:kalson
import sqlalchemy
from sqlalchemy import  create_engine
from sqlalchemy.ext.declarative import declarative_base
from  sqlalchemy import  Column,Integer,String
from  sqlalchemy.orm import  sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

engine=create_engine("mysql+mysqldb://root:redhat123@192.168.242.129/awesome",encoding='utf-8',echo=True)
Base=declarative_base()
class User(Base):
    __tablename__="user"
    id=Column(Integer,primary_key=True)
    name=Column(String(32))
    password=Column(String(64))
    def __repr__(self):
        return "<User(id=%d, name='%s',  password='%s')>" % (
            self.id,self.name, self.password)
class Address(Base):
    __tablename__='address'
    id=Column(Integer,primary_key=True)
    email_address=Column(String(32),nullable=False)
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship("User",backref="addresses")
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
Base.metadata.create_all(engine)
Session_class=sessionmaker(bind=engine)
Session=Session_class()
user_obj=User(name='alex',password='alex3714')
print (user_obj.name,user_obj.id)
Session.add(user_obj)
print (user_obj.name,user_obj.id)
Session.commit()        #增加
my_user=Session.query(User).filter_by(name='alex').first()
print(my_user)
print (my_user.id,my_user.name,my_user.password)#查询
my_user.name="Alex Li"
Session.commit()
my_user = Session.query(User).filter_by(id=1).first()#回滚
my_user.name = "Jack"
fake_user=User(name='Rain',password='12345')
Session.add(fake_user)
print (Session.query(User).filter(User.name.in_(['Jack','Rain'])).all())
Session.rollback() #此时你rollback一下
print(Session.query(User).filter(User.name.in_(['Jack','rain'])).all() )
print(Session.query(User.name,User.id).all() )
Session.commit()
#========以上是对一个表的增删改查==========
#========以下开始操作联动表格==============
obj=Session.query(User).first()
for i in obj.addresses:
    print(i)
# addr_obj=Session.query(Address).first()
# print (addr_obj.user.name)

obj = Session.query(User).filter(User.name == 'rain').all()[0]
print(obj.addresses)

obj.addresses = [Address(email_address="r1@126.com"),  # 添加关联对象
                 Address(email_address="r2@126.com")]

Session.commit()