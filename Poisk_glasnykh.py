# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 12:23:14 2018

@author: mihalev
"""
s=input()
vowels = 0
for i in s:
    letter = i.lower()
    if letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u" or letter == "y":
        vowels +=1
print('Number of vowels: ' + str(vowels))

    
    