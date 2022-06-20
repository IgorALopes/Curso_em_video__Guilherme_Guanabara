#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n1 = int(input('Digite um número: '))
print('O dobro deste número é {}, o triplo é {} e a raiz quadrada é {}'.format(n1*2, n1*3, n1**(1/2)))

#RESOLUÇÃO PROFESSOR:
n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = 2 ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))
#OU
n = int(input('Digite um número: '))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. \nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))
#Para a raiz quadrada, tbm pode usar pow(n, (1/2))
