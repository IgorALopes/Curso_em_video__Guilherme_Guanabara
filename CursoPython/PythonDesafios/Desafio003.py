#Crie um programa que leia dois números e mostre a soma entre eles.
numx = input('Digite um número. ')
numy = input('Digite outro número. ')
print ('A some de', numx, 'com', numy, 'é igual a', int(numx) + int(numy), '.')

#RESOLUÇÃO PROFESSOR:
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))
