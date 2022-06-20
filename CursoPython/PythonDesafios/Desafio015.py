#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por Km rodado.
km = float(input('Quantos Km o carro andou? '))
d = float(input('Quantos dias o carro ficou alugado? '))
p = (km * 0.15) + (d * 60)
print('Com {} dias alugados e {}Km percorridos, o valor total a ser pago é de R${:.2f}.'.format(d, km, p))

#RESOLUÇÃO PROFESSOR:
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))
