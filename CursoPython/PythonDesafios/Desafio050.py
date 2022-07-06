# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.
soma = 0
for c in range(10, 17):
    if c % 2 == 0:
        soma = soma + c
print(soma)
#Deveria haver input.

# RESOLUÇÃO PROFESSOR:
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('Você infourmou {} números PARES e a soma foi {}'.format(cont, soma))