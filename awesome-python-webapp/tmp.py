import  logging
a='wewe'
logging.basicConfig(level=logging.INFO)
logging.info("swewa%s"%a)
k=(1,2,3)
v=('a','b','c')
# for a,b in zip(k,v):
#     print  a=b
print  zip(k,v)
def method(name=(),value=()):
    print zip(name,value)
method(('sdas','sdfaf'),('wewew','sfsfs'))