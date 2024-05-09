'''Faça um programa para calcular o fatorial de um número qualquer.'''


import math

num = int(input("digite um numero para calcular o fatorial "))
fatorial = math.factorial(num)
print("o numero é {} o seu fatorial é {}".format(num,fatorial))