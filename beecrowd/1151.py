# -*- coding: utf-8 -*-

n = int(input())
if n>0 and n<46:
    s1 = 0
    s2 = 1
    print(0, end=" ")
    for i in range(n-2):
       print(s2, end=" ")
       temp = s1
       s1 = s2
       s2 = s1+temp
    print(s2)
    
