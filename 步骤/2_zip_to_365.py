from numpy import *
import numpy as np
import pandas as pd
import random
import operator
import math

# 365天_编号1000起.xlsx 1004115 / 365 = 2751
# 365天_编号4000起.xlsx 672330 / 365 =  1842
# 365天_编号6000起.xlsx 482530 / 365 = 1322

for k in range(1, 17):
    df = pd.read_excel('365天_编号4000起.xlsx',engine='openpyxl',sheet_name='Sheet' + str(k) + '')
    id = df['id']
    # print(id[17520])
    # time = df['time']
    consumption = df['consumption']
    # print(consumption)
    # consumption = np.array(consumption)
    # date = df['date']
    #
    # tempearture = df['tempearture']
    ##tempearture = np.array(tempearture)
    # humidity = df['humidity']
    ##humidity = np.array(humidity)
    # bad_res = df['bad_res']

    # print(sum(consumption[0:48]))
    id_list = []
    for i in sorted(set(id)):
        for j in range(1,366):
            id_list.append(i)
    consumption_res = consumption.groupby(consumption.index // 48).sum()
    # tempearture_res = tempearture.groupby(tempearture.index // 48).mean()
    # humidity_res = humidity.groupby(humidity.index // 48).mean()
    # bad_res = bad_res.groupby(bad_res.index // 48).sum()
    consumption_res = round(consumption_res, 3)
    # tempearture_res = round(tempearture_res,3)
    # humidity_res = round(humidity_res,3)
    # bad_res = round(bad_res,3)
    #
    # result = zip(consumption_res,tempearture_res,humidity_res,bad_res)
    result = zip(id_list, consumption_res)



    yy = pd.DataFrame(result)

    writer = pd.ExcelWriter('4000起' + str(k) + '.xlsx')

    yy.to_excel(writer, 'Sheet1')

    writer.save()
