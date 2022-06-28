#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida: Média abaixo de 5.0: REPROVADO; Média entre 5.0 e 6.9: RECUPERAÇÃO; Média 7.0 ou superior: APROVADO.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('REPROVADO! Sua média foi {:.2f}'.format(med))
elif med > 7:
    print('APROVADO! Sua média foi {:.2f}'.format(med))
elif med >= 5 and med < 7:
    print('RECUPERAÇÃO! Sua média foi {:.2f}'.format(med))
