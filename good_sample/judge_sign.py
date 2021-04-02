# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 15:00:53 2021

@author: Adm
"""

from numpy import *
import numpy as np
import pandas as pd
import random
import operator
import math

df = pd.read_excel('C:/Users/Adm/Desktop/electricitry/good_sample/good_user1.xlsx',encoding='utf-8',sheet_name='Sheet1')

#consumption = df['consumption']
power_index = df['Power_Index']
#weather_index = df['Weather_Index']

#print(power_index)

#list = []
#for i in range(0,len(power_index)):
#    if power_index[i] < 0 and weather_index[i] < 0:
#        list.append(1)
#    else:
#        list.append(0)
#
#print(len(list))
#
#yy = pd.DataFrame(list)
#
#writer = pd.ExcelWriter('Index_Relation.xlsx')
#
#yy.to_excel(writer,'Sheet1')
#
#writer.save()