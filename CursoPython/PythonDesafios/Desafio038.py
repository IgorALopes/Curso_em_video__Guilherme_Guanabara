#Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem: O primeiro valor é maior; O segundo valor é maior; Não existe valor maior, os dois são iguais.
num1 = int(input('Escreva um número: '))
num2 = int(input('Escreva outro número: '))
if num1 > num2:
    print('O primeiro valor é maior.')
elif num2 > num1:
    print('O segundo valor é maior.')
elif num1 == num2:
    print('Não existe valor maior, os dois são iguais.')

# RESOLUÇÃO PROFESSOR:
n1 = int(input('Primeiro Número: '))
n2 = int(input('Segundo Número: '))
if n1 > n2:
    print('O PRIMEIRO valor é MAIOR.')
elif n2 > n1:
    print('O SEGUNDO valor é MAIOR.')
else:
    print('Os dois valores são IGUAIS.')
