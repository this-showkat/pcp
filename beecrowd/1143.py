# -*- coding: utf-8 -*-

n = int(input())
if n>1 and n<1000:
    for i in range(1, n+1):
        for j in range(1, 3):
            print(i**j, end=" ")
        print(i**(j+1))