# -*- coding: utf-8 -*-

n = int(input())
i = 1

while n>0:
    for k in range(1, 4):
        print(i, end=" ")
        i += 1
    print("PUM")
    i += 1
    n -= 1
