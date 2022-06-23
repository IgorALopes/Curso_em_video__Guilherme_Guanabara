#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
n = int(input('Digite um número: '))
if n % 2 == 0:
    print('Este número é PAR!')
else:
    print('Este número é ÍMPAR!')

#RESOLUÇÃO PROFESSOR:
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))