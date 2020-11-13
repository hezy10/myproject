import os
import pandas as pd
import glob

csv_list = glob.glob(r'./*.csv')

for i in csv_list:
    fr = open(i,'rb').readlines()[1:]
    if fr !=',price,position':
        with open('merge.csv','ab') as f:
            for j in fr:
                f.write(j)
print('合并完成')