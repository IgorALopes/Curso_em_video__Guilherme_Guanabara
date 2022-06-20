#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1,00 = R$ 3,27.
d = float(input('Quantos reais você tem para converter em dolar? '))
print('Com seus R${:.2f}, você pode comprar US${:.2f} com a cotação de 1 dolar valendo 3,27 reais.'.format(d, (d/3.27)))

#RESOLUÇÃO PROFESSOR:
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:2f} você pode comprar US${:2f}'.format(real, dolar))
