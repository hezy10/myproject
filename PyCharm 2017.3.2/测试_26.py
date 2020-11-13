import numpy as np
import pandas as pd
import datetime
df1=pd.read_csv("C:\\Users\\倪敬一\\Desktop\\代码开发测试\\代码开发测试\\基金A净值.csv")
df1["基金种类"]="基金A"
#print(df1)
df2=pd.read_csv("C:\\Users\\倪敬一\\Desktop\\代码开发测试\\代码开发测试\\基金B净值.csv",names=["date","price"])
#print(df2)
df2["基金种类"]="基金B"
df3=pd.read_csv("C:\\Users\\倪敬一\\Desktop\\代码开发测试\\代码开发测试\\基金C净值.csv",names=["date","price"])
#print(df3)
df3["基金种类"]="基金C"
df=pd.concat([df1,df2,df3],axis=0)
print(df)



#print(df[(df.date=="2020/7/1")&(df.基金种类=="基金C")].index.tolist()[0])

def python1(date:"str"="2020/8/25",name:"str"="基金A"):
    df4 = pd.DataFrame(columns = ["date1", "price1"])
    if name == "基金A":
        a_index = df[(df.date == date)&(df.基金种类 == "基金A")].index.tolist()[0]
        a_price = df[(df.date == date) & (df.基金种类 == "基金A")]["price"].tolist()[0]
        for item in range(a_index,df1.count().tolist()[0]):
            if df[item].tolist()[2] == "基金A":
                a_newprine = df[item].tolist()[1]
                a_vaule = a_newprine - a_price
                d1 = datetime.datetime.strptime(df[item].tolist()[0], "%Y/%m/%d")
                d2 = datetime.datetime.strptime(date, "%Y/%m/%d")
                a_days=(d1 - d2).days
                a_rate = (a_vaule/a_price) * 365 / a_days
                if a_rate < 0.02:
                    a_profit = a_vaule + a_price
                    df4.append(df[item].tolist()[0],a_profit)
                elif a_rate > 0.02 and a_rate < 0.12:
                    a_profit = a_price + a_price*0.02 + (a_vaule-a_price*0.02)*0.7
                    df4.append(df[item].tolist()[0], a_profit)
                elif a_rate > 0.12:
                    a_profit = a_price + a_price*0.02 + (a_vaule-a_price*0.02)*0.7 + (a_vaule-a_price*0.12)*0.5
                    df4.append(df[item].tolist()[0], a_profit)
            else:
                continue
        outputpath = '"C:/Users/倪敬一/Desktop/净值计算.csv'
        df.to_csv(outputpath, sep='', index=False, header=True)

    elif name=="基金B":
        b_index=  df[(df.date == date)&(df.基金种类=="基金B")].index.tolist()[0]
        b_price = df[(df.date == date) & (df.基金种类 == "基金B")]["price"].tolist()[0]
        for item in range(b_index,df1.count().tolist()[0]):
            if df[item].tolist()[2] == "基金B":
                b_newprine = df[item].tolist()[1]
                b_vaule = b_newprine-b_price
                d1 = datetime.datetime.strptime(df[item].tolist()[0], "%Y/%m/%d")
                d2 = datetime.datetime.strptime(date, "%Y/%m/%d")
                b_days=(d1 - d2).days
                b_rate = (b_vaule/b_price) * 365 / b_days
                b_profit = b_vaule*0.8+b_price
                df4.append(df[item].tolist()[0],b_profit)
            else:
                continue
        outputpath = '"C:/Users/倪敬一/Desktop/净值计算.csv'
        df.to_csv(outputpath, sep='', index=False, header=True)
    elif name=="基金C":
        c_index=  df[(df.dat == date)&(df.基金种类=="基金C")].index.tolist()[0]
        c_price = df[(df.date == date) & (df.基金种类 == "基金C")]["price"].tolist()[0]
        for item in range(c_index,df1.count().tolist()[0]):
            if df[item].tolist()[2] == "基金A":
                c_newprine = df[item].tolist()[1]
                c_vaule = c_newprine-c_price
                d1 = datetime.datetime.strptime(df[item].tolist()[0], "%Y/%m/%d")
                d2 = datetime.datetime.strptime(date, "%Y/%m/%d")
                c_days=(d1 - d2).days
                c_rate = (c_vaule/c_price) * 365 / c_days
                if c_rate < 0.06:
                    c_profit = c_vaule+c_price
                    df4.append(df[item].tolist()[0],c_profit)
                elif c_rate > 0.06:
                    c_profit = c_price + (c_vaule-c_price*0.06)*0.5
                    df4.append(df[item].tolist()[0], c_profit)
            else:
                continue
        outputpath = '"C:/Users/倪敬一/Desktop/净值计算.csv'
        df.to_csv(outputpath, sep='', index=False, header=True)


if __name__=="__main__":

    pass
