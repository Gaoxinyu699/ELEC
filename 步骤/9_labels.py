import numpy as np
import pandas as pd
nums = np.zeros(2456)
#第一类 50%
# nums[:1285] = 1
0
#第二类 30%
# nums[:300] = 1

#第三类 0%

np.random.shuffle(nums)
print(nums)
yy = pd.DataFrame(nums)
writer = pd.ExcelWriter('label3.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()