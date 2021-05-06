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


label0 = torch.zeros(2470)
label1 = torch.ones(1820)
label2 = torch.ones(1000)
label2 *= 2


d = 60
#print(label2)

df1 = pd.read_excel('第一类.xlsx',sheet_name='Sheet1')
df2 = pd.read_excel('第二类.xlsx',sheet_name='Sheet1')
df3 = pd.read_excel('第三类_polyfit.xlsx',sheet_name='Sheet1')

consumption1 = df1['consumption']
# consumption1 = consumption1 + d
consumption2 = df2['consumption']
consumption2 = consumption2 + d
consumption3 = df3['consumption']


rmse1 = df1['rmse']
rmse2 = df2['rmse']
rmse2 = rmse2 + d
rmse3 = df3['rmse']



res1 = []
res2 = []
res3 = []

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

data0 = torch.tensor(res1)
data1 = torch.tensor(res2)
data2 = torch.tensor(res3)

# print(res1)
# print(len(label0))
# print(len(data0))

x = torch.cat((data0, data1, data2), ).type(torch.FloatTensor)
y = torch.cat((label0, label1, label2), ).type(torch.LongTensor)

#print(y.numpy())

# plt.scatter(x.numpy()[:,0], x.numpy()[:,1], c=y.numpy(), s=10, lw=0, cmap='RdYlGn')
# plt.show()

class Net(torch.nn.Module):
    def __init__(self, input_feature, num_hidden, outputs):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(input_feature, num_hidden)
        self.out = torch.nn.Linear(num_hidden, outputs)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.out(x)
        x = F.softmax(x,dim=1)
        return x

CUDA = torch.cuda.is_available()

if CUDA:
    net = Net(input_feature=2, num_hidden=32, outputs=3).cuda()
    inputs = x.cuda()
    target = y.cuda()
    print('CUDA------------------------------------------')
else:
    net = Net(input_feature=2, num_hidden=32, outputs=3).cpu()
    inputs = x
    target = y


optimizer = torch.optim.SGD(net.parameters(), lr=0.02)

criterion = torch.nn.CrossEntropyLoss()

def draw(output):
    if CUDA:
        output = output.cpu()
    plt.cla()
    output = torch.max((output),1)[1]
    pred_y = output.data.numpy().squeeze()
    # print(pred_y)
    target_y = y.numpy()
    plt.scatter(x.numpy()[:, 0], x.numpy()[:, 1], c=pred_y, s=10, lw=0, cmap='RdYlGn')
    accuracy = sum(pred_y == target_y)/5290
    plt.text(1.5, -4, 'Accuracy=%s' % (accuracy), fontdict={'size':20, 'color':'red'})
    plt.pause(0.5)

    fpr, tpr, thresholds = metrics.roc_curve(target_y, pred_y, pos_label=1)
    roc_auc = metrics.auc(fpr, tpr)  #auc为Roc曲线下的面积
    if roc_auc > 0.9:
        # 保存
        torch.save(net, 'model.pkl')
    plt.plot(fpr, tpr, 'b',label='AUC = %0.2f'% roc_auc)
    plt.legend(loc='lower right')
    # plt.plot([0, 1], [0, 1], 'r--')
    plt.xlim([-0.1, 1.1])
    plt.ylim([-0.1, 1.1])
    plt.xlabel('False Positive Rate') #横坐标是fpr
    plt.ylabel('True Positive Rate')  #纵坐标是tpr
    plt.title('Receiver operating characteristic example')
    plt.pause(0.5)

def train(model, criterion, optimizer, epochs):
    for epoch in range(epochs):

        output = model(inputs)
        loss = criterion(output, target)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if epoch % 1000 ==0:
            draw(output)

train(net, criterion, optimizer, 20000)

