# -*- coding: utf-8 -*-

n = int(input())
if n>0 and n<13:
    res = 1
    for i in range(2, n+1):
        res *= i
    print(res)
