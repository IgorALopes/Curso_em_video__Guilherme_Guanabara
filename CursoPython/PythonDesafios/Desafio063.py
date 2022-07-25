# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8
num = int(input('Número de elementos a serem exibidas numa Sequência de Fibonacci: '))
ult = 1
penult = 1
c = 4
if num == 1:
    print('{}-'.format(num - 1), end='')
elif num == 2:
    print('{}-{}-'.format(num - 2, num - 1), end='')
else:
    print('0-1-1-'.format(), end='')
    while c <= num:
        f = ult + penult
        penult = ult
        ult = f
        c += 1
        print('{}-'.format(f), end='')
print('FIM')

# RESOLUÇÃO PROFESSOR:
print('-'*30)
print('Sequência de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('~'*30)
print('{} ➡ {}'.format(t1, t2), end='')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(' ➡ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' ➡ FIM')
print('~'*30)
