# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
c = 0
soma = 0
mai = 0
men = 0
media = 0
continuar = 'S'
while continuar == 'S':
    n = int(input('Digite um número: '))
    soma += n
    c += 1
    if c == 1:
        mai = n
        men = n
    elif n > mai:
        mai = n
    elif n < men:
        men = n

    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()
media = soma / c
print('Você digitou {} números e a média é {}'.format(c, media))
print('O menor valor é {} e o maior é {}.'.format(men, mai))

# RESOLUÇÃO PROFESSOR:
resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
média = soma / quant
print('Você digitou {} números e a média foi {}'.format(quant, média))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))

