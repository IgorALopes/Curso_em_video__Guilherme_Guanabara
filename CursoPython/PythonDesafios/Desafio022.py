#Crie um programa que leia o nome completo de uma pessoa e mostre:
# – O nome com todas as letras maiúsculas e minúsculas.
# – Quantas letras ao todo (sem considerar espaços).
# – Quantas letras tem o primeiro nome.

n = input('Escreva seu nome completo: ')
print('Seu nome em maiúsculo: {}'.format(n.upper()))
print('Seu nome em minúsculo: {}'.format(n.lower()))
nsplit = n.split()
njoin = ''.join(nsplit)
print('Quantidade de letras em seu nome: {}'.format(len(njoin)))
n1 = nsplit[0]
print('Quantidade de letras em seu primeiro nome {} é {}'.format(n1, len(n1)))

#RESOLUÇÃO PROFESSOR:
nome = str(input('Digite seu nome completo: ')).strip() #.strip remove espaços antes e depois da string
print('Analisando nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
