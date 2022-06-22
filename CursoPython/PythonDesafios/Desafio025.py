#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.
n = str(input('Qual é seu nome completo? ')).strip()
n1 = n.title()
print('Seu nome tem Silva? {}'.format('Silva' in n1))

#RESOLUÇÃO PROFESSOR
nome = str(input('Qual é seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower))
