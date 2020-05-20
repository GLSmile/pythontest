import time

#带多个参数的装饰
def decorator(func):
    def wrapper(*args,**kw):  #*args,**kw  仅是定义的一个形参名称，可以换成任意别的名称
        print('带多个参数的装饰：')
        print(time.time())
        func(*args,**kw)
    return wrapper

@decorator
def f1(func_name):
    print("this is a function named:" + func_name)
    print('\n\n')
@decorator
def f2(func_name1,func_name2):
    print("this is a function named:" + func_name1)
    print("this is a function named:" + func_name2)
    print('\n\n')
@decorator
def f3(func_name1,func_name2,**kw):
    print("this is a function named:" + func_name1)
    print("this is a function named:" + func_name2)
    print(kw)
    print('\n\n')


f1('test_n')
f2('test_n1','test_n2')
f3('test_n1','test_n2',a=1,b=2,c='123')