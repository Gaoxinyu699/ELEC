# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 17:32:45 2021

@author: Adm
"""

from numpy import *
import numpy as np
import pandas as pd
import random
import operator
import math

df = pd.read_excel('C:/Users/Adm/Desktop/electricitry/id-1000.xlsx',encoding='utf-8')
id = df['id']
time = df['time']
consumption = df['consumption']
#consumption = np.array(consumption)
date = df['date']

tempearture = df['tempearture']
#tempearture = np.array(tempearture)
humidity = df['humidity']
#humidity = np.array(humidity)
bad_res = df['bad_res']

#print(sum(consumption[0:48]))
consumption_res = consumption.groupby(consumption.index // 48).sum()
tempearture_res = tempearture.groupby(tempearture.index // 48).mean()
humidity_res = humidity.groupby(humidity.index // 48).mean()
bad_res = bad_res.groupby(bad_res.index // 48).sum()
consumption_res = round(consumption_res,3)
tempearture_res = round(tempearture_res,3)
humidity_res = round(humidity_res,3)
bad_res = round(bad_res,3)

result = zip(consumption_res,tempearture_res,humidity_res,bad_res)

yy = pd.DataFrame(result)

writer = pd.ExcelWriter('result_zip.xlsx')

yy.to_excel(writer,'Sheet1')

writer.save()

