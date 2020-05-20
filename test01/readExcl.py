import xlrd

class read_Excel():
    def red_exc(self):
        # 打开excel,参数url是excel表存放的位置
        exclBook = xlrd.open_workbook("D:/Desktop/work/excleData/testExcel.xlsx")

        # 定位到sheet2页面
        exclTabel = exclBook.sheet_by_name("Sheet1")
        #获取总行数
        all_nrows = exclTabel.nrows
        #获取总列数
        all_ncols = exclTabel.ncols

        # 定义一个空列表存储取出的数据
        s =[]
        # 开始读取第一行作为字典key值
        key =exclTabel.row_values(0)
        print(key)
        #print(type(key))

        # 先判断是否表中有数据，没有则不进行处理，直接提示无数据，有数据再进行读取处理
        if all_nrows < 1:
            print("无数据可读取")
        else:
            #r =[]
            j =1
            #循环取行数
            for i in range(all_nrows-1):
                #定义一个空字典
                d ={}
                #取每一列的所有数据
                col_values = exclTabel.row_values(j)
                print(col_values)

                for x in range(len(col_values)): #循环取每一列
                    #像字典中加入数据
                    d[key[x]] = col_values[x]
                s.append(d)#把字典加入列表 d{key:value}，s[{城市:value},{天气:value},...]
                j += 1  # 完成一次大循环
            return s



if __name__ == "__main__":
    r_ex = read_Excel() #创建实例
    s =r_ex.red_exc() #执行方法调用
    print(s)