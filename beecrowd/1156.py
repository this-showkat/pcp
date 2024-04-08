# -*- coding: utf-8 -*-

s = 1
k = 2
p = 1
for i in range(3,40,2):
    s += i/k**p
    p+= 1
print("%.2f" %s)

