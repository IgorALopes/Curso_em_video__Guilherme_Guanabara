#Um professor que sortear um dos seus quatro alunos para apagar o quarto. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
a1 = input('Escreva o nome do primeiro aluno: ')
a2 = input('Escreva o nome do segundo aluno: ')
a3 = input('Escreva o nome do terceiro aluno: ')
a4 = input('Escreva o nome do quarto aluno: ')
r = random.choice([a1, a2, a3, a4])
print('O aluno sorteado é: {}'.format(r))

#RESOLUÇÃO PROFESSOR:
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}.'.format(escolhido))