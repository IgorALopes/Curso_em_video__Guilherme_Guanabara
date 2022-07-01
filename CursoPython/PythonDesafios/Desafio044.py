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

# RESOLUÇÃO PROFESSOR:
print('{:=^40}'.format(' LOJAS GUANABARA '))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
