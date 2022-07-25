# Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('Escreva um número para saber seu fatorial: '))
c = 1
res = 1
while c <= num:
    res *= c
    c += 1
print('{}! = {}'.format(num, res))

# RESOLUÇÃO PROFESSOR:
from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
f = factorial(n)
print('O fatorial de {} é {}.'.format(n, f))
# OU
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')  # end='' significa que os prints não pularão de linha.
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(n, f))
