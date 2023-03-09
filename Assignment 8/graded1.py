# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 19:25:37 2023

@author: HP
"""
import numpy as np
arr=np.array([
    [4,5,6],[1,2,3],[7,8,9]
    ])
result=np.max(arr,axis=0)- np.min(arr,axis=0)
print(result)
#
min_value=np.min(arr,axis=0)
max_value=np.max(arr,axis=0)

difference=max_value-min_value
print("The Difference between min_value and max_value is: ", difference)