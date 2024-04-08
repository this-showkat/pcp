# -*- coding: utf-8 -*-


x1 = int(input())
x2 = int(input())
a = x1 if x1<x2 else x2
b = x2 if x1<x2 else x1
for i in range(a+1, b):
    if i%5==2 or i%5==3:
        print(i)
