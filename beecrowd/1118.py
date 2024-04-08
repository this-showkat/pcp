# -*- coding: utf-8 -*-


x = 1
while x==1:
    counter = sum = 0
    while counter<2:
        num = float(input())
        if num>=0 and num<=10:
            counter += 1
            sum += num
        else:
            print("nota invalida")
    print("media = %.2f" %(sum/2))
    print("novo calculo (1-sim 2-nao)")
    m = int(input())
    while m!=1 and m!=2:
        print("novo calculo (1-sim 2-nao)")
        m = int(input())
    x=m
