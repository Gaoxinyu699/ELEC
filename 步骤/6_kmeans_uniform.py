import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

df = pd.read_excel('2000.xlsx',sheet_name='Sheet1')
#print(df)
user_id = df['id']
power = df['power']
diff = df['diff']
power = np.array(power)
diff = np.array(diff)
result = zip(power,diff)

res = []
for i in range(0,len(power)):
    temp = []
    temp.append(power[i])
    temp.append(diff[i])
    res.append(temp)
#print(res)
res=np.array(res)
# plt.plot(power,diff,'r.')
# plt.show()

# res_list = []
# for i in range(10,11):
#    kmeans_model = KMeans(n_clusters=i, random_state=1).fit(res)
#    #kmeans_model = KMeans(n_clusters=3, random_state=1).fit_predict(res)
#    #plt.scatter(res[:, 0], res[:, 1], c=kmeans_model)
#    #plt.show()
#    labels = kmeans_model.labels_
#
#    print(labels)
#    x = metrics.silhouette_score(res, labels, metric="euclidean")
#    print(x)
#    res_list.append(x)
# print(res_list)

kmeans_model = KMeans(n_clusters=15, random_state=1).fit(res)
labels = kmeans_model.labels_
diff = pd.DataFrame(diff,columns=['diff_15'])
power = pd.DataFrame(power,columns=['power_15'])
labels = pd.DataFrame(labels,columns=['labels'])
# print(labels)
# print(diff)

diff.insert(1,'power',power)
diff.insert(2,'labels',labels)

# print(res)


tsne = TSNE()
a = tsne.fit_transform(diff)
#print(a)
result = pd.DataFrame(a,index=diff.index)
result.insert(2,'2',user_id)

d1 = result[diff['labels']==0]
#plt.plot(d1[0],d1[1],'r.')
#print(d1)
d2 = result[diff['labels']==1]
#plt.plot(d2[0],d2[1],'go')
d3 = result[diff['labels']==2]
#plt.plot(d3[0],d3[1],'b*')
d4 = result[diff['labels']==3]
d5 = result[diff['labels']==4]
d6 = result[diff['labels']==5]
d7 = result[diff['labels']==6]
d8 = result[diff['labels']==7]
d9 = result[diff['labels']==8]
d10 = result[diff['labels']==9]
d11 = result[diff['labels']==10]
d12 = result[diff['labels']==11]
d13 = result[diff['labels']==12]
d14 = result[diff['labels']==13]
d15 = result[diff['labels']==14]
d16 = result[diff['labels']==15]
d17 = result[diff['labels']==16]
d18 = result[diff['labels']==17]
d19 = result[diff['labels']==18]
d20 = result[diff['labels']==19]

# plt.plot(d1[0],d1[1],'r.',d2[0],d2[1],'g.',d3[0],d3[1],'b.',d4[0],d4[1],'k.')
# plt.show()
# sum = 0
#
# print('red:')
# print(len(list(d1['2'])))
# print(list(d1['2']))
#
# sum += len(list(d1['2']))
#
# print('green:')
# print(len(list(d2['2'])))
# print(list(d2['2']))
#
# sum += len(list(d2['2']))
#
# print('blue:')
# print(len(list(d3['2'])))
# print(list(d3['2']))
#
# sum += len(list(d3['2']))
#
# print('black:')
# print(len(list(d4['2'])))
# print(list(d4['2']))
#
# sum += len(list(d4['2']))
#
# print('yellow:')
# print(len(list(d5['2'])))
# print(list(d5['2']))
# sum += len(list(d5['2']))
#
# print('c:')
# print(len(list(d6['2'])))
# print(list(d6['2']))
# sum += len(list(d6['2']))
#
# print('m:')
# print(len(list(d7['2'])))
# print(list(d7['2']))
# sum += len(list(d7['2']))
#
# print('pink:')
# print(len(list(d8['2'])))
# print(list(d8['2']))
# sum += len(list(d8['2']))
#
# print('brown:')
# print(len(list(d9['2'])))
# print(list(d9['2']))
# sum += len(list(d9['2']))
#
# print('purple:')
# print(len(list(d10['2'])))
# print(list(d10['2']))
# sum += len(list(d10['2']))
#
# print('cyan:')
# print(len(list(d11['2'])))
# print(list(d11['2']))
# sum += len(list(d11['2']))
#
# print('coral:')
# print(len(list(d12['2'])))
# print(list(d12['2']))
# sum += len(list(d12['2']))
#
# print('chocolate:')
# print(len(list(d13['2'])))
# print(list(d13['2']))
# sum += len(list(d13['2']))
#
# print('beige:')
# print(len(list(d14['2'])))
# print(list(d14['2']))
# sum += len(list(d14['2']))
#
# print('blueviolet:')
# print(len(list(d15['2'])))
# print(list(d15['2']))
# sum += len(list(d15['2']))
#
# print('antiquewhite: ')
# print(len(list(d16['2'])))
# print(list(d16['2']))
# sum += len(list(d16['2']))
#
# print('burlywood:')
# print(len(list(d17['2'])))
# print(list(d17['2']))
# sum += len(list(d17['2']))
#
# print('crimson:')
# print(len(list(d18['2'])))
# print(list(d18['2']))
# sum += len(list(d18['2']))
#
# print('cornsilk:')
# print(len(list(d19['2'])))
# print(list(d19['2']))
#
# sum += len(list(d19['2']))
# print('blanchedalmond:')
# print(len(list(d20['2'])))
# print(list(d20['2']))
# sum += len(list(d20['2']))
#
# print(sum)
# #print(d1)
# plt.plot(d1[0],d1[1],'r.',d2[0],d2[1],'g.',d3[0],d3[1],'b.',d4[0],d4[1],'k.',d5[0],d5[1],'y.',d6[0],d6[1],'c.',d7[0],d7[1],'m.',d8[0],d8[1],'pink',d9[0],d9[1],'brown',d10[0],d10[1],'purple',d11[0],d11[1],'cyan',d12[0],d12[1],'coral',d13[0],d13[1],'chocolate',d14[0],d14[1],'beige',d15[0],d15[1],'blueviolet',d16[0],d16[1],'antiquewhite',d17[0],d17[1],'burlywood',d18[0],d18[1],'crimson',d19[0],d19[1],'cornsilk',d20[0],d20[1],'blanchedalmond')
# plt.show()

res1 = list(d7['2'])
res3 = res1
user_id_list = []
mean_consumption_list = []
mse_list = []
for i in range(0,len(df)):
   if df['id'][i] in res3:
#        new_df.insert(0,'userId',df['userId'][i])
#        new_df.insert(1,'mean_consumption',df['mean_consumption'][i])
#        new_df.insert(2,'mse',df['mse'][i])
#        new_df.insert(3,'Power',df['Power'][i])
#        new_df.insert(4,'Diff',df['Diff'][i])
       user_id_list.append(df['id'][i])
       mean_consumption_list.append(df['mean_consumption'][i])
       mse_list.append(df['rmse'][i])
       print(df['id'][i])
       print(df['mean_consumption'][i])
       print(df['rmse'][i])
result = zip(user_id_list,mean_consumption_list,mse_list)
print(result)
yy = pd.DataFrame(result)
writer = pd.ExcelWriter('221.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()