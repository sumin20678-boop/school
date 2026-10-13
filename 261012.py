# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 16:12:44 2026

@author: sumin
"""
"""
from random import randint

class c:
    #생성자 함수, 객체 변수 선언 시 호출
    #self=객체 변수
    def __init__(self):
        self.a=0
        self.b=0
    def main(self):
        self.a=randint(1, 100)
        self.b=randint(1, 100)
        self.f()
    def f(self):
        print(self.a)
        print(self.b)

#객체 변수, instance
cn=c()
cn.main()

from random import randint

class c(self):
    def __init__(self):
        self.a=0
    def main(self):
        self.a=randint(1, 100)
        self.f()
    def f(self):
        print(self.a)
        
cn=c()
cn.main()

class Counter:
    def __init__(self, ini=0):
        self.count=0
    def increment(self):
        self.count+=1

a=Counter(100)
b=Counter()

"""


"""
from random import randint

class Ran:
    def __init__(self):
        self.lst=[randint(1, 100) for _ in range(10)]
    def Pr(self):
        print(self.lst)
a=Ran()
a.Pr()

class Cal:
    def __init__(self):
        self.n1=int(input("첫 번째 정수: "))
        self.n2=int(input("두 번째 정수: "))
        self.Add()
        self.Sub()
        self.Mul()
        self.Div()
    def Add(self):
        print(self.n1+self.n2)
    def Sub(self):
        print(self.n1-self.n2)
    def Mul(self):
        print(self.n1*self.n2)
    def Div(self):
        print(self.n1/self.n2)
b=Cal()
"""
def Cal():
    op=""
    result=int(input("정수: "))
    while op!="=":
        op=input("기호: ")
        if op!="=":
            n=int(input("정수: "))
            if op=="+":
                result+=n
            elif op=="-":
                result-=n
            elif op=="*":
                result*=n
            elif op=="/":
                result/=n
    print(result)
Cal()

























