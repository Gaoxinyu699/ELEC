# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 15:34:57 2021

@author: Adm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#均方误差
def MSE(y, t, n):
    return 1 / n * np.sum((y - t)**2)

df = pd.read_excel('750user_weekmean.xlsx',encoding='utf-8',sheet_name='Sheet1')

print(df)

user_id = df['userId']
consumption = df['consumption']
consumption = np.array(consumption)

ydata = consumption[0:40]

print(ydata)

print(np.mean(ydata))

xdata = range(0,40)

xdata_predict = range(0,52)

f = np.polyfit(xdata, ydata, 4)
#print('f1 is :\n',f1)
p = np.poly1d(f)
#print('p1 is :\n',p1)
#也可使用yvals=np.polyval(f1, x)
yvals = p(xdata_predict)
#拟合y值
print('yvals is :\n',yvals)

mse = MSE(yvals[-12],consumption[40:52],12)

print(mse)
#绘图
plt.figure()
plt.plot(xdata, ydata, 's',label='original values')
plt.plot(xdata_predict, yvals, 'r',label='polyfit values')
plt.show()