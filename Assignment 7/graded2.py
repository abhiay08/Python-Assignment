# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:50:57 2023

@author: HP
"""

# Assignment 7 que 2

import re
regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
def isValid(email):
    if re.fullmatch(regex, email):
      print("Given Email is valid Email")
    else:
      print("Given Email is Invalid Email")

isValid("name.surname@gmail.com")
isValid("anonymous123@yahoo.co.uk")
isValid("anonymous123@...uk")
isValid("...@domain.us")
                  