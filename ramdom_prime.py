# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 11:33:23 2022

@author: lenovo
"""
import random

def prime_test (x):
    r=0
    d=(x-1)
    while (d%2==0):
        d=d//2
        r=r+1
    a=random.randint(2,99)
    y=(a**d)%x
    if y==1 or y==x-1:
        return True
    i=0
    while i<r:
        y = (y*y) % x
        if (y == 1): return False
        if (y == x-1): return True
        i=i+1
    return False
    

def prime(x):
    if (x%2==0 or x%3==0 or x%5==0):
        return False
    else:
        for i in range(5):
            if prime_test(x)==False:
                return False
        return True

a=random.randint(100001,999997)
while (not (prime(a))):
    a=random.randint(100001,999997)
b=random.randint(100001,999997)
while (not (prime(b))):
    b=random.randint(100001,999997)
print(a,b)