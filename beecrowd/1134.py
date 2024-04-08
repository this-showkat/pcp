# -*- coding: utf-8 -*- 


alcool = gasolina = diesel = 0
n = int(input())
while n!=4:
    if n == 1:
        alcool += 1
    elif n== 2:
        gasolina += 1
    elif n==3:
        diesel += 1
    n = int(input())
print("MUITO OBRIGADO")
print("Alcool: %d" %alcool)
print("Gasolina: %d" %gasolina)
print("Diesel: %d" %diesel)
