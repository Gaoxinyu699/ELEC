import numpy as np
import pandas as pd

df = pd.read_excel('2470.xlsx',engine='openpyxl')
user_id = df['id']
power = df['consumption']
diff = df['rmse']

df = df.sample(frac=1.0) 

test = df.iloc[0:200]

train = df.iloc[200:2470]

user_id_list = []
mean_consumption_list = []
mse_list = []

# user_id_list=train['id']
# mean_consumption_list=train['consumption']
# mse_list = train['rmse']

user_id_list=test['id']
mean_consumption_list=test['consumption']
mse_list = test['rmse']

result = zip(user_id_list,mean_consumption_list,mse_list)
print(result)
yy = pd.DataFrame(result)
writer = pd.ExcelWriter('2470_test.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()