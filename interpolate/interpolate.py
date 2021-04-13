# -*- coding: utf-8 -*-
"""
Created on Fri Apr  13 11:20:19 2021

@author: Adm
"""
import torch
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import torch.nn.functional as F


df = pd.read_excel('C:/Users/Adm/Desktop/electricitry/interpolate/第一类.xlsx',sheet_name='Sheet1')
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

#rmse= torch.Tensor(rmse)
print(rmse)
print(rmse.shape)

x = torch.randn([1, 2, 64, 64])

#print(x)

rmse = list(rmse)
consumption = list(consumption)
print(consumption)


result = list(zip(rmse,consumption))


print(result)

result= torch.Tensor(result)

y1 = F.interpolate(result, size=[16,16],mode="linear")
# print(y1)







#y1 = F.interpolate(rmse, size=[32, 32])

# x = torch.randn([1, 3, 64, 64])
# y0 = F.interpolate(x, scale_factor=0.5)
# y1 = F.interpolate(x, size=[32, 32])

# y2 = F.interpolate(x, size=[128, 128], mode="bilinear")

# print(x)
# print(y0)
# print(y1)
# print(y2)
