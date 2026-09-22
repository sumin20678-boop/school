# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 19:54:37 2026

@author: sumin
"""
#0922

from random import randint

def even(n):
    en.append(n)
def odd(n):
    od.append(n)

lst=[randint(1, 15) for _ in range(10)]
print(lst)
en=[]
od=[]
for i in lst:
    if i%2==0:
        even(i)
    else:
        odd(i)
print(en)
print(od)



"""
from random import randint

def dic():
    key=tuple(randint(0, 1) for _ in range(4))
    d={key:randint(1, 15) for _ in range(5)}
    print(d)
    
for _ in range(5):
    dic()
"""
from random import randint

def dic():
    d={tuple(randint(0, 1) for _ in range(4)):randint(1, 15) for _ in range(5)}
    print(d)
    
for _ in range(5):
    dic()



import random

def Ran():
    return random.sample("00001111", 4)

for _ in range(5):
    print(Ran())
