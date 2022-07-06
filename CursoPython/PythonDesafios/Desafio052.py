# Faça um programa que leia um número interio e diga se ele é ou não um número primo.
n = int(input('Escreva um número: '))
cont = 0
for c in range(2, n):
    if n % c == 0:
        cont += 1
if n == 1:
    print('Este número NÃO É PRIMO.')
elif cont == 0:
    print('Este número É PRIMO.')
else:
    print('Este número NÃO É PRIMO.')

# RESOLUÇÃO PROFESSOR:
núm = int(input('Digite um número: '))
tot = 0
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso, ele É PRIMO!')
else:
    print('E por isso, ele NÃO É PRIMO!')