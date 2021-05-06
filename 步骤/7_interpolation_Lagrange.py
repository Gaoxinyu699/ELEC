# import pandas as pd
# from scipy.interpolate import lagrange
# inputfile = '第三类需差值.xlsx'
# outputfile = 'interpolation.xlsx'
# data = pd.read_excel(inputfile, header=None)
# #自定义列向量插值函数
# #s为列向量，n为被插值的位置，k为取前后的数据个数，默认为5
# def ployinterp_column(s, n, k=5):
#   y = s.reindex(list(range(n - k, n)) + list(range(n + 1, n + 1 + k)))
#   y = y[y.notnull()] #剔除空值
#   return lagrange(y.index, list(y))(n)
# for i in data.columns:
#   for j in range(len(data)):
#     if (data[i].isnull())[j]: #如果为空即插值。
#           data[i][j] = ployinterp_column(data[i], j)
#           print(data)
# data.to_excel(outputfile, header=None, index=False) #输出结果


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

df = pd.read_excel('221.xlsx',sheet_name='Sheet1')
#print(df)
user_id = df['id']
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

#多项式插值
xdata = np.arange(25.923,77.566,0.25)
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
writer = pd.ExcelWriter('polyfit_interpolate.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()

