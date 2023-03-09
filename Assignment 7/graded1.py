# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:47:09 2023

@author: HP
"""

# Assignment 7 que 1

def transpose(matrix):
    return [[row [i] for row in matrix] for i in range(len(matrix[0]))]
matrix=[[1,2,3],[4,5,6],[7,8,9]]
result=transpose(matrix)
print(result)