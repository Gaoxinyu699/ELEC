# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 11:49:27 2021

@author: Adm
"""

import pandas as pd
import numpy as np

df = pd.read_excel('750user.xlsx',encoding='utf-8',sheet_name='Sheet1')
print(df)
user_id = df['userId']
consumption = df['consumption']
consumption = np.array(consumption)

week_consumption_mean_list = []
user_id_list = []
user_id = set(user_id)
user_id = list(user_id)
for j in range(0,750):
    
    user_consumption = consumption[j*365:j*365+364]
    
    #week_consumption = user_consumption[0:7]
    
    #temp_week_consumption_mean_list = []
    #temp_user_id_list = []
    for i in range(0,52):
    
        week_consumption_mean = sum(user_consumption[i*7:(i+1)*7])/7
        
        week_consumption_mean = round(week_consumption_mean,3)
    
        print(week_consumption_mean)
    
        week_consumption_mean_list.append(week_consumption_mean)
        
        user_id_list.append(user_id[j])
    
    #print(len(temp_week_consumption_mean_list))
    #user_id_list.append(temp_user_id_list)
    #week_consumption_mean_list.append(temp_week_consumption_mean_list)
    
    #user_id_list
print(user_id_list)
print(week_consumption_mean_list)

result = zip(user_id_list,week_consumption_mean_list)

yy = pd.DataFrame(result)
writer = pd.ExcelWriter('750user_weekmean.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()



