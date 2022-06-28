# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço mprmal e condição de pagamento:
# À vista dinheiro/cheque: 10% de desconto; À vista no cartão: 5% de desconto; em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros.
p = float(input('Qual o preço do produto? R$ '))
pg = int(input('Selecione a forma de pagamento:\n1 - Dinheiro ou cheque à vista.\n2 - À vista no cartão.\n3 - Parcelado.\n'))
if pg == 1:
    print('O valor final a ser pago é de R$ {:.2f}'.format(p - (p / 100 * 10)))
elif pg == 2:
    print('O valor final a ser pago é de R$ {:.2f}'.format(p - (p / 100 * 5)))
elif pg == 3:
    xp = int(input('Em quantas parcelas pretende pagar? '))
    if xp == 2:
        print('O valor total será de R${} sem juros.'.format(p))
    elif xp > 2:
        print('O valor total será de R${} com os juros.'.format(p + (p / 100 * 20)))
else:
    print('Por favor, digite um opção válida.')