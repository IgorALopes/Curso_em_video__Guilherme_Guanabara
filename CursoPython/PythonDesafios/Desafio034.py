#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1250,00, calcule um aumento de 10%. Para os inferiores ou iguais o aumento pe de 15%.
s = float(input('Digite o salário: R$ '))
if s > 1250:
    print('Este salário receberá um aumento de 10% e fica em R${:.2f}.'.format(s + (s/100*10)))
else:
    print('Este salário receberá um aumento de 15% e fica em R${:.2f}.'.format(s + (s/100*15)))

#RESOLUÇÃO PROFESSOR:
salário = float(input('Qual é o salário do funcionário? R$'))
if salário <= 1250:
    novo = salário + (salário * 15 /100)
else:
    novo = salário + (salário * 10 /100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário, novo))
