# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 14:18:36 2026

@author: sumin
"""

"""
from random import randint

class c:
    def __init__(self):
        self.a=int(input("정수(1~100): "))
        self.b=int(input("정수(1~100): "))
        self.lst=[]
    def f(self):
        for _ in range(10):
            self.lst.append(randint(self.a, self.b))
        print(self.lst)
            
x=c()
x.f()
"""

"""
class Cal:
    def __init__(self):
        self.n1=int(input("정수: "))
        self.op=input("기호: ")
        self.n2=int(input("정수: "))
    def f(self):
        if self.op=="+":
            print(self.n1+self.n2)
        elif self.op=="-":
            print(self.n1-self.n2)
        elif self.op=="*":
            print(self.n1*self.n2)
        elif self.op=="/":
            print(self.n1//self.n2)

a=Cal()
a.f()
"""

from random import randint

class c:
    def __init__(self):
        self.d=[randint(1, 100) for _ in range(5)]
    def f(self):
        menu=-1
        while menu!=0:
            menu=int(input("추가: 1, 삭제: 2, 검색: 3, 출력: 4, 종료: 0"))
            if menu==1:
                self.d.append(randint(1, 100))
            elif menu==2:
                idx=int(input("인덱스: "))
                self.d.pop(idx)
            elif menu==3:
                val=int(input("값: "))
                if val in self.d:
                    print(self.d.index(val), val)
                else:
                    print("없음")
            elif menu==4:
                print(self.d)

a=c()
a.f()