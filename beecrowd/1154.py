# -*- coding: utf-8 -*-

n = int(input())
sums = counter = 0
while n>=0:
    counter += 1
    sums += n
    n = int(input())
print("%.2f" %(sums/counter))

