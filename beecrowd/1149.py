# -*- coding: utf-8 -*-

x = [int(i) for i in input().split()]
i = 1
sum = 0
while x[i]<=0:
    i += 1
for j in range(x[0], x[0]+x[i]):
    sum += j
print(sum)
