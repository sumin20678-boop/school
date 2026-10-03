# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 14:11:29 2026

@author: sumin
"""

"""
from random import randint

def f1():
    for _ in range(10):
        d1.append(randint(0, 1))
    
def f2():
    for _ in range(10):
        d2.append(randint(0, 1))
    
def f3():
    
    count=0
    for i in range(10):
        if d1[i]==d2[i]:
            count+=10
    print(count, "%")
    
d1=[]
d2=[]
f1()
print(d1)
f2()
print(d2)
f3()
"""
                                     
"""
from random import randint

def f1():
    for i in range(10):
        if d1[i]==1:
            d2.append(i)


d1=[randint(0, 1) for _ in range(10)]
d2=[]
f1()
print(d1)
print(d2)
"""

from random import randint

def f():
    length=max_length=idx=0
    for i in range(20):
        if d[i]==1:
            length+=1
            if length>max_length:
                max_length=length
                idx=i-length+1
        else:
            length=0
    print(idx)

d=[randint(0, 1) for _ in range(20)]
print(d)
f()






    
    
    
    
    
    
    
    
    
    