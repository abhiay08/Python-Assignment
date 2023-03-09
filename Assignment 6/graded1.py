# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:21:26 2023

@author: HP
"""
'''
6.B.1: ASSIGNMENT '''

def jump_game(arr):
    n = len(arr)   
    dp = [float('inf') for _ in range(n)]
    dp[0] = 0
    for i in range(n):
        for j in range(1, arr[i]+1):
            if i+j < n:
                dp[i+j] = min(dp[i+j], dp[i]+1)
    print("Jumps required in Minimum number : ",dp[-1])
    return dp[-1]
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
jump_game(arr)