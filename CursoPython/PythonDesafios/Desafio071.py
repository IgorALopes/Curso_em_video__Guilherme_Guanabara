#  Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
#  OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
n50 = n20 = n10 = n1 = resto = 0
while True:
    dinheiro = int(input('Quanto deseja sacar? R$ '))
    if dinheiro >= 50:
        n50 = dinheiro // 50
        if dinheiro % 50 == 0:
            dinheiro = 0
        elif dinheiro % 50 != 0:
            dinheiro = dinheiro % 50
    if dinheiro >= 20:
        n20 = dinheiro // 20
        if dinheiro % 20 == 0:
            dinheiro = 0
        if dinheiro % 20 != 0:
            dinheiro = dinheiro % 20
    if dinheiro >= 10:
        n10 = dinheiro // 10
        if dinheiro % 10 == 0:
            dinheiro = 0
        if dinheiro % 10 != 0:
            dinheiro = dinheiro % 10
    if dinheiro >= 1:
        n1 = dinheiro // 1
        dinheiro = 0
    if dinheiro == 0:
        break
print(f'''Você receberá: 
{n50} notas de R$ 50,00;
{n20} notas de R$ 20,00;
{n10} notas de R$ 10,00;
{n1} notas de R$ 1,00''')

# RESOLUÇÃO PROFESSOR:
print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = int(input('Que valor você quer sacar? R$ '))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um com dia!')
