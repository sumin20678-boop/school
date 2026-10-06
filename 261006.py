# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:48:01 2026

@author: sumin
"""

"""
from random import randint

def f():
    n=1
    cur=randint(1, 100)
    n1[0]=cur
    while n<10:
        x=randint(1, 100)
        if x>cur:
            n1[n]=x
            n+=1
            cur=x
            if x==100:
                n=10
    print(n1)
    
n1=[0]*10
f()
"""

from random import randint

def f():
    for i in d1:
        x=i[0]
        n1.append(x)
    for i in d2:
        x=i[0]
        n2.append(x)
    print(n1)
    print(n2)
    
d1={(randint(1, 100),):randint(1, 100) for _ in range(3)}
d2={(randint(1, 100),):randint(1, 100) for _ in range(3)}
print(d1)
print(d2)
n1=[]
n2=[]
f()

"""
ver.2

for i in d1:
    x=i[0]
    n1.append(x)
    
global n1=[i[0] for i in d1]
"""
from random import randint

def f():
    n3=list(zip(n1, n2))
    print(n3)

n1=(randint(1, 100) for _ in range(3)) #1~100 3개
n2=(randint(1, 100) for _ in range(3))
f()