# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 16:22:26 2016

@author: hasee
"""

import pandas as pd
import numpy as np
df = pd.read_excel('010.xlsx')
#df.head()
df['A+'] = df['A']+df['B']+df['C']+df['D']
sum_row=df[['A','B','C','D','A+'].sum()
print sum_row
df_sum = pd.DataFrame(data = sum_row).T
print df_sum
df_sum=df_sum.reindex(columns=df.columns)
print df_sum