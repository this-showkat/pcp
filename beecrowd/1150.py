# -*- coding: utf-8 -*-

a = int(input())
b = int(input())
while a>=b:
    b = int(input())
count = 0
res = a
nt = a
while res <= b:
    res += nt
    nt += 1
    count += 1
print(count+1)
