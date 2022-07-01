#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final de acordo com a média atingida: Média abaixo de 5.0: REPROVADO; Média entre 5.0 e 6.9: RECUPERAÇÃO; Média 7.0 ou superior: APROVADO.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('REPROVADO! Sua média foi {:.2f}'.format(med))
elif med >= 7:
    print('APROVADO! Sua média foi {:.2f}'.format(med))
elif med >= 5 and med < 7:
    print('RECUPERAÇÃO! Sua média foi {:.2f}'.format(med))

# RESOLUÇÃO PROFESSOR:
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
média = (nota1 + nota2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(nota1, nota2, média))
if 7 > média >= 5:
    print('O aluno está em RECUPERAÇÃO.')
elif média < 5:
    print('O aluno está REPROVADO.')
elif média >= 7:
    print('O aluno está APROVADO.')
