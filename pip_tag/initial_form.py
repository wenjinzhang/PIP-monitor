import time
import pandas as pd
from pathlib import Path
now = time.localtime()
nowt = time.strftime("%Y-%m-%d-%H_%M_%S", now)  #这一步就是对时间进行格式化
# print(nowt)

# initialize the csv form
column = ['time','temp','light', 'humidty']
file_root = Path('data.csv')
if not file_root.exists():
    data = pd.DataFrame(columns=column)
    data.to_csv(file_root,index=False)


data = pd.read_csv(file_root)
print(data.tail(1)['temp'])
# if pd.read_csv(file_root) == None:
#     print(1)
# wen = pd.DataFrame(columns=b,data=a)
# data.to_csv(file_root,mode='a',header=False,index=False)
# print(wen)