#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
p = float(input('Qual o preço do produto? '))
print('Aplicando-se 5% de desconto, o valor fica em R${:.2f}.'.format(p-(p/100*5)))

#RESOLUÇÃO PROFESSOR:
preço = float(input('Qual é o preço do produto: R$'))
novo = preço - (preço * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preço, novo))
