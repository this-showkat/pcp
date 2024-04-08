# -*- coding: utf-8 -*-

grenais = inter = gremio = empates = 0
again = True
while again:
    a, b = [int(i) for i in input().split()]
    grenais +=1
    if a==b:
        empates += 1
    elif a>b:
        inter += 1
    else:
        gremio += 1

    print("Novo grenal (1-sim 2-nao)")
    sig = int(input())
    if sig==2:
        again = False

#Resut Print
print("%d grenais" %grenais)
print("Inter:%d" %inter)
print("Gremio:%d" %gremio)
print("Empates:%d" %empates)
if inter==gremio:
    print("Não houve vencedor")
elif inter>gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")
