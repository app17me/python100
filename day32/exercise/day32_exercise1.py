import pandas as pd
from datetime import datetime
import xtools as xt
import random 

today=datetime.now()
today_tuple=(today.month,today.day)
datas=pd.read_csv('birthdays.csv')

#print(datas)

file_path=f'letter_templates/letter_{random.randint(1,3)}.txt'
#print(file_path)

for index,data in datas.iterrows():
    if (data['month'],data['day'])==today_tuple:     
        print('-----------------------------------------')
        file_path=f'letter_templates/letter_{random.randint(1,3)}.txt'
        with open(file_path) as f:
            msg=f.read().replace('[NAME]',data['name'])
            
        xt.sendEmail(data['email'],data['name']+' 生日快樂!',msg)

