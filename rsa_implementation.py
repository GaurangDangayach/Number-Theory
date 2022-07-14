# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 15:11:20 2022

@author: lenovo
"""

import random

def inv_mod(a,p):
    p0 = p
    y = 0
    x = 1
    if (p == 1):
        return 0
 
    while (a > 1):
        q = a//p
        t = p
        p = a%p
        a = t
        t = y
        y = x-q*y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + p0
    return x
        

def swap(a,b):
    return b,a

def gcd(a,b):
    if b>a:
        a,b=swap(a,b)
    if b==0:
        return a
    return gcd(b,a%b)

def prime_test(x):
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

def random_primes():
    a=random.randint(100001,999997)
    while (not (prime(a))):
        a=random.randint(100001,999997)
    b=random.randint(100001,999997)
    while (not (prime(b))):
        b=random.randint(100001,999997)
    return a,b

a,b=random_primes()
p=a*b
pp=(a-1)*(b-1)
e=random.randint(2,pp-1)
while (gcd(e,pp)!=1):
    e=random.randint(2,pp-1)
d=inv_mod(e,pp)
if e>d:
    e,d=swap(e,d)
print(p,e,d)
