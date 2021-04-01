# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 14:38:40 2021

@author: Adm
"""

from numpy import *
import numpy as np
import pandas as pd
import random
import operator
import math

df = pd.read_excel('result_zip.xlsx',encoding='utf-8')
tempearture = df['tempearture']

tempearture = np.array(tempearture)
tempearture = tempearture.tolist()
#print(tempearture)
list = []
for i in range(0,20):
    list += tempearture
#    
print(len(list))

yy = pd.DataFrame(list)

writer = pd.ExcelWriter('weather_tempearture.xlsx')

yy.to_excel(writer,'Sheet1')

writer.save()
