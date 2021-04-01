# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 15:53:50 2021

@author: Adm
"""
from numpy import *
import numpy as np
import pandas as pd
import random
import operator
import math

#def loadData(filename,k1,k2,k3,k4,k5):
#    '''
#    :param k: 随机抽取K条记录，对电表的用电量进行恶意处理
#    '''
#    dataMat = []; labelMat = []
#    fr = open(filename)
#    for line in fr.readlines():
#        lineArr = line.strip().split()
#        dataMat.append([int(lineArr[0]), int(lineArr[1]), float(lineArr[2]), float(lineArr[3]),float(lineArr[4])])
#        labelMat.append(0)
#    list1 = random.sample(dataMat, k1)
#
#    # h1(xt) = αxt, α = random(0.1, 0.8); 通过生成0.1到0.8之间的随机数乘上每条用电量数据作为不诚实的用户用电量
#    index1 = 0
#    t = random.randint(1, 8) / 10
#    for item in dataMat:
#        if item in list1:
#            item[2] = round((item[2] * t), 3)
#            item[3] = round( item[2] ** 2, 3)
#            labelMat[index1] = 1
#        index1 += 1
#
#    return dataMat,labelMat

def fun1(value,t):
    result = round((value * t), 3)
    return result

def fun2(value):
    t = random.randint(1, 8) / 10
    result = round((value * t), 3)
    return result
    
def fun3(average3):
    t = random.randint(1, 8) / 10
    result = round((average3 * t),3)
    return result

def fun4(t,average4):
    result = round((average4 * t),3)
    return result

df = pd.read_excel('C:/Users/Adm/Desktop/electricitry/bad_sample/all_user.xlsx',encoding='utf-8')
id = df['userId']
consumption = df['consumption']
consumption = np.array(consumption)
#print(consumption[0:365])
#print(consumption[1*365:365*2])

all_result = []

for k in range(0,148):
    print(k)
    #print(i*365)
    #print((i+1)*365)
    user_consumption = consumption[k*365:(k+1)*365]
    print(user_consumption)
#time = df['time']
#date = df['date']
#tempearture = df['tempearture']
#humidity = df['humidity']
#print(consumption)
#h1(xt) = αxt, α = random(0.1, 0.8); 通过生成0.1到0.8之间的随机数乘上每条用电量数据作为不诚实的用户用电量
#index1 = 0
#t = random.randint(1, 8) / 10
#for item in dataMat:
#    if item in list1:
#        item[2] = round((item[2] * t), 3)
#        item[3] = round( item[2] ** 2, 3)
#        labelMat[index1] = 1
#    index1 += 1



    consumption1 = user_consumption[0:73]
    consumption2 = user_consumption[73:146]
    consumption3 = user_consumption[146:219]
    average3 = np.average(consumption3)
    consumption4 = user_consumption[219:292]
    average4 = np.average(consumption4)
    consumption5 = user_consumption[292:365]
    
    



    t = random.randint(1, 8) / 10
    result1 = []
    for i in range(0,len(consumption1)):
        temp = fun1(consumption1[i],t)
        result1.append(temp)
    #print(result1)
    
    result2 = []
    for i in range(0,len(consumption2)):
        temp = fun2(consumption2[i])
        result2.append(temp)
    #print(result2)
    
    result3 = []
    for i in range(0,len(consumption3)):
        temp = fun3(average3)
        result3.append(temp)
    #print(result3)
    
    result4 = []
    for i in range(0,len(consumption4)):
        temp = fun4(t,average4)
        result4.append(temp)
    #print(result4)
    
    result5 = []
    for i in range(len(consumption5)-1,-1,-1):
        temp = consumption5[i]
        result5.append(temp)
    #print(result5)
    temp = []
    temp = result1+result2+result3+result4+result5
    print(temp)
    all_result = all_result + temp
#
#print(result)
#print(max(result))
#
#print(len(result))
#
yy = pd.DataFrame(all_result)

writer = pd.ExcelWriter('bad_result.xlsx')

yy.to_excel(writer,'Sheet1')

writer.save()



#print(consumption)

#print(np.average(consumption))

#res = []
#sign = []
#t = random.randint(1, 8) / 10
#for i in range(0,len(consumption)):
#    #res.append(round((consumption[i] * t), 3)
#    a = round((consumption[i] * t), 3)
#    res.append(a)
#    sign.append(1)
#
##print(sign)
#
#result = zip(res,sign)
#
#yy = pd.DataFrame(result)
#
#writer = pd.ExcelWriter('result.xlsx')
#
#yy.to_excel(writer,'Sheet1')
#
#writer.save()



