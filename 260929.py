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
for i in d1:
    x=i[0]
    n1.append(x)
    
global n1=[i[0] for i in d1]
"""
from random import randint

def f():
    n3=[(x, y) for x, y in zip(n1, n2)]
    print(n3)

n1=(randint(1, 100) for _ in range(3)) #1~100 3개
n2=(randint(1, 100) for _ in range(3))
f()


















    
    
    
    
    
    
    
    
    
    