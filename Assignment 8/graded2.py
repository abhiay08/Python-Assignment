# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 17:41:20 2023

@author: HP
"""

import pandas as pd
import numpy as np
year=int(input("Enter a Year: "))
date_range=pd.date_range(start='{}-01-01'.format(year),end='{}-12-31'.format(year))
ts=pd.Series(np.random.randn(len(date_range)), index=date_range)
last_working_day=ts.resample('M').last().index.strftime('%Y-%m-%d') .tolist()
print("In A Year The Last Working Day of Each Month is Given Below: ",format(year))
print(last_working_day)                        