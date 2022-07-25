# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
valor = maisde1000 = soma = quant = valormaisbarato = 0
maisbarato = ' '
while True:
    prod = str(input('Qual é o produto? ')).strip()
    valor = float(input('Qual o preço do produto? R$ '))
    if valor > 0:
        quant += 1
        if quant == 1:
            valormaisbarato = valor
            maisbarato = prod
        if valor < valormaisbarato:
            maisbarato = prod
            valormaisbarato = valor
        soma += valor
    if valor > 1000:
        maisde1000 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer adicionar mais um produto? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O valor total da compra é de R$ {soma:.2f}.')
print(f'{maisde1000} produtos custam mais de R$ 1000,00.')
print(f'O produto mais barato é {maisbarato} no valor de R$ {valormaisbarato:.2f}.')

# RESOLUÇÃO PROFESSOR:
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    total += preço
    if preço > 1000:
        totmil += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {totmil} produtos custando mais de R$ 1000,00')
print(f'O produto mais barato foi {barato} que custa R${menor:.2f}')

