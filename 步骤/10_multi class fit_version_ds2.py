import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F
import pandas as pd
from sklearn import metrics

#cluster = torch.ones(500,2)
#data0 = torch.normal(4*cluster, 2)
#data1 = torch.normal(-4*cluster, 1)
#data2 = torch.normal(-8*cluster, 1)

#print(data2)
#print(len(data2))

label0 = torch.zeros(1362)
label1 = torch.ones(952)
label2 = torch.ones(400)
label2 *= 2

label3 = torch.zeros(300)
label4 = torch.ones(300)
label5 = torch.ones(200)
label5 *= 2


d = 60
#print(label2)
#训练集
#C:/Users/Adm/Desktop/ElecP/train/第一类_train.xlsx
df1 = pd.read_excel('ds2/train/第一类_train.xlsx',sheet_name='Sheet1')
df2 = pd.read_excel('ds2/train/第二类_train.xlsx',sheet_name='Sheet1')
df3 = pd.read_excel('ds2/train/第三类_polyfit_train.xlsx',sheet_name='Sheet1')
#测试集
df4 = pd.read_excel('ds2/test/第一类_test.xlsx',sheet_name='Sheet1')
df5 = pd.read_excel('ds2/test/第二类_test.xlsx',sheet_name='Sheet1')
df6 = pd.read_excel('ds2/test/第三类_polyfit_test.xlsx',sheet_name='Sheet1')

consumption1 = df1['consumption']
consumption2 = df2['consumption']
consumption2 = consumption2 + d
consumption3 = df3['consumption']

consumption4 = df4['consumption']
consumption5 = df5['consumption']
consumption5 = consumption5 + d
consumption6 = df6['consumption']


rmse1 = df1['rmse']
rmse2 = df2['rmse']
rmse2 = rmse2 + d
rmse3 = df3['rmse']

rmse4 = df4['rmse']
rmse5 = df5['rmse']
rmse5 = rmse5 + d
rmse6 = df6['rmse']



res1 = []
res2 = []
res3 = []
res4 = []
res5 = []
res6 = []

for i in range(0,len(consumption1)):
    temp1 = []
    temp1.append(consumption1[i])
    temp1.append(rmse1[i])
    res1.append(temp1)

for i in range(0,len(consumption2)):
    temp2 = []
    temp2.append(consumption2[i])
    temp2.append(rmse2[i])
    res2.append(temp2)

for i in range(0, len(consumption3)):
    temp3 = []
    temp3.append(consumption3[i])
    temp3.append(rmse3[i])
    res3.append(temp3)

for i in range(0,len(consumption4)):
    temp4 = []
    temp4.append(consumption1[i])
    temp4.append(rmse4[i])
    res4.append(temp4)
    
for i in range(0,len(consumption5)):
    temp5 = []
    temp5.append(consumption5[i])
    temp5.append(rmse5[i])
    res5.append(temp5)

for i in range(0, len(consumption6)):
    temp6 = []
    temp6.append(consumption6[i])
    temp6.append(rmse6[i])
    res6.append(temp6)

#训练
data0 = torch.tensor(res1)
data1 = torch.tensor(res2)
data2 = torch.tensor(res3)
#测试
data3 = torch.tensor(res4)
data4 = torch.tensor(res5)
data5 = torch.tensor(res6)

# print(res1)
# print(len(label0))
# print(len(data0))

#训练
x_train = torch.cat((data0, data1, data2), ).type(torch.FloatTensor)
y_train = torch.cat((label0, label1, label2), ).type(torch.LongTensor)
#测试
x_test = torch.cat((data3, data4, data5), ).type(torch.FloatTensor)
y_test = torch.cat((label3, label4, label5), ).type(torch.LongTensor)

# plt.scatter(x_train.numpy()[:,0], x_train.numpy()[:,1], c=y_train.numpy(), s=10, lw=0, cmap='RdYlGn')
# plt.show()

class Net(torch.nn.Module):
    def __init__(self, input_feature, num_hidden, outputs):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(input_feature, num_hidden)
        self.out = torch.nn.Linear(num_hidden, outputs)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.out(x)
        x = F.softmax(x)
        return x

CUDA = torch.cuda.is_available()

if CUDA:
    net = Net(input_feature=2, num_hidden=32, outputs=3).cuda()
    #输入训练
    inputs_train = x_train.cuda()
    target_train = y_train.cuda()
    #输入测试
    inputs_test = x_test.cuda()
    target_test = y_test.cuda()
    print('CUDA------------------------------------------')
else:
    net = Net(input_feature=2, num_hidden=20, outputs=3).cpu()
    net = torch.load('ds2/model.pkl')
    #输入训练
    inputs_train = x_train
    target_train = y_train
    #输入测试
    inputs_test = x_test
    target_test = y_test


#画出训练
def draw_train(output):
    if CUDA:
        output = output.cpu()
    plt.cla()
    output = torch.max((output),1)[1]
    # print(output.data.numpy())
    pred_y = output.data.numpy().squeeze()
    # print(pred_y)
    target_y = y_train.numpy()
    plt.scatter(x_train.numpy()[:, 0], x_train.numpy()[:, 1], c=pred_y, s=10, lw=0, cmap='RdYlGn')
    accuracy = sum(pred_y == target_y)/2714
    print('train准确率为：', accuracy)
    plt.text(1.5, -4, 'Train_Accuracy=%s' % (accuracy), fontdict={'size':20, 'color':'red'})
    plt.pause(1)

    fpr, tpr, thresholds = metrics.roc_curve(target_y, pred_y, pos_label=1)
    roc_auc = metrics.auc(fpr, tpr)  #auc为Roc曲线下的面积
    plt.plot(fpr, tpr, 'b',label='AUC = %0.2f'% roc_auc)
    plt.legend(loc='lower right')
    # plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.xlabel('False Positive Rate') #横坐标是fpr
    plt.ylabel('True Positive Rate')  #纵坐标是tpr
    plt.title('train_example')
    plt.pause(1)

    return roc_auc


#画出测试
def draw_test(output):
    if CUDA:
        output = output.cpu()
    plt.cla()
    output = torch.max((output),1)[1]
    pred_y = output.data.numpy().squeeze()
    # print(pred_y)
    target_y = y_test.numpy()
    plt.scatter(x_test.numpy()[:, 0], x_test.numpy()[:, 1], c=pred_y, s=10, lw=0, cmap='RdYlGn')
    accuracy = sum(pred_y == target_y)/800
    print('test准确率为：',accuracy)
    plt.text(1.5, -4, 'Test_Accuracy=%s' % (accuracy), fontdict={'size':20, 'color':'red'})
    plt.pause(1)

    fpr, tpr, thresholds = metrics.roc_curve(target_y, pred_y, pos_label=1)
    roc_auc = metrics.auc(fpr, tpr)  #auc为Roc曲线下的面积
    plt.plot(fpr, tpr, 'b',label='AUC = %0.2f'% roc_auc)
    plt.legend(loc='lower right')
    # plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.xlabel('False Positive Rate') #横坐标是fpr
    plt.ylabel('True Positive Rate')  #纵坐标是tpr
    plt.title('test_example')
    plt.pause(1)

    return roc_auc


#训练
def train(model, criterion, optimizer, epochs):
    print('训练------------------------')
    for epoch in range(epochs):

        output = model(inputs_train)
        loss = criterion(output, target_train)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 4000 ==0:
            auc = draw_train(output)
    return auc

#测试
def test(model):
    print('测试------------------------')
    output = model(inputs_test)
    # loss = criterion(output, target_test)
    auc = draw_test(output)
    return auc

import time
start1 = time.perf_counter()

# for i in range(0,100):
#     print(i)
optimizer = torch.optim.SGD(net.parameters(), lr=0.01)
criterion = torch.nn.CrossEntropyLoss()
auc_train = train(net, criterion, optimizer, 20000)
auc_test = test(net)
print('trainAUC',auc_train)
print('testAUC',auc_test)

end1 = time.perf_counter()
print("final is in : %s Seconds " % (end1 - start1))

if auc_train > 0.8 and auc_test > 0.8:
    # 保存
    torch.save(net, 'ds2/model.pkl')