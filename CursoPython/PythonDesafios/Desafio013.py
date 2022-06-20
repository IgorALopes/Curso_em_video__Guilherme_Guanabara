#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
s = float(input('Qual o seu salário? '))
print('Seu salário com 15% de aumento ficará em R${:.2f}'.format(s+(s/100*15)))

#RESOLUÇÃO PROFESSOR:
salário = float(input('Qual é o salário do funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}.'.format(salário, novo))