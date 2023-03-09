# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:12:30 2023

@author: HP
"""

# 6.B.2: ASSIGNMENT
# Assignment 6 que 2

def groupAnagram(strs):
    anagram={}
    for s in strs:
        sorted_s=''.join(sorted(s))
        if sorted_s in anagram:
            anagram[sorted_s].append(s)
        else:
            anagram[sorted_s]=[s]
        return list(anagram.values())
    
strs=[['eat', 'ate', 'tea'], ['tan', 'nat'], ['bat']]
print(groupAnagram)