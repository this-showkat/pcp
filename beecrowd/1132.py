# -*- coding: utf-8 -*-

x1 = int(input())
x2 = int(input())
a = x1 if x1<x2 else x2
b = x2 if x1<x2 else x1
sum = 0
for i in range(a, b+1):
    if i%13!=0:
        sum += i

print(sum)
