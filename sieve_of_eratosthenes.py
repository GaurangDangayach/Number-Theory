# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:20:41 2022

@author: lenovo
"""

n=int(input())
nums=list(range(2,n+1))
for i in range(2,n//2+1):
    k=2
    while (i*k<=n):
        if (i*k in nums):
            nums.remove(i*k)
        k=k+1
print(nums)
        