# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 16:17:22 2021

@author: Adm
"""


import numpy as np
import pandas as pd
nums = np.zeros(256)
#第一类 80%
#nums[:205] = 1
#第二类 0%
#
#第三类 50%
nums[:128] = 1
#第四类 20%
#nums[:51] = 1
np.random.shuffle(nums)
print(nums)
yy = pd.DataFrame(nums)
writer = pd.ExcelWriter('label3.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()