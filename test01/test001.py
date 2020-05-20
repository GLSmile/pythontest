
'''
def test01():

#一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
     m = n = 0
     for i in range(2,85):
         if 168 % i ==0:
             j=168/i
         if i>j and (i+j) %2 == 0 and (i-j)%2==0:
             m = (i+j)/2
             n = (i-j)/2
             if(m**2-268) == (n**2-100):
                print(m**2-268)


if __name__ == '__main__':
        test01()
'''


def test01():
    '''
    #输入某年某月某日，判断这一天是这一年的第几天？
    list1=[0,31,29,31,30,31,30,31,31,30,31,30,31] #1.可以被4整除,但不能被100整除 2.可以被400整除  #建立闰年平年每月的天数列表
    list2=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    sum=0
    year =int(input("请输入年份："))
    month =int(input("请输入月份："))
    day =int(input("请输入日期："))
    if ( year %4 ==0 and year %100!=0) or year%400==0:
        for i in  range(1,month):
            sum =sum +list1[i]
        sum +=day  #累计循环加入天数
    else:
        for i in range(1,month):
            sum =sum + list2[i]
        sum +=day
    print("这天是一年中的第",sum ,"天")'''

    '''
    #输出 9*9 乘法口诀表。
    for i in range(1,10):
        print("  ")
        for j in range(1,10):
            print("%d*%d=%d "%(i,j,i*j)) 

    #斐波那数列
   # n = int(input("请输入需求数："))

    def f(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return f(n - 1) + f(n - 2)  # 递归调用原函数

   # print("对应的斐波那契数列为：", f(n))

#古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
  #此问题的解答和上面斐波那数列一致
    m=int(input("请输入月数："))
    def func(n):
        if m==1:
            return 1
        if m==2:
            return 1
        else:
            return f(n-1)+f(n-2)

    print("该月份兔子有", func(m), "只")
    
    '''
    #使用迭代器来实现斐波那数列
    m=0
    def fibon(n):
        a=b=1
        for i in range(n):
            yield a
            a,b=b,a+b

    for x in fibon(5):
        print(x)
        m +=x
    print("这是总数：",m)



if __name__ == '__main__':
        test01()



