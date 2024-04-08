# -*- coding: utf-8 -*-

x = int(input())
while x!=0:
    sum = 0
    if x%2==1:
        x += 1
    for i in range(5):
        sum += x
        x += 2
    print(sum)
    x = int(input())

