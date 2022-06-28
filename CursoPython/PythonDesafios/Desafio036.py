# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
vcasa = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário mensal? R$ '))
anos = int(input('Em quantos anos pretende financiar? '))
p = vcasa / (anos * 12)
if p > sal / 100 * 30:
    print('Infelizmente o valor da parcela mensal de R$ {:.2f} excede 30% do seu salário. Não será possivel realizar o financiamento.'.format(p))
else:
    print('Cada prestação mensal será de R$ {:.2f}.'.format(p))

# RESOLUÇÃO PROFESSOR:
casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salário * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos, '.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
