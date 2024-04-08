# -*- coding: utf-8 -*-

n = int(input())
while n>0:
    a, b = [int(i) for i in input().split()]
    sum = 0
    if a%2==0:
        a += 1
    while b>0:
       sum += a
       a += 2
       b -= 1
    print(sum)
    n -= 1
