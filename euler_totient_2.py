# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:09:42 2022

@author: lenovo
"""

def gcd(a,b):
    if b>a :
        i=b
        b=a
        a=i
    while (b!=0):
        rem=a%b
        a=b
        b=rem
    return a

def utf(n):
    count=0
    for i in range(1,n+1):
        if gcd(i,n)==1:
            count=count+1
    return count

n=int(input())
for i in range(n):
    print(i+1,":",utf(i+1))