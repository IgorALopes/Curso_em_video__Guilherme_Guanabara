#Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor.
n1 = int(input('Digite um número: '))
print('O sucessor deste número é {} e o anteceddor é {}.'.format(n1+1, n1-1))

#RESOLUÇÃO PROFESSOR:
n = int(input('Digite um número: '))
a = n - 1
s = n + 1
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, a, s))
#OU
n = int(input('Digite um número: '))
print('Analisando o valor {}, seu antecessor é {} e o sucessor é {}'.format(n, (n-1), (n+1)))
