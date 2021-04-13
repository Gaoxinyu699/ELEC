# -*- coding: utf-8 -*-
"""
Created on Fri Apr  13 11:20:19 2021

@author: Adm
"""

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from scipy import interpolate 
import pylab as pl 
import matplotlib as mpl 
import random

df = pd.read_excel('第四类.xlsx',sheet_name='Sheet1')
#print(df)
user_id = df['userId']
consumption = df['consumption']
rmse = df['rmse']
rmse = np.array(rmse)
consumption = np.array(consumption)
rmse = np.array(rmse)
consumption = np.array(consumption)
print(rmse)
print(consumption)
#print(sorted(rmse))
#print(sorted(consumption))
print(max(rmse))
print(min(rmse))
print(max(consumption))
print(min(consumption))

#x1,y1 = np.meshgrid(consumption,rmse)
#print(x1)
#print(y1)
#
#result = list(zip(rmse,consumption))
#
#print(result)

#随机数插值
new_rmse = []
new_consumption = []
for i in range(0,172):
    new_rmse.append(round(random.uniform(min(rmse), max(rmse)),3))
    new_consumption.append(round(random.uniform(min(consumption), max(consumption)),3))
#    print(random.uniform(min(rmse), max(rmse)))
#    print(random.uniform(min(consumption), max(consumption)))

result = zip(new_consumption,new_rmse)

print(result)

#多项式插值
xdata = np.arange(20,100,0.5)
f = np.polyfit(consumption, rmse, 4)
p = np.poly1d(f)
yvals = p(xdata)
print(yvals)
new_yvals=[]
for i in range(0,len(yvals)):
    new_yvals.append(round(yvals[i],3))

plt.plot(xdata, new_yvals, 's',label='original values')
plt.show()
result = zip(xdata,new_yvals)

yy = pd.DataFrame(result)
writer = pd.ExcelWriter('interpolate4.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()





#newfunc = interpolate.interp2d(x, y, fvals, kind='cubic') 




#def func(x, y): 
#    return (x+y)*np.exp(-5.0*(x**2 + y**2)) 
#
## X-Y轴分为15*15的网格 
#y,x= np.mgrid[-1:1:15j, -1:1:15j] 
#
#fvals = func(x,y) # 计算每个网格点上的函数值 15*15的值 
#print(len(fvals[0])) 
#
#print(fvals)
#
##三次样条二维插值 
#newfunc = interpolate.interp2d(x, y, fvals, kind='cubic') 
#
## 计算100*100的网格上的插值 
#xnew = np.linspace(-1,1,100)#x 
#ynew = np.linspace(-1,1,100)#y 
#fnew = newfunc(xnew, ynew)#仅仅是y值 100*100的值 
#
## 绘图 
## 为了更明显地比较插值前后的区别，使用关键字参数interpolation='nearest' 
## 关闭imshow()内置的插值运算。 
#pl.subplot(121) 
#im1=pl.imshow(fvals, extent=[-1,1,-1,1], cmap=mpl.cm.hot, interpolation='nearest', origin="lower")#pl.cm.jet 
##extent=[-1,1,-1,1]为x,y范围 favals为 
#pl.colorbar(im1) 
#
#pl.subplot(122) 
#im2=pl.imshow(fnew, extent=[-1,1,-1,1], cmap=mpl.cm.hot, interpolation='nearest', origin="lower") 
#pl.colorbar(im2) 
#
#pl.show()


## 准备数据
#min_x = -50
#max_x = 50
#x = np.linspace(min_x, max_x, 17)
#y = np.sinc(x)
#
## 绘制数据
#plt.grid(linestyle=":")
#plt.scatter(x, y, s=60, color="dodgerblue",
#           marker="o", label="samples")
#
## 通过样本点 ==>  插值函数(线性)
#linear = interpolate.interp1d(x, y, kind="linear")
#
#linear_x = np.linspace(min_x, max_x, 1000)
#linear_y = linear(linear_x)
#plt.plot(linear_x, linear_y, color="g",
#        label="linear interp1d")
#
## 通过样本点 ==>  插值函数(三次样条)
#cubic = interpolate.interp1d(x, y, kind="cubic")
#
#cubic_y = cubic(linear_x)
#plt.plot(linear_x, cubic_y, color="r",
#        label="cubic interp1d")
#
#plt.legend()
#plt.show()




