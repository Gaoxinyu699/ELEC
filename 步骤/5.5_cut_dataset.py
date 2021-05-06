import numpy as np
import pandas as pd

df = pd.read_excel('diff_power_uniform.xlsx',engine='openpyxl')
print(df)
df = df.sample(n=2000)
print(df)
yy = pd.DataFrame(df)
writer = pd.ExcelWriter('2000.xlsx')
yy.to_excel(writer,'Sheet1')
writer.save()
