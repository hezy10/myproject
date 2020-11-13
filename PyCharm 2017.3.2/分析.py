import pandas as pd

data = pd.read_csv(r'./text1.csv',usecols=['price'])
print(data)
ret = pd.cut(data,5)
print(ret)

