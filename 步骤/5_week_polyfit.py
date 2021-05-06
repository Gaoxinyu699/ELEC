import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#均方误差
def MSE(y, t, n):
    return 1 / n * np.sum((y - t)**2)

def RMSE(y, t, n):
    return pow((1 / n * np.sum((y - t)**2)), 0.5)

df = pd.read_excel('excel/编号1000起_user_weekmean.xlsx',engine='openpyxl')

user_id = df['id']
consumption = df['consumption']
consumption = np.array(consumption)

mean_consumption_list = []
rmse_list = []
for i in range(0,2751):

    ydata = consumption[i*52:(i+1)*52-12]
    
    #print(ydata)
    
    #print(np.mean(ydata))
    
    mean = np.mean(ydata)
    
    mean = round(mean,3)
    
    mean_consumption_list.append(mean)
    
    xdata = range(0,40)
    
    xdata_predict = range(0,42)
    
    f = np.polyfit(xdata, ydata, 4)
    #print('f1 is :\n',f1)
    p = np.poly1d(f)
    #print('p1 is :\n',p1)
    #也可使用yvals=np.polyval(f1, x)
    yvals = p(xdata_predict)
    
    #拟合y值
    #print('yvals is :\n')
    print(yvals[-2:])
#    if i == 0:
#        print(consumption[40:42])
#    else:
#        print(consumption[i*52-12:i*52-10])
        
    if i == 0:
        print(consumption[40:42])
        rmse = RMSE(yvals[-2:],consumption[40:42],2)
    else:
        print(consumption[i*52-12:i*52-10])
        rmse = RMSE(yvals[-2:],consumption[i*52-12:i*52-10],2)
    
    print('rmse is :\n')
    print(rmse)
    
    rmse = round(rmse,3)
    
    rmse_list.append(rmse)
    
    #绘图
    plt.figure()
    plt.plot(xdata, ydata, 's',label='original values')
    plt.plot(xdata_predict, yvals, 'r',label='polyfit values')
    plt.show()

user_id = set(user_id)
user_id = list(user_id)

result = zip(user_id,mean_consumption_list,rmse_list)

yy = pd.DataFrame(result)
writer = pd.ExcelWriter('编号1000起_data_rmse.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()