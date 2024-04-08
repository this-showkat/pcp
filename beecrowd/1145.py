# -*- coding: utf-8 -*-

a, b = [int(i) for i in input().split()]
if a<b and a>1 and a<20 and b>a and b<100000:
    lines = b//a if (b//a)==b/a else (b//a)+1 
    i = 1 
    while lines>0:
        for k in range(a-1):
            if i<b:
                print(i, end=" ")
                i += 1
        print(i)
        i+=1
        lines -= 1
           

