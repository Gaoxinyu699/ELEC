import pandas as pd
# dataFrame导入数据集，添加标签
df = pd.read_csv('F:/File3.txt', names=['id', 'time', 'consumption'], header=None, sep=' ')
sort_df = df.sort_values('id')  # 根据用户id进行排序,1000-1999

for i in range(3,7):
    df = pd.read_csv('F:/File' + str(i) + '.txt', names=['id', 'time', 'consumption'], header=None, sep=' ')
    sort_df = df.sort_values('id')  # 根据用户id进行排序,1000-1999

    sort_df1 = sort_df.iloc[0:1000000]  # 选择1048576条数据1000000
    sort_df2 = sort_df.iloc[1000000:2000000]
    sort_df3 = sort_df.iloc[2000000:3000000]
    sort_df4 = sort_df.iloc[3000000:4000000]
    sort_df5 = sort_df.iloc[4000000:5000000]
    sort_df6 = sort_df.iloc[5000000:6000000]
    sort_df7 = sort_df.iloc[6000000:7000000]
    sort_df8 = sort_df.iloc[7000000:8000000]
    sort_df9 = sort_df.iloc[8000000:9000000]
    sort_df10 = sort_df.iloc[9000000:10000000]
    sort_df11 = sort_df.iloc[10000000:11000000]
    sort_df12 = sort_df.iloc[11000000:12000000]
    sort_df13 = sort_df.iloc[12000000:13000000]
    sort_df14 = sort_df.iloc[13000000:14000000]
    sort_df15 = sort_df.iloc[14000000:15000000]
    sort_df16 = sort_df.iloc[15000000:16000000]
    sort_df17 = sort_df.iloc[16000000:17000000]  # 选择1048576条数据1000000
    sort_df18 = sort_df.iloc[17000000:18000000]
    sort_df19 = sort_df.iloc[18000000:19000000]
    sort_df20 = sort_df.iloc[19000000:20000000]
    sort_df21 = sort_df.iloc[20000000:21000000]
    sort_df22 = sort_df.iloc[21000000:22000000]
    sort_df23 = sort_df.iloc[22000000:23000000]
    sort_df24 = sort_df.iloc[23000000:24000000]
    sort_df25 = sort_df.iloc[24000000:]

# sort_df26 = sort_df.iloc[25000000:26000000] #35436012
# sort_df27 = sort_df.iloc[26000000:27000000]
# sort_df28 = sort_df.iloc[27000000:28000000]
# sort_df29 = sort_df.iloc[28000000:29000000]
# sort_df30 = sort_df.iloc[29000000:30000000]
# sort_df31 = sort_df.iloc[30000000:31000000]
# sort_df32 = sort_df.iloc[31000000:32000000]
# sort_df33 = sort_df.iloc[32000000:33000000]
# sort_df34 = sort_df.iloc[33000000:34000000]
# sort_df35 = sort_df.iloc[34000000:35000000]
# sort_df36 = sort_df.iloc[35000000:]


    sort_df010= sort_df.iloc[900000:1900000]
    sort_df020= sort_df.iloc[1900000:2900000]
    sort_df30 = sort_df.iloc[2900000:3900000]
    sort_df40 = sort_df.iloc[3900000:4900000]
    sort_df50 = sort_df.iloc[4900000:5900000]
    sort_df60 = sort_df.iloc[5900000:6900000]
    sort_df70 = sort_df.iloc[6900000:7900000]
    sort_df80 = sort_df.iloc[7900000:8900000]
    sort_df90 = sort_df.iloc[8900000:9900000]
    sort_df100 = sort_df.iloc[9900000:10900000]
    sort_df110 = sort_df.iloc[10900000:11900000]
    sort_df120 = sort_df.iloc[11900000:12900000]
    sort_df130 = sort_df.iloc[12900000:13900000]
    sort_df140 = sort_df.iloc[13900000:14900000]
    sort_df150 = sort_df.iloc[14900000:15900000]
    sort_df160 = sort_df.iloc[15900000:16900000]
    sort_df170 = sort_df.iloc[16900000:17900000]
    sort_df180 = sort_df.iloc[17900000:18900000]
    sort_df190 = sort_df.iloc[18900000:19900000]
    sort_df200 = sort_df.iloc[19900000:20900000]
    sort_df210 = sort_df.iloc[20900000:21900000]
    sort_df220 = sort_df.iloc[21900000:22900000]
    sort_df230 = sort_df.iloc[22900000:23900000]
    sort_df240 = sort_df.iloc[23900000:24900000]

# sort_df250 = sort_df.iloc[24900000:25200000]
# sort_df260 = sort_df.iloc[25900000:26200000]
# sort_df270 = sort_df.iloc[26900000:27200000]
# sort_df280 = sort_df.iloc[27900000:28200000]
# sort_df290 = sort_df.iloc[28900000:29200000]
# sort_df300 = sort_df.iloc[29900000:30200000]
# sort_df310 = sort_df.iloc[30900000:31200000]
# sort_df320 = sort_df.iloc[31900000:32200000]
# sort_df330 = sort_df.iloc[32900000:33200000]
# sort_df340 = sort_df.iloc[33900000:34200000]
# sort_df350 = sort_df.iloc[34900000:35200000]

    sort_df1.to_excel('F:/File'+ str(i) +'-1.xlsx', encoding='utf_8', index=False)
    sort_df2.to_excel('F:/File'+ str(i) +'-2.xlsx', encoding='utf_8', index=False)
    sort_df3.to_excel('F:/File'+ str(i) +'-3.xlsx', encoding='utf_8', index=False)
    sort_df4.to_excel('F:/File'+ str(i) +'-4.xlsx', encoding='utf_8', index=False)
    sort_df5.to_excel('F:/File'+ str(i) +'-5.xlsx', encoding='utf_8', index=False)
    sort_df6.to_excel('F:/File'+ str(i) +'-6.xlsx', encoding='utf_8', index=False)
    sort_df7.to_excel('F:/File'+ str(i) +'-7.xlsx', encoding='utf_8', index=False)
    sort_df8.to_excel('F:/File'+ str(i) +'-8.xlsx', encoding='utf_8', index=False)
    sort_df9.to_excel('F:/File'+ str(i) +'-9.xlsx', encoding='utf_8', index=False)
    sort_df10.to_excel('F:/File'+ str(i) +'-10.xlsx', encoding='utf_8', index=False)
    sort_df11.to_excel('F:/File'+ str(i) +'-11.xlsx', encoding='utf_8', index=False)
    sort_df12.to_excel('F:/File'+ str(i) +'-12.xlsx', encoding='utf_8', index=False)
    sort_df13.to_excel('F:/File'+ str(i) +'-13.xlsx', encoding='utf_8', index=False)
    sort_df14.to_excel('F:/File'+ str(i) +'-14.xlsx', encoding='utf_8', index=False)
    sort_df15.to_excel('F:/File'+ str(i) +'-15.xlsx', encoding='utf_8', index=False)
    sort_df16.to_excel('F:/File'+ str(i) +'-16.xlsx', encoding='utf_8', index=False)
    sort_df17.to_excel('F:/File'+ str(i) +'-17.xlsx', encoding='utf_8', index=False)
    sort_df18.to_excel('F:/File'+ str(i) +'-18.xlsx', encoding='utf_8', index=False)
    sort_df19.to_excel('F:/File'+ str(i) +'-19.xlsx', encoding='utf_8', index=False)
    sort_df20.to_excel('F:/File'+ str(i) +'-20.xlsx', encoding='utf_8', index=False)
    sort_df21.to_excel('F:/File'+ str(i) +'-21.xlsx', encoding='utf_8', index=False)
    sort_df22.to_excel('F:/File'+ str(i) +'-22.xlsx', encoding='utf_8', index=False)
    sort_df23.to_excel('F:/File'+ str(i) +'-23.xlsx', encoding='utf_8', index=False)
    sort_df24.to_excel('F:/File'+ str(i) +'-24.xlsx', encoding='utf_8', index=False)
    sort_df25.to_excel('F:/File'+ str(i) +'-25.xlsx', encoding='utf_8', index=False)

    sort_df010.to_excel('F:/File'+ str(i) +'-010.xlsx', encoding='utf_8', index=False)
    sort_df020.to_excel('F:/File'+ str(i) +'-020.xlsx', encoding='utf_8', index=False)
    sort_df30.to_excel('F:/File'+ str(i) +'-30.xlsx', encoding='utf_8', index=False)
    sort_df40.to_excel('F:/File'+ str(i) +'-40.xlsx', encoding='utf_8', index=False)
    sort_df50.to_excel('F:/File'+ str(i) +'-50.xlsx', encoding='utf_8', index=False)
    sort_df60.to_excel('F:/File'+ str(i) +'-60.xlsx', encoding='utf_8', index=False)
    sort_df70.to_excel('F:/File'+ str(i)+'-70.xlsx', encoding='utf_8', index=False)
    sort_df80.to_excel('F:/File'+ str(i) +'-80.xlsx', encoding='utf_8', index=False)
    sort_df90.to_excel('F:/File'+ str(i) +'-90.xlsx', encoding='utf_8', index=False)
    sort_df100.to_excel('F:/File'+ str(i) +'-100.xlsx', encoding='utf_8', index=False)
    sort_df110.to_excel('F:/File'+ str(i) +'-110.xlsx', encoding='utf_8', index=False)
    sort_df120.to_excel('F:/File'+ str(i) +'-120.xlsx', encoding='utf_8', index=False)
    sort_df130.to_excel('F:/File'+ str(i) +'-130.xlsx', encoding='utf_8', index=False)
    sort_df140.to_excel('F:/File'+ str(i) +'-140.xlsx', encoding='utf_8', index=False)
    sort_df150.to_excel('F:/File'+ str(i) +'-150.xlsx', encoding='utf_8', index=False)
    sort_df160.to_excel('F:/File'+ str(i) +'-160.xlsx', encoding='utf_8', index=False)
    sort_df170.to_excel('F:/File'+ str(i) +'-170.xlsx', encoding='utf_8', index=False)
    sort_df180.to_excel('F:/File'+ str(i) +'-180.xlsx', encoding='utf_8', index=False)
    sort_df190.to_excel('F:/File'+ str(i) +'-190.xlsx', encoding='utf_8', index=False)
    sort_df200.to_excel('F:/File'+ str(i) +'-200.xlsx', encoding='utf_8', index=False)
    sort_df210.to_excel('F:/File'+ str(i) +'-210.xlsx', encoding='utf_8', index=False)
    sort_df220.to_excel('F:/File'+ str(i) +'-220.xlsx', encoding='utf_8', index=False)
    sort_df230.to_excel('F:/File'+ str(i) +'-230.xlsx', encoding='utf_8', index=False)
    sort_df240.to_excel('F:/File'+ str(i) +'-240.xlsx', encoding='utf_8', index=False)


# sort_df26.to_excel('F:/File6-26.xlsx', encoding='utf_8', index=False)
# sort_df27.to_excel('F:/File6-27.xlsx', encoding='utf_8', index=False)
# sort_df28.to_excel('F:/File6-28.xlsx', encoding='utf_8', index=False)
# sort_df29.to_excel('F:/File6-29.xlsx', encoding='utf_8', index=False)
# sort_df30.to_excel('F:/File6-30.xlsx', encoding='utf_8', index=False)
# sort_df31.to_excel('F:/File6-31.xlsx', encoding='utf_8', index=False)
# sort_df32.to_excel('F:/File6-32.xlsx', encoding='utf_8', index=False)

# sort_df010.to_excel('F:/File3-010.xlsx', encoding='utf_8', index=False)
# sort_df020.to_excel('F:/File3-020.xlsx', encoding='utf_8', index=False)
# sort_df30.to_excel('F:/File3-30.xlsx', encoding='utf_8', index=False)
# sort_df40.to_excel('F:/File3-40.xlsx', encoding='utf_8', index=False)
# sort_df50.to_excel('F:/File3-50.xlsx', encoding='utf_8', index=False)
# sort_df60.to_excel('F:/File3-60.xlsx', encoding='utf_8', index=False)
# sort_df70.to_excel('F:/File3-70.xlsx', encoding='utf_8', index=False)
# sort_df80.to_excel('F:/File3-80.xlsx', encoding='utf_8', index=False)
# sort_df90.to_excel('F:/File3-90.xlsx', encoding='utf_8', index=False)
# sort_df100.to_excel('F:/File3-100.xlsx', encoding='utf_8', index=False)
# sort_df110.to_excel('F:/File3-110.xlsx', encoding='utf_8', index=False)
# sort_df120.to_excel('F:/File3-120.xlsx', encoding='utf_8', index=False)
# sort_df130.to_excel('F:/File3-130.xlsx', encoding='utf_8', index=False)
# sort_df140.to_excel('F:/File3-140.xlsx', encoding='utf_8', index=False)
# sort_df150.to_excel('F:/File3-150.xlsx', encoding='utf_8', index=False)
# sort_df160.to_excel('F:/File3-160.xlsx', encoding='utf_8', index=False)
# sort_df170.to_excel('F:/File3-170.xlsx', encoding='utf_8', index=False)
# sort_df180.to_excel('F:/File3-180.xlsx', encoding='utf_8', index=False)
# sort_df190.to_excel('F:/File3-190.xlsx', encoding='utf_8', index=False)
# sort_df200.to_excel('F:/File3-200.xlsx', encoding='utf_8', index=False)
# sort_df210.to_excel('F:/File3-210.xlsx', encoding='utf_8', index=False)
# sort_df220.to_excel('F:/File3-220.xlsx', encoding='utf_8', index=False)
# sort_df230.to_excel('F:/File3-230.xlsx', encoding='utf_8', index=False)
# sort_df240.to_excel('F:/File3-240.xlsx', encoding='utf_8', index=False)
# sort_df250.to_excel('F:/File6-250.xlsx', encoding='utf_8', index=False)
# sort_df260.to_excel('F:/File6-260.xlsx', encoding='utf_8', index=False)
# sort_df270.to_excel('F:/File6-270.xlsx', encoding='utf_8', index=False)
# sort_df280.to_excel('F:/File6-280.xlsx', encoding='utf_8', index=False)
# sort_df290.to_excel('F:/File6-290.xlsx', encoding='utf_8', index=False)
# sort_df300.to_excel('F:/File6-300.xlsx', encoding='utf_8', index=False)
# sort_df310.to_excel('F:/File6-310.xlsx', encoding='utf_8', index=False)
# sort_df320.to_excel('F:/File6-320.xlsx', encoding='utf_8', index=False)
# sort_df330.to_excel('F:/File6-330.xlsx', encoding='utf_8', index=False)
# sort_df340.to_excel('F:/File6-340.xlsx', encoding='utf_8', index=False)
# sort_df350.to_excel('F:/File6-350.xlsx', encoding='utf_8', index=False)