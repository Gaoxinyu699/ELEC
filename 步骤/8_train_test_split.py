import torch  # 导入模块
import torch.utils.data as Data
import pandas as pd
import numpy as np

BATCH_SIZE = 5315  # 每一批的数据量

# x=torch.linspace(1,10,10)          # 定义X为 1 到 10 等距离大小的数
# print(x)
# y=torch.linspace(10,1,10)
# print(type(y))

df = pd.read_excel('5915.xlsx', sheet_name='Sheet1')
user_id = df['id']
user_id = np.array(user_id)
consumption = df['consumption']
consumption = np.array(consumption)
rmse = df['rmse']
rmse = np.array(rmse)
# label = df['label']
# label = np.array(label)

user_id = torch.Tensor(user_id)
consumption = torch.Tensor(consumption)
rmse = torch.Tensor(rmse)
# label = torch.Tensor(label)

# 转换成torch能识别的Dataset
# 这个可以自定义DataSet：https://www.cnblogs.com/douzujun/p/13429912.html
torch_dataset = Data.TensorDataset(user_id, consumption, rmse)  # 将数据放入 torch_dataset

loader = Data.DataLoader(
    dataset=torch_dataset,  # 将数据放入loader
    batch_size=BATCH_SIZE,  # 每个数据段大小为  BATCH_SIZE=5
    shuffle=True,  # 是否打乱数据的排布
    num_workers=0  # 使用多进程加载的进程数，0代表不使用多进程
)

# for epoch in range(3):

#    for step, (batch_x,batch_y,batch_z,batch_w) in enumerate(loader):

#        print('epoch',epoch,'|step:',step," | userId",batch_x.numpy())

# '| consumption:',batch_y.numpy()," | rmse",batch_z.numpy()," | label",batch_w.numpy())

for step, (batch_x, batch_y, batch_z) in enumerate(loader):
    # print('|step:',step," | userId",batch_x.numpy())
    if step == 0:
        train_id_list = batch_x.numpy()
        train_consumption_list = batch_y.numpy()
        train_rmse_list = batch_z.numpy()
        # train_label_list = batch_w.numpy()
    elif step == 1:
        test_id_list = batch_x.numpy()
        test_consumption_list = batch_y.numpy()
        test_rmse_list = batch_z.numpy()
        # test_label_list = batch_w.numpy()

print(len(train_id_list))
print(len(test_id_list))

# train_result = zip(train_id_list, train_consumption_list, train_rmse_list, train_label_list)
train_result = zip(train_id_list, train_consumption_list, train_rmse_list)
yy = pd.DataFrame(train_result)
writer = pd.ExcelWriter('Train.xlsx')
yy.to_excel(writer, 'Sheet1')
writer.save()

test_result = zip(test_id_list, test_consumption_list, test_rmse_list)
yy = pd.DataFrame(test_result)
writer = pd.ExcelWriter('Test.xlsx')
yy.to_excel(writer, 'Sheet1')
writer.save()