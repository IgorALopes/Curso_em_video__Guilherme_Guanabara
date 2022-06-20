#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
print('A média entre as duas notas é {:.2f}'.format((n1+n2)/2))

#RESOLUÇÃO PROFESSOR:
n1 = float(input('Primeira nota do aluno: '))
n1 = float(input('Segunda nota do aluno: '))
média = (n1 + n2) / 2
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}'.format(n1, n2, média))