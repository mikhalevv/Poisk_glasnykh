# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 17:52:27 2018

@author: mihalev
"""

s = str(input())
y = list(s)
z = s.count('a') + s.count('e') + s.count('i') + s.count('o') + s.count('u') + s.count('y')
print('Number of vowels: ' + str(z))
  